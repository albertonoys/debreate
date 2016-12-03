# -*- coding: utf-8 -*-

## \package dbr.wizard

# MIT licensing
# See: docs/LICENSE.txt


import wx
from wx.lib.newevent import NewCommandEvent

from dbr.buttons        import ButtonNext
from dbr.buttons        import ButtonPrev
from dbr.language       import GT
from globals.ident      import ID_BUILD
from globals.ident      import ID_GREETING
from globals.ident      import ID_NEXT
from globals.ident      import ID_PREV
from globals.tooltips   import TT_wiz_next
from globals.tooltips   import TT_wiz_prev


## Wizard class for Debreate
class Wizard(wx.Panel):
    def __init__(self, parent, page_list=None):
        wx.Panel.__init__(self, parent, wx.ID_ANY, page_list)
        
        # List of pages available in the wizard
        self.pages = []
        
        # A Header for the wizard
        pnl_title = wx.Panel(self, style=wx.RAISED_BORDER)
        pnl_title.SetBackgroundColour((10, 47, 162))
        
        # Text displayed from objects "name" - object.GetName()
        self.txt_title = wx.StaticText(pnl_title, label=GT(u'Title'))
        self.txt_title.SetForegroundColour((255, 255, 255))
        
        # font to use in the header
        headerfont = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        
        self.txt_title.SetFont(headerfont)
        
        # Previous and Next buttons
        self.btn_prev = ButtonPrev(self)
        self.btn_prev.SetToolTip(TT_wiz_prev)
        self.btn_next = ButtonNext(self)
        self.btn_next.SetToolTip(TT_wiz_next)
        
        self.ChangePageEvent, self.EVT_CHANGE_PAGE = NewCommandEvent()
        self.evt = self.ChangePageEvent(0)
        
        # These widgets are put into a list so that they are not automatically hidden
        self.permanent_children = (pnl_title, self.btn_prev, self.btn_next)
        
        # *** Layout *** #
        
        # Position the text in the header
        lyt_title = wx.GridSizer(1, 1)
        lyt_title.Add(self.txt_title, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL)
        pnl_title.SetSizer(lyt_title)
        pnl_title.Layout()
        
        # Button sizer includes header
        lyt_buttons = wx.BoxSizer(wx.HORIZONTAL)
        lyt_buttons.AddSpacer(5)
        lyt_buttons.Add(pnl_title, 1, wx.EXPAND|wx.RIGHT, 5)
        lyt_buttons.Add(self.btn_prev)
        lyt_buttons.AddSpacer(5)
        lyt_buttons.Add(self.btn_next)
        lyt_buttons.AddSpacer(5)
        
        lyt_main = wx.BoxSizer(wx.VERTICAL)
        lyt_main.Add(lyt_buttons, 0, wx.EXPAND)
        
        self.SetSizer(lyt_main)
        self.SetAutoLayout(True)
        self.Layout()
        
        # *** Event handlers *** #
        
        self.btn_prev.Bind(wx.EVT_BUTTON, self.ChangePage)
        self.btn_next.Bind(wx.EVT_BUTTON, self.ChangePage)
    
    
    ## TODO: Doxygen
    def ChangePage(self, event=None):
        event_id = event.GetEventObject().GetId()
        
        # Get index of currently shown page
        for page in self.pages:
            if page.IsShown():
                index = self.pages.index(page)
                
                break
        
        if event_id == ID_PREV:
            if index != 0:
                index -= 1
        
        elif event_id == ID_NEXT:
            if index != len(self.pages) - 1:
                index += 1
        
        page_id = self.pages[index].GetId()
        
        # Show the indexed page
        self.ShowPage(page_id)
        
        wx.GetApp().GetTopWindow().menu_page.Check(page_id, True)
    
    
    ## TODO: Doxygen
    def ClearPages(self):
        for page in self.pages:
            self.GetSizer().Remove(page)
        
        self.pages = []
        
        # Re-enable the buttons if they have been disabled
        self.EnableNext()
        self.EnablePrev()
    
    
    ## TODO: Doxygen
    def DisableNext(self):
        self.EnableNext(False)
    
    
    ## TODO: Doxygen
    def DisablePrev(self):
        self.EnablePrev(False)
    
    
    ## TODO: Doxygen
    def EnableNext(self, value=True):
        if isinstance(value, (bool, int)):
            if value:
                self.btn_next.Enable()
            
            else:
                self.btn_next.Disable()
        
        else:
            # FIXME: Should not raise error here???
            raise TypeError(u'Must be bool or int value')
    
    
    ## TODO: Doxygen
    def EnablePrev(self, value=True):
        if isinstance(value, (bool, int)):
            if value:
                self.btn_prev.Enable()
            
            else:
                self.btn_prev.Disable()
        
        else:
            # FIXME: Should not raise error here???
            raise TypeError(u'Must be bool or int value')
    
    
    ## TODO: Doxygen
    def GetCurrentPageId(self):
        for page in self.pages:
            if page.IsShown():
                return page.GetId()
    
    
    ## TODO: Doxygen
    def GetPage(self, page_id):
        for P in self.pages:
            if P.GetId() == page_id:
                return P
        
        return None
    
    
    ## Retrieves the full list of page IDs
    #  
    #  \return
    #        \b e\ tuple : List of all page IDs
    def GetPagesIdList(self):
        page_ids = []
        
        for P in self.pages:
            page_ids.append(P.GetId())
        
        return tuple(page_ids)
    
    
    ## TODO: Doxygen
    def SetPages(self, pages):
        initial_id = pages[0].GetId()
        
        # Make sure all pages are hidden
        children = self.GetChildren()
        for child in children:
            if child not in self.permanent_children:
                child.Hide()
        
        # Remove any current pages from the wizard
        self.ClearPages()
        
        if not isinstance(pages, (list, tuple)):
            # FIXME: Should not raise error here???
            raise TypeError(u'Argument 2 of Wizard.SetPages() must be List or Tuple')
        
        for page in pages:
            self.pages.append(page)
            self.GetSizer().Insert(1, page, 1, wx.EXPAND)
        
        self.ShowPage(initial_id)
        
        self.Layout()
    
    
    ## TODO: Doxygen
    def SetTitle(self, title):
        self.txt_title.SetLabel(title)
        self.Layout()
    
    
    ## TODO: Doxygen
    def ShowPage(self, page_id):
        for p in self.pages:
            if p.GetId() != page_id:
                p.Hide()
            
            else:
                p.Show()
                self.txt_title.SetLabel(p.GetName())
        
        if page_id == ID_GREETING:
            self.btn_prev.Enable(False)
        
        else:
            self.btn_prev.Enable(True)
        
        if page_id == ID_BUILD:
            self.btn_next.Enable(False)
        
        else:
            self.btn_next.Enable(True)
        
        self.Layout()
        
        for child in self.GetChildren():
            wx.PostEvent(child, self.evt)
