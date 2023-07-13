from lexer import Lexer
from parser import Parser

while True:
    text = input("> ")
    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()

    parser = Parser(tokens)
    tree = parser.parse()
    print(tree)
