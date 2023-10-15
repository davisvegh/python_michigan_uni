from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Open the URL with the data to be processed
url = "http://py4e-data.dr-chuck.net/comments_1891872.html"
html = urlopen(url, context=ctx).read()

# Parse the opened URL content
soup = BeautifulSoup(html, "html.parser")

tagsum = 0
# Retrieve all of the SPAN tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('class="comments"', None))
    
    # Print each tag's content
    #print('Contents:', tag.contents[0])

    # Print the tag's attributes
    #print('Attrs:', tag.attrs)
    
    # Summarize the contents
    tagsum += int(tag.contents[0])


print("Sum of the contents of the tags: ", tagsum)