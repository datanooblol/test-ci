import numpy as np
import pytest

from models.train import split_into_training_and_testing_sets



# @pytest.mark.xfail
def test_on_six_rows():
    test_argument = np.array([[2081.0, 314942.0],
                               [1059.0, 186606.0],
                               [1148.0, 206186.0],
                               [1506.0, 248419.0],
                               [1210.0, 214114.0],
                               [1697.0, 277794.0],
                               ]
                              )
    # Fill in with training array's expected number of rows
    expected_training_array_num_rows = 4
    # Fill in with testing array's expected number of rows
    expected_testing_array_num_rows = 2
    actual = split_into_training_and_testing_sets(test_argument)
    # Write the assert statement checking training array's number of rows
    assert len(actual[0]) == expected_training_array_num_rows
    assert len(actual[1]) == expected_testing_array_num_rows