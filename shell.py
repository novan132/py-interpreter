from lexer import Lexer

while True:
    text = input("> ")
    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()
    print(tokens)
