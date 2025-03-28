def parseURL(url):
    link = {}
    urlsplit = url.split('/',3)
    link['protocol'] = urlsplit[0][:-1]
    link['domain'] = urlsplit[2]
    link['path'] = urlsplit[3]

    return link
  
if __name__ == "__main__":
    print("EXAMPLE OF USE")
    print("parseURL('https://en.wikipedia.org/wiki/URL') returns:")
    print(parseURL('https://en.wikipedia.org/wiki/URL'))
