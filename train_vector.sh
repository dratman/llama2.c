#!/bin/bash

python train.py \
    --out_dir="outmini_vector" \
    --batch_size=64 \
    --max_seq_len=64 \
    --gradient_accumulation_steps=1 \
    --vocab_source="custom" \
    --vocab_size=1024 \
    --matrix=False \
    --dim=512 \
    --n_layers=2 \
    --n_heads=2 \
    --n_kv_heads=2 \
    --multiple_of=4 \
    --learning_rate=1e-3 \
    --dropout=0.05 \
    --weight_decay=0.01 \
    --max_iters=100000 \
    --beta2=0.99 \
    --warmup_iters=1000 \
    --eval_interval=2000 \
    --eval_iters=100 \
    --log_interval=250 \
    --compile=True 
