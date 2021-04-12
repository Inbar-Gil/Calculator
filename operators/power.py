from operators import operator


@operator.Operator.register_operator
class Power(operator.Operator):
    """
        The addition operator, this operator allows us to add two numbers together
    """
    def __init__(self):
        super().__init__('**')

    def act(self, x: int, y: int) -> int:
        return x ** y