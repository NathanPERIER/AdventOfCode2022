#!/usr/bin/python3

import sys

class UntilBlankLineIterator :

	def __init__(self, iter) :
		self.iter = iter
	
	def __iter__(self) :
		return self
	
	def __next__(self) :
		res = next(self.iter).rstrip()
		if len(res) == 0 :
			raise StopIteration
		return res

def parseBegin(lines: "list[str]") :
	res = []
	indexes = [i for i, x in enumerate(lines[0]) if x != ' ']
	for _ in indexes :
		res.append([])
	for line in lines[1:] :
		for (stack, i) in zip(res, indexes) :
			if i < len(line) and line[i] != ' ' :
				stack.append(line[i])
	return res

def parseMove(line: str) :
	words = line.split()
	return (int(words[1]), int(words[3]) - 1, int(words[5]) - 1)


def part2() :
	begin = []
	for line in UntilBlankLineIterator(iter(sys.stdin)) :
		begin.insert(0, line)
	stacks = parseBegin(begin)
	for stack in stacks :
		print(stack)
	for line in sys.stdin :
		count, from_stack, to_stack = parseMove(line.strip())
		print(f"{from_stack} -> {to_stack} : {count}")     # x -> y : 2
		source = stacks[from_stack]                        #       [1, 2, 3, 4, 5, 6] <- x
		grabbed = source[(-1*count):]                      # [-2:] [5, 6]
		stacks[from_stack] = source[:(len(source)-count)]  #  [:4] [1, 2, 3, 4] -> x
		stacks[to_stack].extend(grabbed)                   #       [...,  5, 6] -> y
	print("".join(stack[-1] for stack in stacks))


def part1() :
	begin = []
	for line in UntilBlankLineIterator(iter(sys.stdin)) :
		begin.insert(0, line)
	stacks = parseBegin(begin)
	for stack in stacks :
		print(stack)
	for line in sys.stdin :
		count, from_stack, to_stack = parseMove(line.strip())
		print(f"{from_stack} -> {to_stack} : {count}")
		for _ in range(count) :
			crate = stacks[from_stack].pop()
			stacks[to_stack].append(crate)
	print("".join(stack[-1] for stack in stacks)) 


if __name__ == '__main__' :
	part2()