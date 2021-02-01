import hashlib

# input: 10203040
# output: 58f966a9a6f34334c5d70a548d1c04674296c826c5c5162d49425ce2fe9b78cf

q = input("String to be converted to sha256: ")
print(hashlib.sha256(q.encode("utf-8")).hexdigest())