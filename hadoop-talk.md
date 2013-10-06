% Introduction to MapReduce with Hadoop
% Adam Monsen
% October 11, 2013

# Welcome!

<!--
Conference: SeaGL 2013
Target audience experience level: intermediate
-->

- this is the Hadoop talk
- see my article in the [April 2013 issue of Linux Journal](http://www.linuxjournal.com/content/april-2013-issue-linux-journal-high-performance-computing)
- thank you SCCC

<div class="handout">
You'll laugh and you'll cry during this awe-inspiring introduction to big data
processing with MapReduce and Hadoop. I only tested my code on Ubuntu GNU/Linux
and only provide specific instructions for same, but all code is cross-platform.
</div>

# How do you scale when you must?

# Bigger hardware

> In pioneer days they used oxen for heavy pulling, and when one ox couldn't
> budge a log, they didn't try to grow a larger ox. We shouldn't be trying for
> bigger computers, but for more systems of computers. --Grace Hopper

# Try "smarter"

- say we're at the limits of our hardware
- how do we "throw more hardware" at our problem?

# Scale out

- scaling _out_ is hard
    - partitioning
    - communication
    - synchronization
    - hardware failure
    - different paradigms ("process" vs. "job")
    - hardest part is making the above easy

# Hadoop and MapReduce

- MapReduce provides a pattern to scale arbitrarily, linearly
- Hadoop provides an implementation of MapReduce

# Diagram: MapReduce overview

![MapReduce diagram](Mapreduce_Overview.svg)\ 

<div class="handout">
The above diagram is a [work of Wikipedia user Poposhka](http://en.wikipedia.org/wiki/File:Mapreduce_Overview.svg), used here in accordance with the [Creative Commons](http://en.wikipedia.org/wiki/Creative_Commons) [Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/).
</div>

# Example: Log crunching

1. shell version, small input file
    - map only, then add reduce
1. streaming: local (single-node) hadoop
1. Dumbo local
1. Dumbo hadoop

<div class="handout">
These demos are in `example/log-crunch`. Before you start, download and install
Java Hadoop. I used OpenJDK 7 (installed via apt-get) and Hadoop 1.2.1
(downloaded tarball and untarred) when testing these examples. I configured my
environment like so:

    export HADOOP_PREFIX=/heap/tmp/hadoop-1.2.1
    export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64

Install dumbo if you want to run the dumbo examples. I used `easy_install`,
following the [directions on their wiki](https://github.com/klbostee/dumbo/wiki/Building-and-installing).

Here is how to run examples for each of the above bullets:

1. `./map.py < log.txt`, then `make shell`
1. `make hadoop`
1. `make dumbo-local`
1. `make dumbo-hadoop`

`reduce.py` assumes valid input (key=hostname, tab, value=integer), grouped by
key (hostname). It must manually total up values for each consecutive group of
keys (hostnames).

The dumbo example is simpler because our reducer function is guaranteed to only
get one key and a list of associated values.

`map.py` and `reduce.py` borrowed heavily from
[Michael Knoll's post on Hadoop MapReduce in Python](http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/).
</div>

# Log crunching, more data

- shell version with a 1.4G input file took 44 seconds
    - 8-way Intel i7, 8GB RAM, SSD
- streaming with 667M input file on Elastic MapReduce took 7 minutes
    - 1x m1.small master, 2x m1.small core
- much more data needed to overcome cluster overhead

<hr />

> In a one-meter race between a rocket and a scooter, the scooter is gone
> before the rocket's engines are started.

<div class="handout">
Generated large data files like so:
<pre>
for i in {1..100}; do cat log.txt &gt;&gt; /tmp/data23k; done
for i in {1..100}; do cat /tmp/data23k &gt;&gt; /tmp/data2.3M; done
for i in {1..30}; do cat /tmp/data2.3M &gt;&gt; /tmp/data67M; done
for i in {1..10}; do cat /tmp/data67M &gt;&gt; /tmp/data667M; done
for i in {1..20}; do cat /tmp/data67M &gt;&gt; /tmp/data1.4G; done
</pre>
</div>

# Example: Create a book index

- book text
- partially reduced key,value pairs
- final output
- walk through dumbo `mapper()` and `reducer()`

# The End

* <http://adammonsen.com/talks>
* <https://github.com/meonkeys/hadoop-talk>
* [do you have enough data to justify Hadoop?](http://www.chrisstucchio.com/blog/2013/hadoop_hatred.html)

<!--
vim: ft=markdown
-->
