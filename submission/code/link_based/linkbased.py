import networkx as nx
import solr



from urllib2 import *
#conn = urlopen('http://localhost:8983/solr/select?defType=dismax&qf=description^5&q=rifles&wt=python')
list_dict = []

def read_docs():
    conn = urlopen('http://localhost:8983/solr/collection2/select?q=*%3A*&rows=150000&wt=python')
    rsp = eval( conn.read() )
    global list_dict

    for i in range(0,150000):
        d={}
        d["id"] = rsp["response"]["docs"][i]["id"]
        if "seller startdate" in rsp["response"]["docs"][i]:
            d["seller startdate"] = rsp["response"]["docs"][i]["seller startdate"]
        if "url" in rsp["response"]["docs"][i]:
            d["url"] = rsp["response"]["docs"][i]["url"]
        if "latitude" in rsp["response"]["docs"][i]:
            d["latitude"] = rsp["response"]["docs"][i]["latitude"]
        if "longitude" in rsp["response"]["docs"][i]:
            d["longitude"] = rsp["response"]["docs"][i]["longitude"]
        if "itemOffered" in rsp["response"]["docs"][i]:
            d["itemOffered"] = rsp["response"]["docs"][i]["itemOffered"]
        if "title" in rsp["response"]["docs"][i]:
            d["title"] = rsp["response"]["docs"][i]["title"]
        if "description" in rsp["response"]["docs"][i]:
            d["description"] = rsp["response"]["docs"][i]["description"]
        if len(d) == 8:
            list_dict.append(d)

def draw_graph():
    global list_dict
    G=nx.Graph()
    c=0
    for i in range(0,len(list_dict)-1):
        d1 = list_dict[i]
        for j in range(i+1,len(list_dict)):
            d2 = list_dict[j]
            if -124.4<float(d1["longitude"])<-109 and -124.4<float(d2["longitude"])<-109:
                if 31.4<float(d1["latitude"])<42 and 31.4<float(d2["latitude"])<42:
                    G.add_node(d1["id"])
                    G.add_node(d2["id"])
                    G.add_edge(d1["id"],d2["id"],weight=5)
                    date1 = d1["seller startdate"]
                    date2 = d2["seller startdate"]
                    sublist1 = date1.split('-')
                    sublist2 = date2.split('-')
                    if sublist1[0] == sublist2[0] and sublist1[1] == sublist2[1] or d1["itemOffered"] == d2["itemOffered"]:
                        G[d1["id"]][d2["id"]]['weight'] = 10
                    if sublist1[0] == sublist2[0] and sublist1[1] == sublist2[1] and d1["itemOffered"] == d2["itemOffered"]:
                        G[d1["id"]][d2["id"]]['weight'] = 15

                if 42<float(d1["latitude"])<48.7 and 42<float(d2["latitude"])<48.7:
                    G.add_node(d1["id"])
                    G.add_node(d2["id"])
                    G.add_edge(d1["id"],d2["id"],weight=5)
                    date1 = d1["seller startdate"]
                    date2 = d2["seller startdate"]
                    sublist1 = date1.split('-')
                    sublist2 = date2.split('-')
                    if sublist1[0] == sublist2[0] and sublist1[1] == sublist2[1] or d1["itemOffered"] == d2["itemOffered"]:
                        G[d1["id"]][d2["id"]]['weight'] = 10
                    if sublist1[0] == sublist2[0] and sublist1[1] == sublist2[1] and d1["itemOffered"] == d2["itemOffered"]:
                        G[d1["id"]][d2["id"]]['weight'] = 15



            if -109<float(d1["longitude"])<-87.5 and -109<float(d2["longitude"])<-87.5:
                if 31.4<float(d1["latitude"])<42 and 31.4<float(d2["latitude"])<42:
                    G.add_node(d1["id"])
                    G.add_node(d2["id"])
                    G.add_edge(d1["id"],d2["id"],weight=5)
                    date1 = d1["seller startdate"]
                    date2 = d2["seller startdate"]
                    sublist1 = date1.split('-')
                    sublist2 = date2.split('-')
                    if sublist1[0] == sublist2[0] and sublist1[1] == sublist2[1] or d1["itemOffered"] == d2["itemOffered"]:
                        G[d1["id"]][d2["id"]]['weight'] = 10
                    if sublist1[0] == sublist2[0] and sublist1[1] == sublist2[1] and d1["itemOffered"] == d2["itemOffered"]:
                        G[d1["id"]][d2["id"]]['weight'] = 15



                if 42<float(d1["latitude"])<48.7 and 42<float(d2["latitude"])<48.7:
                    G.add_node(d1["id"])
                    G.add_node(d2["id"])
                    G.add_edge(d1["id"],d2["id"],weight=5)
                    date1 = d1["seller startdate"]
                    date2 = d2["seller startdate"]
                    sublist1 = date1.split('-')
                    sublist2 = date2.split('-')
                    if sublist1[0] == sublist2[0] and sublist1[1] == sublist2[1] or d1["itemOffered"] == d2["itemOffered"]:
                        G[d1["id"]][d2["id"]]['weight'] = 10
                    if sublist1[0] == sublist2[0] and sublist1[1] == sublist2[1] and d1["itemOffered"] == d2["itemOffered"]:
                        G[d1["id"]][d2["id"]]['weight'] = 15



            if -87.5<float(d1["longitude"])<-67 and -87.5<float(d2["longitude"])<-67:
                if 31.4<float(d1["latitude"])<42 and 31.4<float(d2["latitude"])<42:
                    G.add_node(d1["id"])
                    G.add_node(d2["id"])
                    G.add_edge(d1["id"],d2["id"],weight=5)
                    date1 = d1["seller startdate"]
                    date2 = d2["seller startdate"]
                    sublist1 = date1.split('-')
                    sublist2 = date2.split('-')
                    if sublist1[0] == sublist2[0] and sublist1[1] == sublist2[1] or d1["itemOffered"] == d2["itemOffered"]:
                        G[d1["id"]][d2["id"]]['weight'] = 10
                    if sublist1[0] == sublist2[0] and sublist1[1] == sublist2[1] and d1["itemOffered"] == d2["itemOffered"]:
                        G[d1["id"]][d2["id"]]['weight'] = 15



                if 42<float(d1["latitude"])<48.7 and 42<float(d2["latitude"])<48.7:
                    G.add_node(d1["id"])
                    G.add_node(d2["id"])
                    G.add_edge(d1["id"],d2["id"],weight=5)
                    date1 = d1["seller startdate"]
                    date2 = d2["seller startdate"]
                    sublist1 = date1.split('-')
                    sublist2 = date2.split('-')
                    if sublist1[0] == sublist2[0] and sublist1[1] == sublist2[1] or d1["itemOffered"] == d2["itemOffered"]:
                        G[d1["id"]][d2["id"]]['weight'] = 10
                    if sublist1[0] == sublist2[0] and sublist1[1] == sublist2[1] and d1["itemOffered"] == d2["itemOffered"]:
                        G[d1["id"]][d2["id"]]['weight'] = 15

    cal_pagerank(G)


def cal_pagerank(G):
    #print G.number_of_nodes()
    #print G.number_of_edges()
    pr = nx.pagerank(G, alpha=0.85,max_iter=100)
    global list_dict
    s = solr.Solr('http://localhost:8983/solr')

    for i in range(0,len(list_dict)):
        try:
            d=list_dict[i]
            if d["id"] in pr:
                d["pagerank"] = pr[d["id"]]
                #print d["id"]
                s.add(d)
                s.commit()
        except solr.core.SolrException:
            pass



def start():
    read_docs()
    draw_graph()

start()
