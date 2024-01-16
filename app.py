from classification.classification import Classification

if __name__ == "__main__":
    classification = Classification()
    [print(classification.classify_test_set_sentence(j)) for i in classification.extract_train_set() for j in i]
