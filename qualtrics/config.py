class Survey():
	def __init__(self, qid, key):
		self.qid = qid
		self.key = key

surveyinfo = dict()
surveyinfo['pico-lab-gate'] = Survey(b'SV_2cx0bicqjAjVxdj', b'W8/j6uBo64bTrqmN')

baseurl = 'http://cambridge.eu.qualtrics.com//SE/?SID='
tokenurl = '&ssotoken='
failurepage = '<p />You stare into the void and blink.<p />Press N, S, E or W to move.'

