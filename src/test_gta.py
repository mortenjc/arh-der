
import gta



def test_count_nucls_emnpty():
    c = gta.count_nucs('')
    assert all(c[k] == 0 for k in c)


def test_count_nucls_all():
    c = gta.count_nucs('ATGC')
    assert all(c[k] == 1 for k in c)


# def test_count_nucls_none():
#     c = gta.count_nucs('OPQR')
#     assert all(c[k] == 0 for k in c)


# def test_count_nucls_some():
#     c = gta.count_nucs('ATQR')
#     assert c['A'] == 1
#     assert c['T'] == 1
#     assert c['C'] == 0
#     assert c['G'] == 0


# script called directly, not a library call, run tests
if __name__ == '__main__':
    import sys
    import pytest
    sys.exit(pytest.main([__file__, '-v']))
