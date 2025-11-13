def is_operator(c):
    return c in ["+", "-", "*", "/", "^"]


def prefix_to_infix(prefix):
    stack = []
    for ch in reversed(prefix):
        if not is_operator(ch):
            stack.append(ch)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            new_expr = f"({op1}{ch}{op2})"
            stack.append(new_expr)
    return stack[-1]


# Example usage
prefix_expr = "*+AB-CD"
print("Prefix Expression: ", prefix_expr)
print("Infix Expression:  ", prefix_to_infix(prefix_expr))
