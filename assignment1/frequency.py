import sys
import json
import re

def count_term(text, regex, this_term):
    words = re.sub(regex, ' ', text).split(' ')
    words = re.split(r"\s+", text)

    for word in words:
        try:
            this_term[word] = this_term[word] + 1
        except KeyError:
            this_term[word] = 1

    return this_term


def hw(text, regex, all_terms):
    words = re.sub(regex, ' ', text).split(' ')
    words = re.split(r"\s+", text)
    
    for word in words:
        all_terms.add(word)

    return all_terms

def main():
    all_terms = set()
    this_term = {}

    pattern = re.compile('\W')

    tweet_file = open(sys.argv[1])

    for line in tweet_file:
        t = json.loads(line)
        try:
            all_terms = hw(t['text'], pattern, all_terms)
            this_term = count_term(t['text'], pattern, this_term)

        except KeyError:
            continue


    for t in this_term:
        #print this_term.get(t)
        #print float(this_term.get(t)) / float(len(all_terms))
        freq = float(this_term.get(t)) / float(len(all_terms))
        print "%s %.4f" % (t, freq)

if __name__ == '__main__':
    main()
