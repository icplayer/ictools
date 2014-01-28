# -*- coding: utf-8 -*-
'''
Created on 27-01-2014

@author: Krzysztof Langner

Text utils
'''

import re

    
def fixHtml(text):
    ''' Fix html problems. Make it valid XML
    '''
    xhtml = text.replace("<br>", "<br/>")
    xhtml = xhtml.replace("&nbsp;", " ")
    xhtml = re.sub(r'{{\d:([^}]+)}}', r'\\choice{\1}', xhtml)
    return xhtml