"""Extract text from various types of files"""

import os
import textract

path = 'module6/dummy/'
files = os.listdir(path)
for f in sorted(files):
    text = textract.process(path+f)
    print(text.decode('utf-8').strip())
