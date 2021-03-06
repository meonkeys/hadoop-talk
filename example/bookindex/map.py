#!/usr/bin/python
import re,sys
for line in sys.stdin:
    page_name, text = line.split(':')
    text = text.rstrip()
    page_number = page_name.split('-')[1]
    words = re.findall('\w+', text)
    for word in words:
        if len(word) < 4: continue
        print('{}\t{}'.format(word.lower(), page_number))
