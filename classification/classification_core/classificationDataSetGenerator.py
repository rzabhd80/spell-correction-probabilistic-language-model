from helpers.file_handler import FileHandler
from Constants import classification_dataset_path, classification_main_dataset_path
from helpers.global_error_handler import global_error_handler
import os


class _ClassificationDataSetGenerator:
    def __init__(self):
        self.__classes: list[str] = list()
        self.__classes_data = list()
        self.classes_token_count: list[int] = list()
        self.__classes_document_count: list[int] = list()
        self.dataset: dict = None
        self.dataset_token_count: dict = None
        self.dataset_prior_probability: dict = None
        self.dataset_document_count: dict = None
        self.dataset_all_tokens: list = None
        self.classes_total_num = 0
        self.total_types = 0

    def __read_files_count_doc_merge(self, files_path: str, class_name: str) -> list:
        total_found_docs = 0
        tokens = list()
        total_found_tokens = list()
        path = files_path.replace("className", f"{class_name}")
        found_files = [i for i in os.listdir(path)]
        for i in found_files:
            total_found_docs += 1
            with open(f"{path}/{i}") as file:
                data = file.readlines()
                tokens.append([i.split(" ") for i in data])
            total_found_tokens = [k for i in tokens for j in i for k in j]
        self.classes_token_count.append(len(total_found_tokens))
        self.__classes_document_count.append(total_found_docs)
        return total_found_tokens

    def __calculate_total_types(self):
        self.total_types = len(set([j for i in self.__classes_data for j in i]))

    def __calculate_prior_probability(self):
        result = [self.dataset_document_count[i] / self.classes_total_num for i in self.__classes]
        return dict(zip(self.__classes, result))

    def __generate_tokens_list(self) -> None:
        self.dataset_all_tokens = [j for i in self.__classes_data for j in i]

    def __extract_classes(self) -> None:
        # Attention: make sure that there is nothing but training data directories in classification
        # main dataset path. Otherwise, this code will not count the total number of classes correctly
        all_dataset_classes = os.listdir(classification_main_dataset_path)
        all_dataset_classes = [i for i in all_dataset_classes if
                               os.path.isdir(f'{classification_main_dataset_path}/{i}')]
        self.classes_total_num = len(all_dataset_classes)
        [self.__classes.append(i) for i in all_dataset_classes]
        for i in self.__classes:
            self.__classes_data.append(self.__read_files_count_doc_merge(classification_dataset_path, i))
        self.dataset = dict(zip(self.__classes, self.__classes_data))
        self.dataset_token_count = dict(zip(self.__classes, self.classes_token_count))
        self.dataset_document_count = dict(zip(self.__classes, self.__classes_document_count))
        self.dataset_prior_probability = self.__calculate_prior_probability()
        self.__calculate_total_types()

    @classmethod
    def generate_dataset(cls):
        data_set = _ClassificationDataSetGenerator()
        data_set.__extract_classes()
        return data_set
