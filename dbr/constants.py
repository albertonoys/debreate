# -*- coding: utf-8 -*-

## \package dbr.constants
#  
#  Global variables used throughout the application & should remain constant.


# System imports
import sys, os

# wx imports
import wx

# Debreate imports
from dbr.language import GT


# *** System Information *** #

## Full path to the application's directory
#  
#  FIXME: Hack to get parent directory
application_path = os.path.dirname(os.path.dirname(__file__))

## Root home directory where configuration is stored
#  
#  The configuration file is set to <HOME>/.config/debreate/config
home_path = os.getenv(u'HOME')

## Directory where local files will be stored
#  
#  <HOME>/.local/share/debreate
local_path = u'{}/.local/share/debreate'.format(home_path)


# *** Debreate Information *** #

## Application's displayed name
APP_NAME = GT(u'Debreate')

# Version information #
RELEASE = 0
VER_MAJ = 0
VER_MIN = 7
VER_REL = 11

if not RELEASE:
    VER_REL += 1

VERSION = (VER_MAJ, VER_MIN, VER_REL)
VERSION_STRING = u'{}.{}.{}'.format(VER_MAJ, VER_MIN, VER_REL)

# Development version
if not RELEASE:
    VERSION_STRING = u'{}-dev'.format(VERSION_STRING)

# Website & hosting information #
HOMEPAGE = u'http://debreate.sourceforge.net/'
gh_project = u'https://github.com/AntumDeluge/debreate'
sf_project = u'https://sourceforge.net/projects/debreate'

PROJECT_FILENAME_SUFFIX = u'dbpz'

# *** Python Info *** #

PY_VER_MAJ = sys.version_info[0]
PY_VER_MIN = sys.version_info[1]
PY_VER_REL = sys.version_info[2]
PY_VER_STRING = u'{}.{}.{}'.format(PY_VER_MAJ, PY_VER_MIN, PY_VER_REL)


# *** wxWidgets Info *** #

WX_VER_STRING = u'{}.{}.{}'.format(wx.MAJOR_VERSION, wx.MINOR_VERSION, wx.RELEASE_VERSION)


# *** Custom IDs *** #
ID_OVERWRITE = wx.NewId()
ID_APPEND = wx.NewId()
# FIXME: Unused IDs
ID_BIN = wx.NewId()
ID_SRC = wx.NewId()
ID_DSC = wx.NewId()
ID_CNG = wx.NewId()

# Page IDs
ID_BUILD = wx.NewId()
ID_CHANGELOG = wx.NewId()
ID_CONTROL = wx.NewId()
ID_COPYRIGHT = wx.NewId()
ID_DEPENDS = wx.NewId()
ID_FILES = wx.NewId()
ID_GREETING = wx.NewId()
ID_MAN = wx.NewId()
ID_MENU = wx.NewId()
ID_SCRIPTS = wx.NewId()


# *** Icons *** #
ICON_ERROR = u'{}/bitmaps/error64.png'.format(application_path)
ICON_INFORMATION = u'{}/bitmaps/question64.png'.format(application_path)


# *** Colors depicting importance of fields
Mandatory = (255,200,192)
Recommended = (197,204,255)
Optional = (255,255,255)
Unused = (200,200,200)
Disabled = (246, 246, 245)


## Location of common licenses installed on the system
system_licenses_path = u'/usr/share/common-licenses'
