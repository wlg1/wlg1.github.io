# _Brainstorm plans (chrono)

[23 10 21- Plan](_Brainstorm%20plans%20(chrono)%20a93e919e5bff4109bf54f6d3febb05c4/23%2010%2021-%20Plan%2004b6844e61624b28a654df94ee7e7a40.md)

- 23 10 27
    
    Currently working on making the overall diagram to showcase the main idea. I’m deciding which of the 3-4 tasks to showcase. I’m thinking about two very similar (increasing digits, number words), two somewhat similar (increasing digits, decreasing digits) and finally “greater-than”. Now the obstacle is finding “more accurate and interpretable circuits”. But I think in the next few hrs I will just make this overall diagram using “less accurate” circuits as a starting point.
    
    To obtain “more interpretable”, I think one way may be with different tasks + datasets. One issue is that the “pure digits” (1 2 3) circuit seems bigger and harder to interpret than “digits among words” (table 1 lamp house 2 food 3). I may focus more on “digits among words” because I think we can identify how it “detects sequences” then moves them. Perhaps pure digits somehow “spreads out” the signals to more heads, while digits among words concentrates the signals to certain heads specialized to detecting sequence members such as numbers. 
    
    actually from what i've run so far, i think i'll put all the increasing seqs in 1 circuit diagram first. then another one has incr + decr (they're too dissimilar)
    
    - Forgo using ‘embed’ and ‘logits’ start/end nodes for now
    
- 10 28
    - must get acc circ to ensure component func interpret uses actual components that differ between tasks of circs. and ensure truly comparing to greater-than.
    - better dataset than “switch last and 2nd last” or “repeat last”: (bc ISSUE- if repeat last only, then info about all other numbers still there. criticism would mention this).