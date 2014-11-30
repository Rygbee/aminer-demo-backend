# -*- coding: utf-8 -*-
#
# Nicolas Roussel     http://insitu.lri.fr/~roussel/
# In Situ, Université Paris-Sud (LRI) & INRIA Futurs
#
# metrics.py -
#
# See the file LICENSE for information on usage and redistribution of
# this file, and for a DISCLAIMER OF ALL WARRANTIES.

import math
import datetime

# ------------------------------------------------------------------------------

def filterOut(seq, key, ignore):
    result = []
    for r in seq:
        val = r.get(key, ignore)
        if val != ignore: result.append(val)
    return result


def hindex(references):
    h = 0
    references = sorted(references, reverse=True)
    while True:
        h = h + 1
        n = 0
        for r in references:
            if r >= h:
                n = n + 1
        if n < h:
            h = h - 1
            break
    return h


def gindex(references):
    refs = [r.citedby for r in references]
    refs.sort()
    refs.reverse()
    g, citations = 0, 0
    while g < len(refs) and refs[g] > 0:
        citations += refs[g]
        if citations < g * g: break
        g = g + 1
    if not citations: return 0
    return g - 1

# ------------------------------------------------------------------------------

if __name__ == "__main__":
    import sys
    import scholar

    name = sys.argv[1]
    name = name.replace(" ", "+")
    name = name.replace('"', "%22")
    s = scholar.Scholar(cachetimeout=datetime.timedelta(seconds=60))
    (metadata, references) = s.query("as_sauthors=%s" % name)
    s.debugInfo("done")
    print
    print "h-index: %d (a=%.2f, m=%.2f)" % hindex(references)
    print "g-index:", gindex(references)