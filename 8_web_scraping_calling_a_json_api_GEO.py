import urllib.error, urllib.request, urllib.parse
import ssl
import json

api_key = False

# If there is no specific API key for Google Maps, use Dr Chuck's data
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
    
    # Enter a real city or place like 'Barcelona'
    address = input("Enter location: ")

    # Get the parameters, the address and the API key, if there is, and insert it into the URL
    parms = dict()
    parms["address"] = address
    parms["key"] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print("Retrieving", url)
    
    # Open the URL
    uh = urllib.request.urlopen(url, context=ctx)
    
    # Decode the data to be able to process it
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
        
    # Get the place_id for the entered site or location
    place_id = js["results"][0]["place_id"]

    print("Place id", place_id)

