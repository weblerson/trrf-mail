class Elements:

    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)

    def __call__(self):
        return self.__dict__
