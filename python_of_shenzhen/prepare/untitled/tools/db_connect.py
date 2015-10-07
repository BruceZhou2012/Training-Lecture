#!/usr/bin/env python
# coding:utf8
# ==============================================================================
__author__ = 'gubaoer'
# Created: 2014-07-17
# ==============================================================================

import sys, os
# import op_config
# sys.path.append(tri_config.Working_dir)
absolute_file = os.path.realpath(__file__)
# print absolute_file
project_dir = os.path.dirname(os.path.dirname(absolute_file))
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'untitled.settings'
# ----------------Use Django Mysql model----------------
from cmdb.models import *
