import unicodedata
import re


def remove_non_ascii(string: str) -> str:
    return string.encode('ascii', 'ignore').decode('utf8').casefold()


def remove_non_ascii_normalized(string: str) -> str:
    normalized = unicodedata.normalize('NFD', string)
    return normalized.encode('ascii', 'ignore').decode('utf8').casefold()


def remove_combining_regex(string: str) -> str:
    normalized = unicodedata.normalize('NFD', string)
    return re.sub(r'[\u0300-\u036f]', '', normalized).casefold()


def remove_combining_fluent(string: str) -> str:
    normalized = unicodedata.normalize('NFD', string)
    return ''.join(
        [l for l in normalized if not unicodedata.combining(l)]
    ).casefold()


if __name__ == "__main__":
    string = 'Atenção \N{SNAKE}'

    # normalized = unicodedata.normalize('NFD', string)
    # print([(l, f'U+{ord(l):04x}', unicodedata.name(l)) for l in normalized])

    print(string)
    print(remove_non_ascii(string))
    print(remove_non_ascii_normalized(string))
    print(remove_combining_regex(string))
    print(remove_combining_fluent(string))

    print(
        remove_combining_regex('Otávio') == remove_combining_fluent('otavio')
    )
