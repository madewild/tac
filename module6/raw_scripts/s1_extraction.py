"""Extract text from various types of files"""

import os
import textract

path = 'module6/dummy/'
files = os.listdir(path)
for f in sorted(files):
    try:
        text = textract.process(os.path.join(path, f))
        print(text.decode('utf-8').strip())
    except Exception as e:
        print(os.path.join(path, f), e)
