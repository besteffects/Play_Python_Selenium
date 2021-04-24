import scrapy


class TrustingSpider():
    name = "trusting"
    start_urls = ['https://trusting-sinoussi-0dbf65.netlify.app/']


def parse_it(self, response):
    for item in response.xpath("//table[@class='datadisplaytable'][./tbody]//tr[./td]"):
        td_first = item.xpath(".//td[@class='dddefault']/text()").get()
        td_second = item.xpath(".//td[@class='dddefault'][@text-align]/text()").get()
        yield {"Number": td_first, "Text": td_second}
        print(td_first)
        print(td_second)


if __name__ == '__main__':
    parse_it()
