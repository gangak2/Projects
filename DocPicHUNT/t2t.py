
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
import numpy.linalg as LA
import re
from stemming.porter import stem
import Image




def split(paragraph):
    sentenceEnders = re.compile('[, .!?\n]*')
    sentenceList = sentenceEnders.split(paragraph)
    return sentenceList



def stemming(paragraph):
	temp=split(paragraph)
	for i in range(len(temp)):
		temp[i]=stem(temp[i])
	temp_x = ' '.join(temp)
	return temp_x


def text2text(test_file, suggest):



	no_of_suggestion = suggest

	file=open('stopwords.txt','r')
	p=file.read().replace("'",' ').replace("`",'').replace(";",'').replace("!",'.').lower()
	stopWords=split(p)

	#print("Enter 0 for image->text, 1 for image->image, 2 for text->image, 3 for text->text")
	#user_input = int(raw_input("Enter your input: "))



	train_set=[]
	for i in range(1,40):
		file=open('Data_text/'+str(i)+'.txt','r')
		source_p=file.read().replace("'",' ').replace("`",'').replace(";",'').replace("!",'.').replace('"',' ').lower()
		temp = stemming(source_p)
		train_set.append(temp) #Documents
	#print train_set
	#print train_set


	test_set=[]
	file=open('test/'+test_file,'r')
	source_p=file.read().replace("'",' ').replace("`",'').replace(";",'').replace("!",'.').replace('"',' ').lower()
	temp=stemming(source_p)
	test_set.append(temp)
	#print test_set


	vectorizer = CountVectorizer(stop_words = stopWords)
	#print vectorizer
	transformer = TfidfTransformer()
	#print transformer



	trainVectorizerArray = vectorizer.fit_transform(train_set).toarray()
	testVectorizerArray = vectorizer.transform(test_set).toarray()
	#print 'Fit Vectorizer to train set', trainVectorizerArray
	#print 'Transform Vectorizer to test set', testVectorizerArray
	cx = lambda a, b : round(np.inner(a, b)/(LA.norm(a)*LA.norm(b)), 3)



	transformer.fit(trainVectorizerArray)

	train_list = transformer.transform(trainVectorizerArray).toarray()

	transformer.fit(testVectorizerArray)
 
	test_list = transformer.transform(testVectorizerArray).toarray()



	cosine_list=[]
	for vector in train_list:
		for testV in test_list:
			cosine = cx(vector, testV)
        	cosine_list.append(cosine)
#print cosine_list



	sorted_indices = sorted(range(len(cosine_list)), key=lambda i: cosine_list[i])[-no_of_suggestion:]
	#print sorted_indices
	#print len(sorted_indices)


	for i in range(len(sorted_indices)):
		file=open('Data_text/'+str(sorted_indices[i]+1)+'.txt','r')
		source=file.read()
		print("Article no. "+str(i+1))
		print sorted_indices[i]+1
		print source
		print("*******************************************************************************************************************")
		print
		print





