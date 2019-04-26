import wx


class ColumnConfigs(wx.Panel):
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent, style=wx.BORDER_RAISED)
        lbl_header = wx.StaticText(self, wx.ID_ANY, "Column Configurations")
        # lbl_header.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))

        header_line = wx.StaticLine(self, wx.ID_ANY)
        config_box = wx.BoxSizer(wx.VERTICAL)
        # self.SetMinSize((800,400))

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(lbl_header, 0, wx.ALIGN_CENTER | wx.TOP | wx.EXPAND, 5)
        sizer.Add(header_line, 0, wx.ALIGN_BOTTOM | wx.TOP | wx.EXPAND, 5)
        sizer.Add(config_box, 0, wx.ALIGN_BOTTOM | wx.ALL | wx.EXPAND)
        self.SetSizer(sizer)
