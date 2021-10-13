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

## Provide Feedback 👍

If you encounter any bugs or have suggestions, please file an issue in the
[Issues][issues-url]
section of the project.
