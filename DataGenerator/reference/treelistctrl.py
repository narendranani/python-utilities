# import wx, wx.lib.agw.customtreectrl
#
# app = wx.App(False)
#
# fr = wx.Frame(None)
#
# myModule = wx.lib.agw.customtreectrl
# myStyle = (myModule.TR_DEFAULT_STYLE|myModule.TR_MULTIPLE
#            |myModule.TR_FULL_ROW_HIGHLIGHT|myModule.TR_AUTO_CHECK_CHILD
#            |myModule.TR_AUTO_CHECK_PARENT|myModule.TR_AUTO_TOGGLE_CHILD)
#
# tree = myModule.CustomTreeCtrl(fr, style=myStyle)
# treeRoot = tree.AddRoot("PyRx Enzymes",  ct_type=1)
# treeNodes =['Node A','Node B', 'Node C']
# treeItems = ['1', '2', '3']
# for i, _ in enumerate(treeNodes):
#     iNode = tree.AppendItem(treeRoot, treeNodes[i],  ct_type=1)
#     for ii in treeItems:
#         tree.AppendItem(iNode, "%s %s"%(treeNodes[i].replace('Node ',''), ii) )
# tree.Expand(treeRoot)
#
# fr.Show()
#
# app.MainLoop()


import wx, wx.lib.agw.customtreectrl

app = wx.App(False)

fr = wx.Frame(None)

myModule = wx.lib.agw.customtreectrl
myStyle = (myModule.TR_DEFAULT_STYLE|myModule.TR_MULTIPLE
           |myModule.TR_FULL_ROW_HIGHLIGHT|myModule.TR_AUTO_CHECK_CHILD
           |myModule.TR_AUTO_CHECK_PARENT|myModule.TR_AUTO_TOGGLE_CHILD)

tree = myModule.CustomTreeCtrl(fr, agwStyle=myStyle)
treeRoot = tree.AddRoot("PyRx Enzymes")
treeNodes =['Node A','Node B', 'Node C']
treeItems = ['1', '2', '3']
for i, _ in enumerate(treeNodes):
    iNode = tree.AppendItem(treeRoot, treeNodes[i], ct_type=1)
    for ii in treeItems:
        tree.AppendItem(iNode, "%s %s"%(treeNodes[i].replace('Node ',''), ii), ct_type=1)
tree.Expand(treeRoot)

fr.Show()

app.MainLoop()