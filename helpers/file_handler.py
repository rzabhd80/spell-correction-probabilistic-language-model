class FileHandler:

    @classmethod
    def read_data_into_buffer(cls, file_path: str) -> list[str]:
        with open(file_path, "r") as reader:
            buffer = reader.readlines()
        return buffer
