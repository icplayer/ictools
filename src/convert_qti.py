# -*- coding: utf-8 -*-
'''
Created on 2014-05-29

@author: Krzysztof Langner
'''

import sys

from qti.assessment import convert


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "syntax:\n convert_qti <lesson_path> <destination_path>\n"
        sys.exit()

    convert(sys.argv[1], sys.argv[2])
