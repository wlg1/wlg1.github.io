# 746. Min Cost Climbing Stairs

[https://leetcode.com/problems/min-cost-climbing-stairs/description/?envType=study-plan-v2&envId=leetcode-75](https://leetcode.com/problems/min-cost-climbing-stairs/description/?envType=study-plan-v2&envId=leetcode-75)

One misunderstanding to clear up in the problem is that the “top floor” is the end of the array. It’s not; the end of the array, cost[-1], is the cost to reach the step OUT of the array.

Thus, cost[-1] is the cost from the second last floor to the top floor, and cost[-2] is the cost from the third last to the top floor. When you pay cost[-2] to take two steps to the top floor, you have already reached the top floor. You no longer need cost[-1].

That is, you don’t need to pay the cost when you REACH the floor; you pay the cost TO REACH the next floor!

G- Clarify what is defined as each “description”; don’t just assume