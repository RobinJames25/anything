from collections import OrderedDict
glossary=OrderedDict()

glossary['dictionary']='A collection of key-pair values'
glossary['tuples']='An immutable list'
glossary['list']='A collection of items in a particular order'
    

for name, language in glossary.items():
    print(name.title() + '-' +language.title() + ".")


