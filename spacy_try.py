# pip install spacy
# python -m spacy download en_core_web_sm

import spacy
from two_lists_similarity import Calculate_Similarity as cs
from scipy import spatial
from collections import Counter
import math
from statistics import mean
import docx2txt
# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

# Process whole documents

def spacy_match(res,jd):
	score_22= []
	common_score_list =[]
	not_common_list = []
	
	for i in res:
		
		text = docx2txt.process(i)
		text_2= docx2txt.process(jd)


		doc = nlp(text)
		doc2 = nlp(text_2)

		jd_1 = []
		res_1= []
		label_type = ["GPE" , "DATE", "PRODUCT","CARDINAL","NORP","MONEY","PERSON"]
		for entity in doc.ents:
			if entity.label_ not in label_type:
				#print(entity.label_,entity.text)
				jd_1.append(entity.text)

		jobd = [i.replace("\n","") for i in jd_1]


		print("\nthis is new line\n")
		for entity in doc2.ents:
			if entity.label_ not in label_type:
				print(entity.label_,entity.text)
				res_1.append(entity.text)
		resum= [i.replace("\n","") for i in res_1]
		jobd =list(dict.fromkeys(jobd))
		jobd = [str(i) for i in jobd]
		resum = list(dict.fromkeys(resum))
		resum = [str(i) for i in resum]


		def word2vec(word):
		    from collections import Counter
		    from math import sqrt

		    # count the characters in word
		    cw = Counter(word)
		    # precomputes a set of the different characters
		    sw = set(cw)
		    # precomputes the "length" of the word vector
		    lw = sqrt(sum(c*c for c in cw.values()))

		    # return a tuple
		    return cw, sw, lw

		def cosdis(v1, v2):
		    # which characters are common to the two words?
		    common = v1[1].intersection(v2[1])
		    # by definition of cosine distance we have
		    return sum(v1[0][ch]*v2[0][ch] for ch in common)/v1[2]/v2[2]


		list_A = resum
		list_B = jobd
		score=[]
		common_word_1 = []
		threshold = 0.8     # if needed
		for key in list_A:
		    for word in list_B:
		        try:
		            result = cosdis(word2vec(word), word2vec(key))
		            score.append(result)
		            if result > threshold:
		            	common_word_1.append(word)
		            	print("the word is : {} and key is: {} by percentge: {}".format(word, key, result))
		        except IndexError:
		            pass

		mean_score = mean(score)
		mean_score_2 = round(mean_score*100,2)
		#not_common = list(set(resum) - set(common_word_1))
		not_common=list(dict.fromkeys(resum))
		common_word_1=list(dict.fromkeys(common_word_1))
		

		score_22.append(mean_score_2)
		common_score_list.append(common_word_1)
		not_common_list.append(not_common)


	return score_22,not_common_list, common_score_list



if __name__ == "__main__":
	loc1 = ["/Users/amit/Desktop/mohit_project/Ananthi Viswakumar.docx"]
	loc2=str("/Users/amit/Desktop/mohit_project/JDs.docx")
	print(spacy_match(loc1,loc2))

#csObj = cs(jd, res)


#x = csObj.fuzzy_match_output()

#print(csObj.similar_input_items())






