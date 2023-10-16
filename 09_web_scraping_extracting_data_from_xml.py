import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
if (len(address) < 1): address = 'http://py4e-data.dr-chuck.net/comments_1891874.xml'

url = address
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

count_elements = tree.findall('.//count')

count_values = [int(count.text) for count in count_elements]
total_sum = sum(count_values)

print('Total Sum of Count Values:', total_sum)

#http://py4e-data.dr-chuck.net/comments_1891874.xml
