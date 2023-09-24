from unittest import TestCase
from unittest.mock import Mock, patch
from unittest import mock
from additional_funcs import use_fun, make_num, work_on_env
import unittest



class TestAdditional(TestCase):

    @patch('additional_funcs.make_num')
    def test_use_fun(self, mock_make_num):
        mock_make_num.return_value = [5, 12, 20, 20, 20]
        # the above mock will ensure use_fun() will return 'Super'
        isSuper = use_fun()

        self.assertEqual(isSuper, 'Super')
    
    @patch('random.randrange')
    def test_make_num(self, mock_randrange):
        mock_randrange.return_value = 10

        ret_make_num = make_num()


        self.assertEqual(ret_make_num, [10, 10, 10, 10, 10])

    def test_mock_function(self):
        make_num = Mock()
        use_fun = Mock()

        make_num.return_value = [10, 10, 1, 10, 10]

        use_fun.return_value = 'Super'

        isSuper = use_fun()

        self.assertEqual(isSuper, 'Super')
        self.assertEqual(make_num(), [10, 10, 1, 10, 10])

    # Working on the test patch

    def test_mock_work_on_path(self):
        with mock.patch('additional_funcs.print') as mock_print:
            with mock.patch('os.getcwd', return_value='/home/'):
                with mock.patch.dict('os.environ',{'my_var':'testing'}):
                    self.assertEqual(work_on_env(),'/home/testing')
                    mock_print.assert_called_once_with('Working on /home/testing')

    

if __name__ == '__main__':
    unittest.main()
