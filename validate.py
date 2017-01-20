import lxml
from lxml import isoschematron
from lxml import etree

def runschematron(rulesFile, xmlFile):
    try:
        schematron = isoschematron.Schematron(file=rulesFile, store_report = True)

        nodes = open(xmlFile, 'r')     # XML to be checked
        doc = etree.parse(nodes)
        validationResult = schematron.validate(doc)

        report = schematron.validation_report
        if validationResult:
            print("test: passed")
        else:
            print("test: failed")
            print(report)
            
    except lxml.etree.XSLTParseError as err:
        # problem parsing the schema
        print err

    except lxml.etree.XSLTApplyError as err:
        # no problems parsing the schema, we do have a problem compiling it
        print err

#
#
#
        
def main():
    schema = 'schema/reference/eLife-elem-citation-driver-final.sch'
    schema = 'min.sch' # pared down to almost nothing
    xml = 'article-xml/articles/elife-09560-v1.xml'
    runschematron(schema, xml)
    
if __name__ == '__main__':
    main()
