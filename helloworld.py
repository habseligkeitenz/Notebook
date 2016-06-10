# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 14:08:58 2016

@author: zoujinyong
"""
"""
from lxml import etree,html

path = "build.html"

content = open(path,"rb").read()

page = html.document_fromstring(content)

text = page.text_content()

print text
"""
from numpy import *

mymatrix = mat([[-1,3],[2,-1],[0,1]])
#print(mymatrix)

mymatrix2 = 1.5*ones([3,3])
#print(mymatrix2)

#print multiply(mymatrix,mymatrix2)
mymatrix3 = mat([[2,0,3,1],[1,5,-2,4]])
print mymatrix3
print multiply(mymatrix,mymatrix3)