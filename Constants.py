import os

preprocessing_dataset_name = '61085-0.txt'
spellingCorrection_dataset_name = None
classification_dataset_name = None
project_dir = os.getcwd()
project_absolute_path = os.path.abspath(project_dir)
preprocessing_dataset_path = f'{project_dir}/preprocessing/datasets/{preprocessing_dataset_name}'
spellingCorrection_dataset_path = f'{project_dir}/spellingCorrection/datasets/{spellingCorrection_dataset_name}'
classification_dataset_path = f'{project_dir}/classification/datasets/{classification_dataset_name}'
