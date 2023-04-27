# Can you use the 31
dominos to cover the entire board?

PROB: The first and last square, diagonally opposite, are cut off on the 8x8 board.

---

ATTEMPT: 

31 * 2 is 62. However, if we look at the first row, there’s only 7 squares, so on domino must extend to the next row. But now the next row only has 7 squares, so it must extend to the next row. If this keeps going to the last row, the last row will only has 6 …?

Without drawing it, it’s hard to see what happens. Try to solve a smaller problem. Say it’s 2x8, with same cutoffs, but now only 16 / 2 -1 = 7 dominoes. It’s immediately clear you can’t do this b/c when you try to extend this to the next row, it will hit a missing square. 

But if it’s 3x8, with 24 / 2 -1 = 11 dominos,  it IS possible. So we hypothesize that it’s impossible if it’s odd, and possible if it’s even. For the base case, we say that we showed it by brute force for 2x8 and 3x8. 

Now assume it’s true for the even case at i = n. Then the domino must have not been able to be placed at the next row due to the missing square. But at i = n+1, this missing square is restored and instead the row below has a missing square. But by brute force, if we fill it in, we find it’s possible. This proves it for i = n+1, which is odd.

Now if i = m was odd, then by adding one more row and brute forcing, we show it’s impossible again. So i = m+1 is impossible for even.

By the induction hypothesis, we showed our statements are true for both even and odd cases. 

Now since 8x8 is an even case, it’s impossible.

---