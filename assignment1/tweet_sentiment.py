import sys
import json

def hw(text, lookup):
    print text

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    for line in tweet_file:
        t = json.loads(line)
        try:
            hw(t['text'])
        except KeyError:
            continue

    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
