# EMNLP overall plan

Only work with llama-2: (can be **SEPARATE** circs; no need to have shared circuits):

- seq len?
    
    Use sequences of 3 (in llama2 this already has >80 to 90% acc usually, so no need for 4)
    
    but actually we’ll have to increase the number of prompts too to match the “12” in months, so this won’t save tokens
    
    also, when the tokenizer treats numbers differently, you have to use different number of tokens. But each prompts has its own “mean ablation” so we can do this. 
    
1. Run (ablation, logit lens/ov scores, attention heads) on: [just ONE backw run is needed!]
    1. 3 circs: numerals, en nw, en months
        1. *OPT*: daysWeek, letters
    2. Foreign Languages (just Spanish for EMNLP unless no good results)
        1. 2 circs: Number words, months
        2. *OPT*: daysWeek, letters
    3. Intervaled sequences (add [+2, …+100], multp [x2], fibonacci)
        1. 3-6 circs (+2, (+3, +100, + many at once), x2, fibonacci)
            1. *OPT*: Variations: all at once, seperate
    4. addition, multiplication
    - optional (if have time)
        1. *OPT*: Simple ‘next word’ math reasoning
        2. *OPT*: position-specific ablation to check head is on pos or tok
        3. *OPT*: edges to show component interaction

(ALso spanish nw and months in GPT-2)

gpt-2 (simple +1 seqs) and llama-2 (all others):

1. Ablate/scale those 8-11 circuits (poss subsets) and observe effect on mathematical reasoning
    - use mean ablation b/c we’re concat tokens
        - try 0 ablation first? doesn’t take a lot of time to run inference
    - compare to random component ablation
    - GPT2: Run JUST the sub-circuit, (its heads), (mlp9), (9.1), and indiv 3 task circs
        - gpt2 bad at word prompts; just focus on pure seqs & +1 eg.“day after Monday is”
        - put these in a colab section and just copy+change input to run again on new prompt
    - Check which reasoning prompts Llama-2 completes on
        
        [see “list of word prompts”](EMNLP%20overall%20plan%20c32b25f726554e429b3650b264829595.md)  [try 10-20 but choose only the best to show]
        
    - *OPT*: See if circs have backups

The main point is to just record observations (sims + diffs) and speculate on how model could be processing these things, in accordance to what prev papers found. Don’t worry about a new method/useful application here either- still not enough time. No need for really new insights, but try to spin it as furthering how language translation is understood.

Variations of main approach to try

- Mean ablate
    - zero ablate
- single Tok (limited num of prompts)
    - multiTok
- Ablate all pos
    - ONLY ablate CERTAIN tokens in initial prompt
- Ablate the circuit (necessary- likely no backups)
    - keep only the circuit (sufficient- likely may be backups)
    - keep only attn heads or MLPs
    - ablate edges
- Run each task separately to find circuits for each
    - Run tasks bundled together as 1

To-do and done

- llama-2 circuits to find
    
    Integers:
    
    - 1 2 3
    - 2 4 6
        - OPT: 3 6 9
        - OPT: 50 intervals
        - OPT: 100 intervals
    - multiplicative intervals (when does it recog 2 4 6; surely third token is impt to tell not add?)
        - will ablating 2 4 6 additive keep this? try 2 4. will it ‘make it multp’?
    - fibonacci
    - arithmetic circuits
    
    English:
    
    - OPT: days week
    - letters
    
    Spanish: (or another language)
    
    - nw
    - months
        - OPT: days week
    - letters (this is better for greek though; spanish largely same as english)
- circuits found
    
    English:
    
    - nw
    - months
- circuits (and sub-circs) ablated on prompts (pair)

- try both entire circuits and top-50 subset of it on prompts
- list of intersecting component sets (new nb for each; put this in folder)
    - EN with incr +1
        
        llama2_ablate_prompts_ENcircs.ipynb
        
    - SP with incr +1
    - EN with SP
    - numeral seqs (diff intervals)
    - EN, +1 with addition
    - Addition with mutp
    - EN, +1 with multp?
    - All

- things to make
    - mean ablate
    - ablate by pos
    - ablate by edges?
- things MADE
    - ✅ logit diff of multiple tokens

- missing number in seq, Eg. 1 2 y 4
- quatro vs cuatro

Overview Lists

- list of llama-2 circuits
    
    Integers:
    
    - 1 2 3
    - 2 4 6
        - OPT: 3 6 9
    - 50 intervals
        - OPT: 100 intervals
    - fibonacci
    - addition
    - multiplication
    
    English:
    
    - letters
    - nw
    - months
        - OPT: days week
    - word problems
        - What number comes after 3002? Answer:
    
    Spanish: (or another language)
    
    - letters (this is better for greek though; spanish largely same as english)
    - nw
    - months
        - OPT: days week
- list of pure seq prompts
    - 2 4 6
        - 3 6 9
        - 50 intervals
        - 100 intervals
- list of word prompts
    
    [https://chatgpt.com/c/8c5d7cb7-03e1-4fa0-8693-b61cca1f7922](https://chatgpt.com/c/8c5d7cb7-03e1-4fa0-8693-b61cca1f7922)
    
- On single tokens. cannot output the incremented single token, unlike the successor head

Arithmetic

- prompts llama2 succeeds on
    - "5 + 16 = “
    - Be concise. 100 + 58 =
    - 5 x 6 =
    - 2 x 2 =

llama2_testPrompts.ipynb

Word problems

- prompts llama2 succeeds on
    
    ✌️  :prompts that can be ablated by seq cont component sets **AND** random doesn’t work
    
    - ✌️ What are the months in a year?
        - What are the months in a year? Give all of them as a list.
        - What are the months in a year? Give all of them as a list. Be concise.
        - ~~The months in a year are:~~
        - The months in a year are: January,
            - this is very similar to seq cont anyways
    - What are the days of the week?
    - ✌️ "What comes after the second item in a list? The next item in a list is the”
        - "What comes after the first step in a process? Be concise.”
        - "What comes after the second item in a list? Be concise.”
    - ✌️ "If today is the 14th of a month, what date will it be in 10 days?”
        - ✌️Be concise. If today is the 11th of a month, what date will it be in 6 days?
    - ~~Be concise. In a cyclic pattern of colors: Red, Blue, Green, Yellow, what color comes after Green in the 3rd cycle?~~
    - ✌️ What number comes after 3?
    - ✌️ What number comes after 3002? Answer:
    - ✌️ Be concise. If this month is September, and 3 months pass, what is month name is it? Answer: December. If this month is March, and 3 months pass, what month name is it? Answer:
        - ✌️ "Be concise. If this month is July, and 5 months pass, what is month name is it? Answer: December. If this month is March, and 5 months pass, what month name is it? Answer: “
        - ✌️ Be concise. If this month is July, and 5 months pass, what is month name is it? Answer: December. If this month is April, and 5 months pass, what month name is it? Answer:
        - ✌️ Be concise. If this month is July, and 4 months pass, what month name is it? Answer: October. If this month is April, and 4 months pass, what month name is it? Answer:
    - What is the month that is 3 months after January? Answer: March. What is the month that is 3 months after March? Answer:
    - What are all the months in Fall? List them in order.
    - ✌️ Answer yes or [no. Is](http://no.is/) 16 greater than 11? Answer:
    - ✌️ Be concise. What number is greater than 11? Answer:
- prompts llama2 fails on
    - The months in a year are:
    - Two days after Monday is
    - "What comes after the second item in a list?”
        - hallucinates ‘apple banana..’
    - "Given the sequence 2, 4, 6, 8, ..., identify the 10th term. Be concise.”
    - Be concise. In the arithmetic sequence starting at 5 and increasing by 3 each time, what is the 7th term?”
    - Be concise. Starting on the 1st of January, what date falls 50 days later?
    - Be concise. If this month is March, and 3 months pass, what month name is it? Answer:
    - Be concise. If this month is September, and 3 months pass, what is month name is it? Answer: December. If this month is February, and 5 months pass, what month name is it? Answer:
    - Be concise. If this month is July, and 5 months pass, what is month name is it? Answer: December. If this month is February, and 5 months pass, what month name is it? Answer:
    - What are all the months in Winter? List them in order.”
    - Be concise. In a cyclic pattern of colors: Red, Blue, Green, Yellow, what color comes after the 3rd color? (it says green)
    - Qué viene después de uno?
        - answers this in numerals correctly
    - Sé conciso. Qué viene después de uno?
        - answers this in numerals correctly

- Spanish prompts llama-2 succeeds on
    - ✌️ uno dos tres
    - ✌️ What are the months in a year in Spanish?
        - What are the months in a year in Spanish? Answer: Enero,
    - ✌️ Be concise. List the months in Spanish. Answer:
    - Be concise. What is uno plus cuatro? Answer:
        - Gets it correct, but in numerals (5)
        - must use ‘be concise’ and ‘Answer: ‘ ,else it rambles on unrelated topics liek the card game
        - This doesn’t work either
            
            Be concise. Answer in Spanish. What is uno plus uno? Answer: dos. What is uno plus cuatro? Answer:
            
    - Be concise. What is cinco minus dos? Answer:
        - arithm is too sensitive; random often works!
- fails on
    - uno dos tres cuatro cinco seis siete ocho nueve diez
    - uno dos tres cuatro cinco seis
    - cuatro cinco seis
    - dos cuatro seis
    - uno mas cuatro

- french success
    - un, deux, trois, quatre
- french fail
    - un, deux, trois, quatre

The aim is to test that it not only fails the next token, but fails if it continues. Also to show that our discovery vs testing prompts don’t need to be in the same format. Thirdly, to show that if we don’t “feed it” enough hints to push it to give the next one, it will (as it loftily wanders) still give it if clean, but not if it’s corrupted

---

---

Future papers

- future work tasks (no need to be exhaustive, just enough to prove the point that methods works)
    - Fibonacci variants
    - Pattern: a b c ; (such that a= b+c)
    - Seq lengths
    - negatives, fractions
- steering tasks
    - Create interval-2 in other languages
    - Mathematical reasoning in other langauges
    - Create circular fiboanacci

 OPT: [try these, but report neg results in appendix if doesnt work]:

1. Steer prompts across domains
    1. First try across foreign languages on +1
        1. See 3 previous papers on foreign languages in llama-2 (Wendler, Kojima, Quirke)
        2. Activation Addition
    2. Steer across foreign languages on other prompts (intervaled seqs, reasoning, etc)
    3. Steer from 1-interval to 2-interval, etc. within a language

Requires more compute:

- SAEs on Lllama to get steering features
- feature circuits
- New methods?
    
    (No time for new method; save this for next paper)
    
    New method: match circuits with different components based on same functionality (use matching algorithm on graph based on func scores, or Dar et all embedding mappings)
    
    start simple; later papers can build on this to make it more effective with more sophisticated approaches
    
    The MLPs show there is something “similar” between the two, yet different attention heads activate. What is the similarity? Check features of MLPs. Use SVD first if cant use SAEs.
    
    Try simple activation addition
    
    New method 2: use SAEs and/or (language neuron/vector) findings to translate using natural number as common abstraction. 
    

Limitations: We have not yet… training SAEs on Llama-2 would require more compute