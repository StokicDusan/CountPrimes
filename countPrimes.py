from math import log2
from time import perf_counter
from doctest import testmod
import sys


class Stopwatch:
    def __init__(self):
        self.reset()

    def start(self):
        if not self.__running:
            self.__start_time = perf_counter()
            self.__running = True
        else:
            print('Stopwatch already running')

    def stop(self):
        if self.__running:
            self.__elapsed += perf_counter()-self.__start_time
            self.__running = False
        else:
            print('Stopwatch not running')

    def reset(self):
        self.__start_time = self.__elapsed = 0
        self.__running = False

    def elapsed(self):
        if not self.__running:
            return self.__elapsed
        else:
            print('Stopwatch must be stopped')
            return None


def TCS(yy):
    global nonprimes
    global allPrimeCount, pythagoreanPrimeCount, twinPrimeCount
    global cousinPrimeCount, sexyPrimeCount
    if (yy-1)/4 == ((yy-1)/4)//1:
        pythagoreanPrimeCount += 1
    if (yy+2 <= int(sys.argv[2]) and not nonprimes[yy] and not nonprimes[yy+2]):
        twinPrimeCount += 1
    if (yy+4 <= int(sys.argv[2]) and not nonprimes[yy] and not nonprimes[yy+4]):
        cousinPrimeCount += 1
    if (yy+6 <= int(sys.argv[2]) and not nonprimes[yy] and not nonprimes[yy+6]):
        sexyPrimeCount += 1


def euclid(yy):
    global euclidPrimeCount, Euclid_Primes, nonprimes
    product = 1
    i = 2
    while (product < yy):
        if not nonprimes[i]:
            product = product * i
        if (product + 1 == yy):
            if yy not in Euclid_Primes:
                euclidPrimeCount += 1
                Euclid_Primes += [yy]
                return True
        i += 1


def mersenne(yy):
    global mersennePrimeCount, Mersenne_Primes
    if log2(yy+1) == log2(yy+1)//1:
        trial_factor = 2
        is_Mersenne = True
        while trial_factor < log2(yy+1):
            if log2(yy+1) % trial_factor == 0:
                is_Mersenne = False
                break
            trial_factor += 1
        if is_Mersenne:
            if yy not in Mersenne_Primes:
                Mersenne_Primes += [yy]
                mersennePrimeCount += 1


def count(pr: int, max_value: int) -> int:
    global allPrimeCount, nonprimes, timer
    timer.start()
    nonprimes = max_value * [False]
    nonprimes[0] = nonprimes[1] = True
    for i in range(2, max_value):
        if not nonprimes[i]:
            for j in range(2*i, max_value, i):
                nonprimes[j] = True
    if pr == 2 or pr == 3:
        for i in range(2, max_value):
            if not nonprimes[i]:
                allPrimeCount += 1
                TCS(i)
                mersenne(i)
                euclid(i)
    timer.stop()
    if pr == 1 or pr == 3:
        k = 0
        for i in nonprimes:
            if i == False:
                print(k, end=" ")
                k += 1
            else:
                k += 1
    print()
    return max_value


def test_main():
    """
    >>> main(1,10)
    2 3 5 7 
    >>> main(1,15)
    2 3 5 7 11 13 
    >>> main(1,17)
    2 3 5 7 11 13 17 
    """
    pass


def display(n):
    global allPrimeCount, mersennePrimeCount, Mersenne_Primes
    global twinPrimeCount, cousinPrimeCount
    global sexyPrimeCount, pythagoreanPrimeCount
    global euclidPrimeCount, Euclid_Primes, timer
    print('There are', f'{allPrimeCount:,}', 'Primes!!!!')
    print('%.3f' % (allPrimeCount*100/n), '% are Primes', sep="")
    print('There are', f'{mersennePrimeCount:,}',
          'Mersenne Primes { Mp=2**p-1 }', end=": ")
    for i in Mersenne_Primes:
        print(i, end=" ")
    print()
    print('There are', f'{euclidPrimeCount:,}',
          'Euclid Primes { Ep=pn#+1 }', end=": ")
    for i in Euclid_Primes:
        print(i, end=" ")
    print()
    print('There are', f'{twinPrimeCount:,}', 'Twin Primes')
    print('There are', f'{cousinPrimeCount:,}', 'Cousin Primes')
    print('There are', f'{sexyPrimeCount:,}', 'Sexy Primes')
    print('There are', f'{pythagoreanPrimeCount:,}',
          'Pythagorean Primes { Pp=4n+1 }', end="")
    print()
    print('Elapsed:', round(timer.elapsed(), 6), 'seconds')


def main(argv1, argv2):
    n = count(int(argv1), int(argv2)+1)
    if int(argv1) == 2 or int(argv1) == 3:
        display(n)


nonprimes = 0
allPrimeCount = 0
mersennePrimeCount = 0
twinPrimeCount = 0
cousinPrimeCount = 0
sexyPrimeCount = 0
euclidPrimeCount = 0
pythagoreanPrimeCount = 0
Mersenne_Primes = []
Euclid_Primes = []
timer = Stopwatch()


if __name__ == "__main__":
    if(sys.argv[1:] and sys.argv[2:]):
        main(int(sys.argv[1]), int(sys.argv[2]))
    else:
        testmod()
    print()
