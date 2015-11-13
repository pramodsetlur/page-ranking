#Page Ranking
###Building an Apache-Solr  based Search Engine, Ranking Algorithms and NER for Weapons Datasets

The solr config folder "config_files" contains schema.xml and solrconfig.xml

##Task #2
dump_index.py is present in code/indexing_data. 
It indexes the metadata extracted from the dump file to Solr.

NER_index.py is present in code/indexing_data
The response of each Html/image to OCR, GeoTopic parser and Ctakes is indexed to Solr

###Task #3
ContentBased.java is located in code/content_based. This implements the content based algorithm.
linkbased.py is located in code/link_based. This implements the link based algorithm.


###Task #5
query_run.py is located in code/. This runs the queries in task #4.
$ python query_run.py > /tmp/output


###Task #6
bin/indexDirectory files indexDir Ldadir
bin/queryWithVSM indexDir queryDir resultsDirSVM
bin/queryWithLDA indexDir Ldadir queryDir resultsDirLDA