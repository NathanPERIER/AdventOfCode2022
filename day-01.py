#!/usr/bin/python3

import sys
from typing import Optional

class InputIterator :

	def __init__(self, stdin) :
		self.stdin = stdin

	def readline(self) -> Optional[int] :
		line = next(self.stdin).strip()
		if len(line) == 0 :
			return None
		return int(line)
	
	def __iter__(self) -> "InputIterator" :
		return self
	
	def __next__(self) -> int :
		res = 0
		line = self.readline()
		try :
			while line is not None :
				res += line
				line = self.readline()
		except StopIteration :
			pass
		return res

def main() :
	# print(max(enumerate(InputIterator(sys.stdin)), key = lambda x: x[1]))
	top_three = [0, 0, 0]
	min_top = 0
	for count in InputIterator(sys.stdin) :
		if count > min_top :
			top_three.append(count)
			top_three.sort(reverse=True)
			top_three.pop()
	print(top_three)
	print(sum(top_three))

if __name__ == '__main__' :
	main()