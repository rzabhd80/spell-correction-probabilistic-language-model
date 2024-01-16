from classification.classification_core.classificationProbabilityCalculator import ClassificationProbabilityCalculator
import math, numpy as np


class _Classifier:
    def __init__(self):
        self.is_model_trained: bool = False
        self.classifierCalculator = ClassificationProbabilityCalculator()
        self.probabilities = None
        self.dataset = self.classifierCalculator.dataset
        self.__check_model_status()
        self.score = 0
        self.total_doc_analyzed = 0

    def __check_model_status(self) -> None:
        if not self.is_model_trained and self.probabilities is None:
            self.probabilities = self.classifierCalculator.train()
            self.is_model_trained = True

    def __calculate_unknown_word_probability(self, class_name: str) -> float:
        return 1 / (len(
            self.dataset[class_name]) + self.classifierCalculator.classifier_data_extractor.total_types) + 1

    def __calculate_class_score_for_token(self, token: str, class_name: str) -> float:
        if token not in self.dataset[class_name]:
            return self.__calculate_unknown_word_probability(class_name)
        return self.probabilities[class_name][token]

    def classify(self, text: str) -> str:
        self.total_doc_analyzed += 1
        prior_probabilities = self.classifierCalculator.classifier_data_extractor.dataset_prior_probability
        class_name, text = text.split("\t")
        tokens = [i.strip() for i in text.split(" ")]
        class_scores = dict()
        for i in self.dataset.keys():
            class_scores[i] = 0
            for j in tokens:
                class_scores[i] += np.log(self.__calculate_class_score_for_token(j, i))
            prior = np.log(prior_probabilities[i])
            class_scores[i] = prior + class_scores.get(i)
        max_class = max(class_scores.items(), key=lambda item: item[1])[0]
        if class_name == max_class:
            self.score += 1
        return max_class
