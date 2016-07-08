#!/usr/bin/env python
import requests, json

class Facebook:

	app_id, app_secret = ('670423706326155','4a27fbaff89c7af041ec6fa884c9de95')
	url, token = ('https://graph.facebook.com', None)
	
	def __init__(self, token=''):
		if token:
			self.token = token
		else:
			self.token = self.get_app_token(self.app_id, self.app_secret)

	def get_app_token(self, app_id, app_secret):           
		payload = {'grant_type': 'client_credentials', 'client_id': app_id, 'client_secret': app_secret}
		return requests.post(self.url+'/oauth/access_token?', params = payload).text.split("=")[1]
		
	def get_user(self, node='me', fields=[]):
		url = self.url+'/%s?access_token=%s&fields=%s' % (node, self.token, ','.join(fields))
		return json.loads(requests.get(url).text)
		
# fb = Facebook()
# print(fb.get_user('100001795849314', ['name','user_birthday','email']))