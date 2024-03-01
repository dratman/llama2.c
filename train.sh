#!/bin/bash


# conda create -n pt python==3.10 -y
# conda activate pt
# conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia -y
# conda install -c conda-forge tqdm sentencepiece -y

# python tinystories.py download
# python tinystories.py train_vocab --vocab_size=4096
# python tinystories.py pretokenize --vocab_size=4096

python train.py \
    --out_dir="outmini" \
    --batch_size=128 \
    --max_seq_len=256 \
    --gradient_accumulation_steps=1 \
    --vocab_source="custom" \
    --vocab_size=4096 \
    --dim=256 \
    --n_layers=6 \
    --n_heads=6 \
    --n_kv_heads=6 \
    --multiple_of=4 \
    --learning_rate=1e-3 \
    --dropout=0.05 \
    --weight_decay=0.01 \
    --max_iters=100000 \
    --beta2=0.99 \
    --warmup_iters=1000 \
    --eval_interval=5000 \
    --eval_iters=100 \
    --log_interval=500 \
    --compile=True

