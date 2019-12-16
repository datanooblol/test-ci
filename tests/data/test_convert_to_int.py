import pytest
import numpy as np
from data.preprocessing_helpers import convert_to_int
from data.preprocessing_helpers import row_to_list

a = np.arange(10**3)

def test_convert_to_int(): 
    assert convert_to_int("0") == False, "ว่าวไอ้สาส"

def test_for_missing_area_with_message():
    actual = row_to_list("\t293,410\n")
    expected = None
    message = ("row_to_list('\t293,410\n') returned {0} instead of {1}".format(actual, expected))

    assert actual is expected, message

# for i in a:
#     def test_convert_to_int():
#         assert convert_to_int(str(a[i])) == a[i]