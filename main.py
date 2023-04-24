import kivy
from kivy.app import App
from kivy.uix.label import Label

from bs4 import BeautifulSoup as bs
from requests import get
import re

def get_chap():
    res = get("https://readnovelfull.com/dimensional-descent.html")        
            soup = bs(res.text, "html.parser")
                div = soup.find("div", {"class":"item-value"})
                    div = div.find("a")
                        return (div.contents[0][1::])

class TestApp(App):
    def build(self):
        return Button(text=get_chap());

if __name__ == "__main__":
    TestApp().run()
