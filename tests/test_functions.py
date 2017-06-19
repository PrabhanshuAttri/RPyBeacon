from PyBeacon import PyBeacon

def test_encode():
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
