import urllib.error, urllib.request, urllib.parse
import ssl
import json

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else :
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:

    address = input("Enter location: ")

    parms = dict()
    parms["address"] = address
    parms["key"] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print("Retrieving", url)

    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read().decode()

    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or "status" not in js or js["status"] != "OK":
        print("==== Failure to retrieve ====")
        print(data)
        continue

    place_id = js["results"][0]["place_id"]

    #print(json.dumps(js, indent=2))
    print("Place id", place_id)

