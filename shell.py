from lexer import Lexer
from parser import Parser
from interpreter import Interpreter
from data import Data


base = Data()

while True:
    text = input("> ")
    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()

    parser = Parser(tokens)
    tree = parser.parse()

    interpreter = Interpreter(tree, base)
    result = interpreter.interpret()
    print(result)
    

