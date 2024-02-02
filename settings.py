#!/usr/bin/env python
# -*- coding: utf-8 -*-

# settings.py
from dotenv import load_dotenv, find_dotenv
from pathlib import Path

# 自动搜索 .env 文件
load_dotenv(find_dotenv(),verbose=True,override=True)
