import re

SGML_TAG = re.compile(r'<[^>]+>') 
ENTITIES = re.compile(r'&[^&]+;')
NON_ALPHA = re.compile(r"""[ \–\-,.։:"'՝`՛«»…()՞~]+""")

def cleanHTML(text):
    return ENTITIES.sub('', SGML_TAG.sub('', text))

def getWords(text):
    words = NON_ALPHA.split(text)
    return (word.strip() for word in words 
            if word.strip()
            and len(word.strip()) > 1
            and not word.strip().isdecimal())
