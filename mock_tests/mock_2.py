import unittest
from unittest import TestCase, mock
from additional_funcs import work_on


class TestWorkOn(TestCase):

    def test_work_on_fun(self):

        #with mock.patch('work_on.os') as mock_work:
        with mock.patch('additional_funcs.os') as mock_work:
            work_on()
            mock_work.getcwd.assert_called_once() 

if __name__ == '__main__':
    unittest.main()