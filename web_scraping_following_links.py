import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")

num_times = int(input("Enter count: "))
pos = int(input("Enter position: "))

print("Retrieving: ", url)

for i in range(num_times):
    # Open the URL
    html = urllib.request.urlopen(url, context=ctx).read()

    # Parse the HTML page
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the anchor tags and get a list of .html files
    html_urls = [a["href"] for a in soup("a", href=True) if a["href"].endswith(".html")]
    print("Retrieving: ", html_urls[pos])
    url = html_urls[pos]

    # Check if there are enough elements in the list
    if i < len(html_urls):
        continue
    else:
        print("Not enough elements in the list. Please check the folder structure.")
        break


#http://py4e-data.dr-chuck.net/known_by_Fikret.html

#$ python3 solution.py
#Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
#Enter count: 4
#Enter position: 3
#Retrieving: http://py4e-data.dr-chuck.net/known_by_Fikret.html
#Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html
#Retrieving: http://py4e-data.dr-chuck.net/known_by_Mhairade.html
#Retrieving: http://py4e-data.dr-chuck.net/known_by_Butchi.html
#Retrieving: http://py4e-data.dr-chuck.net/known_by_Anayah.html
