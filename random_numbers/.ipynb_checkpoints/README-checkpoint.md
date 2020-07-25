# <font color="gold">__Random Number Generator__</font>
- Random Numbers with Python
- Random Numbers with NumPy
## <font color="purple"><ins><b>Random Numbers with Python</b></ins></font>
Python uses a popular and robust pseudorandom number generator called the [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister). The pseudorandom number generator is a mathematical function that generates a sequence of nearly random numbers. It takes a parameter to start off the sequence, called the <font color="gren">seed</font>.

- <font color="gren">Pseudorandomness</font> is a sample of numbers that look close to random, but were generated using a deterministic process.

- The <font color="gren">function generating the sequence is deterministic</font>, meaning given the same seed, it will produce the same sequence of numbers every time

- The value of the seed does not matter. Choose anything you wish. What does matter is that the same seeding of the process will result in the same sequence of random numbers.

- If you do not explicitly seed the pseudorandom number generator, then it may use the <font color="gren">current system time in seconds or milliseconds as the seed</font>

<font color="teal"><ins><b>__1) Random Floating Values__</ins></b></font>
- <font color="red">__Python__</font>
```python
# seed the pseudorandom number generator
from random import seed
from random import random
# seed random number generator
seed(1)
# generate some random numbers
print(random(), random(), random())
# reset the seed
seed(1)
# generate some random numbers
print(random(), random(), random())
```
Output: 
> 0.13436424411240122 0.8474337369372327 0.763774618976614
> 0.13436424411240122 0.8474337369372327 0.763774618976614

- <font color="red">__Numpy__</font>
```python
# generate random floating point values
from numpy.random import seed, rand
seed(1)
# generate random numbers between 0-1
values = rand(10)
print(values)
```
Output:
> [4.17022005e-01 7.20324493e-01 1.14374817e-04 3.02332573e-01
 1.46755891e-01 9.23385948e-02 1.86260211e-01 3.45560727e-01
 3.96767474e-01 5.38816734e-01]
 
> <font color="yellow">Note the values generated are randomly generated floating values</font>


<font color="teal"><ins><b>__2) Random Integer Values__</ins></b></font>
- <font color="red">__Python__</font>
```python
# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(1)
# generate some integers
for _ in range(10):
	value = randint(0, 10)
	print(value)
```
Output:
> 2, 9, 1, 4, 1, 7, 7, 7, 10, 6

- <font color="red">__Numpy__</font>
```python
from numpy.random import seed, randint
seed(1)
values = randint(0, 10, 20)
print(values)
```
Ouput
> [5 8 9 5 0 0 1 7 6 9 2 4 5 2 4 2 4 7 7 9]


<font color="teal"><ins><b>__3) Random Gaussian Values__</ins></b></font>
- <font color="red">__Python__</font>
<br>Random floating point values can be drawn from a Gaussian distribution using the gauss() function<br>
This function takes two arguments that correspond to the parameters that control the size of the distribution, specifically the mean and the standard deviation
```python
# generate random Gaussian values
from random import seed, guass
# seed random number generator
seed(1)
# generate some Gaussian values
for _ in range(10):
	value = gauss(0, 1)
	print(value)
```
output
> 1.2881847531554629, 1.449445608699771, 0.06633580893826191, -0.7645436509716318, -1.0921732151041414, 0.03133451683171687, -1.022103170010873, -1.4368294451025299, 0.19931197648375384, 0.13337460465860485

- <font color="red">__Numpy__</font>
```python
# generate random Gaussian values
from numpy.random import seed, randn
seed(1)
values = randn(10)
print(values)
```
Output
> [ 1.62434536 -0.61175641 -0.52817175 -1.07296862  0.86540763 -2.3015387
  1.74481176 -0.7612069   0.3190391  -0.24937038]

<font color="teal"><ins><b>__4) Randomly Choosing From a List__</ins></b></font>
- <font color="red">__Python__</font>
```python
from random import seed,choice
seed(1)
# prepare a sequence
sequence = [i for i in range(20)]
print(sequence)
# make choices from the sequence
for _ in range(5):
	selection = choice(sequence)
	print(selection)
```
Output: 
> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]<br>
> 4, 18, 2, 8, 3

- <font color="red">__Numpy__</font>
```python
```

<font color="teal"><ins><b>__5) Randomly Shuffle a List__</ins></b></font>
- <font color="red">__Python__</font>
```python
from random import seed, shuffle
# seed random number generator
seed(1)
# prepare a sequence
sequence = [i for i in range(20)]
print(sequence)
# randomly shuffle the sequence
shuffle(sequence)
print(sequence)
```
Output: <br>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]<br>
[11, 5, 17, 19, 9, 0, 16, 1, 15, 6, 10, 13, 14, 12, 7, 3, 8, 2, 18, 4]<br>

- <font color="red">__Numpy__</font>
```python
# randomly shuffle a sequence
from numpy.random import seed, shuffle
seed(1)
sequence = [i for i in range(20)]
print(sequence)
# randomly shuffle the sequence
shuffle(sequence)
print(sequence)
```
Output:
> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
[3, 16, 6, 10, 2, 14, 4, 17, 7, 1, 13, 0, 19, 18, 9, 15, 8, 12, 11, 5]