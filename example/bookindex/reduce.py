#!/usr/bin/python
import sys
pages = set()
word = None
this_word = None

def emit(word, pages):
    sorted_pages = list(pages)
    sorted_pages.sort()
    print('{}\t{}'.format(word, ','.join(sorted_pages)))

for line in sys.stdin:
    this_word, page_numbers = line.split('\t')
    page_numbers = page_numbers.rstrip()
    if this_word == word:
        for page_number in page_numbers.split(','):
            pages.add(page_number)
    else:
        if word:
            emit(word, pages)
        word = this_word
        pages = set([page_numbers,])

if this_word == word:
    emit(word, pages)
