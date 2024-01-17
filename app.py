from classification.classification import Classification
from preprocessing.preprocessing import PreProcessingHandler

if __name__ == "__main__":
    pre_pro = PreProcessingHandler()
    classification = Classification()
    [print(classification.classify_test_set_sentence(j)) for i in classification.extract_train_set() for j in i]
