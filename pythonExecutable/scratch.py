from lxml import etree


def main():
    # Create a new XML document
    doc = etree.Element('doc')

    # Create root element
    root = etree.Element('root')

    # Create new element
    elem = etree.Element('elem')

    # Append element to root
    root.append(elem)

    # Append root to document
    doc.append(root)

    # Add inner text to element
    elem.text = 'Hello World!'

    # Add attribute to element
    elem.set('attr', 'value')
    