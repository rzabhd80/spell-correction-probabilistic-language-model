import json

from Constants import spellCorrection_dataset_spell_errors, spellCorrection_dataset_train_name, \
    spellCorrection_channel_dictionary_path, spellCorrection_channel_dataset_path, spellCorrection_confusion_matrix, \
    spellCorrection_dataset_path


class SpellCorrectionDataExtractor:
    def __init__(self):
        self.spell_errors = {}
        self.spell_test_set = None
        self.spell_channel_dataset = None
        self.spell_channel_dictionary = None
        self.confusion_matrix = None

    def __read_spell_test_set(self):
        with open(spellCorrection_dataset_path, 'r') as f:
            self.spell_test_set = [i.strip() for i in f.read().split(" ")]

    def __read_spell_errors(self) -> None:
        with open(spellCorrection_dataset_spell_errors) as f:
            file_data = f.readlines()
        file_data = [i.strip() for i in file_data]
        for i in file_data:
            word, errors = i.split(':')
            errors_array = [v.strip() for v in errors.split(',')]
            self.spell_errors[word] = errors_array

    def __read_channel_dataset(self) -> None:
        with open(spellCorrection_channel_dataset_path, 'r', encoding='utf-8-sig') as file:
            file_contents = file.read()
        self.spell_channel_dataset = file_contents.split(" ")

    def __read_dataset(self) -> None:
        with open(spellCorrection_channel_dataset_path, 'r', encoding='utf-8-sig') as file:
            file_contents = file.read()

    def __read_confusion_matrix(self) -> None:
        self.confusion_matrix = {}
        operation_list = ['del', 'ins', 'sub', 'Transposition']
        for i in operation_list:
            with open(spellCorrection_confusion_matrix.replace("action", f"{i}")) as f:
                self.confusion_matrix[i] = json.loads(f.read().replace("'", '"'))

    @classmethod
    def extractData(cls):
        instance = SpellCorrectionDataExtractor()
        instance.__read_spell_test_set()
        instance.__read_spell_errors()
        instance.__read_channel_dataset()
        instance.__read_confusion_matrix()
        return instance
