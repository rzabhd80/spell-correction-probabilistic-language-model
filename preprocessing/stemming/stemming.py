from nltk.stem import PorterStemmer
from Constants import output_preprocessing_stem

from Constants import preprocessing_dataset_path


class Stemming:
    def __int__(self):
        self.stemmer = PorterStemmer()
        self.dataset = None
        self.__read_dataset()

    def __read_dataset(self):
        with open(preprocessing_dataset_path) as f:
            self.dataset = f.readlines()

    def replace_key_dictionary(self, data_set: dict, old_key: str):
        value = data_set[old_key]
        data_set.pop(old_key)
        new_key = self.stemmer.stem(word=old_key)
        data_set[new_key] = value

    def stem_data(self) -> list:
        data_set = dict()
        all_words = self.dataset
        stemmed_words = [self.stemmer.stem(word) for word in all_words]
        [self.replace_key_dictionary(data_set, i) for i in data_set.keys()]
        return stemmed_words
