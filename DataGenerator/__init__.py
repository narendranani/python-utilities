import wx
from common import project_configurations as pc
from common import table_columns_view as tcv
from common import preview as pr
from common import column_configurations as cc
from common import utils
from wx.lib.buttons import ThemedGenBitmapTextButton, GenBitmapTextButton


class MainView(wx.Frame):
    # wx.Frame.ShowFullScreen()
    def __init__(self):
        """Main Application Window"""
        # wx.Frame.__init__(self, None, title="Data Generator")
        wx.Frame.__init__(self, None, title="Data Generator", style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL) #style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.adds()
        self.toolbar()
        self.Maximize(True)
        self.SetMinSize(wx.Size(800, 600))

        # Create a panel and notebook (tabs holder)
        main_panel = wx.Panel(self)
        notebook = wx.Notebook(main_panel)

        # Create the tab windows
        project_tab = AddTab(notebook)

        # Add the windows to tabs and name them.
        notebook.AddPage(project_tab, "Untitled_1")

        # Set noteboook in a sizer to create the layout
        sizer = wx.BoxSizer()
        sizer.Add(notebook, 1, wx.EXPAND)
        main_panel.SetSizer(sizer)

    def adds(self):
        """
        Add the menu items to the menu bar
        :return:None
        """
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        actions_menu = wx.Menu()
        # file_menu.SetFont(wx.Font(23, wx.DEFAULT, style=wx.NORMAL, weight=wx.NORMAL))
        new_project = file_menu.Append(wx.NewId(), "New Project",
                                                 "Exit the application")
        open_project = file_menu.Append(wx.NewId(), "Open Project",
                                                  "Open the existing project")
        close_project = file_menu.Append(wx.NewId(), "Close Project",
                                                   "Close the project")
        save_project = file_menu.Append(wx.NewId(), "Save",
                                                  "Save the project")
        save_as_project = file_menu.Append(wx.NewId(), "Save Project As...",
                                                     "Save the project")
        exit = file_menu.Append(wx.NewId(), "Exit",
                                          "Exit the application")
        generate_data = actions_menu.Append(wx.NewId(), "Generate Data",
                                          "Generate the data")
        self.Bind(wx.EVT_MENU, self.on_exit, exit)
        self.Bind(wx.EVT_MENU, lambda event: pc.project_configuration(event, parent=self, from_main_window=True),
                  new_project)
        help_menu = wx.Menu()
        documentaion = help_menu.Append(wx.NewId(), "Documentation",
                                                  "Provides the documentation on tool")

        menu_bar.Append(file_menu, "&File")
        menu_bar.Append(actions_menu, "&Actions")
        menu_bar.Append(help_menu, "&Help")
        self.SetMenuBar(menu_bar)

    def toolbar(self):
        self.toolbar = self.CreateToolBar(style=(wx.TB_HORZ_LAYOUT | wx.TB_TEXT))


        new_project = wx.Bitmap(
            utils.resize_images(r'.\icons\new.png', 16, 16))

        # self.new_project = GenBitmapTextButton(parent=self, bitmap=new_project, name="New Project")
        self.toolbar.AddTool(wx.ID_ANY, label='New Project', bitmap=new_project)
        self.open_project = wx.Bitmap(
            utils.resize_images(r'.\icons\open.png', 16, 16))
        self.toolbar.AddTool(wx.ID_ANY, 'Open', self.open_project)
        self.save_project = wx.Bitmap(
            utils.resize_images(r'.\icons\save.png', 16, 16))
        self.toolbar.AddTool(wx.ID_ANY, 'Save', self.save_project)
        self.generate_data = wx.Bitmap(
            utils.resize_images(r'.\icons\generatedata.png', 16, 16))
        self.toolbar.AddTool(wx.ID_ANY, 'Generate Data', self.generate_data)

        self.toolbar.Realize()

    def on_exit(self, event):
        """close the application"""
        self.Close()


class AddTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.splitter()

    def splitter(self):
        v_splitter = wx.SplitterWindow(self, style=wx.SP_3DBORDER)
        h_splitter = wx.SplitterWindow(v_splitter, style=wx.SP_3DBORDER)
        v_splitter.SetMinimumPaneSize(200)
        h_splitter.SetMinimumPaneSize(300)
        h_splitter.SetSashGravity(0.5)

        pnl_tree_view = tcv.TableColumnPanel(v_splitter)
        # pnl_tree_view.SetBackgroundColour(wx.WHITE)

        pnl_col_configs = cc.ColumnConfigs(h_splitter)
        # pnl_col_configs.SetBackgroundColour(wx.WHITE)

        pnl_preview = pr.PreviewPanel(h_splitter)
        # pnl_preview.SetBackgroundColour(wx.WHITE)

        v_splitter.SplitVertically(pnl_tree_view, h_splitter, 350)
        h_splitter.SplitHorizontally(pnl_col_configs, pnl_preview, 300)

        sizer = wx.BoxSizer()
        sizer.Add(v_splitter, 1, wx.EXPAND)
        self.SetSizer(sizer)


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
