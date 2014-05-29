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

    lesson_path = sys.argv[1]
    dest_path = sys.argv[2] 
    if not dest_path.endswith("/"):
        dest_path += "/"
    convert(lesson_path, dest_path)
