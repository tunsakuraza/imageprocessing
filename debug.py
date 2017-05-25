import xml.etree.ElementTree as XML
import os, pprint

tree = XML.parse('cascade.xml')
root = tree.getroot()
list_element = [elem.text.strip()  for elem in tree.iter(tag='_') ]
list_element = ''.join(list_element)
list_element = list_element.split('.')
list_element = [text.split(' ') for text in list_element]

f = open('tmp.txt', 'w')
f.write(str(len(list_element))+'\n')

for index in range(1, len(list_element), 2):
	with open('tmp.txt', 'a') as file:
		file.write('\n %s \n %s \n %s \n' %(list_element[index-1], list_element[index], '-'*50))