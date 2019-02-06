using System;
using System.Net.Http;
using System.Threading.Tasks;
using Randomizer.Common.Exceptions;


namespace Randomizer.Infrastructure
{
    public static class TVMazeCaller
    {
        private static readonly string baseURL= @"https://api.tvmaze.com/singlesearch/shows?q=";
        private static readonly string embed = @"&embed=episodes";

        //example: https://api.tvmaze.com/singlesearch/shows?q=bobs+burgers&embed=episodes

        private static Uri CreateUrl(string title) => new Uri(baseURL + title + embed);

        public static string CallApi_Sync(string title)
        {
            var json = string.Empty;
            try
            {
                var url = CreateUrl(title);

                json = InternalCallApi_Sync(url);
            }
            catch(HttpRequestException hex)
            {
                throw hex;
            }

            if (string.IsNullOrEmpty(json))
                throw new BadApiCallException("Nothing returned from api call");

            return json;
        }
        public static async Task<string> CallApi_Async(string title)
        {
            var json = string.Empty;
            try
            {
                var url = CreateUrl(title);

                json = await InternalCallApi_Async(url);
            }
            catch(HttpRequestException hex)
            {
                throw hex;
            }

            if (string.IsNullOrEmpty(json))
                throw new BadApiCallException("Nothing returned from api call");

            return json;
        }

        private static async Task<string> InternalCallApi_Async(Uri url)
        {
            try
            {
                using(var api = new HttpClient())
                {
                    var response = await api.GetAsync(url);
                    if (response.IsSuccessStatusCode)
                        return response.Content.ReadAsStringAsync().GetAwaiter().GetResult();
                    else
                    return string.Empty;
                }
            }
            catch(HttpRequestException hex)
            {
                throw hex;
            }
        }

        private static string InternalCallApi_Sync(Uri url)
        {
            try
            {
                using (var api = new HttpClient())
                {
                    var response = api.GetAsync(url).GetAwaiter().GetResult();
                    if (response.IsSuccessStatusCode)
                        return response.Content.ReadAsStringAsync().GetAwaiter().GetResult();
                    else
                        return string.Empty;
                }
            }
            catch (HttpRequestException hex)
            {
                throw hex;
            }
        }
    }
}