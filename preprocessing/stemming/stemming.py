from nltk.stem import PorterStemmer
from Constants import output_preprocessing_stem

from Constants import preprocessing_dataset_path


class Stemming:
    def __init__(self):
        self.stemmer = PorterStemmer()
        self.dataset = None
        self.__read_dataset()

    def __read_dataset(self):
        with open(preprocessing_dataset_path) as f:
            self.dataset = f.readlines()

    def stem_data(self) -> list:
        self.__read_dataset()
        all_words = self.dataset
        stemmed_words = [self.stemmer.stem(word) for word in all_words]
        return stemmed_words
