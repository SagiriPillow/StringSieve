"""
========
StringSieve
========

:SourceCode:    `GitHub <https://github.com/SagiriPillow/StringSieve>`
"""


def sieve(string: str, template: str, identifier: str = '*', ware: dict = None):
    if ware is None:
        ware: dict = {}
    times: float = template.count(identifier)
    times: float = times / 2
    count: int = 0
    while count != times:
        start: int = template.find(identifier)
        template: str = template[start + 1:]
        end: int = template.find(identifier)
        name: str = template[:end]
        template: str = template[end + 1:]
        last: int = template.find(identifier)
        if last == -1:
            last: None = None
        behind: str = template[:last]
        string: str = string[start:]
        end: int = string.find(behind)
        if behind == string:
            value :str = ''
        else:
            value: str = string[:end]
        string: str = string[end:]
        ware[name]: str = value
        count: int = count + 1
    return ware
