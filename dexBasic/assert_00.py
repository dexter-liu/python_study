#!/usr/bin/env python
# -*- coding:utf-8 -*-

# assert用于判断一个表达式，在表达式条件为false的时候触发异常

import sys
assert ('linux' in sys.platform), "该代码只能运行在linux环境上"

print('run on linux')