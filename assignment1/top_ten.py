import sys
import json
import re
from operator import itemgetter, attrgetter

def hw(text, regex, all_tags):
    # [{u'indices': [21, 34], u'text': u'OklahomaCity'}, {u'indices': [40, 49], u'text': u'FortSill'}, {u'indices': [50, 59], u'text': u'RoadTrip'}]
    for t in text:
        try:
            all_tags[t['text']] = all_tags[t['text']] + 1
        except KeyError:
            all_tags[t['text']] = 1

    return all_tags

def main():
    all_tags = {}

    pattern = re.compile('\W')

    tweet_file = open(sys.argv[1])

    for line in tweet_file:
        t = json.loads(line)
        try:
            all_tags = hw(t['entities']['hashtags'], pattern, all_tags)

        except KeyError:
            continue

    sorted_tags = sorted(all_tags.iteritems(), key=itemgetter(1), reverse=True)
    for i in sorted_tags[:10]:
        print "%s %.1f" % (i[0], i[1])

if __name__ == '__main__':
    main()
