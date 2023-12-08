import os
from itertools import product

from constants import ( 
    DISTRO_LIST,
    POETRY_VERSION,
    PYTHON_VERSION_LIST
)

from template import dockerfile_template

for PYTHON_VERSION, DISTRO in product(PYTHON_VERSION_LIST, DISTRO_LIST):

    filename = f'{PYTHON_VERSION}/{DISTRO}/Dockerfile'

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    file = open(filename, "wt")
    file.write(dockerfile_template(
        POETRY_VERSION, 
        PYTHON_VERSION_LIST[PYTHON_VERSION], 
        DISTRO)
    )
    file.close()
