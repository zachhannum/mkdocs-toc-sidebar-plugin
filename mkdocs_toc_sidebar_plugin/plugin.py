import os
import sys
from timeit import default_timer as timer
from datetime import datetime, timedelta

from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin

from bs4 import BeautifulSoup
import markdown
import codecs

class TocSidebar(BasePlugin):

    config_scheme = (
        ('param', config_options.Type(mkdocs_utils.string_types, default='')),
    )

    def __init__(self):
        self.enabled = True
        self.total_time = 0

    def on_post_page(self, output_content, page, config):
        soup = BeautifulSoup(output_content, 'html.parser')
        nav_extra = soup.find("div", {"class": "sidebar"})
        if nav_extra:
            soup_toc = soup.find("div", {"data-md-type" : "toc"})
            if soup_toc:
                scrollwrap = soup_toc.find("div", {"class" : "md-sidebar__scrollwrap"})
                if scrollwrap:
                    scrollwrap.insert(0, nav_extra)
                else:
                    print("WARNING (ToC Sidebar): Insertion point not found in %s" % page.file.src_path)
            else:
                print("WARNING (ToC Sidebar): Table of Contents in sidebar not found in %s" % page.file.src_path)
   
        souped_html = soup.encode(soup.original_encoding) if soup.original_encoding else str(soup)
        return souped_html 

