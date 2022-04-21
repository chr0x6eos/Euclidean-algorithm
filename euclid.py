#!/usr/bin/env python3
import argparse
from typing import List


class Euclid:
    i = 1
    a = [1, 0]
    b = [0, 1]
    q = [None, None]
    r = []

    def __init__(self, a, b) -> None:
        self.r.append(a)
        self.r.append(b)

    def calc_next(self) -> None:
        self.q.append(self.r[self.i - 1] // self.r[self.i])
        self.r.append(self.r[self.i - 1] % self.r[self.i])
        self.a.append(self.a[self.i - 1] - self.a[self.i] * self.q[self.i + 1])
        self.b.append(self.b[self.i - 1] - self.b[self.i] * self.q[self.i + 1])

    def format_line(self, header: str, list: List) -> str:
        tab = '\t'
        for i, x in enumerate(list):
            if x == None:
                list[i] = ""
            else:
                if x >= 0:
                    list[i] = " " + str(x)
                else:
                    list[i] = str(x)
        return f'{header}{tab}{f"{tab}".join(list)}'

    def print_final(self) -> None:
        data = []
        i = self.format_line("i", [x-1 for x in range(0, self.i+1)])
        a = self.format_line("ai", self.a)
        b = self.format_line("bi", self.b)
        q = self.format_line("qi", self.q)
        r = self.format_line("ri", self.r)
        [print(x) for x in [i, a, b, q, r]]
        print(f"\nggT({self.r[0]},{self.r[1]}) = {self.r[-2]}")

    def euclid_algo(self) -> None:
        while self.r[self.i] != 0:
            self.calc_next()
            self.i += 1

    def run(self) -> None:
        self.euclid_algo()
        self.print_final()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Euclidean Algorithm Calculator by Simon Possegger')
    parser.add_argument('a', nargs='?', help="Number a", type=int)
    parser.add_argument('b', nargs='?', help="Number b", type=int)
    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
        exit(1)

    algo = Euclid(args.a, args.b)
    algo.run()
