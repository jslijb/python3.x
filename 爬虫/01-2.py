import requests
import xml.etree.ElementTree as ET
from xml.parsers.expat import  ParserCreate
class DefaultSaxHandler(object):
    def __init__(self,provinces):
        self.provinces = provinces
    def startElement(self,name,attrs):
        if name != 'map':
            name = attrs['title']
            number = attrs['href']
            self.provinces.append((name,number))
            print('provinces:',provinces)
    def end_element(self,name):
        pass

    def char_data(self,text):
        pass


def get_province_entry(url):
    content = requests.get(url).content.decode("gb2312")
    start = content.find('<map name = \"map_86\" id=\"map_86\">')
    end = content.find('</map>')
    content = content[start:end + len('</map>')].strip()
    provinces = []
    handler = DefaultSaxHandler(provinces)
    print('handler:',handler)
    parser = ParserCreate()
    parser.StartElementHandler = handler.startElement
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(content)
    return provinces

provinces = get_province_entry('http://www.ip138.com/post')
print(provinces)