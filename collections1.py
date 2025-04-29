from collections import Counter, deque, OrderedDict

c = Counter(p=4, q=2, r=0, s=-2)
print(list(c.elements()))


s = 'lkseropewdssafsdfafkpwe'
print("Original string: "+s)
print("most common three char of the said str")
print(Counter(s).most_common(3))

dq = deque('aeiou')
for i in dq:
    print(i)

text = """Python is a widely used high-level programming language for general-purpose programming,
created by Guido van Rossum and first released in 1991. Python has a design philosophy that
emphasizes code readability, and a syntax that allows programmers to express concepts in fewer
lines of code than might be used in languages such as C++ or Java."""

words = text.lower().split()
word_counts = Counter(words)
most_common = word_counts.most_common(10)

print(most_common)

n = int(input("Enter number of words: "))


words = [input().strip() for _ in range(n)]
word_counter = OrderedDict()

for word in words:
    word_counter[word] = word_counter.get(word, 0) + 1


print(len(word_counter))
print(" ".join(str(count) for count in word_counter.values()))