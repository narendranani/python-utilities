import wx
from common import utils

class PreviewPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, style=wx.BORDER_RAISED)
        # hbox_header = wx.GridBagSizer(hgap=10, vgap=0)
        hbox_header = wx.BoxSizer(wx.HORIZONTAL)
        lbl_header = wx.StaticText(self, -1, "Preview of data to be generated")
        # lbl_header.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))
        refresh_icon = utils.resize_images(r'.\icons\refresh-icon_1.png', 10, 10)
        btn_refresh = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(refresh_icon))#, style=wx.NO_BORDER)
        hbox_header.Add(lbl_header, flag=wx.ALIGN_LEFT | wx.EXPAND)
        hbox_header.Add(btn_refresh, flag=wx.ALIGN_RIGHT | wx.EXPAND)
        header_line = wx.StaticLine(self, wx.ID_ANY)
        config_box = wx.BoxSizer(wx.VERTICAL)
        # self.SetMinSize((800,400))

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(hbox_header, 0, wx.ALIGN_TOP | wx.TOP | wx.EXPAND, 5)
        sizer.Add(header_line, 0, wx.ALIGN_TOP | wx.TOP | wx.EXPAND, 5)
        self.SetSizer(sizer)
