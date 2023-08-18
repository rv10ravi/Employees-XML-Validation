from validator import validate

if validate("employee.xml", "schema-definition.xsd"):
    print('Valid! :)')
else:
    print('Not valid! :(')