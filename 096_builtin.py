# 파이썬의 내장함수( built-in functions)
# 별도의 import 없이 바로 사용 가능한 함수들.

# 레퍼런스 :  https://docs.python.org/3/library/functions.html

# abs()	dict()	help()	min()	setattr()
# all()	dir()	hex()	next()	slice()
# any()	divmod()	id()	object()	sorted()
# ascii()	enumerate()	input()	oct()	staticmethod()
# bin()	eval()	int()	open()	str()
# bool()	exec()	isinstance()	ord()	sum()
# bytearray()	filter()	issubclass()	pow()	super()
# bytes()	float()	iter()	print()	tuple()
# callable()	format()	len()	property()	type()
# chr()	frozenset()	list()	range()	vars()
# classmethod()	getattr()	locals()	repr()	zip()
# compile()	globals()	map()	reversed()	__import__()
# complex()	hasattr()	max()	round()
# delattr()	hash()	memoryview()	set()

print(abs(-111))

data = [10, 20, 30, 40]

print(min(data), max(data), sum(data))

print(type(sum))

# 실수로 내장함수를 덮어쓰기 하면????

sum = 10 + 20
print(sum, type(sum))
# print(sum(data))

sum = __builtins__.sum # 원래 내장함수로 복원
print(sum(data))


