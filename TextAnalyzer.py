#import TextHighlighter
import Corpus
import nltk 
from nltk.corpus import stopwords
from nltk.corpus import wordnet

stop_words = set(stopwords.words('english'))

def rawText(file):

    processed = []
    file = file.lower()
    sentences = nltk.sent_tokenize(file) #Splits the text file into multiple setences
    for sentence in sentences:
        tokens = nltk.word_tokenize(sentence) #Tokenizes the setence

        filtered_words = [] #Used to remove any filler words
        for index in range(len(tokens)):
            if tokens[index] not in stop_words and tokens[index] != "the":
                if tokens[index].isdigit() and index >0: #Adjust this to find the previous JJ or JJs
                    filtered_words.append(tokens[index] + " " + tokens[index-1])
                    filtered_words.append(tokens[index-1] + " " + tokens[index])
                filtered_words.append(tokens[index])
            index+=1

        #print(filtered_words)
        tag = nltk.pos_tag(filtered_words) #Tags the non-stop words
        #print(tag)
        refinedList = []

        for tags in tag:
            if tags[1] == 'NNP' or tags[1] == 'CD' or tags[1] == 'NN': #Gonna restrict the criteria for parsing even move this to corpus to check dictionary as a way to restrict
                tokens.append(tags[0])

    #print(file)
    return Corpus.corpusMatch(tokens, file)
    #TextHighlighter.highlightedKeywords(tokens, refinedList)
'''
def providedKeywordContext(keyWords):

    context = [()]
    for words in KeyWords:
        context.append(Corpus.checkCorpus(word[0]))
'''


#rawText("Metro 9417 Alpha 417 Imperial detention 239 contest 865 Imperial Beach Boulevard deserve 53 copy will generate a walk-up response crash, accident")