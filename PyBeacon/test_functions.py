from PyBeacon import encodeurl

def test_encode():
	urlToEncode = "https://goo.gl/a0mnsS"
	data = [
	  0x03,  #Length of Service List
	  0x03,  #Param: Service List
	  0xAA, 0xFE,  # Eddystone ID
	  0x13,  # Length of Service Data
	  0x16,  # Service Data
	  0xAA, 0xFE,# Eddystone ID
	  0x10,  #Frame type: URL
	  0xF8, # Power
	  0x03, # https://
	  'g',
	  'o',
	  'o',
	  '.',
	  'g',
	  'l',
	  '/',
	  'a',
	  '0',
	  'm',
	  'n',
	  's',
	  'S',
	]
	assert encodeurl(urlToEncode) == data