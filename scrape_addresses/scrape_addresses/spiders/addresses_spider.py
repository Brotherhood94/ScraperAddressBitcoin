import scrapy


path_addresses = '/home/alessandro/Github/Discovering_Wheel/tests/addrIdMapping/addrIdMapping_test_26375136'

base_url = 'https://btc.com/'

'''
        urls = [
            'https://btc.com/14gZfnEn8Xd3ofkjr5s7rKoC3bi8J4Yfyy',
            'https://btc.com/1dice4J1mFEvVuFqD14HzdViHFGi9h4Pp',
            'https://btc.com/1VayNert3x1KzbpzMGt2qdqrAThiRovi8',
            'https://btc.com/1dice6DPtUMBpWgv8i4pG8HMjXv9qDJWN',
        ]
'''

class AddressesSpider(scrapy.Spider):
    name = "addresses"

    def readAddresses(self, path_addresses):
        addresses = []
        with open(path_addresses) as rpa:
            while True:
                line = rpa.readline()
                if not line: break
                addr = (line.split(',')[0]).strip()
                addresses.append(base_url+addr)
        return addresses

    def start_requests(self):
        urls = self.readAddresses(path_addresses)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'scrapedAddressBTC.com.csv'
        address = response.url.split("/")[3].strip()
        name = response.selector.xpath('//ol[@class="breadcrumb bm"]//span/text()').get()
        if name is not None:
            with open(filename, 'a') as f:
                f.write(address+','+name+'\n')
            self.log('Saved file %s' % filename)
