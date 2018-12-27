import urllib
import requests
import bs4 
from bs4 import BeautifulSoup
import re
import time
from time import*
import os

def getUrl():
 url=("https://9gag.com/")
 html=requests.get('https://9gag.com/') 
 soup=BeautifulSoup(html.text,'html.parser')
 div=soup.find(type='application/ld+json')
 for line in div:
    r1 = re.findall(r"(?:[^a-zA-Z'-]+[a-zA-Z'-]+){0,5}url(?:[^a-zA-Z'-]+[a-zA-Z'-]+){0,7}", line)
        
 return r1  

def getUrl_Funny():
    url=("https://9gag.com/funny")
    
    html=requests.get(url) 
    soup=BeautifulSoup(html.text,'html.parser')
    div=soup.find(type='application/ld+json')
    
    for line in div :
            r1 = re.findall(r"(?:[^a-zA-Z'-]+[a-zA-Z'-]+){0,5}url(?:[^a-zA-Z'-]+[a-zA-Z'-]+){0,7}", line)
        
           
    return r1  


def Hot_9gag():

    url=("https://9gag.com/hot?fbclid=IwAR1iEogBC50cOlCmIIFYGUHHxJ46gEDxAJ2_1S23sMVH5feClr8a70nk1rY")
    
    html=requests.get(url) 
    soup=BeautifulSoup(html.text,'html.parser')
    div=soup.find(type='application/ld+json')
    
    for line in div :
      r1 = re.findall(r"(?:[^a-zA-Z'-]+[a-zA-Z'-]+){0,5}url(?:[^a-zA-Z'-]+[a-zA-Z'-]+){0,7}", line)
        
           
    return r1  
def Top_9gag():

    url=("https://9gag.com/trending")
    
    html=requests.get(url) 
    soup=BeautifulSoup(html.text,'html.parser')
    div=soup.find(type='application/ld+json')
    
    for line in div :
            r1 = re.findall(r"(?:[^a-zA-Z'-]+[a-zA-Z'-]+){0,5}url(?:[^a-zA-Z'-]+[a-zA-Z'-]+){0,7}", line)
        
           
    return r1  
