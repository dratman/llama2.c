#!/bin/bash
python tinystories.py train_vocab --vocab_size=512
python tinystories.py pretokenize --vocab_size=512
echo "--- Begin training a 260K model ---"
python train.py \
    --out_dir="outmini" \
    --batch_size=128 \
    --max_seq_len=1024 \
    --gradient_accumulation_steps=1 \
    --vocab_source="custom" \
    --vocab_size=512 \
    --dim=64 \
    --n_layers=20 \
    --n_heads=8 \
    --n_kv_heads=4 \
    --multiple_of=4 \
    --learning_rate=1e-3 \
    --dropout=0.05 \
    --weight_decay=0.01 \
    --max_iters=500000 \
    --beta2=0.99 \
    --warmup_iters=1000 \
    --eval_interval=2000 \
    --eval_iters=100 \
    --compile=True
echo "--- training completed ---"
python tokenizer.py --tokenizer-model=data/tok1024.model
echo "--- Begin inferencing the model just created ---"
./run outmini/model.bin -z data/tok1024.bin