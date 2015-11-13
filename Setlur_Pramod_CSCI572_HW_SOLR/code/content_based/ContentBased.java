package ContentBasedRanking;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class tfidf {

	static List<String> stop_words =new ArrayList<String>();
	public static HashMap<DocObject, HashMap<String, Float>> doc_tf_map = new HashMap<DocObject, HashMap<String, Float>>();
	public static HashMap<String, Integer> word_dict= new HashMap<String, Integer>();
	public static HashMap<String, Float> idf= new HashMap<String, Float>();
	public static HashMap<String,Float>tfidf_query=new HashMap<String, Float>();
	public static HashMap<DocObject,HashMap<String, Float>>tfidf_doc=new HashMap<DocObject, HashMap<String, Float>>();
	public static HashMap<DocObject,Float> cosine_similarity=new HashMap<DocObject,Float>();
	@SuppressWarnings("rawtypes")
	public static void main(String[] args) throws Exception
	{
		
		
		ReadLines("stop_words");
		int id, content;
		File doc1 = new File("index");
		FileReader fr1 = new FileReader(doc1);
		BufferedReader b1 = new BufferedReader(fr1);
		StringBuffer stringBuffer1 = new StringBuffer();
		String line1, mysz2;
		//Read from the file
		String url=null;
		List<DocObject> documents= new ArrayList<DocObject>();
		line1 = b1.readLine();
		mysz2 = line1.replaceAll("\\s","");
		
		while (line1 != null) {
			DocObject doc11 = new DocObject();
			id=0;
			content=0;
			
			while ( id==0 || content==0 )
			{
				String[] line2=mysz2.split("::");
				if(line2[0].equals("id"))
				{
					id=1;
					doc11.id=line2[1].toString();
				}
				else if(line2[0].equals("content"))
				{
					content=1;
					doc11.content=line2[1];
				}
				line1=b1.readLine();
				mysz2 = line1.replaceAll("\\s","");
				
			}
			documents.add(doc11);
		}
		
		
		
		
		
		//Calculating the term frequencies for each doc
		for(DocObject doc : documents)
		{
			HashMap<String, Float> term_to_freq= new HashMap<String, Float>();
			String[] tokens=doc.content.split(" ");
			
			for(String word: tokens)
			{
				
				if(term_to_freq.containsKey(word.toLowerCase()))
				{
					term_to_freq.put(word.toLowerCase(), term_to_freq.get(word) + 1);
				}
				else
				{
					term_to_freq.put(word.toLowerCase(),(float) 1);
				}
				
				
			}
			
			for(Map.Entry<String, Float> words: term_to_freq.entrySet())
			{
					term_to_freq.put(words.getKey().toLowerCase(), words.getValue()/tokens.length);
			}
			
			doc_tf_map.put(doc,term_to_freq);
		}
		
		//Mapping all words to the number of documents they are present in
		for(Map.Entry<DocObject, HashMap<String, Float>> entry : doc_tf_map.entrySet())
		{
			for(Map.Entry<String, Float> term_to_freq: entry.getValue().entrySet())
			{
				
				if(word_dict.containsKey(term_to_freq.getKey().toLowerCase()))
				{
					word_dict.put(term_to_freq.getKey().toLowerCase(), word_dict.get(term_to_freq.getKey().toLowerCase()) + 1);
				}
				else
				{
					word_dict.put(term_to_freq.getKey().toLowerCase(), 1);
				}		
			}
		}
		
		//IDF calculation
		for(Map.Entry<String, Integer> entry : word_dict.entrySet())
		{
			idf.put(entry.getKey(), (float) (1+(float)(Math.log(documents.size()/(float)entry.getValue()))));
		}
		
		
		//print the idf values
		for(Map.Entry<String, Float> entry : idf.entrySet())
		{
			System.out.println(entry.getKey() + " : " + entry.getValue());
			
		}
		
		//Parsing the query
		String query="life learning";
		String []queryList=query.split(" ");
		
		//Calculating tf for query
		HashMap<String, Float> query_term_to_freq= new HashMap<String, Float>();
		for(String word: queryList)
		{
			
			if(query_term_to_freq.containsKey(word.toLowerCase()))
			{
				query_term_to_freq.put(word.toLowerCase(), query_term_to_freq.get(word) + 1);
			}
			else
			{
				query_term_to_freq.put(word.toLowerCase(),(float) 1);
			}
			
			
		}
		
		for(Map.Entry<String, Float> words: query_term_to_freq.entrySet())
		{
			query_term_to_freq.put(words.getKey().toLowerCase(), words.getValue()/queryList.length);
		}
		
		
		//tf-idf for query terms
		for(Map.Entry<String, Float> words: query_term_to_freq.entrySet())
		{
			if(idf.containsKey(words.getKey().toLowerCase()))
			{
				tfidf_query.put(words.getKey().toLowerCase(), words.getValue() * idf.get(words.getKey().toLowerCase()));
			}
			else
			{
				tfidf_query.put(words.getKey().toLowerCase(),(float) 0);
			}
			
		}
		
		//print the query tf idf values
		
				for(Map.Entry<String, Float> entry : tfidf_query.entrySet())
				{
					System.out.println(entry.getKey() + " : " + entry.getValue());
					
				}
		
				
		//tf -idf for query terms in documents
		for(DocObject doc : documents)
		{
			HashMap<String, Float> tfidf= new HashMap<String, Float>();
			for(Map.Entry<String, Float> words: query_term_to_freq.entrySet())
			{
				if(idf.containsKey(words.getKey().toLowerCase()) && doc_tf_map.get(doc).containsKey(words.getKey().toLowerCase()))
				{
					tfidf.put(words.getKey().toLowerCase(), doc_tf_map.get(doc).get(words.getKey().toLowerCase()) * idf.get(words.getKey().toLowerCase()));
				}
				else
				{
					tfidf.put(words.getKey().toLowerCase(),(float) 0);
				}
			}
			tfidf_doc.put(doc, tfidf);
		}
		
		//print the tfidf values for document
		
		for(Map.Entry<DocObject, HashMap<String, Float>> entry : tfidf_doc.entrySet())
		{
			System.out.println(entry.getKey().id);
			for(Map.Entry<String, Float> words: entry.getValue().entrySet())
			{
				System.out.println(words.getKey() + " : " + words.getValue());
			}
			System.out.println();
		}
		
		double modquery=0;
		//Calculate modquery
		for(Map.Entry<String, Float> entry : tfidf_query.entrySet())
		{
			modquery+=Math.pow(entry.getValue(), 2);
		}
		modquery=Math.sqrt(modquery);
		//finding cosine similarity
		for(Map.Entry<DocObject, HashMap<String, Float>> entry : tfidf_doc.entrySet())
		{
			cosine_similarity.put(entry.getKey(), (float) (dotproduct(tfidf_query,tfidf_doc.get(entry.getKey()))/(moddocument(tfidf_doc.get(entry.getKey())) * modquery)));
		}
		
		//print cosine similarity
		
		System.out.println("Cosine similarity");
		for(Map.Entry<DocObject,Float> entry : cosine_similarity.entrySet())
		{
			System.out.println(entry.getKey().id +" : " + entry.getValue());
		}
		
		for(Map.Entry<DocObject, HashMap<String, Float>> entry : tfidf_doc.entrySet())
		{
			System.out.println(entry.getKey().id);
			for(Map.Entry<String, Float> words: entry.getValue().entrySet())
			{
				System.out.println(words.getKey() + " : " + words.getValue());
			}
			System.out.println();
		}
		//Printing the term frequencies for each doc
		/*for(Map.Entry<DocObject, HashMap<String, Float>> entry : doc_tf_map.entrySet())
		{
			System.out.println(entry.getKey().id);
			for(Map.Entry<String, Float> words: entry.getValue().entrySet())
			{
				System.out.println(words.getKey() + " : " + words.getValue());
			}
			System.out.println();
		}*/
		
		
		
		
		
	}
		
	private static double dotproduct(HashMap<String,Float> querytfidf, HashMap<String,Float> doctfidf)
	{
		double dotprod=0;
		for(Map.Entry<String, Float> entry : tfidf_query.entrySet())
		{
			dotprod+=(entry.getValue() * doctfidf.get(entry.getKey()));
		}
		return dotprod;
	}
	
	private static double moddocument(HashMap<String,Float> doctfidf)
	{
		double modquery=0;
		for(Map.Entry<String, Float> entry : doctfidf.entrySet())
		{
			modquery+=Math.pow(entry.getValue(), 2);
		}
		modquery=Math.sqrt(modquery);
		return modquery;
	}
	
	private static void ReadLines(String fileName) throws IOException {
		// TODO Auto-generated method stub
		File doc1 = new File(fileName);
		FileReader fr1 = new FileReader(doc1);
		BufferedReader b1 = new BufferedReader(fr1);
		String line1;
		String url=null;
		//read line from the file
		while ((line1 = b1.readLine()) != null) {
			if(!(line1.equals("") || line1.equals(null)))
			{
				stop_words .add(line1.trim());
			}
		}
		
	}


	
}
