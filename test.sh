#!/bin/bash

python test.py \
    --checkpoint=outmini/ckpt.pt \
    --tokenizer=data/tok4096.model \
    --temperature=0.7 \
    --max_new_tokens=257

