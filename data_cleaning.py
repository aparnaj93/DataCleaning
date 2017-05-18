import csv
import nltk
# NLTK is a leading platform for building Python programs to work with human language data
# http://www.nltk.org/
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('words')
from nltk.corpus import words

print("Running data cleaning script")

#List of english words
word_list=words.words()

#Open CSV file for reading
f = open('jr_data_engineer_assignment.csv','rU')
readCSV=csv.reader(f)
	
all_nouns = []      
#For every row in the CSV file, do the following:
for row in readCSV:
	#Description is the second column
	description = row[1]
	#If the row is in title case  
	if description.istitle():
		#Tokenize each word in the description
		tokens = nltk.word_tokenize(description)
		#tag each token
		tagged = nltk.pos_tag(tokens)
		#Filter out words which are NOUNS
		nouns = [words for words,pos in tagged if (pos=='NNP' or pos=='NNPS')]
		#Add it to the list of all_nouns
		all_nouns.extend(nouns)
		
#Eliminate duplicates by converting to set
all_nouns = set(all_nouns)
proper_nouns = []
		
for noun in all_nouns:
# Filter out plurals and verbs to eliminate False positives.
	if noun.endswith('s') or noun.endswith('ing') or noun.endswith('ed'):
		continue
	else:
	# If noun is not in word_list, then it is most likely a Proper noun
		if noun.lower() not in word_list:
			proper_nouns.append(noun)

proper_nouns=set(proper_nouns)			
f.close()

# Open CSV file again for reading
f=open('jr_data_engineer_assignment.csv','rU')
readCSV=csv.reader(f)

# Open empty CSV file for writing result
w = open('output_csv.csv','w')
# Reset pointer to beginning of the file
w.seek(0)
output_file=csv.writer(w, delimiter=',')
# Add headers to CSV file
output_file.writerow(['id','description'])

for row in readCSV:
	if row[1].istitle():
		# Convert to sentence case from title case (i.e Capitalize first letter of every sentence)
		# For example, "Hello There. My Name Is Aparna" becomes "Hello there. My name is aparna"
		description = '. '.join(x.lower().capitalize() for x in row[1].split('. '))
		# Convert description into list of Title case words.
		# For eg, "Hello there. My name is aparna" ----> ["Hello", "There.", "My", "Name", "Is", "Aparna"] 
		list_words = description.title().split(' ')
		# Remove "." and "," from words in list_words
		list_words=[word[:-1] if word.endswith('.') or word.endswith(',') else word for word in list_words]
		# Check if the list of words contains any Proper nouns.
		replacements = proper_nouns.intersection(list_words)
		# For every word in the replacements, do the following:
		for word in replacements:
			# Replace the word in description with it's sentence form.
			# For Eg: Consider the description "Hi my name is aparna".
			# Assume that "Aparna" is a proper-noun. We replace "aparna" with "Aparna" in the description.  
			description = description.replace(word.lower(), word)
		output_file.writerow([row[0],description])	

f.close()
w.close()	

print ("Data Cleaning successfully completed. Output file saved as output_csv.csv")		
