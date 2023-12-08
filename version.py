import json

from urllib.request import urlopen

from constants import ( 
    DISTRO_LIST,
    POETRY_VERSION,
    PYTHON_VERSION_LIST,
    URL_FORKED_VERSION
)

raw_forked_version = urlopen( URL_FORKED_VERSION )
json_forked_version = json.loads( raw_forked_version.read() )

version = {}

for PYTHON_VERSION in PYTHON_VERSION_LIST.keys():

    try:
        version[PYTHON_VERSION] = {
            'get-pip': json_forked_version[PYTHON_VERSION]['get-pip']['version'],
            'pip': json_forked_version[PYTHON_VERSION]['pip']['version'],
            'poetry': POETRY_VERSION,
            'setuptools': json_forked_version[PYTHON_VERSION]['setuptools']['version'],
            'variants': DISTRO_LIST,
            'version': PYTHON_VERSION_LIST[PYTHON_VERSION]
        }
    except:
        version[PYTHON_VERSION] = {
            'get-pip': json_forked_version[PYTHON_VERSION]['get-pip']['version'],
            'pip': json_forked_version[PYTHON_VERSION]['pip']['version'],
            'poetry': POETRY_VERSION,
            'variants': DISTRO_LIST,
            'version': PYTHON_VERSION_LIST[PYTHON_VERSION]
        }

if __name__ == "__main__":
    
    file = open('version.json', "wt")
    file.write(json.dumps(version, indent = 4))
    file.close()