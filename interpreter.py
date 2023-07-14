class Interpreter:
    def __init__(self, tree):
        self.tree = tree

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
            return left + right

    def interpret(self):
        left_node = self.tree[0]
        right_node = self.tree[2]
        operator = self.tree[1]

        return self.compute_bin(left_node, operator, right_node)
