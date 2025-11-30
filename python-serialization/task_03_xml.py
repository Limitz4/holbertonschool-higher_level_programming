#!/usr/bin/python3
"""XML serialization and deserialization"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize dictionary to XML file"""
    root = ET.Element("data")
    
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserialize XML file to dictionary"""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        result = {}
        for child in root:
            result[child.tag] = child.text
        
        return result
    except Exception:
        return {}
