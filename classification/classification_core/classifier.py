from classificationProbabilityCalculator import ClassificationProbabilityCalculator


class Classifier:
    def __init__(self):
        self.classifierCalculator = ClassificationProbabilityCalculator()
        self.probabilities = self.classifierCalculator.train()
        self.dataset = self.classifierCalculator.dataset

    def __calculate_unknown_word_probability(self, class_name: str):
        return 1 / len(
            self.dataset[class_name]) + self.classifierCalculator.classifier_data_extractor.total_types

    def __calculate_class_score(self, token: str) -> list[float]:
        return [self.__calculate_class_score_for_token(token, i) for i in self.dataset.keys()]

    def __calculate_class_score_for_token(self, token: str, class_name: str) -> float:
        if token not in self.dataset[class_name]:
            return self.__calculate_unknown_word_probability(class_name)
        return [i[2] for i in self.probabilities if i[0] == class_name and i[1] == token][0]

    def classify(self, text: str) -> dict:
        tokens = [i.strip() for i in text.split(" ")]
        each_token_score = list()
        [each_token_score.append(self.__calculate_class_score(i)) for i in tokens]
        return dict(zip(tokens, each_token_score))
