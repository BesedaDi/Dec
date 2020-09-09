import json
import functools

def rec(func):
    @functools.wraps(func)
    def decorator(func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(file_name, 'w') as f:
                file_in = json.load(f)
                f.write(str(result))
            return result
        return wrapped
    return decorator

@rec('log.txt')
def comparison(*args):
    return max(args)



print(comparison.__name__)