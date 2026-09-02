# Probability Notes

## Basic Concepts

- Probability of an event A: P(A) = (number of favorable outcomes) / (total outcomes)
- 0 ≤ P(A) ≤ 1

## Coin Toss Example

Probability of heads in a fair coin: 0.5

## Dice Example

Probability of rolling a 4 on a fair six-sided die: 1/6

## Simulations (Python)

```python
import random
coin_tosses = [random.choice(['H', 'T']) for _ in range(10)]    # call a face 10 times, randomly put H/T on each face
print('Coin tosses:', coin_tosses)  # print the tosses
dice_rolls = [random.randint(1, 6) for _ in range(10)]  # call 10 times a int value b/w 1-6
print('Dice rolls:', dice_rolls)
```
