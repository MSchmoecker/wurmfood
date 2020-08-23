from html.parser import HTMLParser


class HTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ingredients = {}
        self.cur_label = ""

    def handle_data(self, data):
        if data.split("+").__len__() != 2:
            return
        try:
            self.ingredients[self.cur_label][data.split("+")[0].replace(" ", "")] = data.split("+")[1]
        except:
            pass

    def handle_starttag(self, tag, attrs):
        if tag == "optgroup":
            self.cur_label = attrs[0][1]
            if not self.ingredients.__contains__(self.cur_label):
                self.ingredients[self.cur_label] = {}

# Open a file: file
filename = input("inputfile no.*>")
file = open(filename,mode='r')
 
# read all lines at once
all_of_it = file.read()
 
# close the file
file.close()
text = all_of_it
text = text.replace("\n", "")# .replace(" ", "")

parser = HTMLParser()
parser.feed(text)
ingredients = parser.ingredients

import json
with open(f'{filename}.json', 'w') as fp:
    json.dump(ingredients, fp)