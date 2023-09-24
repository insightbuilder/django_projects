import unittest
from my_functions import get_holidays, is_weekday
from requests.exceptions import Timeout
from unittest.mock import patch
from datetime import datetime


class TestCalendar(unittest.TestCase):
    @patch('my_functions.requests')
    def test_get_holiday_timeout(self, mock_requests):

        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()
            mock_requests.get.assert_called_once()

    @patch('my_functions.datetime')
    def test_get_weekday(self,mock_datetime):
        tuesday = datetime(year=2023,month=9,day=26)
        print(tuesday)

        mock_datetime.today().return_value = tuesday 
        self.assertTrue(is_weekday)


if __name__ == '__main__':
    unittest.main()
