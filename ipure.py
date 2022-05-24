from itertools import count
from selenium import webdriver 
from rich.table import Table
from rich.console import Console
import time
from selenium.webdriver.firefox.options import Options
def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
clear()
print("{i}IPure-start...")
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins,secs)
        print(timeformat,end='\r')
        time.sleep(1)
        time_sec -= 1

        



options = Options()
options.headless = True
d = webdriver.Firefox(options=options)
print ("Headless Firefox Initialized")
d.get("https://www.top10vpn.com/tools/what-is-my-ip/")

countdown(2)


ipv4 = d.find_element_by_id("wimi-ipv4")
ipv4 = (ipv4.text)

ipv6  = d.find_element_by_id("wimi-ipv6")
ipv6  = (ipv6.text)

info = d.find_element_by_xpath("/html/body/div/div/main/div[1]/div/div[3]/div")
info = (info.text)

ip4info = d.find_element_by_xpath("/html/body/div/div/main/div[1]/div/div[5]/div")
ip4info = (ip4info.text)

browser = d.find_element_by_id("wimi-browser")
browser = (browser.text)


clear()
table = Table(title="IPure-Info")

table.add_column("info", style="yellow")
table.add_column("about", style="red")

table.add_row(ipv4, "ipv4")
table.add_row("-------------------------------------")
table.add_row(ip4info, "ip4-info")
table.add_row("-------------------------------------")
table.add_row(ipv6, "ipv6")
table.add_row("-------------------------------------")
table.add_row(info, "Geolocation")
table.add_row("-------------------------------------")
table.add_row(browser, "browser")


consle = Console()
consle.print(table)

d.quit()
