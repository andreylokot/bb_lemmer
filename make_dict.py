#!/usr/bin/python

def read_words():
    words = {'V': set(), 'N': set(), 'A': set()}
    with open('spanish.learn.txt') as learn:
        for line in learn:
            line = line.strip()
            if line:
                answers = line.split('\t')[1:]
                for answer in answers:
                    words[answer[-1]].add(answer[:-2])
    return words

def main():
    words = read_words()
    for part, part_words in words.iteritems():
        # foma requires Unix newlines in 'read text'
        with open('words.' + part + '.txt', 'wb') as output:
            output.write('\n'.join(sorted(part_words)))
            output.write('\n')

if __name__ == '__main__':
    main()
