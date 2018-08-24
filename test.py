# from nltk.tokenize import RegexpTokenizer
#
# text = "plot: two teen couples?? go to a church!! || party , drink and then drive."
#
# tokenizer  = RegexpTokenizer(r'\w+')
# tokens = tokenizer.tokenize(text)
# print(tokens)



import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize

afile = open("CDotNotes_Example_Combined.txt", encoding='utf-8')
atext = afile.read()
print("###Original Text\r\n")
print(atext + "\r\n")
# print("###Split Text - sorted\r\n")
# print(sorted(atext.split()))
# print("\r\n###Tokenized Text - sorted")
# print(sorted(word_tokenize(atext)))

print("###Split Text\r\n")
print(atext.split())
print("\r\n###Tokenized Text")
print(word_tokenize(atext))

arrayStopWordsExclusion = ['from', 'to']
arrayStandardStopWords= stopwords.words('english')
sRegExp = "[\w]+"

# Function to exclude a group of words from standard stopwords list, e.g 'from', 'to', etc.
def modifyStopWords(arrayStandardStopWords, arrayExclusionStopWords):
    # arrayStandardStopWords_modified = [sw for sw in arrayStandardStopWords if sw.lower() not in arrayExclusionStopWords ]
    arrayStandardStopWords_modified = arrayStandardStopWords
    for esw in arrayExclusionStopWords:
        if esw in arrayStandardStopWords_modified:
            arrayStandardStopWords.remove(esw)
    return arrayStandardStopWords_modified


# Function to remove symboles and stops words
def removeStopWords(arrayTokens, arrayStopWords):
    returnTokens = arrayTokens
    for wd in returnTokens:
        if wd in arrayStopWords:
            returnTokens.remove(wd)
    return returnTokens

# Function to remove a token that does not contain letters and numbers.
def removeSymboles(arrayTokens, sRegExp):
    returnTokens = arrayTokens
    RegExpMatcher = re.compile(sRegExp)
    for wd in returnTokens:
        print("word is: " + wd)
        if RegExpMatcher.search(wd) is None:
            returnTokens.remove(wd)
    return returnTokens