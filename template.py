from constants import WARNING_HEADER

def dockerfile_template(poetry_version, python_version, distro):
    template = f"""{WARNING_HEADER}

FROM python:{python_version}-{distro}

ENV POETRY_VERSION={poetry_version} \\
    POETRY_NO_INTERACTION=1 \\
    POETRY_VIRTUALENVS_CREATE=false

RUN pip install "poetry==$POETRY_VERSION"

CMD ["python3"]
"""
    return template