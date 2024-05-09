def makeDecorator(decorator_func):
    def decorator_wrapper(func):
        def wrapped_func(*args, **kwargs):
            print(func.__name__)
            return decorator_func(func)(*args, **kwargs)

        return wrapped_func

    return decorator_wrapper


@makeDecorator
def introduce(func):
    def inner_wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return inner_wrapper


@introduce
def id(*whatever):
    return whatever


# Example usage
result = id(40, 2)
print(result)
