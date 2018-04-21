#!python
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 22, 2017 Tue
# Last update :
# Est time    :

# Imports
from __future__ import print_function, with_statement, division, unicode_literals, absolute_import
import string

# Global Variables
ofile = 'greek_parenthesis.csv'
grk = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa',
       'lambda', 'mu', 'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi',
       'chi', 'psi', 'omega', 'Gamma', 'Delta', 'Theta', 'Lambda', 'Xi', 'Pi', 'Sigma', 'Phi', 'Psi']
alph = list('abgdezhqiklmnxoprstufcywGDQLXPSFY')
comment = r""

data = [  # greek
    # greek parenthesis
    ['Parenthesis', '', 'rr', '', '(\\', ')'],

]


def snippet(h0, h1, p0, p1, b0, b1):
  for i in range(len(grk)):
    snip = p0 + alph[i]+p1+','+b0+grk[i]+b1+','
    print(snip, file=open(ofile, 'a'))


def main():
  open(ofile, 'w')
  for d in data:
    h0, h1, p0, p1, b0, b1 = d
    snippet(h0, h1, p0, p1, b0, b1)


if __name__ == "__main__":
  main()
