from helpers.file_handler import FileHandler
from Constants import classification_dataset_path, classification_main_dataset_path
import os


class ClassificationDataSetGenerator:
    def __int__(self):
        self.classes: list[str] = list()
        self.classes_data = list()
        self.classes_token_count: list[int] = list()
        self.classes_document_count: list[int] = list()
        self.data_set = None
        self.data_set_token_count = None
        self.dataset_prior_probability = None
        self.classes_total_num = 0
        self.total_types = 0

    def __read_files_count_doc_merge(self, files_path: str, class_name: str) -> list:
        merged_data = list()
        total_found_docs = 0
        tokens = list()
        path = files_path.replace("className", f"{class_name}")
        found_files = [i for i in os.listdir(path) if os.path.isfile(path)]
        for i in found_files:
            total_found_docs += 1
            with open(f"{os.listdir(path)}/{i}") as file:
                data = file.readlines()
                tokens.append([i.split(" ") for i in data])
                self.classes_token_count.append(len(tokens))
                merged_data.append(data)
            self.classes_token_count.append(len(set([j for i in tokens for j in i])))
            self.classes_document_count.append(total_found_docs)
        return merged_data

    def __calculate_total_types(self):
        self.total_types = len(set([j for i in self.classes_data for _, _, j in i]))

    def __calculate_prior_probability(self):
        pass

    def __extract_classes(self) -> None:
        all_dataset_classes = os.listdir(classification_main_dataset_path)
        self.classes_total_num = len(all_dataset_classes)
        [self.classes.append(i) for i in all_dataset_classes]
        for i in self.classes:
            self.classes_data.append(self.__read_files_count_doc_merge(classification_dataset_path, i))
        self.data_set = dict(zip(self.classes, self.classes_data))
        self.data_set_token_count = dict(zip(self.classes, self.classes_token_count))
        self.__calculate_total_types()
