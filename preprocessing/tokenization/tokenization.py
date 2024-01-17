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
        self.all_words = [re.sub(r'[^a-zA-Z0-9]+', '', i) for i in self.buffer]

    def convert_to_lower_case(self) -> list:
        all_words = self.tokenize()
        return [i.lower() for i in self.all_words]

    def tokenize(self) -> list:
        self.__extract_data()
        return self.all_words
