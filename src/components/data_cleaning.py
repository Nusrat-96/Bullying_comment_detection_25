import pandas as pd
import numpy as np
import string
import emoji
import emojis
from string import punctuation
import re
import os
import pickle
from sklearn.base import BaseEstimator, TransformerMixin
from src.utils import save_object



class DataCleaningConfig:
    data_cleaning_file_path = os.path.join("artifacts", "data_cleaner.pkl")

class DataCleaner(BaseEstimator, TransformerMixin):
    """Reusable data cleaning object that can be pickled"""
    def __init__(self):
        # Load resources once during initialization
        self._load_spelling_dictionary()
        self._load_abusive_words()
        self._load_positive_words()
        
    def _load_spelling_dictionary(self):
        """Load spelling correction dictionary"""
        self.spelling_dict = {}
        with open("notebook/data/bangla_spelling_correction_dectionary.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("\t")
                if len(parts) >= 3:
                    correct = parts[0]
                    incorrect = parts[2:]
                    for word in incorrect:
                        self.spelling_dict[word] = correct
    
    def _load_abusive_words(self):
        """Load abusive words list"""
        with open('notebook/data/bengali_swear_word.txt', 'r', encoding="utf8") as f:
            self.abusive_words = set()
            for line in f:
                words = line.strip().split("\t")
                self.abusive_words.update(words)
    
    def _load_positive_words(self):
        """Load positive words list"""
        with open('notebook/data/Bengali_positive_word.txt', 'r', encoding="utf8") as f:
            self.positive_words = set()
            for line in f:
                words = line.strip().split("\t")
                self.positive_words.update(words)
    
    def url_remove(self, comment):
        comment = str(comment).lower()
        return re.sub(r'https?://\S+|www\.\S+', '', comment)
    
    def emoji_count(self, comment):
        return emojis.count(comment)
    
    def remove_emoji(self, comment):
        return emoji.replace_emoji(comment, replace='')
    
    def punctuation_number(self, comment):
        return sum(1 for char in str(comment) if char in string.punctuation)
    
    def remove_punc(self, comment):
        comment = str(comment)
        punctuations = '''()-[]{};:"',<>./?@#$%^*_~\n\r'''
        no_punc = ""
        for char in comment:
            if char not in punctuations:
                no_punc=no_punc+char
        return no_punc
    
    def spell_correction(self, text):
        words = str(text).split()
        corrected = [self.spelling_dict.get(word, word) for word in words]
        return ' '.join(corrected)     
    
    def abusive_word_number(self, text):
        words = set(re.sub(' +', ' ', str(text).strip()).split())
        return len(words & self.abusive_words)
    
    def positive_word_number(self, text):
        words = set(re.sub(' +', ' ', str(text).strip()).split())
        return len(words & self.positive_words)
    
    def transform(self, df):
        """Clean the input DataFrame"""
        df = df.copy()
        df["comments"] = df['comments'].astype(str)
        
        # Apply cleaning steps
        df['url_extract'] = df['comments'].apply(self.url_remove)
        df['punc_number'] = df['url_extract'].apply(self.punctuation_number)
        df['emoji_number'] = df['comments'].apply(self.emoji_count)
        df['process_comments'] = df['url_extract'].apply(self.remove_punc)

        df['token1']=(df['process_comments'].apply(lambda comment: comment.strip().split(" ")))


        df['spell_correct_with_emo'] = df['token1'].apply(self.spell_correction)
        df['spell_correct_without_emo'] = df['spell_correct_with_emo'].apply(self.remove_emoji)
        df['abusive_word_number'] = df['spell_correct_without_emo'].apply(self.abusive_word_number)
        df['positive_word_number'] = df['spell_correct_with_emo'].apply(self.positive_word_number)
        
        # Select final columns
        columns = ['comments', 'process_comments', 'spell_correct_with_emo',
                  'spell_correct_without_emo', 'likes', 'Related_to_post',
                  'punc_number', 'emoji_number', 'abusive_word_number',
                  'positive_word_number', 'Bsentiment', 'label']
        
        return df[columns]
    
    def fit(self, X, y=None):
        return self

class DataCleaning:
    def __init__(self):
        self.data_cleaning_config = DataCleaningConfig()
        self.cleaner = DataCleaner()
    
    def data_cleaning_process(self):
        # Load raw data
        corpus = pd.read_csv("notebook/data/data_set_2025.csv", 
                           usecols=["comments", "likes", "label", "Bsentiment", "Related_to_post"])
        
        # Clean data
        cleaned_data = self.cleaner.transform(corpus)
        
        # Save cleaned data
        os.makedirs(os.path.dirname(self.data_cleaning_config.data_cleaning_file_path), exist_ok=True)
        cleaned_data.to_csv(self.data_cleaning_config.data_cleaning_file_path, index=False)
        
        # Save the cleaning object
        save_object(
            file_path=os.path.join("artifacts", "data_cleaner.pkl"),
            obj=self.cleaner
        )
        
        return cleaned_data