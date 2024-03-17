# llama2.c
test on llama2 with tinystories

## Install the requirements

```sh
pip install -r requirements.txt
```

## For conda based Setup
```sh
conda create -n pt python==3.10 -y
conda activate pt
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia -y
conda install -c conda-forge tqdm sentencepiece -y
```


## Download, train the tokenizer and tokenize the dataset

```sh
python tinystories.py download
python tinystories.py train_vocab --vocab_size=1024
python tinystories.py pretokenize --vocab_size=1024
```

## Training with the vector based token representation

```sh
./train_vector.sh
```

## Training with the matrix based token representation

```sh
./train_matrix.sh
```