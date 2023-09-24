from unittest import TestCase, mock, expectedFailure
import unittest
from additional_classes import Worker, Helper, Pricer


class TestClassWorker(TestCase):

    def test_patching_class(self):
        with mock.patch('additional_classes.Helper') as MockHelper:
            # When the object's function is called, the return_value
            # is chained
            MockHelper.return_value.get_path.return_value = 'testing'
            my_worker = Worker()
            MockHelper.assert_called_once()
            MockHelper.assert_called_once_with('db')
            self.assertEqual(my_worker.work(), 'testing')
    
    def test_speccing_class(self):
        with mock.patch('additional_classes.Helper', autospec=True) as MockHelper:
            # This way of patching will ensure the correct method 
            # is only chained
            MockHelper.return_value.get_path.return_value = 'testing'
            MockHelper.return_value.get_folder.return_value = 'testing'
            my_worker = Worker()
            MockHelper.assert_called_once()
            MockHelper.assert_called_once_with('db')
            self.assertEqual(my_worker.work(), 'testing')

    def test_partial_patching(self):
        with mock.patch.object(Helper, 'get_path', return_value='testing'):
            work = Worker()
            self.assertEqual(work.helper.path,'db')
            self.assertEqual(work.work(),'testing')


class TestClassPricer(TestCase):

    # This is directly calling the class
    def test_patch_instance_attribute(self):
        pricer = Pricer()
        pricer.DISCOUNT = 0.5
        self.assertAlmostEqual(pricer.get_discounted_price(100), 50.0)

    # this is mocking the class
    def test_patch_class_attribute(self):
        with mock.patch.object(Pricer, 'PERCENTAGE', 1):
            pricer = Pricer()
            self.assertAlmostEqual(pricer.get_discounted_price(100), 100)

if __name__ == '__main__':
    unittest.main()