#!/bin/bash

python train.py \
    --out_dir="outmini" \
    --batch_size=3 \
    --max_seq_len=32 \
    --gradient_accumulation_steps=1 \
    --vocab_source="custom" \
    --vocab_size=1024 \
    --matrix=True \
    --dim=16 \
    --n_layers=2 \
    --n_heads=2 \
    --n_kv_heads=1 \
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
