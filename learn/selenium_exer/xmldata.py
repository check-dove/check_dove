from xml.etree.ElementTree import tostring, Element
import base64

dictcon = {'name': 'zhangshan', 'age': '12', 'female': 'man', 'address': 'tiannanyicun'}


def covert(tagname, dict_):
    elem = Element(tagname)

    for eachkey, eachvalue in dict_.items():
        xml_elem = Element(eachkey)
        xml_elem.text = eachvalue
        xml_elem.attrib = {'class': 'new_line'}

        elem.append(xml_elem)
    return elem

