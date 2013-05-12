import sys
import json
import re

def hw(text, lookup, regex):
    sent = 0
    words = re.sub(regex, ' ', text).split(' ')
    #words = text.split(' ')
    
    for word in words:
        try:
            sent = sent + lookup[word]
        except KeyError:
            continue
    return float(sent)    

def main():
    pattern = re.compile('\W')

    sent_file = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary

    tweet_file = open(sys.argv[2])

    for line in tweet_file:
        t = json.loads(line)
        try:
            #print t['text']
            print hw(t['text'], scores, pattern)
        except KeyError:
            continue

if __name__ == '__main__':
    main()
