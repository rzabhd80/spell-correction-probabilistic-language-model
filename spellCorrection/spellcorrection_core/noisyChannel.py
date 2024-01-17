import json

from spellCorrection.spellcorrection_core.spellCorrectionDataExctractor import SpellCorrectionDataExtractor


class NoisyChannel:
    def __init__(self):
        self.datasets_instance = SpellCorrectionDataExtractor.extractData()
        self.confusion_matrices = self.datasets_instance.confusion_matrix

    def __action_probability_measure(self, probability: dict, action: str, count):
        correct_word = probability[f'{action}'].split('|')[1]
        wrong_word = probability[f'{action}'].split('|')[0]
        data_dict = {"delete": "del", "insert": "inst", "sub": "sub", "trans": "Transposition"}
        matrix = self.confusion_matrices[f"{data_dict[action]}"]
        matrix_value = matrix[f'{wrong_word + correct_word}']
        for word in self.datasets_instance.spell_channel_dataset:
            count += word.count(f'{wrong_word + correct_word}')
        return matrix_value

    def channel_model(self, probability):
        count = 1
        if 'delete' in probability:
            matrix_value = self.__action_probability_measure(probability, "delete", count)

        elif 'insert' in probability:
            matrix_value = self.__action_probability_measure(probability, "insert", count)

        elif 'trans' in probability:

            matrix_value = self.__action_probability_measure(probability, "trans", count)

        elif 'sub' in probability:

            matrix_value = self.__action_probability_measure(probability, "sub", count)

        else:
            matrix_value = 95
            count = 100

        return matrix_value / count
