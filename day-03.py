#!/usr/bin/python3

import sys

def priority(item: str) -> int :
	res = ord(item)
	if res >= 65 and res <= 90 :
		return res - 38 # - 65 + 27
	if res >= 97 and res <= 122 :
		return res - 96
	raise ValueError(f"Invalid item {res}")


class GroupByIterator :

	def __init__(self, iter, num: int) :
		self.iter = iter
		self.num = num
	
	def __iter__(self) :
		return self
	
	def __next__(self) :
		res = [next(self.iter)]
		try :
			for _ in range(1, self.num) :
				res.append(next(self.iter))
		except StopIteration :
			raise ValueError(f"Input line count is not a multiple of {self.num}")
		return res

def common(bag1: str, bag2: str, bag3: str) -> str :
	for item in bag1 :
		if item in bag2 and item in bag3 :
			return item
	raise ValueError(f"No common item found ({bag1}, {bag2}, {bag3})")

def part2() :
	total = 0
	for bags in GroupByIterator(iter(sys.stdin), 3) :
		item = common(bags[0].strip(), bags[1].strip(), bags[2].strip())
		prio = priority(item)
		total += prio
	print(total)


def dup(bag: str) -> str :
	first = bag[:len(bag)//2]
	second = bag[len(bag)//2:]
	for item in first :
		if item in second : 
			return item
	raise ValueError(f"No duplicate found ({first} / {second})")

def part1() :
	total = 0
	for line in sys.stdin :
		line = line.strip()
		item = dup(line)
		prio = priority(item)
		# print(item, prio)
		total += prio
	print(total)


if __name__ == '__main__' :
	part2()