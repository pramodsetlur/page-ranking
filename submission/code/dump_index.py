import tika
import solr
tika.initVM()
from tika import parser
URLlist = []
items_index_list = []


def items_to_index():
	global items_index_list
	items_index_list.append('Image Width')
	items_index_list.append('File Size')
	items_index_list.append('tiff:ImageLength')
	items_index_list.append('X Resolution')
	items_index_list.append('Image Height')	
	items_index_list.append('File Modified Date')	
	items_index_list.append('Color Space')	
	items_index_list.append('Y Resolution')
	items_index_list.append('tiff:ImageWidth')	
	items_index_list.append('Compression Type')	
	items_index_list.append('Content-Type')	
	items_index_list.append('description')
	#items_index_list.append('title')
	items_index_list.append('keywords')
	items_index_list.append('author')
	items_index_list.append('owner')
	#items_index_list.append('resourceName')
	items_index_list.append('dc:title')
	items_index_list.append('PICS-Label')
	
	#print items_index_list
	
# Reads dump file and extracts only image URLs and writes to a file called URLlist.txt
def read_dump():
	fr = open('dump','r')
	fw = open('URLlist.txt','w')
	lines = fr.readlines()
	for i in range(0,len(lines)):
		sublist = []
		if lines[i].startswith("URL"):
			sublist = lines[i].split(":: ")
			if len(sublist) > 1:
				if sublist[1].endswith("html\n") or sublist[1].endswith("jpg\n") or sublist[1].endswith("JPG\n") or sublist[1].endswith("png\n") or sublist[1].endswith("PNG\n") or sublist[1].endswith("gif\n") or sublist[1].endswith("GIF\n") or sublist[1].endswith("bmp\n") or sublist[1].endswith("BMP\n"):
					fw.write((sublist[1].strip('\n'))+'\n')
					
	fr.close()
	fw.close()

# Reads URLlist.txt and extracts metadata from the image URLs using tika parser and writes the metadata to image_metadata.txt	
def extract_metadata():
	global URLlist
	s = solr.Solr('http://localhost:8983/solr')
	fr = open('URLlist.txt','r')
	lines = fr.readlines()
	for line in lines:
		URLlist.append(line.strip('\n'))
	fr.close()
	
	c=100
	for i in range(0,len(URLlist)):
		parsed = parser.from_file(URLlist[i])
		d = {}
		c+=1
		d["id"] = c
		d["url"] = URLlist[i]
		for k,v in parsed["metadata"].iteritems():
			if k in items_index_list:
				try:
					d[str(k)] = v
				except:
					d[str(k)] = v.encode('utf-8')
		print d
		s.add(d)
		s.commit()
		

def main():
	items_to_index()
	read_dump()
	extract_metadata()

if __name__ == '__main__':
	main()
