# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger('ploomcake.pa')


def uninstall(portal, reinstall=False):
    if not reinstall:
        # Don't want to delete stuff on reinstall
        setup_tool = portal.portal_setup
        setup_tool.runAllImportStepsFromProfile('profile-ploomcake.pa:uninstall')
        logger.info("Uninstalled")
