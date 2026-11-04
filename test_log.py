import unittest

from log import parse_log

SAMPLE = [
    'level=info response_body="" request_to="https://a.com" response_headers=map[] response_status="200"\n',
    'level=info response_body="" request_to="https://b.com" response_headers=map[] response_status="404"\n',
    'level=info response_body="" request_to="https://a.com" response_headers=map[] response_status="404"\n',
    'some unrelated line\n',
]


class ParseLogTest(unittest.TestCase):
    def test_counts_urls_and_statuses(self):
        urls, statuses = parse_log(SAMPLE)
        self.assertEqual(urls, {'https://a.com': 2, 'https://b.com': 1})
        self.assertEqual(statuses, {'404': 2, '200': 1})

    def test_most_common_order(self):
        urls, statuses = parse_log(SAMPLE)
        self.assertEqual(urls.most_common(1), [('https://a.com', 2)])
        self.assertEqual(statuses.most_common(1), [('404', 2)])


if __name__ == '__main__':
    unittest.main()
