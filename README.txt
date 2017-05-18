NLTK (Natural Language Toolkit) is a platform that works with human language data. It categorizes text, analyzing linguistic structure to draw insights from raw data.
It provides various text processing libraries for tokenization, tagging, stemming, etc. 
Among those libraries, tokenization and tagging were used in this assignment. 

-------------------------------------------------------------------------------------------------------------------

Installation Instructions. 

1. Open Terminal
2. Make a directory using mkdir command
3. Download files from Github reposistory
4. Install dependencies as follows:
   sudo pip install -U nltk
   sudo pip install requests
5. Run Data cleaning script using the following command
   python data_cleaning.py 
6. The output can be seen in the file output_csv.csv     

-------------------------------------------------------------------------------------------------------------------


The following steps were followed to attain a solution close to accuracy: 
1. Identify rows that were wrongly Title cased. 
2. Tokenize the raw text and tag each token with part-of-speech tag( eg., noun, verb, adjective, etc). 
   Identifying words that are proper nouns helps us create a list of only those words that are to be Capitalized.
3. The list of nouns identified are then compared to a word list which consists of all the words in the English language dictionary. If a noun is not present in the word list then it is most likely a proper noun.  
4. Finally we go over every row that are title cased in the original CSV file, convert the row to sentence case and  identify proper nouns and replace it with Capital case.


-------------------------------------------------------------------------------------------------------------------

Limitations: 

1. Although NLTK is a powerful module, it is challenge to correct identify nouns and proper nouns. 
(For eg, words such as Presenting, Presented as wrongly classified as proper nouns since they're in Title case in the raw text)
2. Certain words like Homeownership that appear in the original CSV file are wrongly classified as proper noun. This is 
due to spelling mistakes in the CSV file. Ideally "Homeownership" should have been "Home ownership", in which case they would not have been idenfied as proper nouns.

-------------------------------------------------------------------------------------------------------------------


Overcome Challenges:

1. Filter out verbs that have been falsely identified as Proper nouns.
Eg: Words like Boating, Bored (which are verbs) are falsely identified as proper nouns because they begin with capital letters.
2. Filter out false positive proper nouns by utilizing a word dictionary.
If a noun is NOT present in the word dictionary, then it most likely is a Proper Noun.







