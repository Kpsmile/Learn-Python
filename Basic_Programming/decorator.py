def decorated_function(original_func):
    def wrapper_function(*args, **kwargs):
        print("wrapper function executed this before {}".format(original_func.__name__))
        return original_func(*args, **kwargs)
    return wrapper_function

## Creating logger decorator
def logger_decorator(original_func):
    import logging
    logging.basicConfig(file_name='{}.log'.format(original_func.__name__), level=logging.INFO)
    def wrapper_func(*args, **kwargs):
        logging.info(
                     'Ran with args:{}, and kwargs:{}'.format(args, kwargs))
        return original_func(*args, **kwargs)
    return wrapper_func

@decorated_function
def display():
    print("Dispay ran successfully")

# @decorated_function
@logger_decorator
def display_info(name, age):
    print("display with arguments {},{}".format(name, age))
    

display_info("Kpsingh",26)
display()