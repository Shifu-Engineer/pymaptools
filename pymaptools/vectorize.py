import collections
from pymaptools.utils import doc


class enumerator(collections.Mapping):
    """A simple vectorizer for text tokens

    ``enumerator`` is a key-value mapping that maps keys to numeric indices
    assigned in the order of first access. You can use it to vectorize strings.

    ::

        >>> enum = enumerator()
        >>> enum["cat"]
        0
        >>> enum["dog"]
        1
        >>> enum["cat"]
        0
        >>> len(enum)
        2
    """
    def __init__(self):
        self.d = {}

    @doc(dict.__getitem__)
    def __getitem__(self, item):
        if item in self.d:
            return self.d[item]
        else:
            val = len(self.d)
            self.d[item] = val
            return val

    @doc(dict.__str__)
    def __str__(self):
        return str(self.d)

    @doc(dict.__iter__)
    def __iter__(self):
        return iter(self.d)

    @doc(dict.__len__)
    def __len__(self):
        return len(self.d)

    @doc(dict.get)
    def get(self, key, default=None):
        return self.d.get(key, default)
