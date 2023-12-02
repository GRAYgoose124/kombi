import ast, inspect


def infer_lambda_return_type(lambda_str, resolved_type=None):
    lambda_ast = ast.parse(lambda_str, mode="eval")

    if not hasattr(lambda_ast, "body"):
        if resolved_type is None:
            resolved_type = type(ast.literal_eval(lambda_ast.body))
        return resolved_type

    body = lambda_ast.body

    if hasattr(body, "body"):
        body2 = body.body
        if isinstance(body2, ast.BinOp):
            binop = body2
            left = infer_lambda_return_type(binop.left, resolved_type)
            right = infer_lambda_return_type(binop.right, resolved_type)
            if left == right:
                return left
            else:
                return None


class LambdaTypeInferer:
    def __init__(self, lambda_func):
        self.lambda_func = lambda_func
        self.test_values = [0, 1, 1.0, "", [], (), {}, set(), True, None]

    def infer_types(self):
        valid_types = set()
        for value in self.test_values:
            try:
                self.lambda_func(value)
                valid_types.add(type(value))
            except Exception:
                pass
        return valid_types

    def check_relative_to_caller(self, caller):
        valid_types = self.infer_types()
        caller_sig = inspect.signature(caller)


__all__ = ["infer_lambda_return_type", "LambdaTypeInferer"]
