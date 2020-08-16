#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#
# Imports
#
from future import standard_library
standard_library.install_aliases()
from builtins import str
import os
import sys
import urllib.parse
import xbmc
import xbmcaddon

LIB_DIR = xbmc.translatePath( os.path.join( xbmcaddon.Addon(id='plugin.video.uitzendinggemistnet').getAddonInfo('path'), 'resources', 'lib' ) )
sys.path.append (LIB_DIR)

from uitzendinggemistnet_const import ADDON, SETTINGS, LANGUAGE, IMAGES_PATH, DATE, VERSION

# Parse parameters...
if len(sys.argv[2]) == 0:
    #
    # Main menu
    #
    xbmc.log("[ADDON] %s, Python Version %s" % (ADDON, str(sys.version)), xbmc.LOGDEBUG)
    xbmc.log( "[ADDON] %s v%s (%s) is starting, ARGV = %s" % ( ADDON, VERSION, DATE, repr(sys.argv) ), xbmc.LOGDEBUG )

    if SETTINGS.getSetting('onlyshowrecentepisodescategory') == 'true':
        import uitzendinggemistnet_list_episodes as plugin
    else:
        import uitzendinggemistnet_main as plugin
else:
    action = urllib.parse.parse_qs(urllib.parse.urlparse(sys.argv[2]).query)['action'][0]

    xbmc.log("[ADDON] %s, Action: %s" % (ADDON, str(action)), xbmc.LOGDEBUG)

    #
    # list tv shows
    #
    if action == 'list-tv-shows':
        import uitzendinggemistnet_list_tv_shows as plugin
    #
    # List all tv shows
    #
    elif action == 'list-tv-shows-all':
        import uitzendinggemistnet_list_tv_shows_all as plugin
    #
    # List episodes
    #
    elif action == 'list-episodes':
        import uitzendinggemistnet_list_episodes as plugin
    #
    # Play
    #
    elif action == 'play-episode':
        import uitzendinggemistnet_play_episode as plugin
    #
    # Search
    #
    elif action == 'search':
        import uitzendinggemistnet_search as plugin

plugin.Main()
