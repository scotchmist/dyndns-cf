#!/usr/bin/env python

import urllib2, json, socket
from urllib import urlencode

def setipforsubdomain(subdomain, domain, email, tkn, apiaddr, ip):
	dictionary = dict([
		('a', 'rec_edit'), 
		('type', 'A'), 
		('z', domain), 
		('tkn', tkn), 
		('email', email), 
		('name', subdomain), 
		('content', ip), 
		('service_mode', '0'), 
		('ttl', '1')])

	rec_all = urllib2.urlopen(apiaddr, urlencode(dict([
		('a', 'rec_load_all'), 
		('tkn', tkn), 
		('email', email), 
		('z', domain)])))

	rec_all = json.loads(rec_all.read())
	for dicts in rec_all['response']['recs']['objs']:
		if dicts['name'] == host:
			id = dicts['rec_id']
		else:
			pass

	dictionary['id'] = id
	rec_edit = urllib2.urlopen(apiaddr, urlencode(dictionary))
	print urlencode(dictionary)
	print rec_edit.read()


if __name__ == "__main__":

	subdomain = "home"
	domain = "example.co.uk"
	email = "address@example.co.uk"
	tkn = "Your Cloudflare API token goes here."
	apiaddr = "https://www.cloudflare.com/api_json.html"
	host = "%s.%s" % (subdomain, domain)
	ip = urllib2.urlopen("http://icanhazip.com").read()[:-1]
	current_ip = socket.gethostbyname(host)

	if ip == current_ip:
		pass
	else:
		setipforsubdomain(subdomain, domain, email, tkn, apiaddr, ip)
