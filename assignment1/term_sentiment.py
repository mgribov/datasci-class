import sys
import json
import re

def hw(text, lookup, regex):
    new = {}
    sent = 0
    words = re.sub(regex, ' ', text).split(' ')
    
    for word in words:
        try:
            sent = sent + lookup[word]
        except KeyError,ValueError:
            
            try:
                new[word] = new[word] + 1
            except KeyError,ValueError:
                new[word] = 1
                
            continue

    return (float(sent), new)    


def main():
    sentiments = {}
    counts = {}
    new = {}

    pattern = re.compile('\W')

    sent_file = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

    tweet_file = open(sys.argv[2])

    for line in tweet_file:
        t = json.loads(line)
        try:
            (tweet_sent, new) = hw(t['text'], scores, pattern)
            for n in new:
                try:
                    sentiments[n] = sentiments[n] + tweet_sent
                    counts[n] = counts[n] + 1
                except KeyError,ValueError:
                    sentiments[n] = tweet_sent
                    counts[n] = 1

        except KeyError:
            continue

    for term in sentiments:
        print "%s %.3f" % (term, sentiments.get(term) / counts.get(term))


if __name__ == '__main__':
    main()
