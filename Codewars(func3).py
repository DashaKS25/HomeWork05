#

SUFFIXES = {
    # Accented
    #'ar': 'o as a amos áis an'.split(),
    #'er': 'o es e emos éis en'.split(),
    #'ir': 'o es e imos ís en'.split(),
    # Unaccented
    'ar': 'o as a amos ais an'.split(),
    'er': 'o es e emos eis en'.split(),
    'ir': 'o es e imos is en'.split(),
}

def conjugate(verb):
    return {verb: [verb[:-2] + suffix for suffix in SUFFIXES[verb[-2:]]]}