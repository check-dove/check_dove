import pytest


@pytest.mark.parametrize(
    "base, exponent, expected",
    [(2, 2, 4),
     (2, 3, 8),
     (3, 3, 27),
     (4, 3, 64)],
    ids=["case1", "case2", "case3", "case4"]
)
def test_po(base, exponent, expected):
    assert base ** exponent == expected, "{} is fail".format(test_po.name)


if __name__ == '__main__':
    # '--pastebin=all'
    pytest.main(['-s', '--junit-xml=./report/log.xml'])
