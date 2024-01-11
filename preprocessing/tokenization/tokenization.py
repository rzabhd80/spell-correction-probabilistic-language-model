import re
from Constants import preprocessing_dataset_name
from helpers.file_handler import FileHandler


class Tokenizer:
    def __init__(self):
        self.all_words = None

    def __int__(self):
        self.buffer = []
        self.word_dictionary = {}
        self.unique_set = None
        self.all_words = None

    def __extract_data(self) -> None:
        self.buffer = FileHandler.read_data_into_buffer(file_path=preprocessing_dataset_name)
        [i.split(" ") for i in self.buffer if i != " " and i != "\n" and i != "\r"]
        [j.strip() for i in self.buffer for j in i]
        self.all_words = [j for i in self.buffer for j in i]
        self.unique_set = set(self.buffer)

    def __generate_dictionary_and_words(self) -> None:
        for i in self.unique_set:
            self.word_dictionary[i] = 0 if i not in self.word_dictionary.keys() else None

    def __compare_and_increment(self, unique_word: str, compared_word: str) -> None:
        self.word_dictionary[unique_word] += 1 if unique_word == compared_word else None

    def __count_unique_tokens(self) -> None:
        [self.__compare_and_increment(i, j) for i in self.word_dictionary.keys() for j in self.all_words if i == j]

    def convert_to_lower_case(self) -> None:
        self.all_words = [i.lower() for i in self.all_words]

    def tokenize(self) -> bool:
        try:
            self.__generate_dictionary_and_words()
            self.__count_unique_tokens()
            return True
        except:
            return False

