from classification_core.classifier import Classifier
import os, math


class Classification:
    def __int__(self):
        self.classifier = Classifier()

    def __read_test_set(self, files_path: str, class_name: str) -> list[list[str]]:
        sentences = list()
        path = files_path.replace("className", f"{class_name}")
        found_files = [i for i in os.listdir(path) if os.path.isfile(path)]
        for i in found_files:
            with open(f"{os.listdir(path)}/{i}") as file:
                sentences.append(file.readlines())
        return sentences

    def __classify_test_set_sentence(self, inpt: str):
        token_score = self.classifier.classify(inpt)



if __name__ == "__main__":
    classification = Classification()

    classification.classify("")
