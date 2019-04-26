import wx
import wx.gizmos
import random


class TableColumnPanel(wx.Panel):
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent, style=wx.BORDER_STATIC)
        lbl_header = wx.StaticText(self, wx.ID_ANY, "Tables and columns to populate")
        # lbl_header.SetFont(wx.Font(9, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))

        tv_tables = MyGizmos(self)
        tv_tables.SetBackgroundColour(wx.WHITE)
        # self.SetMinSize((500,400))

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(lbl_header, 0, wx.ALIGN_CENTER | wx.TOP | wx.EXPAND, 5)
        sizer.Add(tv_tables, 11, wx.ALIGN_BOTTOM | wx.TOP | wx.EXPAND, 5)
        self.SetSizer(sizer)


class MyGizmos(wx.gizmos.TreeListCtrl):
    def __init__(self, parent):
        super(MyGizmos, self).__init__(parent)
        self.AddColumn('vars')
        self.AddColumn('vals')
        self.SetColumnWidth(0, 100)
        self.SetColumnWidth(1, 100)
        root = self.AddRoot('foodata')
        self.SetItemText(self.AppendItem(root, 'var 1'), 'val 1', 1)
        self.Bind(wx.EVT_LIST_COL_CLICK, self.OnLabel)

    def OnLabel(self, event):
        print('col label clicked, but which one ???')
        item = event.GetItem()
        print(item)  # prints wx._controls.ListItem
        print(item.GetColumn())  # always 0
        # print item.GetColumn(0) # fails
