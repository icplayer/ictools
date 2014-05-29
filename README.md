# ictools

Python tools for processing icplayer files. Contains the following packages:
* icplayer to [qti](http://www.imsglobal.org/question/) converter
* icplayer to [epub3](http://idpf.org/epub/30) converter

## Installation
* Download code using git or 'Download ZIP' button
* Extract to folder _ictools_
* Download SCORM package with lesson and extract it to folder _lesson_

## QTI converter
To convert lesson to QTI package run converter with the command:
```sh
python ictools/src/convert_qti.py <lesson_path> <destination_folder>
```


## Supported modules
Only the following modules are supported:
* Text
* Image
* Choice
