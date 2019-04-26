import wx
from common import project_configurations as pc


class MainView(wx.Frame):
    # wx.Frame.ShowFullScreen()
    def __init__(self):
        """Main Application Window"""
        # wx.Frame.__init__(self, None, title="Data Generator")
        wx.Frame.__init__(self, None, title="Data Generator", style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        # font = wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD)
        # self.SetFont(font)
        # self.SetTitle("Testing")
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.add_menu_items()
        self.Maximize(True)

    def add_menu_items(self):
        """
        Add the menu items to the menu bar
        :return:None
        """
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        new_project_menu_item = file_menu.Append(wx.NewId(), "New Project",
                                                 "Exit the application")
        open_project_menu_item = file_menu.Append(wx.NewId(), "Open Project",
                                                  "Open the existing project")
        close_project_menu_item = file_menu.Append(wx.NewId(), "Close Project",
                                                   "Close the project")
        save_project_menu_item = file_menu.Append(wx.NewId(), "Save",
                                                  "Save the project")
        save_as_project_menu_item = file_menu.Append(wx.NewId(), "Save Project As...",
                                                     "Save the project")
        exit_menu_item = file_menu.Append(wx.NewId(), "Exit",
                                          "Exit the application")
        self.Bind(wx.EVT_MENU, self.on_exit, exit_menu_item)
        self.Bind(wx.EVT_MENU, lambda event: pc.project_configuration(event, parent=self), new_project_menu_item)
        help_menu = wx.Menu()
        documentaion_menu_item = help_menu.Append(wx.NewId(), "Documentation",
                                                  "Provides the documentation on tool")

        menu_bar.Append(file_menu, "&File")
        menu_bar.Append(help_menu, "&Help")
        self.SetMenuBar(menu_bar)

    def on_exit(self, event):
        """close the application"""
        self.Close()


class MainViewController(wx.Frame):
    def __init__(self):
        pass


class MainModel(wx.Frame):
    def __init__(self):
        pass


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainView()
    frame.Show()
    pc.project_configuration(None, parent=frame)
    app.MainLoop()
