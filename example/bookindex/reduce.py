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
    word, page_numbers = line.split('\t')
    pages = page_numbers.rstrip()
    if last_word == word:
        for page_number in pages.split(','):
            last_pages.add(page_number)
    else:
        if last_word:
            emit(last_word, last_pages)
        last_word = word
        last_pages = set([pages,])

if last_word != None:
    emit(last_word, last_pages)
