from classification.classification_core.classificationProbabilityCalculator import ClassificationProbabilityCalculator
import math


class _Classifier:
    def __init__(self):
        self.classifierCalculator = ClassificationProbabilityCalculator()
        self.probabilities = self.classifierCalculator.train()
        self.dataset = self.classifierCalculator.dataset

    def __calculate_unknown_word_probability(self, class_name: str) -> float:
        return 1 / len(
            self.dataset[class_name]) + self.classifierCalculator.classifier_data_extractor.total_types

    def __calculate_class_score_for_token(self, token: str, class_name: str) -> float:
        if token not in self.dataset[class_name]:
            return self.__calculate_unknown_word_probability(class_name)
        return [i[2] for i in self.probabilities if i[0] == class_name and i[1] == token][0]

    def classify(self, text: str) -> str:
        tokens = [i.strip() for i in text.split(" ")]
        class_scores = {
            class_label: sum(
                math.log(self.__calculate_class_score_for_token(token, class_label))

                for token in tokens
            )
            for class_label in self.dataset.keys()
        }
        max_class = max(class_scores, key=class_scores.get)
        return max_class
