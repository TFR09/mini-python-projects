def parseURL(webAddress):
    link = {}
    urlsplit = webAddress.split('/',3)
    link['protocol'] = urlsplit[0][:-1]
    link['domain'] = urlsplit[2]
    link['path'] = urlsplit[3]

    return link

def readURLs(filename):
    urls = []
    file = open(filename)
    for line in file:
        urls.append(parseURL(line.strip()))
    file.close()
    return urls

def getDomains(urlList):
    domains = set()
    for url in urlList:
        domains.add(url['domain'])
    return domains
          
if __name__ == "__main__":
    print("EXAMPLE OF USE")
    print("getDomains(readURLs('bookmarks1.txt') returns:")
    print(getDomains(readURLs('bookmarks1.txt')))