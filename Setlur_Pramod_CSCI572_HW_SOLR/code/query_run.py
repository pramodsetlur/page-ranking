__author__ = 'sanjay'

import solr
from urllib2 import *
query_list =[]
query_list.append('http://localhost:8983/solr/collection2/select?defType=edismax&qf=description^10&qf=itemOffered^10&q=(itemOffered:Shotguns AND geo_name:Idaho)&fq={!field f="seller startdate" op=Contains}[2010-10]&rows=150&wt=json&indent=true')
query_list.append('http://localhost:8983/solr/collection2/select?defType=edismax&qf=description^10&qf=title^10&q=description:nuclear OR description:chemical OR description:fusion OR description:fission&rows=1500&wt=json&indent=true')
query_list.append('http://localhost:8983/solr/collection2/select?q=(description:ad OR url:ad OR title:ad) AND (geo_name:Texas)&facet=true&facet.date=tstamp&facet.date.start=NOW/month-12MONTHS&facet.date.end=NOW/MONTH&facet.date.gap=%2B1MONTH')
#query_list.append('http://localhost:8983/solr/collection2/select?defType=edismax&qf=description^10&qf=title^10&q=description:nuclear%20OR%20description:chemical&rows=1500&wt=json&indent=true')
for i in range(0,len(query_list)):
    conn = urlopen(query_list[i])
    rsp = eval(conn.read())
    for i in range(0,len(rsp['response']['docs'])):
        print "tstamp:", rsp["response"]["docs"][i]["seller startdate"]
        print "availableAtOrFrom:", rsp["response"]["docs"][i]["availableAtOrFrom"]
        print "title:", rsp["response"]["docs"][i]["title"]
        print "description:", rsp["response"]["docs"][i]["description"]
    print '\n'
