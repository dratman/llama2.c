#!/bin/bash

python test.py \
    --checkpoint=outmini_matrix/ckpt.pt \
    --tokenizer=data/tok1024.model \
    --temperature=0.7 \
    --max_new_tokens=64 

