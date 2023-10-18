#!/usr/bin/env python2.7
#!coding=utf-8
from BeautifulSoup import BeautifulSoup as BS
import requests
import shutil
import argparse

class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-p', '--profile', help='Get profile image', action='store_true')
group.add_argument('-n', '--normal', help='Get normal image', action='store_true')
parser.add_argument('-f', '--filename', help='filename to save as (example.jpg)', required=True)
parser.add_argument('URL', help='Link to photo')
args = parser.parse_args()

if args.normal:
	html_link = args.URL
	html = requests.get(html_link)
	if html.status_code == 200:
		print bcolors.OKGREEN+"200 OK (site opened)"+bcolors.ENDC
	else:
		print bcolors.FAIL+"Kod: %d %s" % (html.status_code, bcolors.FAIL+" Błąd!"+bcolors.ENDC)
		exit()
	parsed_html = BS(html.text)
	image = parsed_html.html.find('meta', attrs={'property':'og:image'})
	img_url = image.get('content')
	response = requests.get(img_url, stream=True)

	with open(args.filename, 'wb') as file:
		shutil.copyfileobj(response.raw, file)
	del response
	print bcolors.OKGREEN+'Done!'+bcolors.ENDC
	exit()
elif args.profile:
	html_link = args.URL
        html = requests.get(html_link)
        if html.status_code == 200:
                print bcolors.OKGREEN+"200 OK (site opened)"+bcolors.ENDC
        else:
                print bcolors.FAIL+"Kod: %d %s" % (html.status_code, bcolors.FAIL+" Błąd!"+bcolors.ENDC)
                exit()
        parsed_html = BS(html.text)
        image = parsed_html.html.find('meta', attrs={'property':'og:image'})
        img_url = image.get('content')
	img_url_split = img_url.split('s150x150/')
	img_url = img_url_split[0]+img_url_split[1]
        response = requests.get(img_url, stream=True)

        with open(args.filename, 'wb') as file:
                shutil.copyfileobj(response.raw, file)
        del response
        print bcolors.OKGREEN+'Done!'+bcolors.ENDC
        exit()

