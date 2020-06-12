from itertools import groupby
l = [(len(list(c)), int(k)) for k, c in groupby(input())]
print(*l) # * adds a whitespace and joins the elements, much like " ".join(l)