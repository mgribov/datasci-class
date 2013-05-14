import sys
import json
import re
from operator import itemgetter, attrgetter

def sentiment(text, lookup, regex):
    sent = 0
    words = re.sub(regex, ' ', text['text']).split(' ')
    #words = text.split(' ')

    for word in words:
        try:
            sent = sent + lookup[word]
        except KeyError:
            continue

    return sent

def get_state(text, regex, lookup, all_states):

    if text['place'] != None and text['place']['country'] == 'United States':
        state = text['place']['full_name'].split(', ')
        if len(state[1]) == 2:
            try:
                all_states[state[1]] = all_states[state[1]] + sentiment(text, lookup, regex)
            except KeyError:
                all_states[state[1]] = sentiment(text, lookup, regex)
 
    return all_states

def main():
    all_states = {}

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
            all_states = get_state(t, pattern, scores, all_states)

        except KeyError:
            continue

    sorted_s = sorted(all_states.iteritems(), key=itemgetter(1), reverse=True)
    for i in sorted_s[:1]:
        print i[0]


if __name__ == '__main__':
    main()
