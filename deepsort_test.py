import pytest
from deepsort import deep_sorted
from testcases import parse_testcases

testcases = parse_testcases("testcases.txt")

def run_testcase(input:str):
    return deep_sorted(input)


@pytest.mark.parametrize("testcase", testcases, ids=[testcase["name"] for testcase in testcases])
def test_cases(testcase):
    actual_output = str(run_testcase(testcase["input"])).replace('"',"'")
    expected_output = str(testcase["output"]).replace('"',"'")
    assert actual_output == expected_output, f"Expected {expected_output}, got {actual_output}"


def test_new_cases():
    # your new tests here
    pass
