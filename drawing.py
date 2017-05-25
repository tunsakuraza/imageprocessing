import xml.etree.ElementTree as XML
import cv2

tree = XML.parse('cascade.xml')
root = tree.getroot()

# print elem.tag, elem.attrib, elem.text
list_element = [elem.text.strip()  for elem in tree.iter(tag='_') ]
list_element = ''.join(list_element)
list_element = list_element.split('.')
list_element = [text.split(' ') for text in list_element]

for index in range(0, len(list_element)-1, 2):

		zone = {
			'white': [
				tuple(
						[int(list_element[index][0]), int(list_element[index][1])]
					),
				tuple(
						[
							int(list_element[index][2]) + int(list_element[index][0]), 
							int(list_element[index][3]) + int(list_element[index][1])
						]
					)
			],
			'black': [
				tuple(
						[int(list_element[index+1][0]), int(list_element[index+1][1])]
					),
				tuple(
						[
							int(list_element[index+1][2]) + int(list_element[index+1][0]), 
							int(list_element[index+1][3]) + int(list_element[index+1][1])
						]
					)
			]
		}

		img = cv2.imread('haar.png')
		cv2.rectangle(img, zone['white'][0], zone['white'][1], (255,255,255), -1)
		cv2.rectangle(img, zone['black'][0], zone['black'][1], (0,0,0), -1)
		cv2.imwrite('pic/'+str(index)+'.jpg', img)