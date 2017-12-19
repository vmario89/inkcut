#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2017, Jairus Martin.

Distributed under the terms of the GPL v3 License.

The full license is in the file LICENSE, distributed with this software.

Created on Jul 12, 2015

@author: jrm
"""
import faulthandler
from inkcut.core.workbench import InkcutWorkbench


def main():
    faulthandler.enable()
    workbench = InkcutWorkbench()
    workbench.run()

if __name__ == '__main__':
    main()

