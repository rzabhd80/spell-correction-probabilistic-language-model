from classification.classification_core.classificationProbabilityCalculator import ClassificationProbabilityCalculator
import math


class _Classifier:
    def __init__(self):
        self.is_model_trained: bool = False
        self.classifierCalculator = ClassificationProbabilityCalculator()
        self.probabilities = None
        self.dataset = self.classifierCalculator.dataset
        self.__check_model_status()

    def __check_model_status(self) -> None:
        if not self.is_model_trained and self.probabilities is None:
            self.probabilities = self.classifierCalculator.train()
            self.is_model_trained = True

    def __calculate_unknown_word_probability(self, class_name: str) -> float:
        return 1 / len(
            self.dataset[class_name]) + self.classifierCalculator.classifier_data_extractor.total_types

    def __calculate_class_score_for_token(self, token: str, class_name: str) -> float:
        if token not in self.dataset[class_name]:
            return self.__calculate_unknown_word_probability(class_name)
        return self.probabilities[class_name][token]

    def classify(self, text: str) -> str:
        tokens = [i.strip() for i in text.split(" ")]
        class_scores = dict()
        for i in self.dataset.keys():
            class_scores[i] = sum(math.log(self.__calculate_class_score_for_token(token, i)) for token in tokens)
        max_class = max(class_scores, key=class_scores.get)
        return max_class
