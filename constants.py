DOCKER_REGISTRY_NAME = 'manuelslemos/poetry'

PIP_VERSION = '23.1.2'

POETRY_VERSION = '1.7.1'

PYTHON_VERSION_LIST = {
    '3.8': '3.8.16',
    '3.9': '3.9.16',
    '3.10': '3.10.11',
    '3.11': '3.11.13',
    '3.12': '3.12.1'  
}

DISTRO_LIST = [
    'bullseye',
    'slim-bullseye',
    'buster',
    'slim-buster',
    'alpine3.18',
    'alpine3.17',
]

URL_FORKED_VERSION = 'https://raw.githubusercontent.com/docker-library/python/master/versions.json'

WARNING_HEADER = f'''#
# NOTE: THIS DOCKERFILE IS GENERATED VIA "apply-templates.py"
#
# PLEASE DO NOT EDIT IT DIRECTLY.
#
'''