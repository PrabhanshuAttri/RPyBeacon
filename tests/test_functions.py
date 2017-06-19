from PyBeacon import PyBeacon

def test_encode():
	urlToEncode = "https://goggles.com"
	data = [
		0x03,  
		0x03,  
		0xAA, 0xFE, 
		0x0E,  
		0x16,  
		0xAA, 0xFE,
		0x10,  
		0xF8, 
		0x03, 
		'g',
		'o',
		'g',
		'g',
		'l',
		'e',
		's',
		0x07, 
	]
	assert PyBeacon.encodeurl(urlToEncode) == data

def test_success():
	assert 1 == 1