# -*- coding: utf-8 -*-

## \package dbr.distcache

# MIT licensing
# See: docs/LICENSE.txt


import os, wx

from dbr.dialogs            import BaseDialog
from dbr.language           import GT
from dbr.panel              import BorderedPanel
from dbr.textpreview        import TextPreview
from globals.system         import FILE_distnames, UpdateDistNamesCache
from globals.fileio import ReadFile
from dbr.log import Logger


## Dialog displaying controls for updating distribution names cache file
class DistNamesCacheDialog(BaseDialog):
    def __init__(self):
        BaseDialog.__init__(self, title=GT(u'Update Dist Names Cache'),
                style=wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER)
        
        self.SetMinSize(wx.Size(300, 150))
        
        txt_types = wx.StaticText(self, label=GT(u'Include the following:'))
        
        pnl_types = BorderedPanel(self)
        
        self.chk_unstable = wx.CheckBox(pnl_types, label=GT(u'Unstable'))
        self.chk_obsolete = wx.CheckBox(pnl_types, label=GT(u'Obsolete'))
        self.chk_generic = wx.CheckBox(pnl_types, label=GT(u'Generic (Debian names only)'))
        
        self.btn_preview = wx.Button(self, label=GT(u'Preview cache'))
        btn_update = wx.Button(self, label=GT(u'Update cache'))
        
        # Keep preview dialog in memory so position/size is saved
        self.preview = TextPreview(self, title=GT(u'Available Distribution Names'),
                size=(500,400))
        
        # *** Event Handling *** #
        
        self.btn_preview.Bind(wx.EVT_BUTTON, self.OnPreviewCache)
        btn_update.Bind(wx.EVT_BUTTON, self.OnUpdateCache)
        
        # *** Layout *** #
        
        lyt_types = wx.BoxSizer(wx.VERTICAL)
        lyt_types.AddSpacer(5)
        
        for CHK in (self.chk_unstable, self.chk_obsolete, self.chk_generic,):
            lyt_types.Add(CHK, 0, wx.LEFT|wx.RIGHT, 5)
        
        lyt_types.AddSpacer(5)
        
        pnl_types.SetAutoLayout(True)
        pnl_types.SetSizerAndFit(lyt_types)
        pnl_types.Layout()
        
        lyt_buttons = wx.BoxSizer(wx.HORIZONTAL)
        lyt_buttons.Add(self.btn_preview, 1)
        lyt_buttons.Add(btn_update, 1)
        
        lyt_main = wx.BoxSizer(wx.VERTICAL)
        lyt_main.Add(txt_types, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT|wx.TOP, 5)
        lyt_main.Add(pnl_types, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT, 5)
        lyt_main.Add(lyt_buttons, 1, wx.ALIGN_CENTER|wx.ALL, 5)
        
        self.SetAutoLayout(True)
        self.SetSizer(lyt_main)
        self.Layout()
        
        # *** Post-layout Actions *** #
        
        if not os.path.isfile(FILE_distnames):
            self.btn_preview.Disable()
        
        if self.Parent:
            self.CenterOnParent()
    
    
    ## Opens cache file for previewing
    def OnPreviewCache(self, event=None):
        self.preview.SetValue(ReadFile(FILE_distnames))
        self.preview.ShowModal()
    
    
    ## Creates/Updates the distribution names cache file
    def OnUpdateCache(self, event):
        Logger.Debug(__name__, GT(u'Updating cache ...'))
        
        # FIXME: Should open a new thread & show progress dialog that can be cancelled
        title_orig = self.GetTitle()
        self.SetTitle(GT(u'Updating cache ...'))
        
        self.Disable()
        
        wx.Yield()
        # FIXME: Should check timestamps to make sure file was updated
        UpdateDistNamesCache(self.chk_unstable.GetValue(), self.chk_obsolete.GetValue(),
                self.chk_generic.GetValue())
        
        self.SetTitle(title_orig)
        self.Enable()
        
        self.btn_preview.Enable(os.path.isfile(FILE_distnames))
