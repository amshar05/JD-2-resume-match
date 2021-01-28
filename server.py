from flask import redirect,  url_for, render_template,request,Flask
from flask_ngrok import run_with_ngrok
from match_pos import matcher
import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import nltk

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])

def home():
	return render_template('Index.html')

@app.route("/result", methods=['GET','POST'])

def result():
	if request.method == 'POST':
		#jd = request.files['jd']
		#resume = request.files['resume']
		if request.files['jd'].filename != "":
			jd = request.files['jd']
			if request.files['resume'].filename!="":
				resume = request.files['resume']

				percentage,word_list,common_list=matcher(resume,jd)

				return render_template("result.html",percentage=percentage,word_list=word_list, common_list= common_list,count_skill=len(word_list),count_common=len(common_list))
			else:
				return render_template("notfound.html")
		else: 
			return render_template("notfound.html")


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port= 5000)


