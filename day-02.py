#!/usr/bin/python3

import sys

opponent_moves = { 'A': 1, 'B': 2, 'C': 3 }
player_moves   = { 'X': 1, 'Y': 2, 'Z': 3 }
player_strategies = {
	'X': (0, lambda x: ((x + 1) % 3) + 1),
	'Y': (3, lambda x: x),
	'Z': (6, lambda x: (x % 3) + 1)
}


def part2() :
	total = 0
	for line in sys.stdin :
		line = line.strip().split(' ')
		opponent = opponent_moves[line[0]]
		outcome, move = player_strategies[line[1]]
		total += outcome + move(opponent)
	print(total)


def part1() :
	total = 0
	for line in sys.stdin :
		line = line.strip().split(' ')
		opponent = opponent_moves[line[0]]
		player   = player_moves[line[1]]
		bonus = 3 if player == opponent else 6 if player == (opponent % 3) + 1 else 0
		total += player + bonus
	print(total)


if __name__ == '__main__' :
	part2()