#!python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Jul 24, 2017 Mon
# Last update : 
#
# Imports
from __future__ import print_function, with_statement,division,unicode_literals, absolute_import

# Lists
headers, prefixes, bodies = [], [], []

def parse_atom_snippets():
    h = ''
    with open('a.cson', 'r') as fin, open('tmp.csv', 'w') as fo:
        for line in fin:
            parts = line.split(':')
            if ':' in line and 'prefix' in line:
                h = parts[1].strip()
                h = h.replace("'", "")
                
            if ':' in line and 'body' in line:
                bodies.append(parts[1])
                body = parts[1]
                body = parts[1].split(r'\n')
                for b in body:
                    b = b.replace('\\ $0','')
                    b = b.replace('\\\\\\\\','\\')
                    b = b.replace('\\$','$')
                    b = b.replace('\\partial','\\partial{')
                    b = b.replace("'",'')
                    if not b == "'''":
                      output = h.strip() + ',"'.lstrip() + b
                      output = output.replace('" ', '"')
                      fo.write(output)
    
if __name__ == '__main__':
    parse_atom_snippets()


"""
Exceptions:
a)
n0x n1x etc
search for " u}

b) n0 n1 etc
search for \\\

c) search for \boldsymbol{

conflicts:
tbx  \boldsymbol{x}
tbx $\bar{\tau}$


"""
