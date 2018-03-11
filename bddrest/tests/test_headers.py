import unittest

from bddrest.specification.common import HeaderSet


class HeaderSetTestCase(unittest.TestCase):

    def test_constructor(self):
        expected_headers = [('A', 'B'), ('C', 'D')]
        headers = HeaderSet(('A: B', 'C: D'))
        self.assertListEqual(expected_headers, headers)

        headers = HeaderSet({'A': 'B', 'C': 'D'})
        self.assertListEqual(expected_headers, headers)

    def test_append(self):
        expected_headers = [('A', 'B'), ('C', 'D')]
        headers = HeaderSet()
        headers.append(('A', 'B'))
        headers.append(('C', 'D'))
        self.assertListEqual(expected_headers, headers)

        headers = HeaderSet()
        headers.append('A: B')
        headers.append('C: D')
        self.assertListEqual(expected_headers, headers)

        headers = HeaderSet()
        headers.append('A', 'B')
        headers.append('C', 'D')
        self.assertListEqual(expected_headers, headers)



        #    def test_insert(self):
if __name__ == '__main__':
    unittest.main()
