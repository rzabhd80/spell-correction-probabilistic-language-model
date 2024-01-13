from classification_core.classifier import Classifier


class Classification:
    def __int__(self):
        self.classifier = Classifier()

    def classify(self, inpt: str):
        self.classifier.classify(inpt)
