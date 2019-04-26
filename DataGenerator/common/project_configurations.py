import wx


class ProjectConfiguration(wx.Dialog):
    def __init__(self, parent=None, from_main_window=None):
        """
        Default class constructor
        :param parent: parent window for the project configuration dialog
        """
        self.from_main_window = from_main_window
        self.parent = parent
        wx.Dialog.__init__(self, self.parent, id=wx.ID_ANY, title="Project Configuration")
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.view()
        self.ShowWindowModal()

    def view(self):
        """
        Build the UI for project configuration dialog.
        Here we have three types of project configurations.
        1. Custom Project: Users can give their own table and column names and generate data for thoss custom table
        2. From Database: Users can populate the metadata(tables and its columns) from database directly.
        3. Existing Project: Users can edit the previously saved project(it may either Custom or From Database)
        Default selection: Custom Project
        :return: None
        """
        sb = wx.StaticBox(self, label="Select The Project Type")
        sb.SetFont(wx.Font(wx.DEFAULT, wx.DEFAULT, style=wx.NORMAL, weight=wx.BOLD))
        sbox_select_project_type = wx.StaticBoxSizer(sb, wx.VERTICAL)
        sbox_select_project_type.SetSizeHints(self)

        rbtn_custom_project = wx.RadioButton(self, label="Custom Project")
        sbox_select_project_type.Add(rbtn_custom_project, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 10)
        rbtn_from_database = wx.RadioButton(self, label="From Database")
        sbox_select_project_type.Add(rbtn_from_database, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 10)
        rbtn_existing_project = wx.RadioButton(self, label="Existing Project")
        sbox_select_project_type.Add(rbtn_existing_project, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 10)

        hbox_btns = wx.BoxSizer(wx.HORIZONTAL)
        btn_ok = wx.Button(self, wx.ID_ANY, "OK", wx.DefaultPosition, wx.DefaultSize, 10)

        btn_cancel = wx.Button(self, wx.ID_ANY, "Cancel", wx.DefaultPosition, wx.DefaultSize, 10)
        self.Bind(wx.EVT_BUTTON, self.evnt_cancel, btn_cancel)

        hbox_btns.Add(btn_ok, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 7)
        hbox_btns.Add(btn_cancel, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 7)
        hbox_btns.Fit(self)
        hbox_btns.AddStretchSpacer(0)

        existing_project = self.existing_project_ui()
        from_database = self.from_database_ui()

        # Add elements to Main Sizer
        self.sizer.Add(sbox_select_project_type, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER, 10)
        self.sizer.Add(existing_project, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER, 10)
        self.sizer.Add(from_database, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER, 10)
        self.sizer.Add(hbox_btns, 0, wx.ALIGN_RIGHT | wx.ALIGN_BOTTOM, 0)

        # Bind the events to project type options
        self.Bind(wx.EVT_RADIOBUTTON,
                  lambda event: self.evnt_change_project_type_ui(event=event, show_ui=existing_project,
                                                                 hide_ui=from_database, dialog_height=0.31),
                  rbtn_existing_project)
        self.Bind(wx.EVT_RADIOBUTTON,
                  lambda event: self.evnt_change_project_type_ui(event=event, show_ui=from_database,
                                                                 hide_ui=existing_project, dialog_height=0.5),
                  rbtn_from_database)
        self.Bind(wx.EVT_RADIOBUTTON,
                  lambda event: self.evnt_custom_project(event=event, hide_ui=[existing_project, from_database]),
                  rbtn_custom_project)

        self.lbl_auth.Hide()
        self.choice_auth.Hide()
        self.sizer.Fit(self)
        self.SetSizer(self.sizer)
        self.Center(True)
        self.SetAutoLayout(1)

    def existing_project_ui(self):
        """
        Build UI for existing project
        :return: UI- Static Box Sizer contains text control and Browse button
        """
        sb = wx.StaticBox(self, label="Browse Project")
        sb.SetFont(wx.Font(wx.DEFAULT, wx.DEFAULT, style=wx.NORMAL, weight=wx.BOLD))
        sbox_browse_project = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
        te_project_path = wx.TextCtrl(sb, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        te_project_path.SetFont(wx.Font(wx.DEFAULT, wx.DEFAULT, style=wx.NORMAL, weight=wx.NORMAL))
        btn_browse = wx.Button(sb, wx.ID_ANY, "Browse", wx.DefaultPosition, wx.DefaultSize, 10)
        btn_browse.SetFont(wx.Font(wx.DEFAULT, wx.DEFAULT, style=wx.NORMAL, weight=wx.NORMAL))
        sbox_browse_project.Add(te_project_path, 3, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 10)
        sbox_browse_project.Add(btn_browse, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 10)
        return sbox_browse_project

    def from_database_ui(self):
        """
        Build UI for From Database
        :return: UI- Static Box Sizer contains db connection details
        """
        sb = wx.StaticBox(self, label="Database Connection")
        sb.SetFont(wx.Font(wx.DEFAULT, wx.DEFAULT, style=wx.NORMAL, weight=wx.BOLD))
        sbox_db_connection = wx.StaticBoxSizer(sb, wx.VERTICAL)

        self.lbl_db_type = wx.StaticText(sb, wx.ID_ANY, "Db Type")

        self.gsizer_db_details = wx.GridBagSizer(hgap=50, vgap=5)
        self.lbl_server = wx.StaticText(sb, wx.ID_ANY, "Server")
        self.te_server = wx.TextCtrl(sb, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        self.lbl_port = wx.StaticText(sb, wx.ID_ANY, "Port")
        self.te_port = wx.TextCtrl(sb, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        self.lbl_auth = wx.StaticText(sb, wx.ID_ANY, "Authentication")
        auth_types = ["Windows Authentication", "SQL Server Authentication"]
        self.choice_auth = wx.Choice(sb, choices=auth_types, size=wx.DefaultSize)
        self.Bind(wx.EVT_CHOICE, self.evnt_mssql_auth_type, self.choice_auth)
        self.choice_auth.SetSelection(0)
        databases = ['Microsoft SQL Server     ', 'Oracle', 'MySQL', 'Amazon Redshift']
        self.choice_dbtype = wx.Choice(sb, choices=databases, size=wx.DefaultSize)
        self.Bind(wx.EVT_CHOICE, self.evnt_change_dbtype, self.choice_dbtype)
        self.choice_dbtype.SetSelection(0)
        self.lbl_username = wx.StaticText(sb, wx.ID_ANY, "Username")
        self.te_username = wx.TextCtrl(sb, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.lbl_password = wx.StaticText(sb, wx.ID_ANY, "Password")
        self.te_password = wx.TextCtrl(sb, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.lbl_database = wx.StaticText(sb, wx.ID_ANY, "Database")
        self.te_database = wx.TextCtrl(sb, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.evnt_mssql_auth_type()

        self.set_default_font_style(
            [self.lbl_db_type, self.choice_dbtype, self.lbl_server, self.te_server, self.lbl_port, self.te_port,
             self.lbl_username, self.te_username,
             self.lbl_password, self.te_password,
             self.lbl_database, self.te_database, self.lbl_auth, self.choice_auth])
        self.gsizer_db_details.Add(self.lbl_db_type, pos=(1, 0), flag=wx.ALL | wx.ALIGN_LEFT, border=0)
        self.gsizer_db_details.Add(self.choice_dbtype, pos=(1, 1), flag=wx.EXPAND | wx.ALL | wx.ALIGN_CENTRE, border=0)
        self.gsizer_db_details.Add(self.lbl_server, pos=(2, 0), flag=wx.ALL | wx.ALIGN_LEFT, border=0)
        self.gsizer_db_details.Add(self.te_server, pos=(2, 1), flag=wx.EXPAND | wx.ALIGN_CENTRE, border=0)
        self.gsizer_db_details.Add(self.lbl_port, pos=(3, 0), flag=wx.ALL | wx.ALIGN_LEFT, border=0)
        self.gsizer_db_details.Add(self.te_port, pos=(3, 1), flag=wx.EXPAND | wx.ALIGN_CENTRE, border=0)
        self.gsizer_db_details.Add(self.lbl_auth, pos=(4, 0), flag=wx.ALL | wx.ALIGN_LEFT, border=0)
        self.gsizer_db_details.Add(self.choice_auth, pos=(4, 1), flag=wx.EXPAND | wx.ALIGN_CENTRE, border=0)
        self.gsizer_db_details.Add(self.lbl_username, pos=(5, 0), flag=wx.ALL | wx.ALIGN_LEFT, border=0)
        self.gsizer_db_details.Add(self.te_username, pos=(5, 1), flag=wx.EXPAND | wx.ALIGN_CENTRE, border=0)
        self.gsizer_db_details.Add(self.lbl_password, pos=(6, 0), flag=wx.ALL | wx.ALIGN_LEFT, border=0)
        self.gsizer_db_details.Add(self.te_password, pos=(6, 1), flag=wx.EXPAND | wx.ALIGN_CENTRE, border=0)
        self.gsizer_db_details.Add(self.lbl_database, pos=(7, 0), flag=wx.ALL | wx.ALIGN_LEFT, border=0)
        self.gsizer_db_details.Add(self.te_database, pos=(7, 1), flag=wx.EXPAND | wx.ALIGN_CENTRE, border=0)

        btn_test_connection = wx.Button(sb, wx.ID_ANY, "Test Connection", wx.DefaultPosition, wx.DefaultSize, 0)
        btn_test_connection.SetFont(wx.Font(wx.DEFAULT, wx.DEFAULT, style=wx.NORMAL, weight=wx.NORMAL))
        sbox_db_connection.AddSpacer(10)
        sbox_db_connection.Add(self.gsizer_db_details, 0, wx.LEFT | wx.LEFT , 30)
        sbox_db_connection.AddSpacer(10)
        sbox_db_connection.Add(btn_test_connection, 0, wx.BOTTOM | wx.ALIGN_CENTRE, 10)
        self.gsizer_db_details.SetEmptyCellSize((0, 0))
        return sbox_db_connection

    def evnt_custom_project(self, event=None, hide_ui=None):
        """
        Trigger the event that hides the UI for other project type(Existing Project and From Database) whenever user selects the Custom Project as project type
        :param event: Button event
        :param hide_ui: List of UI to hide(here Existing Project and From Database)
        """
        # self.Center(True)
        self.SetMinSize(wx.Size(wx.DisplaySize()[0] * 0.25, wx.DisplaySize()[1] * 0.22))
        for ui in hide_ui:
            self.sizer.Hide(ui)
        self.Fit()
        self.evnt_mssql_auth_type()
        self.evnt_change_dbtype()

    def evnt_change_project_type_ui(self, event=None, show_ui=None, hide_ui=None, dialog_height=None):
        """
        Show UI dynamically based on the user selection of project type
        :param event: Button event
        :param show_ui: UI to be shown(either Existing Project or From Database)
        :param dialog_height: Height of the dialog box to set
        :return:
        """
        self.sizer.Hide(hide_ui)
        self.sizer.Show(show_ui)
        self.Fit()
        self.evnt_mssql_auth_type()
        self.evnt_change_dbtype()

    def evnt_change_dbtype(self, event=None):
        if self.choice_dbtype.GetSelection() == 0:
            self.lbl_auth.Show(True)
            self.choice_auth.Show(True)
        else:
            self.lbl_auth.Hide()
            self.choice_auth.Hide()
        self.Fit()
        self.evnt_mssql_auth_type()

    def set_default_font_style(self, elements=[]):
        for element in elements:
            element.SetFont(wx.Font(wx.DEFAULT, wx.DEFAULT, style=wx.NORMAL, weight=wx.NORMAL))

    def evnt_mssql_auth_type(self, event=None):
        if self.choice_auth.GetSelection() == 0 and self.choice_dbtype.GetSelection() == 0:
            self.lbl_username.Disable()
            self.te_username.Disable()
            self.lbl_password.Disable()
            self.te_password.Disable()
        else:
            self.lbl_username.Enable(True)
            self.te_username.Enable(True)
            self.lbl_password.Enable(True)
            self.te_password.Enable(True)
        self.Fit()

    def evnt_cancel(self, event=None):
        self.Destroy()
        if not self.from_main_window:
            self.parent.Close()


def project_configuration(event, parent=None, from_main_window=False):
    """
    Open the project configuration window
    :param parent: parent window for the project configuration dialog
    :return: None
    """
    dlg = ProjectConfiguration(parent, from_main_window)
    dlg.Show()
    dlg.Destroy()
