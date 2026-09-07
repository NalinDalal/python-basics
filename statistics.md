# Statistics Notes

## Mean

The average value: mean = (sum of all values) / (number of values); a value to represent every no in set
how would you do it in python: loop through array, sum it, then divide with size

```python
import numpy as np
array=[1,2,3,4,5,6]

#call the mean operation ddirectly
mean=np.mean(array)

```

## Variance

measure of how far a set of numbers are spread out from their average value

```python
var=np.var(array)
```

## Normal Distribution

A bell-shaped curve, symmetric about the mean.

---

## Example (Python)

```python
import numpy as np
nums = [1, 2, 3, 4, 5]
print('Mean:', np.mean(nums))
print('Variance:', np.var(nums))
# Normal distribution
samples = np.random.normal(loc=0, scale=1, size=5)
print('Normal distribution samples:', samples)
```
