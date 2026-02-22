"""
Реалізація каталогу бібліотеки через хеш-таблицю з методом ланцюжків.
"""

_table = []
_author_index = {}
_capacity = 10007


def init():
    global _table, _author_index
    _table = [[] for _ in range(_capacity)]
    _author_index = {}


def _get_hash(author, title):
    return hash((author, title)) % _capacity


def addBook(author, title):
    h = _get_hash(author, title)

    for a, t in _table[h]:
        if a == author and t == title:
            return

    _table[h].append((author, title))

    if author not in _author_index:
        _author_index[author] = set()
    _author_index[author].add(title)


def find(author, title):
    h = _get_hash(author, title)
    for a, t in _table[h]:
        if a == author and t == title:
            return True
    return False


def delete(author, title):
    h = _get_hash(author, title)
    bucket = _table[h]
    for i in range(len(bucket)):
        if bucket[i][0] == author and bucket[i][1] == title:
            bucket.pop(i)
            if author in _author_index:
                _author_index[author].discard(title)
            return


def findByAuthor(author):
    if author in _author_index:
        return sorted(list(_author_index[author]))
    return []
