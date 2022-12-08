import doctest


doctest.testfile('tests/utils/files.txt', verbose=False)
doctest.testfile('tests/crypto/keys.txt', verbose=True)
