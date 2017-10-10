# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 08:20:11 2017

@author: Paul Louie L. Tito
"""

import requests
from bs4 import BeautifulSoup
 

req = requests.get('https://www.youtube.com/watch?v=OGxgnH8y2NM&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v')
soup = BeautifulSoup(req.text, "lxml")

for title in soup.find_all("li", "yt-uix-scroller-scroll-unit vve-check"):
    print title['data-video-title']
