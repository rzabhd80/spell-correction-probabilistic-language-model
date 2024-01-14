from classification_core.classifier import Classifier
import os, math
from Constants import classification_dataset_test_path


class Classification:
    def __int__(self):
        self.classifier = Classifier()
        self.extracted_train_set = list()

    def __read_test_set(self, files_path: str, class_name: str) -> list[str]:
        sentences = list()
        path = files_path.replace("className", f"{class_name}")
        found_files = [i for i in os.listdir(path) if os.path.isfile(path)]
        for i in found_files:
            with open(f"{os.listdir(path)}/{i}") as file:
                sentences.append(file.readlines())
        return [j for i in sentences for j in i]

    def extract_train_set(self) -> list[str]:
        all_dataset_classes = os.listdir(classification_dataset_test_path)
        all_dataset_classes = [i for i in all_dataset_classes if os.path.isdir(i)]
        for i in all_dataset_classes:
            self.extracted_train_set.append(self.__read_test_set(classification_dataset_test_path, i))
        return self.extracted_train_set

    def classify_test_set_sentence(self, inpt: str):
        return self.classifier.classify(inpt)


if __name__ == "__main__":
    classification = Classification()
    [print(classification.classify_test_set_sentence(i)) for i in classification.extract_train_set()]
