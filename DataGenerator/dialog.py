#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx, wx.lib.mixins.listctrl as wxlc


class EditVariable(wx.Dialog):
    def __init__(self, parent, data=None):
        wx.Dialog.__init__(self, parent, title='VQ: Edit Variable')

        sizer = wx.BoxSizer(wx.VERTICAL)
        grid = wx.GridBagSizer(6, 6)
        # grid.AddGrowableCol(1)

        grid.Add(wx.StaticText(self, label='Type:'), (0, 0))
        self.choType = wx.Choice(self, choices=['Distributed value',
                                                'Enumerated choice'])
        self.choType.Bind(wx.EVT_CHOICE, self.choType_change)
        grid.Add(self.choType, (0, 1), flag=wx.EXPAND)

        self.lblDistribution = wx.StaticText(self, label='Distribution:')
        self.choDistribution = wx.Choice(self, choices=['Normal',
                                                        'Uniform',
                                                        'Uniform discrete',
                                                        'Geometric',
                                                        'Binomial',
                                                        'Poisson'])
        grid.Add(self.lblDistribution, (1, 0))
        grid.Add(self.choDistribution, (1, 1), flag=wx.EXPAND)
        self.choDistribution.Bind(wx.EVT_CHOICE, self.choDistribution_change)

        self.lblMean = wx.StaticText(self, label='Mean:')
        self.txtMean = wx.TextCtrl(self)
        grid.Add(self.lblMean, (2, 0))
        grid.Add(self.txtMean, (2, 1), flag=wx.EXPAND)

        self.lblVariance = wx.StaticText(self, label='Variance:')
        self.txtVariance = wx.TextCtrl(self)
        grid.Add(self.lblVariance, (3, 0))
        grid.Add(self.txtVariance, (3, 1), flag=wx.EXPAND)

        self.lblStep = wx.StaticText(self, label='Step:')
        self.txtStep = wx.TextCtrl(self)
        grid.Add(self.lblStep, (4, 0))
        grid.Add(self.txtStep, (4, 1), flag=wx.EXPAND)

        self.lblSigFigs = wx.StaticText(self, label='Significant figures:')
        self.txtSigFigs = wx.TextCtrl(self)
        grid.Add(self.lblSigFigs, (5, 0))
        grid.Add(self.txtSigFigs, (5, 1), flag=wx.EXPAND)

        self.lstEnum = EditListCtrl(self)
        self.lstEnum.InsertColumn(0, 'Text')
        self.lstEnum.InsertColumn(1, 'Value')
        self.lstEnum.SetColumnWidth(0, wx.LIST_AUTOSIZE_USEHEADER)
        self.lstEnum.SetColumnWidth(1, wx.LIST_AUTOSIZE_USEHEADER)
        self.lstEnum.setResizeColumn(0)
        self.lstEnum.Append(['', '0'])
        self.lstEnum.SetInitialSize((120, 240))
        grid.Add(self.lstEnum, (6, 0), span=(1, 2), flag=wx.EXPAND | wx.ALL)

        self.btnAdd = wx.Button(self, label='Add')
        self.btnAdd.Bind(wx.EVT_BUTTON, self.btnAdd_click)
        self.btnRemove = wx.Button(self, label='Remove')
        self.btnRemove.Bind(wx.EVT_BUTTON, self.btnRemove_click)
        grid.Add(self.btnAdd, (7, 0))
        grid.Add(self.btnRemove, (7, 1))

        grid.Add(wx.Button(self, label='Test'), (8, 0), span=(1, 2))
        grid.Add(wx.StaticText(self, label='Text:'), (9, 0))
        grid.Add(wx.StaticText(self), (9, 1))
        grid.Add(wx.StaticText(self, label='Value:'), (10, 0))
        grid.Add(wx.StaticText(self), (10, 1))

        buttonsSizer = wx.BoxSizer(wx.HORIZONTAL)
        buttonsSizer.Add(wx.Button(self, label='Save && close'),
                         flag=wx.ALIGN_RIGHT)
        grid.Add(buttonsSizer, (11, 0), span=(1, 2), flag=wx.ALIGN_RIGHT)

        sizer.Add(grid, 0, wx.EXPAND | wx.ALL, 6)

        self.SetSizer(sizer)
        # self.CreateStatusBar()
        self.SetAutoLayout(1)
        sizer.Fit(self)
        self.Show(True)

        grid.SetEmptyCellSize((0, 0))  # added by Jerry
        self.UpdateFields()

    def choType_change(self, e):
        self.UpdateFields()

    def choDistribution_change(self, e):
        self.UpdateFields()

    def UpdateFields(self):
        isDistr = self.choType.GetSelection() == 0

        self.choDistribution.Show(isDistr)
        self.lblMean.Show(isDistr)
        self.txtMean.Show(isDistr)
        self.lblVariance.Show(isDistr)
        self.txtVariance.Show(isDistr)
        self.lblStep.Show(isDistr)
        self.txtStep.Show(isDistr)
        self.lblSigFigs.Show(isDistr)
        self.txtSigFigs.Show(isDistr)

        self.lstEnum.Show(not isDistr)
        self.btnAdd.Show(not isDistr)
        self.btnRemove.Show(not isDistr)

        if isDistr:
            self.lblDistribution.SetLabel('Distribution:')
            n = self.choDistribution.GetSelection()
            if n == 0:
                # Normal
                self.lblMean.SetLabel('Mean:')
                self.lblVariance.SetLabel('Variance:')
                self.lblStep.Hide()
                self.txtStep.Hide()
            elif n == 1:
                # Uniform
                self.lblMean.SetLabel('Minimum:')
                self.lblVariance.SetLabel('Maximum:')
                self.lblStep.Hide()
                self.txtStep.Hide()
            elif n == 2:
                # Uniform discrete
                self.lblMean.SetLabel('Minimum:')
                self.lblVariance.SetLabel('Maximum:')
                self.lblStep.SetLabel('Step:')
            elif n == 3:
                # Geometric
                self.lblMean.SetLabel('Probability:')
                self.lblVariance.Hide()
                self.txtVariance.Hide()
                self.lblStep.Hide()
                self.txtStep.Hide()
            elif n == 4:
                # Binomial
                self.lblMean.SetLabel('Number:')
                self.lblVariance.SetLabel('Probability:')
                self.lblStep.Hide()
                self.txtStep.Hide()
            elif n == 5:
                # Poisson
                self.lblMean.SetLabel('Mean:')
                self.lblVariance.Hide()
                self.txtVariance.Hide()
                self.lblStep.Hide()
                self.txtStep.Hide()
        else:
            self.lblDistribution.SetLabel('Options:')
        # self.Layout()
        self.Fit()  # added by Jerry

    def btnAdd_click(self, e):
        self.lstEnum.Append(['', '0'])
        for i in range(self.lstEnum.GetItemCount() - 1):
            self.lstEnum.Select(i, 0)
        self.lstEnum.Select(self.lstEnum.GetItemCount() - 1)

    def btnRemove_click(self, e):
        item = self.lstEnum.GetFirstSelected()
        while item != -1:
            self.lstEnum.DeleteItem(item)
            item = self.lstEnum.GetFirstSelected()


class EditListCtrl(wx.ListCtrl, wxlc.TextEditMixin,
                   wxlc.ListCtrlAutoWidthMixin):
    def __init__(self, parent, id=-1, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.LC_REPORT):
        wx.ListCtrl.__init__(self, parent, id, pos, size, style | wx.LC_REPORT)
        wxlc.TextEditMixin.__init__(self)
        wxlc.ListCtrlAutoWidthMixin.__init__(self)


if __name__ == '__main__':
    app = wx.App(redirect=False)
    main = EditVariable(None, 'VQ')
    app.MainLoop()
