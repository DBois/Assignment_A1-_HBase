import happybase
import xml.etree.ElementTree as ET
from pprint import pprint
import json


def populate():
    connection = happybase.Connection('127.0.0.1')
    table = connection.table('foods')
    # use the parse() function to load and parse an XML file
    tree = ET.parse("D:\\Downloads\\myfoodapediadata\\Food_Display_Table.xml")
    root = tree.getroot()
    for parent in root:
        row = {}
        for child in parent:
            row[child.tag] = child.text

        food_code = row.get("Food_Code")
        portion_display_name = row.get("Portion_Display_Name")
        del row["Food_Code"]
        del row["Portion_Display_Name"]
        table.put(food_code, {'facts:{0}'.format(portion_display_name) : json.dumps(row)})
    connection.close()


if __name__ == "__main__":
    populate()

