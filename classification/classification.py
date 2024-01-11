from helpers.file_handler import FileHandler
from Constants import classification_dataset_path, classification_main_dataset_path
import os


class Classification:

    def __int__(self):
        self.classes = list()
        self.classes_data = list()
        self.classes_token_count = list()
        self.data_set = None
        self.total_types = 0

    def __read_files_merge(self, files_path: str, class_name: str):
        merged_data = list()
        path = files_path.replace("className", f"{class_name}")
        found_files = [i for i in os.listdir(path) if os.path.isfile(path)]
        for i in found_files:
            with open(f"{os.listdir(path)}/{i}") as file:
                data = file.readlines()
                tokens = [i.split(" ") for i in data]
                self.classes_token_count.append(len(tokens))
                merged_data.append(file.readlines())
        return merged_data

    def __extract_classes(self):
        all_dataset_classes = os.listdir(classification_main_dataset_path)
        [self.classes.append(i) for i in all_dataset_classes]
        for i in self.classes:
            self.classes_data.append(self.__read_files_merge(classification_dataset_path, i))
        self.data_set = dict(zip(self.classes, self.classes_token_count, self.classes_data))
