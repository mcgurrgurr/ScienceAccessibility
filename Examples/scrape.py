# Scientific readability project
# authors: other authors,
# ...,
# Russell Jarvis
# https://github.com/russelljjarvis/
# rjjarvis@asu.edu


# for some reason the docker build does not properly install the fake user_agent, oh well do it again here
# NB move this to the Docker container
# import os
# os.system('sudo /opt/conda/bin/pip install fake_useragent')

import selenium
from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(1024, 768))
display.start()
driver = webdriver.Firefox()
from fake_useragent import UserAgent
ua = UserAgent()


import pickle
from GoogleScraper import scrape_with_config, GoogleSearchError
from utils_and_paramaters import search_params, engine_dict_list
from numpy import random
import pickle

SEARCHLIST, WEB, LINKSTOGET = search_params()
se, _ = engine_dict_list()
flat_iter = [ (b,category) for category in SEARCHLIST for b in range(0,4) ]
# traverse this list randomly as hierarchial traversal may be a bot give away.
random.shuffle(flat_iter)

# If one was to seperate data, from code this would be how:
# if not os.path.exists('cached'):
#    os.makedirs('cached')
# if not os.path.exists('text_dump'):
#    os.makedirs('text_dump')
# os.chdir('text_dump')
def scrapelandtext(fi):
    b,category = fi
    config = {}
    stalk_relative = str('https://scholar.google.com/citations?user=2agHNksAAAAJ&hl=en&oi=sra')
    if b==4: # google scholar is not supported by google scraper
             # duckduckgo bang expansion can be used as to access engines that GS does not support.
             # for example twitter etc
        config['keyword'] = str('!scholar ')+str(category)
    else:
        config['keyword'] = str(category)
    config['search_engine'] = str(se[b])
    config['scrape_method'] = str('selenium')
    config['num_pages_for_keyword'] = 10
    config['use_own_ip'] = True
    config['sel_browser'] = str('firefox')
    config['do_caching'] = True # bloat warning.

    # NB caching results in only text snippets, which are merely previews
    # of the web pages, visible from the page-ranked search engine results. The snippets are not a total
    # text dump suitable for analysis (however initially I was confused and I thought it was).
    # It's more just log keeping of what has already been obtained, as opposed to substantial content
    # The file crawl.py contains methods for crawling the scrapped links.
    # For this reason, a subsequent action, crawling will be necessary.
    # Crawling is a lot more trivial than SE scrapping. Probably more so SE servers are fortified against scrapping
    # but regular web servers probably don't care.
    # crawling the returned links probably does not require any masqaruading or evasion. So a crawl function could be very basic.

    config['output_filename'] = str(category)+str(' ')+str(se[b])+str('.csv')
    try:
        search = scrape_with_config(config)
    except GoogleSearchError as e:
        print(e)

_ = list(map(scrapelandtext,flat_iter))
