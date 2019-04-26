import wx
import wx.lib.agw.customtreectrl as CT
from common import utils

class MyFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "CustomTreeCtrl Demo")

        # Create a CustomTreeCtrl instance
        custom_tree = CT.CustomTreeCtrl(self, agwStyle=wx.TR_NO_LINES | wx.TR_HAS_BUTTONS) #agwStyle=wx.TR_EDIT_LABELS)

        # Add a root node to it
        root = custom_tree.AddRoot("The Root Item")

        # Create an image list to add icons next to an item
        il = wx.ImageList(16, 16)
        fldridx = il.Add(wx.ArtProvider.GetBitmap(wx.ART_HARDDISK, wx.ART_OTHER, (16, 16)))
        # fldridx = il.Add(wx.ArtProvider.GetBitmap(utils.resize_images(r'.\icons\generatedata.png', 16, 16), wx.ART_OTHER, (16, 16)))
        fldropenidx = il.Add(wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_OTHER, (16, 16)))
        fileidx = il.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, (16, 16)))

        custom_tree.SetImageList(il)

        custom_tree.SetItemImage(root, fldridx, wx.TreeItemIcon_Normal)
        custom_tree.SetItemImage(root, fldropenidx, wx.TreeItemIcon_Expanded)

        for x in range(15):
            child = custom_tree.AppendItem(root, "Item %d" % x)
            custom_tree.SetItemImage(child, fldridx, wx.TreeItemIcon_Normal)
            custom_tree.SetItemImage(child, fldropenidx, wx.TreeItemIcon_Expanded)

        custom_tree.Expand(root)


# our normal wxApp-derived class, as usual

app = wx.App(0)

frame = MyFrame(None)
app.SetTopWindow(frame)
frame.Show()

app.MainLoop()
