import scrapy


path_addresses = '/home/alessandro/Github/Discovering_Wheel/tests/addrIdMapping/addrIdMapping_1'

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
                print(base_url+addr)
                addresses.append(base_url+addr)
        return addresses

    def start_requests(self):
        urls = self.readAddresses(path_addresses)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'scrapedAddressBTC.com.csv'
        address = response.url.split("/")[3].strip()
        name = str((response.css('span::text').getall()[1].strip()))
        if name != '0000':
            with open(filename, 'a') as f:
                f.write(address+','+name+'\n')
            self.log('Saved file %s' % filename)
