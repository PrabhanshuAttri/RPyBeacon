from PyBeacon.PyBeacon import *
# from PyBeacon.PyBeacon import encodeUid
import pytest


def testEncodeUrlSuccess():
    urlToEncode = "https://goggles.com"
    data = [
        3,
        ord('g'),
        ord('o'),
        ord('g'),
        ord('g'),
        ord('l'),
        ord('e'),
        ord('s'),
        0x07,
    ]
    assert encodeurl(urlToEncode) == data


def testEncodeUrlFailure():
    urlToEncode = "https://goggles.com"
    data = [
        1,
        'g',
        'a',
        'r',
        'b',
    ]
    assert encodeurl(urlToEncode) != data


def testEncodeUrlRaisesException():
    urlToEncode = "test.com"
    with pytest.raises(Exception) as excinfo:
        encodeurl(urlToEncode)
    assert 'Invalid url scheme' in str(excinfo.value)


def testDecodeUrlSuccess():
    url = "https://goggles.com"
    dataToDecode = [
        3,
        ord('g'),
        ord('o'),
        ord('g'),
        ord('g'),
        ord('l'),
        ord('e'),
        ord('s'),
        0x07,
    ]
    assert decodeUrl(dataToDecode) == url

'''
def testEncodeUidSuccess():
    uidToEncode = "EDD1EBEAC04E5DEFA0170BDB87539B67"
    ret = []
    assert encodeUid(uidToEncode) == ret
'''

def testEncodeUidRaisesException():
    uidToEncode = "test.com"
    with pytest.raises(ValueError) as excinfo:
        encodeUid(uidToEncode)
    assert 'Invalid uid. Please specify a valid \ 16-byte (e.g 32 hex digits) hex string' in str(excinfo.value)
