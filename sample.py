import rnn
import json
CHECKPOINT_PATH = './cp'
VOCABULARY_PATH = './vocab.json'


if __name__ == '__main__':
    vocab_file = open(VOCABULARY_PATH, encoding='utf-8')
    text = vocab_file.read()
    vocab_file.close()
    vocab = json.loads(text)

    sampler = rnn.Sampler(CHECKPOINT_PATH, vocab)
    samples = []
    for _ in range(10):
        raw_name = sampler.sample()
        name = raw_name.split()[0]
        samples.append(name)
    for name in samples:
        print(name)
