#@coding  :utf-8
#@FileName: bin.py
#@Author  :辰晨
#@Time    :2019/4/25 15:54

import sys
import os

from mudule import main
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_DIR)

main.main()