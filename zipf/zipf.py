import re


def _build_char_map(text):
    '''Builds a map with all words as keys and their counts as values.'''

    text = text.lower()
    # clear all non-word chars:
    text = re.sub(r'\W^\'|\d|"|,|\.|\?|!', ' ', text)
    # clear multiple spaces (TODO is this faster than dropping them in the loop?):
    text = re.sub(r'[\s]+', ' ', text)
    words = text.split(' ')

    word_counts = {}
    for w in words:
        if word_counts.has_key(w):
            word_counts[w] += 1
        else:
            word_counts[w] = 1

    return word_counts


def _sort_by_values(map):
    '''Sorts the input map by its values and returns a 2d array. Largest values come first.
       Returns: [[key0, val0], [key1, val1], ..]
    '''
    inverse_map = {}
    for k in map.keys():
        if inverse_map.has_key(map[k]):
            inverse_map[map[k]].append(k)
        else:
            inverse_map[map[k]] = [k]

    result = []
    keys = inverse_map.keys()
    keys.sort()  # sort() sorts in-place, so it doesn't return a value
    keys.reverse()
    for i in keys:
        for j in inverse_map[i]:
            result.append([j, i])

    return result


def zipf(text):
    arr = _sort_by_values(_build_char_map(text))
    for pair in arr:
        print pair[0], pair[1]
