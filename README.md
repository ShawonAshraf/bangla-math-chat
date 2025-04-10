# bangla-math-chat

A math dataset for fine-tuning LLMs to chat on math problems in Bangla. This dataset is a reformatted version of 
[BanglaLLM/bangla_math_by_Ashrafur](https://huggingface.co/datasets/BanglaLLM/bangla_math_by_Ashrafur). 


# HF Hub

The dataset can be used via the `datasets` library using the identifier `shawon/bangla-math-chat`.

## Usage via the datasets library

Install the datasets library

```bash
pip install datasets
```

Then load the dataset

```
from datasets import load_dataset

# loads the train split
# if you want to load the entire datsaet, don't use the `split` param
dataset = load_dataset("shawon/bangla-math-chat", split="train")

print(dataset[10])
```
