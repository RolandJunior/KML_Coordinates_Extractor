# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import re

# KML parse
tree = ET.parse('input.kml')
root = tree.getroot()

# Identify default namespace
namespace = re.match('\{(.*?)\}kml', root.tag).group(1)
ns = {'def': namespace}

# Create file with coordinates
f = open('output.txt','w')
for i in root.findall('.//def:Placemark[def:Point]', ns):
  name = i.find('def:name', ns).text
  coord = i.find('.//def:coordinates', ns).text.split(',')
  f.write(f'{name},{coord[1]},{coord[0]}\n')
f.close() 
