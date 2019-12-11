#!/usr/bin/env python3

# gui_class.py

# TODO: all of this code needs to be deleted and refactored to tkinter
# TODO: first, worry about getting something working, then refactor
# to SOLID principles

import tkinter


# import wx
# from myLib.Logic.tv_class import TVShow


# class MainGUI:
#     '''This class holds all the GUI stuff'''
#     def __init__(self):
#         self.__app = wx.App()
#         self.__frame = wx.Frame(None, title='Random Episode Generator',
#                                 size=(850, 550))
#         self.setup()
#         self.__show = TVShow()

#     def setup(self):
#         '''sets all the widgets, also calls header()'''
#         self.show_name_txt = wx.TextCtrl(self.__frame, pos=(25, 50),
#                                          size=(200, 25))
#         self._name_label = wx.StaticText(self.__frame, pos=(25, 25), \
#                                         label='Enter a Show Title Here')

#         self.main_text = wx.TextCtrl(self.__frame, pos=(25, 150),
#                                      size=(500, 350),\
#                 style=wx.TE_MULTILINE | wx.HSCROLL)

#         # the next two variables are for images.
#         # .FromRGBA(alpha=0) will make the Bitmap completely transparent
#         img = wx.Bitmap.FromRGBA(100, 100, alpha=0)
#         #this image will be filled after the user enters a show title
#         self.image = wx.StaticBitmap(self.__frame, wx.ID_ANY, wx.Bitmap(img),
#                                      pos=(600, 100))

#         #region Buttons
#         self.get_show_btn = wx.Button(parent=self.__frame,
#                                       label="Get Title's Info",
#                                       pos=(25, 100))
#         self.get_show_btn.Bind(wx.EVT_BUTTON, self.get_show_info)

#         self.nxt_rand_btn = wx.Button(self.__frame,
#                                       label='Next Random Episode',
#                                       pos=(140, 100))
#         self.nxt_rand_btn.Bind(wx.EVT_BUTTON, self.next_rand)

#         self.show_db_btn = wx.Button(self.__frame, label='Show Database',
#                                      pos=(300, 100))
#         self.show_db_btn.Bind(wx.EVT_BUTTON, self.show_db)

#         self.clear_db_btn = wx.Button(self.__frame, label='Clear Database',
#                                       pos=(425, 100))
#         self.clear_db_btn.Bind(wx.EVT_BUTTON, self.clear_db)
#         #endregion

#        #show the initial instructions to the user
#         self.header()

#     #region Button Events
#     def get_show_info(self, event):
#         '''calls show.get_info() and sets picture if it is found'''
#         if self.show_name_txt.IsEmpty():
#             self.print_message('\nPlease enter the name of show before "
#                                "clicking any buttons!')
#             return
#         # get the name of the show, set it into TVShow class and
#         # call the api
#         self.__show.set_name(self.show_name_txt.GetValue())

#         flag = self.__show.get_info()

#         # flag will be a string if something went wrong in get_info()
#         if isinstance(flag, str):
#             self.print_message(flag)
#             return
#         else:
#             self.print_message('\nHere is the information for %s'
#                                % self.__show.name)
#             self.print_message(repr(self.__show))

#         # the api has a link to a jpg, this will get the picture
#         # and then set it into the StaticBitmap
#         flag = self.__show.get_pic()
#         if flag is True:
#             self.set_pic()

#     def next_rand(self, event):
#         '''get a random combination from TVShow class'''
#         #checking if the name member in the show class is empty
#         if self.__show.name == '':
#             self.print_message('\nPlease enter the name of show before "
#                                "clicking anything')
#             return
#         #checking if the names in the class and in the textfiels are similar
#         elif self.__show.name != self.show_name_txt.GetValue():
#             self.__show.set_name(self.show_name_txt.GetValue())
#             flag = self.__show.get_info()
#             # flag will be a string if something went wrong in get_info()
#             if isinstance(flag, str):
#                 self.print_message(flag)
#                 return
#         # if next_combo returns a string hen something went wrong
#         combo = self.__show.next_combo()
#         if isinstance(combo, str):
#             self.print_message(combo)
#             return
#         elif combo is False:
#             self.print_message("Please enter a valid show name before "
#                                "clicking this buton")
#             return
#         _str = '\nGoTo Season %i, Episode %i\n' % (combo[0], combo[1])
#         self.print_message(_str)

#     def show_db(self, event):
#         '''displays everything in TVShow.db'''
#         flag = self.__show.show_db()

#         if flag is None:
#             self.print_message('\nDatabase is Empty!\n')
#             return
#         elif flag is False:
#             self.print_message('\nSomething went wrong getting the "
#                                "information from the database!')
#             return

#         _str = ''
#         for item in flag:
#             _str += str(item)

#         self.print_message(_str)

#     def clear_db(self, event):
#         '''uses the title in the class or text field to create delete
#         statement this method does not remove everything from the database,
#         just rows with the same name
#         '''
#         if self.__show.name == '':
#             if self.show_name_txt.IsEmpty():
#                 self.print_message('\nEnter the title of a show before "
#                                    "clicking anything!')
#                 return
#             else:
#                 self.__show.set_name(self.show_name_txt.GetValue())
#                 flag = self.__show.get_info()
#                 # flag will be a string if something went wrong in get_info()
#                 if isinstance(flag, str):
#                     self.print_message(flag)
#                     return

#         elif self.__show.name != self.show_name_txt.GetValue():
#             self.__show.set_name(self.show_name_txt.GetValue())
#             flag = self.__show.get_info()
#             # flag will be a string if something went wrong in get_info()
#             if isinstance(flag, str):
#                 self.print_message(flag)
#                 return

#         flag = self.__show.clear_db()
#         if isinstance(flag, str):
#             self.print_message(flag)
#         else:
#             self.print_message('\nShow successfully cleared from database!')

#     def print_message(self, message):
#         '''A simple method to replace repeated code
#         method to implement D.R.Y. paradigm'''
#         self.main_text.AppendText(message)
#         self.main_text.AppendText('\n')
#     #endregion

#     #region Utility Methods
#     def set_pic(self):
#         '''sets image.jpg into a Bitmap for user to see
#         don't need to worry about checking here, that is handled in a
#         different method
#         '''
#         self.image.SetBitmap(wx.Bitmap(self.__show.pic_path()))

#     def start_gui(self):
#         '''gets the GUI ball rolling'''
#         self.__frame.Show()
#         self.__app.MainLoop()

#     def header(self):
#         '''present title of project and instructions to user'''
#         _str = '\nWelcome to my SUPER AMAZING TV SHOW EPISODE SHUFFLER!!!!'
#         _str += '\nThis program utilizes an api to shuffle through the '\
#          'seasons and episode of any \nshow you enter. It then spits out a '\
#          'random combination of a season and episode \nfor your viewing '\
#           'pleasure'
#         _str += '\nBefore clicking any of the buttons, please enter the'\
#                 ' name of show in the text area above.'
#         _str += '\nClick "Get Title\'s Info" to get the necessary data, '\
#                 'then click "Next Random Episode".'\
#                 "\nThe first button goes to the api and gets all the '\
#                 'information for that show."
#         _str += "\nThe second button can only work if all the data needed'\
#                 ' has been gathered first."
#         _str += '\n\nSide note: "Clear Database" only deletes the show '\
#                 'in the text field above. \n\t\tIt does not delete the '\
#                 'entire database.\n\n'
#         self.print_message(_str)
#     #endregion
# #End of GuiClass
