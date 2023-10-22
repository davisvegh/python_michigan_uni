import sqlite3
import urllib.error
import ssl
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

# Create the table for the webpages connecting to the user defined webpage
cur.execute('''CREATE TABLE IF NOT EXISTS Pages
            (id INTEGER PRIMARY KEY, url TEXT UNIQUE, html TEXT,
            error INTEGER, old_rank REAL, new_rank REAL)''')

# Create the table for connecting the tables which have many to many relationship
cur.execute('''CREATE TABLE IF NOT EXISTS Links
            (from_id INTEGER, to_id INTEGER)''')

# Create a table in case there are more than one user given websites
cur.execute('''CREATE TABLE IF NOT EXISTS Websites (url TEXT UNIQUE)''')

# Check to see if we are already in progress
cur.execute('SELECT id, url FROM Pages WHERE html IS NULL and error is NULL ORDER BY RANDOM() LIMIT 1')
row = cur.fetchone()
if row is not None:
    print("Restarting existing crawl. Remove spider.sqlite to start a fresh crawl.")
else:
    starturl = input('Enter web URL or enter: ')
    # Fall back to the default webpage
    if ( len(starturl) < 1): starturl = 'http://www.dr-chuck.com/'
    # Remove the / if it ends to /
    if ( starturl.endswith('/') ): starturl = starturl[:-1]
    web = starturl
    if ( len(web) > 1 ):
        # Insert the entered URL
        cur.execute('INSERT OR IGNORE INTO Websites (url) VALUES ( ? )', (web, ))           <<<<<
        cur.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ()')      <<<<<

# Get the given website - only check links for the user given websites - and make it a list
cur.execute('''SELECT url FROM Websites''')
webs = list()
for row in cur:
    webs.append(str(row[0]))

print(webs)

many = 0
while True:
    if ( many < 1 ):
        sval = input('Up until how many links you want to find: ')
        if ( len( sval) < 1 ): break
        many = int(sval)
    many = many - 1

    # Looking for a NULL page which was not returned up until now
    cur.execute('SELECT id, url FROM Pages WHERE html is NULL and error is NULL ORDER BY RANDOM() LIMIT 1')


