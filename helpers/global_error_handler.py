def global_error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            wrapper(*args, **kwargs)
        except Exception as e:
            print(f'exception : {e}')
