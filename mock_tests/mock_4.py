from unittest import mock


class A:
    foo = "new"
    bar = "Super"

    def real_method(self):
        print("real one")


mock_a = mock.Mock(spec=A)

assert isinstance(mock_a.foo, mock.Mock)
assert isinstance(mock_a.bar, mock.Mock)
assert isinstance(mock_a.real_method, mock.Mock)
assert isinstance(mock_a.real_method(), mock.Mock)

assert isinstance(mock_a.some_foo, mock.Mock)