import wx


class FrameConfiguration(wx.Frame):
    def __init__(self, parent=None):
        wx.Frame.__init__(self, None, title="Data Gene", style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        # font = wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD)
        # self.SetFont(font)
        # self.SetTitle("Testing")
        # self.panel = wx.Panel(self, wx.ID_ANY)
        self.Maximize(True)

        Mainsplitter = wx.SplitterWindow(self, style=wx.SP_3D)
        Hsplitter = wx.SplitterWindow(Mainsplitter, style=wx.SP_3D)

        panel1 = wx.Panel(Mainsplitter, wx.ID_ANY)
        panel1.SetBackgroundColour(wx.WHITE)

        panel2 = wx.Panel(Hsplitter, wx.ID_ANY)
        panel2.SetBackgroundColour(wx.WHITE)

        panel3 = wx.Panel(Hsplitter, wx.ID_ANY)
        panel3.SetBackgroundColour(wx.WHITE)

        Mainsplitter.SplitVertically(panel1, Hsplitter, 400)
        Hsplitter.SplitHorizontally(panel2, panel3, 600)

        # self.Column_Config(panel2)
        self.toolbar()

    def Table_Config(self, panel_type):
        title = wx.StaticText(panel_type, label="Table Generation Configurations")
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        title.SetFont(font)

        ln = wx.StaticLine(panel_type, -1, style=wx.LI_HORIZONTAL)

        wx.StaticText(panel_type, pos=(100, 100), label="Number of rows to be Generated:", style=wx.ALIGN_CENTRE)
        wx.TextCtrl(panel_type, pos=(300, 100))

    def Column_Config(self, panel_type):
        title = wx.StaticText(panel_type, label="Column Generation Configurations")
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        title.SetFont(font)

        wx.StaticText(panel_type, pos=(100, 100), label="Country:", style=wx.ALIGN_CENTRE)
        wx.TextCtrl(panel_type, pos=(150, 100))

        sb = wx.StaticBox(panel_type)
        select_country = wx.StaticBoxSizer(sb, wx.VERTICAL)

        cb1 = wx.CheckBox(panel_type, label='AAaaaaaaaaa', pos=(10, 10))
        select_country.Add(cb1, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 10)
        cb2 = wx.CheckBox(panel_type, label='B', pos=(10, 30))
        select_country.Add(cb2, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 10)
        cb3 = wx.CheckBox(panel_type, label='C', pos=(10, 50))
        select_country.Add(cb3, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 10)

    def toolbar(self):
        self.toolbar = self.CreateToolBar()

        new_project = wx.Bitmap(r'F:\Narendra\ggk_projects\DataGenerator_Mocks\icons\new.png')
        # self.new_project = GenBitmapTextButton(parent=self, bitmap=new_project, name="New Project")
        self.toolbar.AddTool(wx.ID_ANY, 'New Project', new_project)
        self.open_project = wx.Bitmap(r'F:\Narendra\ggk_projects\DataGenerator_Mocks\icons\open.png')
        self.toolbar.AddTool(wx.ID_ANY, '', self.open_project)
        self.save_project = wx.Bitmap(r'F:\Narendra\ggk_projects\DataGenerator_Mocks\icons\save.png')
        self.toolbar.AddTool(wx.ID_ANY, 'New Project', self.save_project)
        self.generate_data = wx.Bitmap(r'F:\Narendra\ggk_projects\DataGenerator_Mocks\icons\generatedata.png')
        self.toolbar.AddTool(wx.ID_ANY, '', self.generate_data)
        self.toolbar.Realize()

if __name__ == "__main__":
    app = wx.App(False)
    frame = FrameConfiguration()
    frame.Show()

    app.MainLoop()