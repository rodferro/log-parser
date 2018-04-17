from collections import Counter
from collections import defaultdict
import re

FILENAME = 'log.txt'
URL_PATTERN = r'request_to="(.*?)"'
STATUS_PATTERN = r'response_status="(.*?)"'

def parse_log(filename=FILENAME, url_pattern=URL_PATTERN, status_pattern=STATUS_PATTERN):
    webhooks_count = defaultdict(int)
    statuses_count = defaultdict(int)
    with open(filename, encoding='ISO-8859-1') as file:
        for line in file:
            if not line.startswith('level'):
                continue
            url = re.findall(url_pattern, line)[0]
            status = re.findall(status_pattern, line)[0]
            webhooks_count[url] += 1
            statuses_count[status] += 1
    print_most_common(webhooks_count)
    print_most_common(statuses_count)

def print_most_common(dictionary, n=3):
    for k, v in Counter(dictionary).most_common(n):
        print('{} - {}'.format(k, v))

if __name__ == '__main__':
    parse_log()