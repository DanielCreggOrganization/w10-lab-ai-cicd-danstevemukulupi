import pytest


@pytest.mark.xfail(reason="intentional failing test")
def test_math_fail():
    assert 1 + 1 == 3
