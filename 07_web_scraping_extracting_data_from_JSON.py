import json
import urllib.parse, urllib.error, urllib.request
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Enter the URL from where the data will be processed
url = input("Enter location: ")
if (len(url) < 1): url = 'http://py4e-data.dr-chuck.net/comments_1891875.json'
print("Retrieving ", url)

# Retrieve data from the URL
data = urllib.request.urlopen(url, context=ctx).read()

# Load it into JSON and check the length
jsondata = json.loads(data)
print("Retrieved", len(data), "characters")

# Grab a specific value from the JSON data
comments = jsondata["comments"]
sum = 0

for comment in comments:
    count = comment["count"]
    sum += count
    
print("Sum: ", sum)

# http://py4e-data.dr-chuck.net/comments_1891875.json
