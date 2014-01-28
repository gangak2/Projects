
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
import numpy.linalg as LA
import re
from stemming.porter import stem
import Image
from subprocess import call

no_of_suggestion = 3


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



file=open('stopwords.txt','r')
p=file.read().replace("'",' ').replace("`",'').replace(";",'').replace("!",'.').lower()
stopWords=split(p)

print("Enter 0 for image->text, 1 for image->image, 2 for text->image, 3 for text->text")
user_input = int(raw_input("Enter your input: "))



train_set=[]
for i in range(1,40):
	if(user_input==0 or user_input==3):
		file=open('Data_text/'+str(i)+'.txt','r')
	elif(user_input==1 or user_input==2):
		file=open('Data_image/Tags/'+str(i/10)+'.txt','r')
	source_p=file.read().replace("'",' ').replace("`",'').replace(";",'').replace("!",'.').replace('"',' ').lower()
	temp = stemming(source_p)
	train_set.append(temp) #Documents
	#print train_set
print train_set


test_set=[]
if (user_input==0 or user_input==1):
	string = raw_input("Enter name of the test image file: ")
	file=open('test_images/'+string[:-4]+'.txt','r')
elif (user_input==2 or user_input==3):
	string = raw_input("Enter name of the test document file: ")
	file=open('test/'+string,'r')
else:
	print ("Incorrect input")



source_p=file.read().replace("'",' ').replace("`",'').replace(";",'').replace("!",'.').replace('"',' ').lower()
temp=stemming(source_p)
test_set.append(temp)
print test_set


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
    #print vector
    for testV in test_list:
        #print testV
        cosine = cx(vector, testV)
        cosine_list.append(cosine)
print cosine_list



sorted_indices = sorted(range(len(cosine_list)), key=lambda i: cosine_list[i])[-no_of_suggestion:]
print sorted_indices
print len(sorted_indices)


if(user_input==0 or user_input==3):
	for i in range(len(sorted_indices)):
		file=open('Data_text/'+str(sorted_indices[i]+1)+'.txt','r')
		call(['gedit ', 'Data_text/'+str(sorted_indices[i]+1)+'.txt']);
		source=file.read()
		print("Article no. "+str(i+1))
		print sorted_indices[i]+1
		print source
		print("*******************************************************************************************************************")
		print
		print
		
elif(user_input==1 or user_input==2):
	for i in range(len(sorted_indices)):
		img = Image.open(r"Data_image/"+str(sorted_indices[i]+1)+'.jpg')
		img.show()



