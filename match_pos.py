import docx2txt

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.metrics.pairwise import cosine_similarity

import pandas as pd
import nltk

def matcher(res,jd):
	#nltk.download()
	resume = res #"/Users/amit/Desktop/mohit_project/Dinesh Gandhi.docx" # Change path

	jobDesc = jd #"/Users/amit/Desktop/mohit_project/Senior Project Manager - JG 3.docx" # Change path

	resume_2 = docx2txt.process(resume)

	jobDesc_2 = docx2txt.process(jobDesc)


	############addition########
	to_check = ["JJ","NNS","RB","VB","NN","VBZ","NNP"]

	###########REsume conversion##########

	inter_res =[] 	# intermediate jd list

	for i in resume_2.strip().split():
		inter_res.append(i)

	inter_res_nltk = nltk.pos_tag([i for i in inter_res if i])



	inter_final_res=[]
	i = 0
	while i<len(inter_res_nltk):
		if inter_res_nltk[i][1] in to_check:
			inter_final_res.append(inter_res_nltk[i][0])
		else:
			pass
		i=i+1

	inter_final_res_2 = [i for i in inter_final_res if len(i) > 3]	

	resume_3 = (" ".join(inter_final_res_2))



	#######JD conversion
	inter_jd =[] 	# intermediate jd list

	for i in jobDesc_2.strip().split():
		inter_jd.append(i)

	inter_jd_nltk = nltk.pos_tag([i for i in inter_jd if i])



	inter_final_jd=[]
	i=0
	while i<len(inter_jd_nltk):
		if inter_jd_nltk[i][1] in to_check:
			inter_final_jd.append(inter_jd_nltk[i][0])
		else:
			pass
		i=i+1
	inter_final_jd_2 = [i for i in inter_final_jd if len(i) > 3]

	jobDesc_3 = (" ".join(inter_final_jd_2))

	####################


	text = [resume_3,jobDesc_3]

	#print(text)
	#######sklearn

	cv = CountVectorizer()
	count_matrix = cv.fit_transform(text)

	#print("\n Similarity Scores: ")
	#print(cosine_similarity(count_matrix))


	# Match percentage

	matchPercentage = cosine_similarity(count_matrix)[0][1]*100
	matchPercentage = round(matchPercentage,2)

	print("\n Result for Ananthi Viswakumar\n")

	print("\nYour Resume matches about: " + str( matchPercentage)+ "% of the job description")

	X_train_counts = cv.fit_transform(text)


	x = pd.DataFrame(X_train_counts.toarray(),columns=cv.get_feature_names(),index=['resume','JD'])
	print(x)
	y = x.transpose()

	print("\n")
	print("this is a test")
	common = list((y.loc[(y['resume']!=0) & (y['JD']!=0)]).index)

	print("\nWords not present in resume are: ")
	z = x.columns[(x==0).iloc[0]]
	z1 = z.values.tolist()

	z2 = [x for x in z1 if not (x.isdigit() or x[0] == '-' and x[1:].isdigit())]


	z3 = [i for i in z2 if len(i) > 3]
	#print(z3)

	tagged = nltk.pos_tag(z3)

	final =[]
	i =0

	while i < len(tagged):
		final.append(tagged[i][0])
		i=i+1

	print(final)

	print("\n")




	return matchPercentage,final,common

if __name__ == "__main__":
	loc1 = "/Users/amit/Desktop/mohit_project/Dinesh Gandhi.docx"
	loc2="/Users/amit/Desktop/mohit_project/Senior Project Manager - JG 3.docx"
	matcher(loc1,loc2)
#print(y.query('resume == "0"',inplace = True))

"""
>>> for line in jd_txt.split(" "):
...     content.append(line)
content_2 = nltk.pos_tag([i for i in content if i])

"""

