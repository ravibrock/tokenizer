#!/usr/bin/env python
import sys
from transformers import GPT2TokenizerFast
tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")


def connect(file):
    f = open(file, "r")
    content = f.read().split()
    f.close()
    return str(tokenizer(content))


def write(text, file):
    text_file = open(file, "w")
    text_file.write(text)
    text_file.close()


def main():
    if len(sys.argv) >= 2:
        text = connect(sys.argv[1])
        if len(sys.argv) == 3:
            write(text, sys.argv[2])
        count = text.count(",") - text.count("],")
        print(f"Number of tokens: {count}\n")
    elif len(sys.argv) == 1:
        print("Usage: Tokenizer <path to plaintext file> <path to write tokenized file to> [optional]\n")


if __name__ == "__main__":
    main()
