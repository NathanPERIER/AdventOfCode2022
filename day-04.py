#!/usr/bin/python3

import sys

def parseRanges(line: str) :
	ranges = [
		[int(i) for i in r.split('-')] 
		for r in line.split(',')
	]
	return ((ranges[0][0], ranges[0][1]), (ranges[1][0], ranges[1][1]))


def partialOverlap(r11, r12, r21, r22) -> bool :
	if r11 <= r21 and r21 <= r12 :
		return True
	if r21 <= r11 and r11 <= r22 :
		return True
	return False

def part2() :
	total = 0
	for line in sys.stdin :
		((r11, r12), (r21, r22)) = parseRanges(line.strip())
		if partialOverlap(r11, r12, r21, r22) :
			total += 1
	print(total)


def fullOverlap(r11, r12, r21, r22) -> bool :
	if r11 <= r21 and r22 <= r12 :
		return True
	if r21 <= r11 and r12 <= r22 :
		return True
	return False

def part1() :
	total = 0
	for line in sys.stdin :
		((r11, r12), (r21, r22)) = parseRanges(line.strip())
		if fullOverlap(r11, r12, r21, r22) :
			total += 1
	print(total)


if __name__ == '__main__' :
	part2()