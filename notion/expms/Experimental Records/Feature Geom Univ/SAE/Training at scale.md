# Training at scale

[https://www.youtube.com/watch?v=sQar5NNGbw4&t=1320s&ab_channel=Anthropic](https://www.youtube.com/watch?v=sQar5NNGbw4&t=1320s&ab_channel=Anthropic)

[https://x.com/OpenAI/status/1798762092528586945](https://x.com/OpenAI/status/1798762092528586945)

[https://www.lesswrong.com/posts/fifPCos6ddsmJYahD/my-best-guess-at-the-important-tricks-for-training-1l-saes](https://www.lesswrong.com/posts/fifPCos6ddsmJYahD/my-best-guess-at-the-important-tricks-for-training-1l-saes)

standard data parallel and tensor sharding

https://youtube.com/playlist?list=PL_lsbAsL_o2CSuhUhJIiW0IkdT5C2wGWj&si=Z1_4jpNugFeZ9Rvh

https://chatgpt.com/share/ef4d8d8d-91a3-4a25-9d53-3f9982baa7b6

2) Do you use tmux to create virtual sessions that persist between logins3) 

,(1) Currently the model I used is small enough to be put in a single GPU so I just use naive data parallel to do multi-gpu training. Specifically, I use the huggingface trainer,  a nice encapsulation of parallel training.(2) I use screen but I think it is very similar to tmux and tmux probably works too.(3) 

https://huggingface.co/docs/transformers/main/en/perf_train_gpu_many