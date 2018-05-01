# Wikipedia crawling program built during Udacity "Introduction to Python Programming"

import time
import urllib
import requests
from bs4 import BeautifulSoup

def find_first_link(url):
	"""
	Crawls a Wikipedia page and returns the link to the first article
	linked from that page.
	url = Wikipedia page to be searched
	"""
	first_link = None
	
	# Prepare page to be searched
	page = requests.get(url)
	html_text = page.text
	page_parser = BeautifulSoup(html_text, "html.parser")
	
	# Search in main body of page (as designated by below div tags)
	article_body = page_parser.find(id = "mw-content-text").find(class_= "mw-parser-output")
	
	for component in article_body.find_all("p", recursive = False):
		# Find link and strip anchor tag text
		if component.find("a", recursive = False):
			first_link = component.find("a", recursive = False).get("href")
			break
	if first_link:
		wiki_link = urllib.parse.urljoin("https://en.wikipedia.org/", first_link)
		return wiki_link
	else:
		return None
		
def continue_crawl(search_history, target_url, max_steps=25):
    """
    Determines whether Wikipedia crawl continues.
    search_history = list of visited pages
    target_url = goal Wikipedia page to be reached
    """
    if search_history[-1] == target_url:
        print("Search has reached the goal page and will end.")
        print("Search took " + str(len(search_history)) + " to reach goal.")
        return False
    elif len(search_history) > max_steps:
        print("Search has exceeded maximum depth and will end.")
        return False
    elif search_history[-1] in search_history[0:-1]:
        print("Search has entered a loop and will end.")
        return False
    else:
        return True

def wiki_crawl(starting_url="https://en.wikipedia.org/wiki/Special:Random", target_url="https://en.wikipedia.org/wiki/Philosophy"):
	"""
	Crawls Wikipedia to explore path of articles from start to target
	starting_url = beginning page for Wikipedia crawl
	target_url = target ending page for Wikipedia crawl
	"""
	article_chain = [starting_url]
	print("Starting point is " + starting_url)
	count = 0
	while continue_crawl(article_chain, target_url):
		# Find the first link on the current Wikipedia page
		first_link = find_first_link(article_chain[-1])
		
		# If no links, end search
		if not first_link:
			print("No more links available.  Search will end.")
			break
		
		# If links, make first link the next item to search
		article_chain.append(first_link)
		count += 1
		print("Step " + str(count) + " is " + article_chain[-1])
		
		# Pause so as to not overload Wikipedia servers
		time.sleep(2)
        
wiki_crawl()
