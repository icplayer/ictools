# -*- coding: utf-8 -*-
'''
Created on 23 maj 2014

@author: Krzysztof Langner
'''

def writeToFile(templatePath, destFilename, params):
    ''' Parse template parameters and write contents to given folder 
        with the same name as template
    '''
    templateFile = open(templatePath, 'r')
    content = templateFile.read()
    templateFile.close()
    for key,value in params.iteritems():
        content = content.replace('{{' + key + '}}', value)
    outFile = open(destFilename, 'w')
    outFile.write(content)
    outFile.close()
