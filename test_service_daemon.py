import unittest
from service_daemon import *


class TestInputValidator(unittest.TestCase):

    def test_validDate(self):
        self.assertEqual(valid_date('00:01'), True)
        self.assertEqual(valid_date('00:00'), True)
        self.assertEqual(valid_date('2:01'), True)
        self.assertEqual(valid_date('000:00'), False)
        self.assertEqual(valid_date(0), False)
        self.assertEqual(valid_date('00:'), False)
        self.assertEqual(valid_date('string'), False)

    def test_input_is_valid(self):
        self.assertEqual(input_is_valid(['service_daemon.py', 'daily', '02:01']), True)
        self.assertEqual(input_is_valid(['service_daemon.py', 'da', '02:01']), False)
        self.assertEqual(input_is_valid(['service_daemon.py', 'daily', 0]), False)

if __name__ == "__main__":
    unittest.main()
