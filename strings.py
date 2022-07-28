# strings could be encoded or decoded with standard library translate method
source, dest, decoded, encoded = ('abcd', '*d%#', 'abacabadaba', '#*%*d*%')
print(decoded.translate(str.maketrans(source, dest)))
print(encoded.translate(str.maketrans(dest, source)))
