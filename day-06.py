#!/usr/bin/python3

import sys


def getMatchingPair(line: str, start: int, length: int) :
	for i in range(length - 1) :
		first_idx = start + i
		first = line[first_idx]
		for j in range(length - 1 - i) :
			second_idx = first_idx + j + 1
			second = line[second_idx]
			if first == second :
				return (first_idx, second_idx)
	return None


def part2() :
	line = sys.stdin.readline()
	i = 0
	while True :
		pair = getMatchingPair(line, i, 14)
		if pair is None :
			print(i+14)
			return
		i = pair[0] + 1


def part1() :
	line = sys.stdin.readline()
	i = 0
	while True :
		pair = getMatchingPair(line, i, 4)
		if pair is None :
			print(i+4)
			return
		i = pair[0] + 1


if __name__ == '__main__' :
	part2()