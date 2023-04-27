# MNIST_1_vs_7- find_avg_diffs.ipynb

Link to notebook: [https://colab.research.google.com/drive/1NfYhLjJEanWE3iu191-qzZi26ZIFeWVk#scrollTo=6Cli8rxOMNSf](https://colab.research.google.com/drive/1NfYhLjJEanWE3iu191-qzZi26ZIFeWVk#scrollTo=6Cli8rxOMNSf)

### Type of Notebook: Draft

---

### **Attempt 1: Average each neuron**

For Question/Task: Find the neurons that control for the top line that distinguishes b/w 1 and 7

---

- EXPERIMENT: Get neurons w/ biggest avg diffs b/w classes
    
    

---

- EXPM: Set weights above threshold to 0 and compare to hist of random weights set to 0
    
    DESC: Set weights where diff of ones and sevens above certain threshold to 0. Compare with avg of same # of weights chosen randomly set to 0, to see if any sigf. Get histogram of random weights set to 0.
    
    RESULT: 
    
    ![Untitled](MNIST_1_vs_7-%20find_avg_diffs%20ipynb%20ddf4463fc3374e91ad6ccaadbd8a2e97/Untitled.png)
    
    Find the percentage of neurons that have an activation difference of under 0.2 (meaning there is not much difference between them, on avg, for class 1 vs class 7):
    
    ```python
    sum(abs(i) < 0.2 for i in diffs.tolist() ) / len(diffs)
    ```
    
    ANALYSIS:
    
    Around 60% of neurons have an activation difference of less than 0.2. Notice that destroying neurons which have a difference above 0.4 doesn't have as much effect as destroying those above 0.3, and even more so for 0.2.
    
    From this, it seems like the 'highest activated neurons' are not so important as the number of neurons firing above some level. Those neurons b/w 0.3 and 0.4 are very impt.
    
    Is this because of the % of neurons destroyed, or specifically those neurons above a certain threshold?
    

---

STUCK