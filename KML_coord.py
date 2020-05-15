# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import re

def main():
  # KML parse
    tree = ET.parse('input.kml')
    root = tree.getroot()
    
  # Identify default namespace
    namespace = re.match('\{(.*?)\}kml', root.tag).group(1)
    ns = {'def': namespace}
    
  # Define coordinates RegEx
    coord_ex = '(-?\d+\.\d+),'
    heig_ex = '(\d+)'
    regex = coord_ex + coord_ex + heig_ex
    
  # Create output files (overwrite if already exist)
    with open('output_pins.txt','w') as out_pin,  \
         open('output_paths.txt','w') as out_pat, \
         open('output_polygons.txt','w') as out_pol:
      
      # Add headers
        out_pin.write('Pin Name,Latitude,Longitude,Height\n')
        out_pat.write('Pin Name,Pin_#,Latitude,Longitude,Height\n')
        out_pol.write('Pin Name,Pin_#,Latitude,Longitude,Height\n')

      # Find coordinates
        for i in root.findall('.//def:Placemark', ns):
          name = i.find('def:name', ns).text
          coord = i.find('.//def:coordinates', ns)
        # Check for placeless placemark     
          if not coord is None:
              coord = coord.text.strip()
              coord = re.findall(regex, coord)
            # Save data
              pin = 0
              for (long, lat, heig) in coord:
                  pin += 1
                  if i.find('.//def:Point', ns):
                      out_pin.write(f'{name},{lat},{long},{heig}\n')
                  elif i.find('.//def:LineString', ns):   
                      out_pat.write(f'{name},pin_{pin},{lat},{long},{heig}\n')
                  elif i.find('.//def:Polygon', ns):   
                      out_pol.write(f'{name},pin_{pin},{lat},{long},{heig}\n')

if __name__ == '__main__':
    main()