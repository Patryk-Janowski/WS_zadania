#!/usr/bin/env python3

import sys

class Fibonacci:
    # Jako że miałem więcej czasu to zrobiłem klasę
    # w init zdefiniowane są 2 początkowe elementy
    def __init__(self):
        self.prev = 0
        self.curr = 1

    # Metodą klasy jest generator, który zachowuje wewnętrzny stan i nie zajmuje zbyt wiele
    # miejsca w pamięci co pozwala na wydajne działanie programu
    def get_elements(self):
        res = self.prev
        self.prev = self.curr
        self.curr = self.curr + res
        yield res

    # Funkcja to korzysta z generatora stworzonego powyżej
    def print_elements(self, n):
        for _ in range(n):
            print(self.get_elements().__next__())
            

if __name__ == '__main__':
    if len(sys.argv) == 2:
        f = Fibonacci()
        f.print_elements(int(sys.argv[1]))
    else:
        print(f'usage {sys.argv[0]} [num of elements to print]')
