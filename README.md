[![Contributors][contributors-shield]][contributors-url]
[![Commit-activity][commit-activity-shield]][commit-activity-url]
[![Issues][issues-shield]][issues-url]
[![Repo-size][repo-size-shield]][repo-size-url]
[![License][license-shield]][license-url]  
[![Forks][forks-shield]][forks-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

# Count Primes

A script for printing and/or counting prime numbers.

## What does the script do?
The script calculates primes using the sieve of eratosthenes and count how many there are. 
It displays the number of Mersenne, Twin, Cousin, Sexy and Pythagorean primes.

## `countPrimes.py` :
This script is ready to use script which uses two arguments to run. The first argument decides what will be displayed and the second decides the upper bound for the search (including that number).


## Installing the dependencies

### Used packages
This script require the time, math, sys and doctest package.

## How to use it
#### 1. Clone this repository:
```bash
$ git clone https://github.com/StokicDusan/CountPrimes.git
$ cd CountPrimes/
```
#### 2. Launch:
In the command line simply invoke the script with two arguments:
```bash
$ python countPrimes.py argv1 argv2
```
* argv1:  
    | argv1                   | Value |
    |:------------------------|:-----:|
    | print primes               | 1 |
    | count primes               | 2 |
    | print and count primes     | 3 |

* argv2:  
Any positive integer  

:warning: *Note:* Other inputs will result in an error

Invoking the script with no or less arguments will run testmod().

## Examples

The following code block shows examples of calling the countPrimes script from terminal.

```bash
$ python3 countPrimes.py 1 1


$ python3 countPrimes.py 1 17
2 3 5 7 11 13 17 

$ python3 countPrimes.py 1 25
2 3 5 7 11 13 17 19 23 

$ python3 countPrimes.py 2 90

There are 24 Primes!!!!
26.374% are Primes
There are 3 Mersenne Primes { Mp=2**p-1 }: 3 7 31 
There are 3 Euclid Primes { Ep=pn#+1 }: 3 7 31 
There are 8 Twin Primes
There are 8 Cousin Primes
There are 15 Sexy Primes
There are 10 Pythagorean Primes { Pp=4n+1 }
Elapsed: 9.8e-05 seconds

$ python3 countPrimes.py 3 31
2 3 5 7 11 13 17 19 23 29 31 
There are 11 Primes!!!!
34.375% are Primes
There are 3 Mersenne Primes { Mp=2**p-1 }: 3 7 31 
There are 3 Euclid Primes { Ep=pn#+1 }: 3 7 31 
There are 5 Twin Primes
There are 4 Cousin Primes
There are 6 Sexy Primes
There are 4 Pythagorean Primes { Pp=4n+1 }
Elapsed: 5.6e-05 seconds
```
## Provide Feedback 👍

If you encounter any bugs or have suggestions, please file an issue in the
[Issues][issues-url]
section of the project.

[contributors-shield]: https://img.shields.io/github/contributors/StokicDusan/CountPrimes
[contributors-url]: https://github.com/StokicDusan/CountPrimes/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/StokicDusan/CountPrimes?style=social
[forks-url]: https://github.com/StokicDusan/CountPrimes/network/members
[issues-shield]: https://img.shields.io/github/issues/StokicDusan/CountPrimes
[issues-url]: https://github.com/StokicDusan/CountPrimes/issues
[commit-activity-shield]: https://img.shields.io/github/last-commit/StokicDusan/CountPrimes
[commit-activity-url]: https://github.com/StokicDusan/CountPrimes/graphs/commit-activity
[license-url]: https://github.com/StokicDusan/CountPrimes/blob/main/LICENSE
[license-shield]: https://img.shields.io/github/license/StokicDusan/CountPrimes
[repo-size-shield]: https://img.shields.io/github/repo-size/StokicDusan/CountPrimes
[repo-size-url]: https://img.shields.io/github/repo-size/StokicDusan/CountPrimes
[linkedin-shield]: https://img.shields.io/badge/LinkedIn-0077B5?style=plastice&logo=linkedin&logoColor=white
[linkedin-url]: https://linkedin.com/in/stokicdusan
