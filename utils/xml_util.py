import lxml.etree as et


def print_xml(elem):
    print(et.tostring(elem, xml_declaration=True, encoding="utf-8", pretty_print=True).decode())


def set_elem_attr(elem, attr):
    # a = dict()
    # for k, v in a.
    for k, v in attr.items():
        elem.attrib[k] = v


def save_xml(file, elem, xml_declaration=True):
    s = et.tostring(elem, xml_declaration=xml_declaration, encoding="utf-8", pretty_print=True).decode()
    if not file.endswith(".xml"):
        file += ".xml"
    with open(file, mode='w', encoding="utf-8") as f:
        f.write(s)
