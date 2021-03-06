"""
Asserts that converts a `str` to a `int`.
"""

from py_jobject import to_dict
from ..objects import Person

def test_to_dict_convert_str_to_int():
    """
    Execute the test.
    """

    obj = Person()
    obj.name = 'Fernando Cicconeto'
    obj.age = '29'

    result = to_dict(obj)

    assert result == {
        'name': 'Fernando Cicconeto',
        'age': 29
    }
