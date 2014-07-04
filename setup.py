#!/usr/bin/env python
from distutils.core import setup, Extension

opts = dict(name='ebp',
            packages=['ebp',
                      'ebp.leastsqbound'])

if __name__ == '__main__':
    setup(**opts)
