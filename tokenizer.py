#!/usr/bin/env python
import argparse
from os.path import expanduser as exp
from transformers import GPT2TokenizerFast


def connect(file):
    tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
    with open(exp(file), "r") as f:
        file = f.read().split()
    return tokenizer(file)


def main():
    parser = argparse.ArgumentParser("Count tokens in a file")
    parser.add_argument("input", help="Text file", type=str, default=None)
    args = parser.parse_args()
    if args.input is None:
        raise Exception("First argument must be filepath to tokenize.")
    tokens = connect(args.input)

    count = 0
    for sublist in tokens["input_ids"]:
        count += len(sublist)
    print(f"Number of tokens: {count}")


if __name__ == "__main__":
    main()
