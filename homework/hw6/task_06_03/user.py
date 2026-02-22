"""
Реалізація каталогу бібліотеки.
Використовується відкрита адресація з лінійним зондуванням.
"""

_EMPTY = None
_DELETED = ("<DELETED>", "<DELETED>")

_table = []
_capacity = 200003
_size = 0


def init():
    global _table, _size
    _table = [_EMPTY] * _capacity
    _size = 0


def _get_hash(author, title):
    return hash((author, title)) % _capacity


def addBook(author, title):
    global _size
    idx = _get_hash(author, title)

    while _table[idx] is not _EMPTY:
        if _table[idx] == (author, title):
            return
        if _table[idx] == _DELETED:
            break
        idx = (idx + 1) % _capacity

    _table[idx] = (author, title)
    _size += 1


def find(author, title):
    idx = _get_hash(author, title)
    start_idx = idx

    while _table[idx] is not _EMPTY:
        if _table[idx] == (author, title):
            return True
        idx = (idx + 1) % _capacity
        if idx == start_idx: break
    return False


def delete(author, title):
    global _size
    idx = _get_hash(author, title)
    start_idx = idx

    while _table[idx] is not _EMPTY:
        if _table[idx] == (author, title):
            _table[idx] = _DELETED
            _size -= 1
            return
        idx = (idx + 1) % _capacity
        if idx == start_idx: break


def findByAuthor(author):
    titles = []
    for item in _table:
        if item is not _EMPTY and item is not _DELETED:
            if item[0] == author:
                titles.append(item[1])
    return sorted(titles)
