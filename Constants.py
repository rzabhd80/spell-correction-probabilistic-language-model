import os

preprocessing_dataset_name = '61085-0.txt'
spellCorrection_dataset_train_name = "spell-testset.txt"
spellCorrection_dataset_train_spell_err_name = "spell-errors.txt"
project_dir = os.getcwd()
project_absolute_path = os.path.abspath(project_dir)
preprocessing_dataset_path = f'{project_dir}/preprocessing/datasets/{preprocessing_dataset_name}'
classification_main_dataset_path = f'{project_dir}/classification/datasets/'
classification_dataset_path = f'{project_dir}/classification/datasets/className/'
classification_test_set_path = f'{project_dir}/classification/datasets/className/test'
classification_dataset_test_path = f'{project_dir}/classification/datasets/className/test/'
spellCorrection_dataset_path = f'{project_dir}/spellCorrection/dataset/test/{spellCorrection_dataset_train_name}'
spellCorrection_dataset_spell_errors = f'{project_dir}/spellCorrection/dataset/{spellCorrection_dataset_train_spell_err_name}'
spellCorrection_channel_dataset_name = "Dataset.data.txt"
spellCorrection_channel_dataset_path = f"{project_dir}/spellCorrection/dataset/Dictionary/{spellCorrection_channel_dataset_name}"
spellCorrection_channel_dictionary_path = f'{project_dir}/spellCorrection/dataset/test/Dictionary/dictionary.Data.txt'
spellCorrection_confusion_matrix = f'{project_dir}/spellCorrection/dataset/test/Confusion Matrix/x-confusion.data.txt'
