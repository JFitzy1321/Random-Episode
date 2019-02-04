using System;
using System.Threading.Tasks;

namespace Randomizer.Logic
{
    public interface ILayerCommunication
    {
        void SetTvTitle(string title);
        bool CallApi();
        Task<bool> CallApi_Async();
        Tuple<int, int> GetRandomPair();

        Task<Tuple<int, int>> GetRandomPair_Async();
    }
}