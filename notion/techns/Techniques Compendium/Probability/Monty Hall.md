# Monty Hall

Problem:
You're a contestant on a game show and you're given the choice of three doors. Behind one door is a car, and behind the other two doors are goats. You pick a door, say number 1, and the host, who knows what's behind the doors, opens another door, say number 3, which has a goat. The host then asks you if you want to switch your choice to door number 2 or stay with door number 1. What should you do?

Solution:
The optimal strategy is to switch your choice to door number 2. This might seem counterintuitive, but the probability of winning the car increases from 1/3 to 2/3 if you switch. This can be explained by the fact that when you initially pick door number 1, the probability of the car being behind it is 1/3. This means that the probability of the car being behind either door number 2 or 3 is 2/3. When the host opens door number 3 and reveals a goat, the probability of the car being behind door number 2 increases to 2/3 because if the car was behind door number 1 initially, it must be behind door number 2 now. Therefore, switching to door number 2 is the optimal strategy.

---

### Gen

PROB: 

Someone is asked to choose between several options, only one of which is correct, and then given additional information that allows them to revise their initial choice.

SOLN:

The reason why switching in the Monty Hall problem works is because the initial probability of choosing the correct door is 1/3, while the probability that the car is behind one of the other two doors is 2/3. When one of the incorrect doors is revealed, the probability of the car being behind the remaining door increases to 2/3. Therefore, switching to the other door gives the contestant a higher probability of winning the prize.

An example of using this principle to solve another problem is in A/B testing for website design. In A/B testing, two versions of a website are shown to different groups of users, and the goal is to determine which version leads to more conversions (e.g. sign-ups, purchases, etc.). By randomly assigning users to one of the two versions, the initial probability of a user converting is the same for both versions. However, if one version is found to lead to significantly more conversions, it can be inferred that it is the correct option, and additional users can be directed to that version to maximize conversions. This is similar to switching doors in the Monty Hall problem, in that the initial probability of success is the same for all options, but additional information can be used to revise the initial decision and improve the probability of success.

Ask GPT4 to draw a picture of this?

---

### Links

[https://www.youtube.com/watch?v=ngUyyFd86FQ&list=PLDZcGqoKA84Eo56G1kIFE6IYwpxFgxFXB&index=3&ab_channel=MindYourDecisions](https://www.youtube.com/watch?v=ngUyyFd86FQ&list=PLDZcGqoKA84Eo56G1kIFE6IYwpxFgxFXB&index=3&ab_channel=MindYourDecisions)

When you stay, you only win for when car at chosen spot 1

When you switch, you win for when car at chosen spots 2 or 3. 

---

### Other Notes

Becomes clearer if have 100 doors, where you open 98 doors.

Strong evidence of ‘switch’ solution being correct comes from simulations