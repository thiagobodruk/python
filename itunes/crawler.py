from lxml import html
import requests
import time

class AppCrawler:

    def __init__(self, starting_url, depth):
        self.starting_url = starting_url
        self.depth = depth
        self.current_depth = 0
        self.depth_links = []
        self.apps = []

    def crawl(self):
        app = self.get_app_from_link(self.starting_url)
        self.apps.append(app)
        self.depth_links.append(app.links)

        while self.current_depth < self.depth:
            current_links = []
            for link in self.depth_links[self.current_depth]:
                current_app = self.get_app_from_link(link)
                current_links.extend(current_app.links)
                self.apps.append(current_app)
                time.sleep(5)
            self.current_depth += 1
            self.depth_links.append(current_links)


    def get_app_from_link(self, link):
        start_page = requests.get(link)
        tree = html.fromstring(start_page.text)

        name = tree.xpath('//h1[@itemprop="name"]/text()')[0]
        developer = tree.xpath('//div[@class="left"]/h2/text()')[0]
        price = tree.xpath('//div[@itemprop="price"]/text()')[0]
        links = tree.xpath('//div[@class="center-stack"]//*/a[@class="name"]/@href')

        app = App(name, developer, price, links)

        return app


class App:

    def __init__(self, name, developer, price, links):
        self.name = name
        self.developer = developer
        self.price = price
        self.links = links

    def __str__(self):
        return ("Name: " + self.name + 
        "\r\nDeveloper: " + self.developer + 
        "\r\nPrice: " + self.price + "\r\n")


crawler = AppCrawler('https://itunes.apple.com/us/app/candy-crush-saga/id553834731', 1)
crawler.crawl()

for app in crawler.apps:
    print(app)