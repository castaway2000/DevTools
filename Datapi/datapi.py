import os
import sys
import urllib2
import git
from git import Repo
from bs4 import BeautifulSoup
os.getenv('IP', '0.0.0.0')
os.getenv('PORT', '8080')


def settings():
    headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    settings = {'address' : 'http://www.amazon.com', 'port': '80', 'headers': headers}
    return settings

def crawl(settings):
    page = urllib2.Request(settings['address'], headers=settings['headers'])
    req = urllib2.urlopen(page)
    data = BeautifulSoup(req, "html5lib")
    return data

def main():
    data = crawl(settings())
    return data


if __name__ == "__main__":
    sys.exit(main())
