import re
from typing import List, Any

from Constants import preprocessing_dataset_path, output_preprocessing_stem, output_preprocessing_tokenizer, \
    output_preprocessing_lowercase
from helpers.file_handler import FileHandler


class Tokenizer:

    def __init__(self):
        self.buffer = []
        self.word_dictionary = {}
        self.unique_set = None
        self.all_words = None

    def __extract_data(self) -> None:
        self.buffer = FileHandler.read_data_into_buffer(file_path=preprocessing_dataset_path)
        self.buffer = [i.split(" ") for i in self.buffer if i != " " and i != "\n" and i != "\r"]
        self.buffer = [re.sub(r'[^a-zA-Z0-9]+', '', j.strip()) for i in self.buffer for j in i]
        self.all_words = [re.sub(r'[^a-zA-Z0-9]+', '', j) for i in self.buffer for j in i]
        self.unique_set = set(self.buffer)

    def __generate_dictionary_and_words(self) -> None:
        for i in self.unique_set:
            if i not in self.word_dictionary.keys():
                self.word_dictionary[i] = 0

    def __compare_and_increment(self, unique_word: str, compared_word: str) -> None:
        self.word_dictionary[unique_word] += 1 if unique_word == compared_word else None

    def __count_unique_tokens(self) -> None:
        [self.__compare_and_increment(i, j) for i in self.word_dictionary.keys() for j in self.all_words if i == j]

    def convert_to_lower_case(self) -> list:
        return [i.lower() for i in self.all_words]

    def tokenize(self) -> list:

        self.__extract_data()
        self.__generate_dictionary_and_words()
        self.__count_unique_tokens()
        return self.all_words
