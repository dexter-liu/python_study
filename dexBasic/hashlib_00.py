#!/usr/bin/env python
# -*- coding:utf-8 -*-

import hashlib

md = hashlib.sha1()
md.update('你好'.encode('utf-8'))
rel = md.hexdigest()
print(rel)
print(len(rel))


md_1 = hashlib.sha1()
md_1.update(bytes('你好', encoding='utf-8'))
rel = md_1.hexdigest()
print(rel)
print(len(rel))


md_1 = hashlib.sha1()
md_1.update(b'123ABC')
rel = md_1.hexdigest()
print(rel)
print(len(rel))


h = hashlib.new('sha1', b'123ABC')
print(h.digest())
print(h.hexdigest())

print(hashlib.algorithms_guaranteed)
print()
print(hashlib.algorithms_available)

print('-'*50)
high = hashlib.sha1(b'123')
print(high.name)
high.update('你好'.encode('utf-8'))
print(high.block_size)
rel_high = high.hexdigest()
print(rel_high)
