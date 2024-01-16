from tokenization.tokenization import Tokenizer
from stemming.stemming import Stemming


class InputHandler:
    def __init__(self, tokenizer: Tokenizer, stemmer: Stemming):
        self.methods_references = {"tokenize": tokenizer.tokenize, "lowercase conversion":
                                   tokenizer.convert_to_lower_case, "stem": stemmer.stem_data}

    def resolve_input(self, inpt: str) -> None:
        correct_input = False
        while not correct_input:
            given_operation = input("type the operation:\n tokenizer\n lowercase conversion\n stem\n")
            correct_input = True if given_operation in self.methods_references.keys() else None
        [self.methods_references[i]() for i in self.methods_references.keys() if i == inpt]


class PreProcessingHandler:
    def __int__(self, inpt: str):
        self.tokenizer = Tokenizer()
        self.stemmer = Stemming()
        self.input_handler = InputHandler(tokenizer=self.tokenizer, stemmer=self.stemmer)
        self.input_handler.resolve_input(inpt)


if __name__ == "__main__":
    pass
