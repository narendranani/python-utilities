import wx


def project_configuration(event, parent=None):
    """
    Open the project configuration window
    :return:None
    """
    dlg = ProjectConfiguration(parent)
    dlg.Show()
    # dlg.ShowModal()
    dlg.Destroy()


class ProjectConfiguration(wx.Dialog):
    def __init__(self, parent=None):
        wx.Dialog.__init__(self, parent, wx.ID_ANY, "Project Configuration",
                           size=(wx.DisplaySize()[0] * 0.29, wx.DisplaySize()[1] * 0.56))
        self.Center(True)
        # dlg.ShowModal()
        self.view()
        self.ShowWindowModal()
        self.Destroy()

    def view(self):
        pass
