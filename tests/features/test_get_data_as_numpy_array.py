import numpy as np
import pytest
from features.as_numpy import get_data_as_numpy_array
# @pytest.mark.xfail
def test_on_clean_file():
  expected = np.array([[2081.0, 314942.0],
                       [1059.0, 186606.0],
  					           [1148.0, 206186.0]
                       ]
                      )
  path = "C:/Users/Admin/Desktop/unit-test-for-data-science-master/unit-test-for-data-science-master/data/clean/example_clean_data.txt"
  actual = get_data_as_numpy_array(path, num_columns=2)
  message = "Expected return value: {0}, Actual Return value: {1}".format(expected, actual)
  # Complete your test
  assert actual == pytest.approx(expected), message