# -*- coding:utf-8 -*-
import re
def ReadFile(filename):
    with open(filename,'r') as f:
        return f.read()

#print ReadFile("data.txt")
