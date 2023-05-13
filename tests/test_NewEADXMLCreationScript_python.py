import unittest
from pythonExecutableSource.NewEADXMLCreationScript_python import codedDate, convert_to_xml

class TestNewEADXMLCreationScript_python(unittest.TestCase):
 def test_codedDate(self):
        test_cases = [
            ('October 16-18, 2001', '2001-10-16/2001-10-18'),
            ('1958-1986 and undated', '1958/1986'),
            ('October-December, 2001', '2001-10/2001-12'),
            ('January 24, 2014 - February 24, 2018', '2014-01-24/2018-02-24'),
            ('c 1790s', '1790/1799'),
            ('1790s', '1790/1799'),
            ('1970s-1980s', '1970/1989'),
            ('October, 2001', '2001-10'),
            ('1978-1984', '1978/1984'),
            ('c. 1978', '1978'),
            ('Spring, 2001', '2001'),
            ('October 16, 2001', '2001-10-16'),
            ('c. 1945-1947', '1945/1947'),
            ('circa 1945', '1945'),
            ('c. 1946', '1946'),
            ('1942, 1045, 1945-1947', '1045/1947'),
            ('undated', 'REPLACEMEASUNDATED'),
        ]

        for i, (input, expected_output) in enumerate(test_cases):
            with self.subTest(i=i):
                self.assertEqual(codedDate(input), expected_output)

if __name__ == '__main__':
    unittest.main()    

