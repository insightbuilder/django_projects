from unittest import mock
from unittest import TestCase, mock
import unittest

class A:
  foo = "foo"
  bar = "bar"
  
  def real_method(self):
    print("The real one")


"""
mock_a = mock.Mock(spec=A)
assert isinstance(mock_a.foo, mock.Mock)
assert isinstance(mock_a.bar, mock.Mock)
assert isinstance(mock_a.real_method, mock.Mock)
assert isinstance(mock_a.real_method(), mock.Mock)

# This code will raise an AttributeError
assert isinstance(mock_a.other_method, mock.Mock)
"""


class Task:
  
  def action(self):
    return "FOO BAR"


@mock.patch("__main__.Task")
def test_mock_task_class(mock_class):
  print(mock_class) # Will print MagicMock instance
  mock_class.return_value.action.return_value = "FOO ONLY"
  task_instance = Task()
  print(task_instance) # Will print "FOO ONLY"

if __name__ == "__main__":
  unittest.main()