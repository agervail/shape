import xml.etree.ElementTree as ET
tree = ET.parse('all_objects_A11.svg')
root = tree.getroot()
ET.register_namespace('', 'http://www.w3.org/2000/svg')

k = root.findall("*[@id='Shape109']")[0]
tree.write('new_shape_nonamespace.svg')
