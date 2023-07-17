from tokens import Integer, Float
class Interpreter:
    def __init__(self, tree, base):
        self.tree = tree
        self.data = base

    def read_INT(self, value):
        return int(value)

    def read_FLT(self, value):
        return float(value)

    def compute_bin(self, left, op, right):
        left_type = left.type
        right_type = right.type

        left = getattr(self, f"read_{left_type}")(left.value)
        right = getattr(self, f"read_{right_type}")(right.value)

        if op.value == "+":
            output =  left + right
        elif op.value == "-":
            output = left - right
        elif op.value == "*":
            output = left * right
        elif op.value == "/":
            output = left / right

        return Integer(output) if (left_type == "INT" and right_type == "INT") else Float(output)


    def interpret(self, tree=None):
        if tree is None:
            tree = self.tree

        # evaluate left subtree
        left_node = tree[0]
        if isinstance(left_node, list):
            left_node = self.interpret(left_node)

        # evaluate right subtree
        right_node = tree[2]
        if isinstance(right_node, list):
            right_node = self.interpret(right_node)

        operator = tree[1]

        return self.compute_bin(left_node, operator, right_node)
