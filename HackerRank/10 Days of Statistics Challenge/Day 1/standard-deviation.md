## Objective
In this challenge, we practice calculating standard deviation. Check out the Tutorial tab for learning materials and an instructional video!

## Task
Given an array, $X$, of $N$ integers, calculate and print the standard deviation. Your answer should be in decimal form, rounded to a scale of 1 decimal place (i.e., 12.3 format). An error margin of $\pm 0.1$ will be tolerated for the standard deviation.

##Input Format

The first line contains an integer, $N$, denoting the number of elements in the array.
The second line contains $N$ space-separated integers describing the respective elements of the array.

## Constraints

- $5 <= N <= 100$
- $0 < x_{i} <= 10^{5}$, where $x_{i}$ is the i^{th} element of array .

## Output Format

Print the standard deviation on a new line, rounded to a scale of 1 decimal place (i.e., 12.3 format).

## Sample Input
```
5
10 40 30 50 20
```

## Sample Output
```
14.1
```

## Explanation

First, we find the mean:
$$\mu = \frac{\sum_{i=0}^{N-1}x_{i}}{N} = 30.0$$

Next, we calculate the squared distance from the mean, $(x_{i} - \mu)^{2}$, for each x_{i}:

1. $(x_{0} - \mu)^{2} = (10 - 30)^{2} = 400$<br>
2. $(x_{1} - \mu)^{2} = (40 - 30)^{2} = 100$<br>
3. $(x_{2} - \mu)^{2} = (30 - 30)^{2} = 0$<br>
4. $(x_{3} - \mu)^{2} = (50 - 30)^{2} = 400$<br>
5. $(x_{4} - \mu)^{2} = (20 - 30)^{2} = 100$<br>

Now we can compute $\sum_{i=0}^{N-1}(x_{i} - \mu)^{2} = 400 + 100 + 0 + 400 + 100 = 1000$, so:
$$ \sigma = \sqrt{\frac{\sum_{i=0}^{N-1}(x_{i} - \mu)^{2}}{N}} = \sqrt{\frac{1000}{5}} = \sqrt{200} = 14.1421356 $$

Once rounded to a scale of 1 decimal place, our result is 14.1.