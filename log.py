import re
import sys
from collections import Counter

URL_RE = re.compile(r'request_to="(.*?)"')
STATUS_RE = re.compile(r'response_status="(.*?)"')


def parse_log(lines):
    urls = Counter()
    statuses = Counter()
    for line in lines:
        url = URL_RE.search(line)
        status = STATUS_RE.search(line)
        if url and status:
            urls[url.group(1)] += 1
            statuses[status.group(1)] += 1
    return urls, statuses


def print_most_common(title, counter, n=3):
    print(title)
    for key, count in counter.most_common(n):
        print('{} - {}'.format(key, count))


if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else 'log.txt'
    with open(filename, encoding='utf-8') as file:
        urls, statuses = parse_log(file)
    print_most_common('Top 3 URLs:', urls)
    print()
    print_most_common('Top 3 status codes:', statuses)
