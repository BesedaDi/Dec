import json
import functools

def rec(func): # декоратор должен расширять функционал
    @functools.wraps(func)
    def decorator(func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(file_name, 'w') as f:
                json.dump(result, f)
            return result
        return wrapped
    return decorator

@rec
def comparison(*args):
    return max(args)


print(comparison(["dfgh", "fghfghjj"]))
print(comparison.__name__)
