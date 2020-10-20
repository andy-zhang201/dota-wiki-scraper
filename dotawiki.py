import requests
import re
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from tkinter import *      


result= requests.get("https://dota2.gamepedia.com/Dota_2_Wiki")
src = result.content

soup = BeautifulSoup(src,"lxml")
# Find all the div tags of the class "hero entry" and put them in a list called hero_links
hero_links = soup.find_all("div", class_="heroentry")
# print(links)
# print("\n")

# Iterate through the list and print out the text element of each div tag from hero_links
for link in hero_links:
    print(link.text)


#Iterate through each a tag and pick out interesting components
# for link in hero_links:
#     print(link)
    # if "Contact" in link:
    #     print(link)

    # if "title=" in link:
    #     print(link)
    
#Tkinter
# root = Tk()      
# canvas = Canvas(root, width = 300, height = 300)      
# canvas.pack()      
# img = PhotoImage(file="ball.ppm")      
# canvas.create_image(20,20, anchor=NW, image=img)      
# mainloop() 