#!/bin/bash

#python tinystories.py train_vocab --vocab_size=512
#python tinystories.py pretokenize --vocab_size=512

python train.py \
    --out_dir="outmini_vector" \
    --batch_size=64 \
    --max_seq_len=256 \
    --gradient_accumulation_steps=1 \
    --vocab_source="custom" \
    --vocab_size=512 \
    --matrix=False \
    --dim=512 \
    --n_layers=5 \
    --n_heads=8 \
    --n_kv_heads=4 \
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

# This is the way Karpathy set up custom training:
# python train.py \
#     --out_dir="outmini" \
#     --batch_size=128 \
#     --max_seq_len=512 \
#     --gradient_accumulation_steps=1 \
#     --vocab_source="custom" \
#     --vocab_size=512 \
#     --dim=32 \
#     --n_layers=5 \
#     --n_heads=8 \
#     --n_kv_heads=4 \
#     --multiple_of=4 \
#     --learning_rate=1e-3 \
#     --dropout=0.05 \
#     --weight_decay=0.01 \
#     --max_iters=100000 \
#     --beta2=0.99 \
#     --warmup_iters=1000 \
#     --eval_interval=2000 \
#     --eval_iters=100 \
#     --compile=True