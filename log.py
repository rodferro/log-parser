import re
from collections import defaultdict
from collections import Counter

FILE_NAME = "log.txt"

URL_PATTERN = r'request_to="(.*?)"'
STATUS_PATTERN = r'response_status="(.*?)"'

def parse_log():
	file = open(FILE_NAME, "r");

	webhooks_count = defaultdict(int)
	statuses_count = defaultdict(int)

	for line in file:
		if not line.startswith("level"):
			continue

		url = re.findall(URL_PATTERN, line)[0]
		status = re.findall(STATUS_PATTERN, line)[0]

		webhooks_count[url] += 1
		statuses_count[status] += 1

	print_table(webhooks_count)
	print_table(statuses_count)

def print_table(dictionary):
	for k, v in Counter(dictionary).most_common(3):
		print '%s - %i' % (k, v)

if __name__ == '__main__':
    parse_log()
