import json
import functools

def rec(func): # декоратор должен расширять функционал
    @functools.wraps(func)
    def decorator(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            with open('sw_comp.json', 'w') as f:
                json.dump(list(result), f)
            return result
        return wrapped
    return decorator

@rec('sw_comp.json')
def comparison(*args):
    return max(args)


print(comparison(["dfgh", "fghfghjj"]))
print(comparison.__name__)
