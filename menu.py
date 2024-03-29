from classification.classification import Classification
from preprocessing.preprocessing import PreProcessingHandler
from spellCorrection.spellCorrection import SpellCorrection


class InputHandler:

    def __init__(self):
        self.preprocessing = PreProcessingHandler()
        self.spell_correction = SpellCorrection()
        self.classification = Classification()
        self.methods_references = {"tokenize": self.preprocessing.tokenize, "lowercase conversion":
            self.preprocessing.to_lower_case, "stem": self.preprocessing.stem,
                                   "spell correction": self.spell_correction.spell_correction_handler,
                                   "classification": self.classification_executor}

    def resolve_input(self) -> None:
        correct_input = False
        while not correct_input:
            given_operation = input(
                "type the operation:\n tokenize\n lowercase conversion\n stem\n spell correction\n classification\n exit\n")
            if given_operation == "exit":
                exit()
            correct_input = True if given_operation in self.methods_references.keys() else None
        [self.methods_references[i]() for i in self.methods_references.keys() if i == given_operation]
        print("output written in file")

    def classification_executor(self):
        [print(self.classification.classify_test_set_sentence(j)) for i in self.classification.extract_train_set() for j
         in i]

    def menu_handler(self):
        exit_command = False
        while not exit_command:
            self.resolve_input()
            print("\n just print exit if you wanna exit")
