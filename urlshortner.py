import random
import string

d = {}


def getShortURL(longURL):
    
    # randomly creating the length of short url
    length = random.randint(6, 10) 
    
    # getting values to choose randomly
    char = string.ascii_lowercase + string.ascii_uppercase + string.digits # 62 characters
    
    a = "" # Empty string of store the short URL
    
    shorturl = [] # Creating empty list to store the random variables
    
    while(length > 0) :
        shorturl.append(random.choice(char))
        length -= 1
    shorturl = ''.join(shorturl) 

    if shorturl in d :
        return getShortURL(longURL)
    
    else:
        d[shorturl] = longURL
        
    a = "http://www.shorty.com/" + shorturl
    
    return a
    
def getLongURL(a):
    
    k = a[24:]

    if k in d :
        return d[k]
    else :
        return None

getShortURL("https://github.com/umeshc9988/URL-Shortner")
