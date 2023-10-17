# Find kth largest element

SOLN: search k times, finding largest then 2nd largest… to kth largest.

Has O(kn) time

---

SOLN: sort then find kth last

O(nlog(n)) time

---

SOLN: heapify then extract from heap

O(n + k*log(n)) time

WHY: heapify doesn't need to sort, but allows you to obtain the largest or smallest element in O(log(n)) since it'd be on root, depending on max or min heap. Log(n) to rearrange heap from leaf swapped up to root since root is now gone