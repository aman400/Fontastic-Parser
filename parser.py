from bs4 import BeautifulSoup
import sys
import os
from lxml import etree

# input_file = "/Users/Aman/Documents/untitled-font-1/icons-reference.html"
# output_file = "font_icon_mapping.xml"
input_file = ''
output_file = ''

try:
    input_file = str(sys.argv[1])
except:
    print "Input file not passed\n"
    print "Format : \n \n"
    print "python parser.py input_file output_file"
    sys.exit(1)

try:
    output_file = str(sys.argv[2])
except:
    print "Output file not passed\n"
    print "Format : "
    print "python parser.py input_file output_file"
    sys.exit(2)


soup = BeautifulSoup(open(input_file), "lxml")

div = soup.html.body.div
names = []
chars = []

ul_tag_css_mapping = div.find('ul', 'glyphs css-mapping')
li_tags_css_mapping = ul_tag_css_mapping.find_all('input')

for each in li_tags_css_mapping:
    names.append('icon_' + each.get('value').replace('-', '_'))

ul_tag_char_mapping = div.find('ul', 'glyphs character-mapping')
li_tags_char_mapping = ul_tag_char_mapping.find_all('input')

for each in li_tags_char_mapping:
    chars.append(each.get('value'))


# Create new xml file where all tags will be written

# Open file in writtable mode
file = open(output_file, "w")


root = etree.Element('resources')

# Make a new document tree
doc = etree.ElementTree(root)

for i in range(0, len(names)):
    element = etree.SubElement(root, 'string', {'name':names[i], 'translatable':'false'})
    element.text = chars[i]

doc.write(file, xml_declaration=True, encoding='utf-8', pretty_print=True)
file.close()
