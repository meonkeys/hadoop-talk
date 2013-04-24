shell: clean
	./map.py < log.txt | sort | ./reduce.py

hadoop: clean
	$(HADOOP_PREFIX)/bin/hadoop jar $(HADOOP_PREFIX)/contrib/streaming/hadoop-streaming-1.0.4.jar -mapper map.py -reducer reduce.py -input log.txt -output output

clean:
	$(RM) -r output
