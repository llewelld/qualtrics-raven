#!/bin/python
from Crypto.Cipher import AES
import hashlib
import base64
import hmac
import time
import config

def gettoken(surveyid, key, data):
	delay = 300
	body = b''
	for name, value in data.iteritems():
		body += name + b'=' + value + '&'

	#body = b"crsid=dl551&timestamp=2016-02-25T20:30:22&expiration=2016-02-25T20:35:22"

	now = time.time()
	expires = now + delay

	body += b'timestamp=' + time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime(now)) + b'&expiration=' + time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime(expires))
	bodyhmac = body + b"&mac=" + base64.b64encode(hmac.new(key, body, hashlib.sha256).digest())
	extrabytes = (16 - len(bodyhmac)) % 16
	bodyhmac += '\0' * extrabytes
	cipher = AES.new(key, AES.MODE_ECB)
	token = base64.b64encode(cipher.encrypt(bodyhmac))
	url = config.baseurl + surveyid + config.tokenurl + token
	return url


