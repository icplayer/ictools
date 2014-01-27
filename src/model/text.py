# -*- coding: utf-8 -*-
'''
Created on 27-01-2014

@author: Krzysztof Langner

Text utils
'''

    
def fixHtml(text):
    ''' Fix html problems. Make it valid XML
    '''
    xhtml = text.replace("<br>", "<br/>")
    xhtml = xhtml.replace("&nbsp;", " ")
    return xhtml