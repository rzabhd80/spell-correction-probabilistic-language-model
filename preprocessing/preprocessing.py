from Constants import output_preprocessing_stem, output_preprocessing_tokenizer, output_preprocessing_lowercase
from preprocessing.stemming.stemming import Stemming
from preprocessing.tokenization.tokenization import Tokenizer


class PreProcessingHandler:
    def __init__(self):
        self.tokenizer = Tokenizer()
        self.stemmer = Stemming()

    def tokenize(self):
        all_words = self.tokenizer.tokenize()
        with open(output_preprocessing_tokenizer, 'w') as f:
            [f.writelines(f'{i}\t') for i in all_words]
        print(f"\ntokenization output written to {output_preprocessing_tokenizer}\n")

    def to_lower_case(self):
        lower_cased_words = self.tokenizer.convert_to_lower_case()
        with open(output_preprocessing_lowercase, 'w') as f:
            [f.writelines(f'{i}\t') for i in lower_cased_words]
        print(f"\nlower case conversion output written to {output_preprocessing_lowercase}\n")

    def stem(self):
        stemmed_words = self.stemmer.stemmer()
        with open(output_preprocessing_stem, 'w') as f:
            [f.writelines(f'{i}\t') for i in stemmed_words]
        print(f"\n stemming output written into {output_preprocessing_stem}")
