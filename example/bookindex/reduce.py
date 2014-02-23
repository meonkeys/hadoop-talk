#!/usr/bin/python
import sys
last_word = None
last_pages = set()
word = None

def emit(word, pages):
    sorted_pages = list(pages)
    sorted_pages.sort()
    print('{}\t{}'.format(word, ','.join(sorted_pages)))

for line in sys.stdin:
    word, page = line.rstrip().split('\t')
    if last_word == word:
        last_pages.add(page)
    else:
        if last_word:
            emit(last_word, last_pages)
        last_word = word
        last_pages = set([page,])

if last_word != None:
    emit(last_word, last_pages)
