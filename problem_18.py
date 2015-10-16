"""
Maximum path sum I
------------------

By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

              75
             95 64
            17 47 82
           18 35 87 10
          20 04 82 47 65
         19 01 23 75 03 34
        88 02 77 73 07 63 67
       99 65 04 28 06 16 70 92
      41 41 26 56 83 40 80 70 33
     41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot
be solved by brute force, and requires a clever method! ;o)
"""

from utils.timer import time_it
from utils.sequences import bitstrings_of_length

#-------------------------------------------------------------------------------------------------

triangle_str = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

#-------------------------------------------------------------------------------------------------

@time_it
def problem_18():
    """ Starting at the top element of the triangle, moving to an adjacent number on the row
    below, you can either go left (and the index of the item of the next row remains the same),
    or you can go right (and the index of the item of the next row is 1 higher than the current
    row).

    For a 15-row triangle, there are 14 choices to make: for each row below the current row,
    choose the item on the left or the item on the right. These choices can be represented as a
    length-14 bitstring, where 0 represents the left item, and 1 represents the right item.
    To enumerate all possible paths down the triangle, we need to generate all bitstrings of
    length 14.

    For each bitstring, we can use the index of each bit (i) to address the row of the triangle
    (as i+1, since row 0 in the triangle is where we start), and the value of each bit can be used
    to determine whether we keep the index within the row the same (aka choosing the left item) or
    increase it by 1 (aka choosing the right item).

    For each bitstring, sum the numbers we traverse along that path down the triangle. After we
    are done, display the largest sum we found.
    """

    triangle = [[int(y) for y in x.split()] for x in triangle_str.splitlines() if x]
    winner = 0

    for s in bitstrings_of_length(len(triangle) - 1):
        curr_index = 0
        curr_sum = triangle[0][0]

        for i, bit in enumerate(s):
            curr_index += int(bit)
            curr_sum += triangle[i + 1][curr_index]

        if curr_sum > winner:
            winner = curr_sum

    print(winner)

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_18()
