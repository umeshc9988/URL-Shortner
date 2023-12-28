import random
import string
import streamlit as st
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
        
    a = "http://www.shortee.com/" + shorturl
    
    return a
    
def getLongURL(a):
    
    k = a[23:]

    if k in d :
        return d[k]
    else :
        return None


# Standard Message :)
st.write('''
         Hello Guys !! 
         ''')

# Button Creation for easy submission
button = '''<button type= "submit">Shortee</button>'''

# User input of URL
a = st.text_input('Enter the URL for shortening : ')
st.markdown(button, unsafe_allow_html = True)


b = getShortURL(a)
long = getLongURL(b)

# Returning the short URL which has reference of long URL
st.write('Shortee URL : [',str(b),'](',str(long),')')
