from classification.classification_core.classificationDataSetGenerator import _ClassificationDataSetGenerator
from helpers.global_error_handler import global_error_handler


class ClassificationProbabilityCalculator:
    def __init__(self):
        self.classifier_data_extractor = _ClassificationDataSetGenerator.generate_dataset()
        self.dataset = self.classifier_data_extractor.dataset
        self.trained_model: dict = dict()

    def __calculate_probability(self, token: str, class_name: str):
        class_data = self.classifier_data_extractor.dataset[class_name]
        if not class_data:
            raise Exception("couldn`t find the class")
        count_of_token = self.classifier_data_extractor.bag_of_words[class_name][token]
        probability = (count_of_token + 1) / (self.classifier_data_extractor.dataset_token_count[class_name]
                                              + self.classifier_data_extractor.total_types)
        return probability

    def train(self) -> dict[str, dict[str, float]]:
        answer = {}
        for class_name in self.classifier_data_extractor.dataset.keys():
            answer[class_name] = {}
            for token in self.classifier_data_extractor.dataset[class_name]:
                answer[class_name][token] = self.__calculate_probability(token, class_name)

        return answer
