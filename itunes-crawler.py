from lxml import html
import requests


class AppCrawler:

    def __init__(self, starting_url, depth):
        self.starting_url = starting_url
        self.depth = depth
        self.apps = []

    def crawl(self):
        return

    def get_app_from_link(self, link):
        return


class App:

    def __init__(self, name, developer, price, links):
        self.name = name
        self.developer = developer
        self.price = price
        self.links = links

    def __str__(self):
        return ("Name: " + self.name.encode('UTF-8') +
                "\r\n Developer: " + self.developer.encode('UTF-8') +
                "\r\n Price: " + self.price.encode('UTF-8') + "\r\n")


crawler = AppCrawler('https://itunes.apple.com/in/app/whatsapp-messenger/id310633997', 0)
crawler.crawl()


for app in crawler.apps:
    print app
