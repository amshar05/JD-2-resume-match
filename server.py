from flask import redirect,  url_for, render_template,request,Flask
from match_pos import matcher
from spacy_try import spacy_match
import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import nltk

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])

def home():
	return render_template('index.html')

@app.route("/result", methods=['GET','POST'])

def result():
	if request.method == 'POST':
		#jd = request.files['jd']
		#resume = request.files['resume']
		if request.files['jd'].filename != "":
			jd = request.files['jd']
			if request.files['resume'].filename!="":
				resume = request.files.getlist('resume')
				print("this is the list:")
				name_list = []
				i = 0
				while i < len(resume):
					name_list.append(resume[i].filename.split(".")[0])
					i=i+1
				id_list = []
				percentage,word_list,common_list=matcher(resume,jd)				
				k=0
				while k < len(percentage):
					id_list.append(k)
					k=k+1
				zip_list = zip(percentage,word_list,common_list,name_list,id_list)
				
				return render_template("result.html",zip_list = zip_list)#percentage=percentage,word_list=word_list, common_list= common_list,count_skill=len(word_list),count_common=len(common_list))
			else:
				return render_template("notfound.html")
		else: 
			return render_template("notfound.html")

@app.route("/newresult",methods=['GET','POST'])

def newresult():
	if request.method == 'POST':
		#jd = request.files['jd']
		#resume = request.files['resume']
		if request.files['jd'].filename != "":
			jd = request.files['jd']
			if request.files['resume'].filename!="":
				resume = request.files.getlist('resume')
				print("this is the list:")
				name_list = []
				i = 0
				while i < len(resume):
					name_list.append(resume[i].filename.split(".")[0])
					i=i+1
				id_list = []
				percentage,word_list,common_list=spacy_match(resume,jd)				
				k=0
				while k < len(percentage):
					id_list.append(k)
					k=k+1
				zip_list = zip(percentage,word_list,common_list,name_list,id_list)
				
				return render_template("newresult.html",zip_list = zip_list)#percentage=percentage,word_list=word_list, common_list= common_list,count_skill=len(word_list),count_common=len(common_list))
			else:
				return render_template("notfound.html")
		else: 
			return render_template("notfound.html")


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0')


