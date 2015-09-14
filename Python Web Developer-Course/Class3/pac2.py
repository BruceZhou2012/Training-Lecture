#! /usr/bin/env python

import sys

def test(**kwargs):
    good_keys = ("container", "class_", "color", 
        "vassal", "level", "line", "filename", 
        "func", "with_total", "range")
    new_kwargs = validate_keys(kwargs, good_keys)
    for t in new_kwargs.items():
        print "%-12s : %r" % t


#def alarms(**kwargs):
    #good_keys = ("container", "class_", "color", 
        #"vassal", "level", "line", "filename", 
        #"func", "with_total", "range")
    #return self.get('alarms', validate_keys(kwargs, good_keys))


def validate_keys(kwargs, good_keys):
    good_keys = set(good_keys)
    bad_keys = set(kwargs.keys()) - good_keys
    if bad_keys:
        bad_keys = ', '.join(bad_keys)
        print >>sys.stderr, "Unknown parameters: %s\n" % bad_keys
        raise KeyError, bad_keys

    new_kwargs = {}  
    for k in good_keys:
        new_kwargs[k.rstrip('_')] = kwargs.get(k, None)
    return new_kwargs


test(color="red", class_="top",
    #bar=1, foo=3,  #Some bad keys
    level=2, func="copy",filename="text.txt")