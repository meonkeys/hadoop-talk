shell: book.txt clean map.py reduce.py
	python map.py < $< | sort | python reduce.py

hadoop: book.txt clean map.py reduce.py
	$(HADOOP_PREFIX)/bin/hadoop jar $(HADOOP_PREFIX)/contrib/streaming/hadoop-streaming-1.2.1.jar -mapper map.py -reducer reduce.py -input $< -output output

dumbo-local: book.txt clean with-dumbo.py
	dumbo start with-dumbo.py -input $< -outputformat text -output output

dumbo-hadoop: book.txt clean with-dumbo.py
	dumbo start with-dumbo.py -hadoop $(HADOOP_PREFIX) -input $< -outputformat text -output output

clean:
	@$(RM) -r output EGG-INFO dumbo tests typedbytes.*
