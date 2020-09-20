#!/usr/bin/python

from selenium import webdriver
import time

url_tmp = "https://www.endomondo.com/rest/v1/users/1516835/workouts/%s/export?format=TCX"

browser = webdriver.Chrome()

time.sleep(15)

with open("tcx.txt") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        url = url_tmp % line
        print(url)
        browser.get(url)
