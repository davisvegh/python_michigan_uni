import json
import urllib.parse, urllib.error, urllib.request
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location: ")
print("Retrieving ", url)

data = urllib.request.urlopen(url, context=ctx).read()

jsondata = json.loads(data)
print("Retrieved", len(data), "characters")

comments = jsondata["comments"]
sum = 0

for comment in comments:
    count = comment["count"]
    sum += count
    
print("Sum: ", sum)

# http://py4e-data.dr-chuck.net/comments_1891875.json