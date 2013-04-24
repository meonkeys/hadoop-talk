% Introduction to MapReduce with Hadoop on Linux
% Adam Monsen
% April 28, 2013

# Welcome!

<!--
Conference: LinuxFest Northwest 2013
Target audience experience level: intermediate
-->

- this is the Hadoop talk
- see my article in the [April 2013 issue of Linux Journal](http://www.linuxjournal.com/content/april-2013-issue-linux-journal-high-performance-computing)
- thank you BLUG and LFNW
- please donate to support this conference

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

- MapReduce provides a pattern to scale **big**
- Hadoop provides an implementation of MapReduce

# Diagram: MapReduce overview

![MapReduce diagram](Mapreduce_Overview.svg)\ 

<div class="handout">
The above diagram is a [work of Wikipedia user Poposhka](http://en.wikipedia.org/wiki/File:Mapreduce_Overview.svg), used here in accordance with the [Creative Commons](http://en.wikipedia.org/wiki/Creative_Commons) [Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/).
</div>

# Example: Log crunching

- TODO: real example, 10-50GB or so of log data (whatever
  it takes to realize a slowdown on my desktop and a speedup
  on Elastic MapReduce)
- TODO: actually try it on Elastic MapReduce

# Example: Create a book index

- TODO (see code on Windows laptop)

# Dumbo

- TODO: revisit examples above in Dumbo

# Screenshot: Elastic MapReduce

# Screenshot: NameNode

# Screenshot: JobTracker

# Conclusion

<!--
vim: ft=markdown
-->

