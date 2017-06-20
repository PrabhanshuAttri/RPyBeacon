from PyBeacon import PyBeacon
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
	assert PyBeacon.encodeurl(urlToEncode) == data

def testEncodeUrlFailure():
	urlToEncode = "https://goggles.com"
	data =[
		1,
		'g',
		'a',
		'r',
		'b',
	]
	assert PyBeacon.encodeurl(urlToEncode) != data

def testEncodeUrlRaisesException():
	urlToEncode = "test.com"
	with pytest.raises(Exception) as excinfo:
		PyBeacon.encodeurl(urlToEncode)
	assert 'Invalid url scheme' in str(excinfo.value)