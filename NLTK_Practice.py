import nltk, re
from nltk import word_tokenize, RegexpTokenizer, pos_tag, ne_chunk
from nltk.corpus import stopwords

myRegexpTokenizer = RegexpTokenizer(r'\w+')

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
        # print("word is: " + wd)
        if RegExpMatcher.search(wd) is None:
            returnTokens.remove(wd)
    return returnTokens

try:
    # CDotNotes_0708_Gen_Med_AM_Rounds_File = open("CDotNotes_0708_Gen_Med_AM_Rounds.txt",encoding = 'utf-8')
    # CDotNotes_0930_AM_Patient_Care_Record_File = open("CDotNotes_0930_AM_Patient_Care_Record.txt", encoding='utf-8')
    # CDotNotes_1355_Occupational_Therapy_File = open("CDotNotes_1355_Occupational_Therapy.txt", encoding='utf-8')
    # CDotNotes_1603_WRN_Review_File = open("CDotNotes_1603_WRN_Review.txt", encoding='utf-8')
    # CDotNotes_1643_Physiotherapy_File = open("CDotNotes_1643_Physiotherapy.txt", encoding='utf-8')
    # CDotNotes_2253_Review_n_SignOff_DP_File = open("CDotNotes_2253_Review&SignOff_DP.txt", encoding='utf-8')
    # CDotNotes_2353_Discharge_Follow_Up_Plan_File = open("CDotNotes_2353_Discharge_Follow_Up_Plan.txt", encoding='utf-8')
    #
    # CDotNotes_0708_Gen_Med_AM_Rounds_Text = CDotNotes_0708_Gen_Med_AM_Rounds_File.read()
    # CDotNotes_0930_AM_Patient_Care_Record_Text = CDotNotes_0930_AM_Patient_Care_Record_File.read()
    # CDotNotes_1355_Occupational_Therapy_Text = CDotNotes_1355_Occupational_Therapy_File.read()
    # CDotNotes_1603_WRN_Review_Text = CDotNotes_1603_WRN_Review_File.read()
    # CDotNotes_1643_Physiotherapy_Text = CDotNotes_1643_Physiotherapy_File.read()
    # CDotNotes_2253_Review_n_SignOff_DP_Text = CDotNotes_2253_Review_n_SignOff_DP_File.read()
    # CDotNotes_2353_Discharge_Follow_Up_Plan_Text = CDotNotes_2353_Discharge_Follow_Up_Plan_File.read()

    # Tokenization with word_tokenizer and RegexpTokenizer
    # CDotNotes_0708_Gen_Med_AM_Rounds_Text_Tokens = nltk.word_tokenize(CDotNotes_0708_Gen_Med_AM_Rounds_Text)
    # CDotNotes_0930_AM_Patient_Care_Record_Text_Tokens = nltk.word_tokenize(CDotNotes_0930_AM_Patient_Care_Record_Text)
    # CDotNotes_1355_Occupational_Therapy_Text_Tokens = nltk.word_tokenize(CDotNotes_1355_Occupational_Therapy_Text)
    # CDotNotes_1603_WRN_Review_Text_Tokens = nltk.word_tokenize(CDotNotes_1603_WRN_Review_Text)
    # CDotNotes_1643_Physiotherapy_Text_Tokens = nltk.word_tokenize(CDotNotes_1643_Physiotherapy_Text)
    # CDotNotes_2253_Review_n_SignOff_DP_Text_Tokens = nltk.word_tokenize(CDotNotes_2253_Review_n_SignOff_DP_Text)
    # CDotNotes_2353_Discharge_Follow_Up_Plan_TextTokens = nltk.word_tokenize(CDotNotes_2353_Discharge_Follow_Up_Plan_Text)
    # CDotNotes_All_Text = CDotNotes_0708_Gen_Med_AM_Rounds_Text + "\r\n" + CDotNotes_0930_AM_Patient_Care_Record_Text + "\r\n" + CDotNotes_1355_Occupational_Therapy_Text + "\r\n" + CDotNotes_1603_WRN_Review_Text + "\r\n" + CDotNotes_1643_Physiotherapy_Text + "\r\n" + CDotNotes_2253_Review_n_SignOff_DP_Text + "\r\n" + CDotNotes_2353_Discharge_Follow_Up_Plan_Text

    CDotNotes_Example_Combined_File = open("CDotNotes_Example_Combined.txt", encoding='utf-8')
    CDotNotes_Example_Combined_Text = CDotNotes_Example_Combined_File.read()

    # CDotNotes_All_Text_Tokens_Regexp = myRegexpTokenizer.tokenize(CDotNotes_All_Text)


finally:
    # CDotNotes_0708_Gen_Med_AM_Rounds_File.close()
    # CDotNotes_0930_AM_Patient_Care_Record_File.close()
    # CDotNotes_1355_Occupational_Therapy_File.close()
    # CDotNotes_1603_WRN_Review_File.close()
    # CDotNotes_1643_Physiotherapy_File.close()
    # CDotNotes_2253_Review_n_SignOff_DP_File.close()
    # CDotNotes_2353_Discharge_Follow_Up_Plan_File.close()
    CDotNotes_Example_Combined_File.close()


# Tokenization
CDotNotes_Example_Combined_Tokens = word_tokenize(CDotNotes_Example_Combined_Text)

# Lower Case
CDotNotes_Example_Combined_Tokens_LC = [tkn.lower() for tkn in CDotNotes_Example_Combined_Tokens]


# Remove pure symbole tokens
sRegExp = "[\w]+"
CDotNotes_Tokens = removeSymboles(CDotNotes_Example_Combined_Tokens_LC, sRegExp)
print
#Remove stopwords from tokens
arrayStopWorkds = modifyStopWords(stopwords.words('english'), ['from', 'to'])
CDotNotes_Tokens = removeStopWords(CDotNotes_Tokens, arrayStopWorkds)

# print("#### Original Tokens\r\n")
# print(CDotNotes_Example_Combined_Text)
print("#### Original Tokens: Size = " + str(len(CDotNotes_Example_Combined_Tokens))+ "\r\n")
print(CDotNotes_Example_Combined_Tokens)
print("\r\n\r\n#### Sanitized Tokens: Size = " + str(len(CDotNotes_Tokens)) + "\r\n")
print(CDotNotes_Tokens)
#NER
CDotNotes_Tokens_POSTagged = pos_tag(CDotNotes_Tokens)
CDotNotes_Tokens_NE_Chunk = ne_chunk(CDotNotes_Tokens_POSTagged)
#print(CDotNotes_Tokens_NE_Chunk)