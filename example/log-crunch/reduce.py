#!/usr/bin/python
import sys
last_host = None
last_count = 0
host = None
for line in sys.stdin: # pre-sorted by Hadoop or our shell pipeline
    host, count = line.split('\t')
    count = int(count)
    if last_host == host: # add more to sum for this host
        last_count += count
    else: # new host -- print last host & count, reset both
        if last_host: # don't print first line
            print '%s\t%s' % (last_host, last_count)
        last_host = host
        last_count = count
if last_host == host: # last line different (we just reset stuff), print
    print '%s\t%s' % (last_host, last_count)
