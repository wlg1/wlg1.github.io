# Aug 12 meeting

luke

corr between multiple saes learning ground truth features, but some have high sim with each other and low sim with GTF. try aux loss and resample to not learn these features, seems dep on initialization. many aux loss DID corr trakc num of features in this bad cluster. when this loss converge sae perform well but oculdnt get it to conv. just re init weights from scratch is loss exceeds certain val- then loss always conv. sounds like compu cost adds a lot; doesnt bc loss always spikes if feats learned in first 100 train steps, only adds another 2 or 3 perc versus trade off of getting GTF. baseline saes get 90% of GTF; re init of weights goes up to 93% of GTF. extra boost using aux loss that encourages cosine sim (1-MMCS and weight this by constant, add this to sae loss) of 2 saes trained in parallel goes up to 95 to 96% ; sae get close to matching gtf. 

just two saes in aux loss are different than another loss

2 diff losses: when this loss spiked, that consistently made that cluster being learned 

---

tingchen

expm on hhrhf; poison some part of this then do pref learn how performance is lower bc of poisoning. 

---

minseon

very hard to find effective data in repr space bc distr of cosine sim is shifted to -1, so most data is dissimilar to safe data. removal obs expms to clean up data. use FID scores to quantify dataset distribution. attribute different parts of dataset to different parts of distribution; what happens to distribution? no categorical distr within user data. 

rmv some portion of user data and see if risk is changed

---

lovis

probing dataset for sae features: cybersecurity. use circ disc method to get feats with high attrb, aggregate over dataset of prompts

---

trajan: can use gpus? 

vanilla stochastic grad descent can train most of transformer, only need adam for small pts of training, layer norm and some loss has something to do with?