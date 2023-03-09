# https://medium.com/mlearning-ai/when-and-why-to-use-over-in-python-b91168875453

f = lambda x: (m := x + 1) + (m ** 2)
g = [y := f(3), y ** 2, y ** 3]  # contents: [5, 25, 125]

# -------------------
# 1
for line in open('text.txt', 'r').read().split('\n'):
    print(line)
# 2
for line in open('text.txt', 'r').readlines():
    print(line)
# 3
while chunk := open('text.txt').read():
    print(chunk)
# -------------------
data = [1, 2, 3, 4]
f_data = [y for x in data if (y := f(x)) != 4]
# -------------------
# Handle a matched regex
# if (match := pattern.search(data)) is not None:
# Do something with match

# A loop that can't be trivially rewritten using 2-arg iter()
while chunk := file.read(8192):
   process(chunk)

# Reuse a value that's expensive to compute
# [y := f(x), y ** 2, y ** 3]

# Share a subexpression between a comprehension filter clause and its output
filtered_data = [y for x in data if (y := f(x)) is not None]
