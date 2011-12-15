#!/usr/bin/python

import sys
import os
import subprocess
from itertools import izip

def clear_debug(result):
    infinitive, plus, other = result.partition('+')
    return infinitive + '+' + other[0]

def main():
    try:
        os.unlink('result.txt')
    except OSError:
        pass
    try:
        os.unlink('result.debug.txt')
    except OSError:
        pass
    try:
        os.unlink('result.send.txt')
    except OSError:
        pass

    words = []
    with open(sys.argv[1]) as input:
        for line in input:
            line = line.strip()
            if line:
                words.append(line.split('\t')[0])

    subprocess.check_call(['foma', '-l', 'spanish.foma', '-e', 'save stack spanish.save', '-e', 'exit'])

    server = subprocess.Popen(['flookup', '-x', 'spanish.save'],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    server_result, server_errors = server.communicate('\n'.join(words))
    if server.returncode != 0:
        raise Exception('flookup returned with error')

    os.unlink('spanish.save')

    word_results = [results.split() for results in server_result.split('\n\n')]

    with open('result.txt', 'w') as output:
        with open('result.debug.txt', 'w') as debug_output:
            for word, results in izip(words, word_results):
                debug_output.write(word + '\t' + '\t'.join(results) + '\n')
                output.write(word + '\t' + '\t'.join(set(clear_debug(result) for result in results)) + '\n')

    with open('result.txt') as output:
        with open('result.send.txt', 'w') as send_output:
            send_output.write(output.read().decode('utf-8').encode('latin-1'))

if __name__ == '__main__':
    main()
