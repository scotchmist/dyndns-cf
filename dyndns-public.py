#!/usr/bin/env python

import urllib2, json, socket
from urllib import urlencode

def get_request(domain, headers, URL=None):
	request = urllib2.Request("https://api.cloudflare.com/client/v4/zones{}".format(URL))
	[request.add_header(key, val) for key, val in headers.iteritems()]
	try:
		response = json.loads(urllib2.urlopen(request).read())
	except urllib2.HTTPError as h:
		return h
	return response


def set_new_ip(record_details, headers, ip, URL=None):
	record_details['result'][0]['content'] = ip
	data = record_details['result'][0]

	opener = urllib2.build_opener(urllib2.HTTPHandler)
	request = urllib2.Request('https://api.cloudflare.com/client/v4/zones{}'.format(URL), json.dumps(data))
	[request.add_header(key, val) for key, val in headers.iteritems()]
	request.get_method = lambda: 'PUT'
	opener.open(request)



if __name__ == "__main__":
	#The following values need to be set.
	subdomain = "home"
	domain = "example.co.uk"
	email = "example@example.co.uk"
	tkn = "Your CloudFlare API key goes here."

	host = "%s.%s" % (subdomain.lower(), domain.lower())
	ip = urllib2.urlopen("http://ipv4.icanhazip.com").read().strip('\n')
	current_ip = socket.gethostbyname(host)

	headers = { 'X-Auth-Email': email,
				'X-Auth-Key': tkn,
				'Content-Type': 'application/json' }

	try:
		zone_id = get_request(domain, headers, "?name={}".format(domain))['result'][0]['id']
		record_id = get_request(domain, headers, "/{}/dns_records?name={}".format(zone_id, host))['result'][0]['id']
	except:
		raise

	if ip != current_ip:
		set_new_ip(record_details, headers, ip, "/{}/dns_records/{}".format(zone_id, record_id))
	else:
		pass