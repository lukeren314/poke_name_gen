import csv
import json

INPUT_PATH = 'pokemon.csv'
OUTPUT_PATH = 'names.txt'
VOCABULARY_PATH = 'vocab.json'
if __name__ == '__main__':
    # extract the names
    csv_file = open(INPUT_PATH, encoding='utf-8')
    csv_reader = csv.reader(csv_file)

    fields = next(csv_reader)
    name_index = fields.index('name')

    names = []

    for row in csv_reader:
        if row[name_index].isascii():
            names.append(row[name_index])

    csv_file.close()

    # write out the names
    output_file = open(OUTPUT_PATH, 'w', encoding='utf-8')

    for name in names:
        output_file.write(name+'\n')

    output_file.close()

    # get the vocabulary
    name_file = open(OUTPUT_PATH, encoding='utf-8')

    text = name_file.read()

    name_file.close()

    vocabulary = []
    for char in text:
        if char not in vocabulary:
            vocabulary.append(char)

    vocab_file = open(VOCABULARY_PATH, 'w', encoding='utf-8')

    vocab_str = json.dumps(vocabulary)
    vocab_file.write(vocab_str)

    vocab_file.close()
