#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Weize
# Software: PyCharm
# Filename: easyseleniumdownload.py
# Date: 2019/10/31

import os
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import IeOptions

class EasySeleniumDownload(object):
    def __init__(self, folder=None):
        if folder:
            if not os.path.exists(folder):
                os.makedirs(folder)
        prefs = {}
        prefs["prefile.default_content_setting.popups"] = 0
        prefs["download.default_directory"] = folder
        self._prefs = prefs

    def generate_download_folder_capability_by_chrome(self):
        options = ChromeOptions()
        options.add_experimental_option("prefs", self._prefs)
        return options

    def generate_download_folder_capability_by_firefox(self):
        options = FirefoxOptions()
        options.add_experimental_option("prefs", self._prefs)
        return options

    def generate_download_folder_capability_by_ie(self):
        options = IeOptions()
        options.add_experimental_option("prefs", self._prefs)
        return options