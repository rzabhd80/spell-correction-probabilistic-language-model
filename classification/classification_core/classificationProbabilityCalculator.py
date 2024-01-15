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
        probability = (count_of_token + 1) / (self.classifier_data_extractor.dataset_document_count[class_name]
                                              + self.classifier_data_extractor.total_types)
        return probability

    # def train(self) -> list[tuple[str, str, int]]:
    #     trained_data = [(i, j, self.__calculate_probability(j, i)) for i in
    #                     self.classifier_data_extractor.dataset.keys() for j in
    #                     self.classifier_data_extractor.dataset[i]]
    #     return trained_data
    def train(self) -> dict[str, dict[str, float]]:
        return {
            class_name: {
                token: self.__calculate_probability(token, class_name)
                for token in self.classifier_data_extractor.dataset[class_name]
            }
            for class_name in self.classifier_data_extractor.dataset.keys()
        }

