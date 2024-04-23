#!/bin/bash
echo
date
echo "train_vocab...  -----------"
date
python tinystories.py train_vocab --vocab_size=4096 2>train_vocab.log
echo
date
echo "pretokenize...  -----------"
echo
date
python tinystories.py pretokenize --vocab_size=4096 2>pretokenize.log

# ./train-short.sh