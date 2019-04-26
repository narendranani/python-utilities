# import wx
# import wx.html
#
#
# class MyHtmlFrame(wx.Frame):
#     def __init__(self, parent, title):
#         wx.Frame.__init__(self, parent, -1, title)
#         html = wx.html.HtmlWindow(self)
#         if "gtk2" in wx.PlatformInfo:
#             html.SetStandardFonts()
#         html.SetPage(
#             "Here is some <b>formatted</b> <i><u>text</u></i> "
#             "loaded from a <font color=\"red\">string</font>.")
#
#
# app = wx.PySimpleApp()
# frm = MyHtmlFrame(None, "Simple HTML")
# frm.Show()
# app.MainLoop()

def my_decorator(some_function):

    def wrapper():

        print("Something is happening before some_function() is called.")

        some_function()

        print("Something is happening after some_function() is called.")

    return wrapper


def just_some_function():
    print("Wheee!")


just_some_function = my_decorator(just_some_function)

just_some_function()
