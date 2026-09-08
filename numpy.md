# NumPy Cheat Sheet

## Import

```python
import numpy as np
```

## Creating Arrays

```python
np.array([1, 2, 3])                    # from list
np.zeros((3, 4))                       # 3x4 zeros
np.ones((2, 3))                        # 2x3 ones
np.empty((2, 3))                       # uninitialized
np.arange(0, 10, 2)                    # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)                   # 5 evenly spaced 0→1
np.random.rand(3, 3)                   # random 3x3 [0,1)
np.eye(4)                              # 4x4 identity
np.full((2, 3), 7)                     # 2x3 filled with 7
```

## Array Properties

```python
a.shape           # dimensions
a.ndim            # number of axes
a.size            # total elements
a.dtype           # data type
a.T               # transpose
```

## Indexing & Slicing

```python
a[0]              # first row
a[:, 1]           # second column
a[0:3, 1:4]       # subarray
a[a > 5]          # boolean indexing
np.where(a > 5, a, 0)  # conditional replace
```

## Reshaping

```python
a.reshape(3, 4)   # reshape
a.flatten()       # 1D copy
a.ravel()         # 1D view
np.expand_dims(a, axis=0)  # add dimension
np.squeeze(a)     # remove size-1 dims
```

## Math Operations

```python
a + b             # element-wise add
a * b             # element-wise multiply
a @ b             # matrix multiply
np.dot(a, b)      # dot product
np.sum(a, axis=0) # sum along axis
np.mean(a)        # mean
np.std(a)         # std deviation
np.min(a)         # min
np.max(a)         # max
np.argmin(a)      # index of min
np.argmax(a)      # index of max
np.cumsum(a)      # cumulative sum
np.sort(a)        # sort
```

## Broadcasting

```python
a + 5             # scalar + array
a * 2             # scalar * array
a + np.array([1, 2, 3])  # 1D broadcast to rows
```

## Useful Functions

```python
np.concatenate([a, b])       # join arrays
np.stack([a, b])             # stack arrays
np.split(a, 3)               # split into 3
np.unique(a)                 # unique values
np.intersect1d(a, b)         # common values
np.union1d(a, b)             # all unique values
np.isin(a, b)                # membership check
np.savetxt('f.txt', a)       # save to file
np.loadtxt('f.txt')          # load from file
```

## Linear Algebra

```python
np.linalg.inv(a)             # inverse
np.linalg.det(a)             # determinant
np.linalg.eig(a)             # eigenvalues/vectors
np.linalg.solve(a, b)        # solve Ax = b
np.linalg.norm(a)            # norm
```

## Random

```python
np.random.seed(42)           # reproducibility
np.random.randint(0, 10, 5)  # 5 random ints 0-9
np.random.choice(a, 3)       # random 3 from a
np.random.shuffle(a)         # shuffle in place
np.random.normal(0, 1, 100)  # normal distribution
```

## Type Conversion

```python
a.astype(np.float32)   # convert dtype
np.float64(a)          # same as above
a.astype(int)          # cast to int
```
