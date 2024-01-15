import os
from Constants import classification_main_dataset_path, classification_dataset_test_path
from classification.classification_core.classificationProbabilityCalculator import ClassificationProbabilityCalculator
import math

from classification.classification_core.classifier import _Classifier


class Classification:
    def __init__(self):
        self.classifier = _Classifier()

    def __read_test_set(self, files_path: str, class_name: str) -> list[str]:
        sentences = list()
        path = files_path.replace("className", f"{class_name}")
        found_files = [i for i in os.listdir(path) if os.path.isfile(f'{path}/{i}')]
        for i in found_files:
            with open(f"{path}/{i}") as file:
                sentences.append(file.readlines())
        return [j for i in sentences for j in i]

    def extract_train_set(self) -> list[list[str]]:
        extracted_train_set = list()
        all_dataset_classes = os.listdir(classification_main_dataset_path)
        all_dataset_classes = [i for i in all_dataset_classes if
                               os.path.isdir(f"{classification_main_dataset_path}/{i}")]
        for i in all_dataset_classes:
            extracted_train_set.append(self.__read_test_set(classification_dataset_test_path, i))
        return extracted_train_set

    def classify_test_set_sentence(self, inpt: str):
        return self.classifier.classify(inpt)
