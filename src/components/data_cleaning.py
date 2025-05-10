#this file will clean the data before transform it to preferable ML input

import pandas as pd
import numpy as np
import string
import emoji
import emojis
from string import punctuation
from collections import Counter
import re
import os

''' 

def spell_correction(comments):

    def dictionary():
        myfile = open ("data/bangla_spelling_correction_dectionary.txt") 
        d = { } 
        for line in myfile: 
            x = line.strip().split("\t") 
            key, values = x[0], x[2:] 
            d.setdefault(key, []).extend(values)
        return d
    
    dictionary_tb = dictionary()
    listOfItems = list(dictionary_tb.items())

    #creat a list of the dictionary values
    dictt_values=list(dictionary_tb.values())
    listn=[]
    for i in range (len(dictt_values)):
        for j in range (len(dictt_values[i])):
            listn.append(dictt_values[i][j])
            
    def find_in_list(word):
        if word in listn:
            return True
        else:
            return False

    def getKeysByValue(valueToFind):
        z=find_in_list(valueToFind)
        if z== True:
            for item  in listOfItems:
                for items in item:
                    for i in range (len(items)):
                        if items[i] == valueToFind:
                            return item[0]
        else:
            return valueToFind
                                
                    
    def pass_comment(comments):
        comment= comments
        for word in comment:
            word=str(word)
            listOfKeys = str(getKeysByValue(word))
            for i in range(len(comment)):
                if comment[i]==word:
                    comment[i]=listOfKeys
        return ' '.join(map(str, comment)) 

'''

'''

def correct_bangla_spelling(comments):
    # Load dictionary and prepare data structures
    def load_dictionary():
        myfile = open("data/bangla_spelling_correction_dectionary.txt") 
        d = {} 
        for line in myfile: 
            x = line.strip().split("\t") 
            key, values = x[0], x[2:] 
            d.setdefault(key, []).extend(values)
        return d
    
    dictionary_tb = load_dictionary()
    listOfItems = list(dictionary_tb.items())
    
    # Create a list of all dictionary values
    dictt_values = list(dictionary_tb.values())
    listn = []
    for i in range(len(dictt_values)):
        for j in range(len(dictt_values[i])):
            listn.append(dictt_values[i][j])
            
    def find_in_list(word):
        return word in listn

    def getKeysByValue(valueToFind):
        if find_in_list(valueToFind):
            for item in listOfItems:
                for items in item:
                    for i in range(len(items)):
                        if items[i] == valueToFind:
                            return item[0]
        return valueToFind
                                
    # Process the comments
    comment_list = comments.split()  # Split input string into words
    for i in range(len(comment_list)):
        word = str(comment_list[i])
        corrected_word = str(getKeysByValue(word))
        if corrected_word != word:
            comment_list[i] = corrected_word
            
    return ' '.join(comment_list)



'''



class DataCleaningConfig:
    data_cleaning_file_path = os.path.join("artifacts", "clean_data.csv")
    data_transform_file_path = os.path.join("artifacts", "process_data.csv")


class DataCleaning:

    def __init__(self):
        self.data_cleaning_config = DataCleaningConfig()
    #data preprocessing

    def url_remove(self, comment):
        comment_lower = str(comment.lower())
        url = re.compile(r'https?://\S+|www.\\S+')
        comment_extract_url = url.sub(r'', comment_lower)
        return comment_extract_url                

    #emoji count
    def emoji_count(self, comment):
        emo = emojis.count(comment)
        return emo

    def remove_emoji(self, comment):
                                                            #return emoji.demojize(comment) #convert emoji to text
        return emoji.replace_emoji(comment, replace='') 


    #punctuation count
    def punctuation_number(self, comment):
        punctuation_counts = 0
        for i in comment:
            if i in string.punctuation:
                punctuation_counts = punctuation_counts+1
        return punctuation_counts


    #remove puctuation
    def remove_punc(self, comments):
        comment = str(comments)
        punctuations = '''()-[]{};:"',<>./?@#$%^*_~\n\r'''
        no_punc = ""
        for char in comment:
            if char not in punctuations:
                no_punc=no_punc+char
        return no_punc




    def  pass_comment(self, comments):
        # Load dictionary and prepare data structures
        def load_dictionary():
            myfile = open("notebook/data/bangla_spelling_correction_dectionary.txt") 
            d = {} 
            for line in myfile: 
                x = line.strip().split("\t") 
                key, values = x[0], x[2:] 
                d.setdefault(key, []).extend(values)
            return d
        
        dictionary_tb = load_dictionary()
        listOfItems = list(dictionary_tb.items())
        
        # Create a list of all dictionary values
        dictt_values = list(dictionary_tb.values())
        listn = []
        for i in range(len(dictt_values)):
            for j in range(len(dictt_values[i])):
                listn.append(dictt_values[i][j])
                
        def find_in_list(word):
            return word in listn

        def getKeysByValue(valueToFind):
            if find_in_list(valueToFind):
                for item in listOfItems:
                    for items in item:
                        for i in range(len(items)):
                            if items[i] == valueToFind:
                                return item[0]
            return valueToFind
                                    
        comment= comments
        for word in comment:
            word=str(word)
            listOfKeys = str(getKeysByValue(word))
            for i in range(len(comment)):
                if comment[i]==word:
                    comment[i]=listOfKeys
        return ' '.join(map(str, comment))      



        

    #count abusive word            
    def abusive_word_number(self, comment):

            #covert abusive word text file to list 
        with open('notebook/data/bengali_swear_word.txt','r',encoding="utf8") as f:
            listabusive=[]
            for line in f:
                strip_lines=line.strip()
                listli=strip_lines.split("\t")

                for i in range (len(listli)):
                    m=listabusive.append(listli[i])

            listabusiveSet = set(listabusive)


        comment = comment.strip()  #remove leading and ending whitespace
        comment=re.sub(' +', ' ',  comment)  #replace multiple whitespace
        comment=comment.split(' ') #convert string to list 
        
        save=[]
        for w in listabusiveSet:
            for word in comment:
                if w==word:
                    save.append(word)
        return len(save)





        
    #count positive word            
    def positive_word_number(self, comment):

        with open('notebook/data/Bengali_positive_word.txt','r', encoding="utf8") as f:
            listPositive=[]
            for line in f:
                strip_lines=line.strip()
                listlp=strip_lines.split("\t")

                for i in range (len(listlp)):
                    m=listPositive.append(listlp[i])
            listPositiveSet = set (listPositive)


        comment = comment.strip()  #remove leading and ending whitespace
        comment=re.sub(' +', ' ',  comment)  #replace multiple whitespace
        comment=comment.split(' ') #convert string to list 
        save=[]
        for w in listPositiveSet:
            for word in comment:
                if w==word:
                    save.append(word)
        return len(save)



    def data_cleaning_process(self):
        spcolumn = ["comments", "likes", "label", "Bsentiment", "Related_to_post"]
    #corpus = pd.read_csv("added data new 500.csv", usecols=spcolumn)
        corpus = pd.read_csv("notebook/data/data_preprocessing_file.csv", usecols=spcolumn)

        corpus["comments"]= corpus['comments'].astype(str)
        
        corpus['url_extract'] = corpus['comments'].apply(lambda comment:self.url_remove(comment))
        corpus['punc_number'] = corpus['url_extract'].apply(lambda comment: self.punctuation_number(comment))
        corpus['emoji_number'] = corpus['comments'].apply(lambda comment:self.emoji_count(comment))
        corpus['process_comments'] = corpus['url_extract'].apply(lambda comment: self.remove_punc(comment))



        corpus['token1']=(corpus['process_comments'].apply(lambda comment: comment.strip().split(" ")))
        corpus['spell_correct_with_emo'] = corpus['token1'].apply(lambda comment: self.pass_comment(comment))




        corpus['process_comments']=corpus['process_comments'].astype(str)
        corpus["spell_correct_without_emo"]= corpus['spell_correct_with_emo'].apply(lambda comment: self.remove_emoji(comment))
        corpus.loc[[1]]


        corpus['abusive_word_number']=corpus['spell_correct_without_emo'].apply(lambda comment: self.abusive_word_number(comment))


        
        corpus['positive_word_number']=corpus['spell_correct_with_emo'].apply(lambda comment: self.positive_word_number(comment))
        print (corpus.loc[[28]])
        
        columns_name=['comments','process_comments','spell_correct_with_emo','spell_correct_without_emo','likes','Related_to_post','punc_number','emoji_number','abusive_word_number', 'positive_word_number', 'Bsentiment','label']
        #df = corpus.to_csv('data_after_cleaning.csv', index=False, columns=columns_name)

        #store the csv file in the specific folder
        folder_path = "notebook/data"
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path,"data_after_cleaning.csv")
        corpus.to_csv(file_path, index=False, columns=columns_name)





    



'''
if __name__=="__main__":
    spcolumn = ["comments", "likes", "label", "Bsentiment", "Related_to_post"]
    #corpus = pd.read_csv("added data new 500.csv", usecols=spcolumn)
    corpus = pd.read_csv("notebook/data/data_preprocessing_file.csv", usecols=spcolumn)

    corpus["comments"]= corpus['comments'].astype(str)
    
    corpus['url_extract'] = corpus['comments'].apply(lambda comment:url_remove(comment))
    corpus['punc_number'] = corpus['url_extract'].apply(lambda comment: punctuation_number(comment))
    corpus['emoji_number'] = corpus['comments'].apply(lambda comment:emoji_count(comment))
    corpus['process_comments'] = corpus['url_extract'].apply(lambda comment: remove_punc(comment))


    # comment='Nick doctor magi'
    # words = comment.strip().split(" ")
    # print(words)
    # pass_comment(words)

    corpus['token1']=(corpus['process_comments'].apply(lambda comment: comment.strip().split(" ")))
    corpus['spell_correct_with_emo'] = corpus['token1'].apply(lambda comment: pass_comment(comment))




    corpus['process_comments']=corpus['process_comments'].astype(str)
    corpus["spell_correct_without_emo"]= corpus['spell_correct_with_emo'].apply(lambda comment: remove_emoji(comment))
    corpus.loc[[1]]


    corpus['abusive_word_number']=corpus['spell_correct_without_emo'].apply(lambda comment: abusive_word_number(comment))


    
    corpus['positive_word_number']=corpus['spell_correct_with_emo'].apply(lambda comment: positive_word_number(comment))
    print (corpus.loc[[28]])
    
    columns_name=['comments','process_comments','spell_correct_with_emo','spell_correct_without_emo','likes','Related_to_post','punc_number','emoji_number','abusive_word_number', 'positive_word_number', 'Bsentiment','label']
    #df = corpus.to_csv('data_after_cleaning.csv', index=False, columns=columns_name)

    #store the csv file in the specific folder
    folder_path = "notebook/data"
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path,"data_after_cleaning.csv")
    corpus.to_csv(file_path, index=False, columns=columns_name)

    '''





    