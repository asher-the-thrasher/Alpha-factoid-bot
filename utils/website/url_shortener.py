domains=['amazon.eg','amazon.com.br','amazon.ca','amazon.com.mx','amazon.com','amazon.cn','amazon.in','amazon.co.jp','amazon.sg','amazon.ae','amazon.sa','amazon.fr','amazon.de','amazon.it','amazon.nl	','amazon.pl','amazon.es','amazon.se','amazon.com.tr	','amazon.co.uk','amazon.com.au']


def shortener(url):
  correct = False
  for domain in domains:
    if domain in url:
      correct = True
      url_end=  url.split(domain,1)[1]
      try:
        if '/dp/' in url_end: #dp
          final=  url_end.split('dp/',1)[1].split('/',1)[0]
          final_url = 'https://' + domain + "/dp/" + final + '/'
          return (f"\n"+final_url+"\n")

        elif '/gp/product/' in url_end:
          final=  url_end.split('/gp/product/',1)[1].split('?',1)[0]
          final_url = 'https://' + domain + "/dp/" + final + '/'
          return("\n"+final_url+"\n")
        elif '/gp/aw/d/' in url_end:
          final=  url_end.split('/gp/aw/d/',1)[1].split('/',1)[0]
          final_url = 'https://' + domain + "/dp/" + final + '/'
          return("\n"+final_url+"\n")

        else:
          return("There was an issue converting the URL, please confirm that the link has a product in it.\n")
          return
      except Exception as g:
        return(g)
  if not correct: 
      return("That is not a valid Amazon URL\n")