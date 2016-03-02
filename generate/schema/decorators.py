#decorators

def elements(type, name=None):
    def decorator(func):
        def wrapper(self):
            elements = self.element.findall(name or func.__name__)
            return tuple(type(e) for e in elements)
        return property(wrapper)
    return decorator

def element(type, name=None):
    def decorator(func):
        def wrapper(self):
            element = self.element.find(name or func.__name__)
            return type(element)
        return property(wrapper)
    return decorator

def attribute(name=None):
    def decorator(func):
        def wrapper(self):
            return self.element.get(name or func.__name__)
        return property(wrapper)
    return decorator
