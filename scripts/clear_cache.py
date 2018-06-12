#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
import glob

files = glob.glob('./cache/*')
for f in files:
  os.remove(f)