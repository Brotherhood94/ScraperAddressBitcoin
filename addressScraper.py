import scrapy

#1dice6DPtUMBpWgv8i4pG8HMjXv9qDJWN,3516175
path_addresses = '/home/alessandro/Github/Discovering_Wheel/tests/addrIdMapping/addrIdMapping_1'

path_resolved_addresses = './resolved_addresses.csv'

base_url = 'https://btc.com/'

f = open(path_resolved_addresses, 'w')

def readAddresses(path_addresses):
    addresses = []
    with open(path_addresses) as rpa:
        while True:
            line = rpa.readline()
            if not line: break
            addr = (line.split(',')[0]).strip()
            addresses.append(addr)
    return addresses


addresses = readAddresses(path_addresses)
print(len(addresses))
print("Start Scraping")
