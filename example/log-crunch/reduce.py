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
    else: # new host -- maybe print, reset state
        if last_host:
            print '%s\t%s' % (last_host, last_count)
        last_host = host
        last_count = count
if last_host == host:
    print '%s\t%s' % (last_host, last_count)
