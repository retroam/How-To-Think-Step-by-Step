# %%
copy_index = [{'noise_index': 0,  'accuracy_index': 7,  'accuracy': 0.85,  'head_removed': 186},
 {'noise_index': 1, 'accuracy_index': 2, 'accuracy': 0.77, 'head_removed': 61},
 {'noise_index': 2, 'accuracy_index': 2, 'accuracy': 0.98, 'head_removed': 61},
 {'noise_index': 3,  'accuracy_index': 19,  'accuracy': 0.89,  'head_removed': 486},
 {'noise_index': 4,  'accuracy_index': 14,  'accuracy': 0.95,  'head_removed': 361},
 {'noise_index': 5, 'accuracy_index': 2, 'accuracy': 0.99, 'head_removed': 61},
 {'noise_index': 6, 'accuracy_index': 2, 'accuracy': 0.98, 'head_removed': 61},
 {'noise_index': 7, 'accuracy_index': 1, 'accuracy': 0.99, 'head_removed': 36},
 {'noise_index': 8, 'accuracy_index': 3, 'accuracy': 0.89, 'head_removed': 86},
 {'noise_index': 9,  'accuracy_index': 19,  'accuracy': 0.9,  'head_removed': 486}]




decision_index = [{'noise_index': 0,  'accuracy_index': 19,  'accuracy': 0.89,  'head_removed': 486},
 {'noise_index': 1, 'accuracy_index': 2, 'accuracy': 0.93, 'head_removed': 61},
 {'noise_index': 2, 'accuracy_index': 1, 'accuracy': 0.95, 'head_removed': 36},
 {'noise_index': 3,  'accuracy_index': 4,  'accuracy': 0.89,  'head_removed': 111},
 {'noise_index': 4,  'accuracy_index': 13,  'accuracy': 0.92,  'head_removed': 336},
 {'noise_index': 5, 'accuracy_index': 2, 'accuracy': 0.84, 'head_removed': 61},
 {'noise_index': 6, 'accuracy_index': 3, 'accuracy': 0.89, 'head_removed': 86},
 {'noise_index': 7, 'accuracy_index': 3, 'accuracy': 0.95, 'head_removed': 86},
 {'noise_index': 8,  'accuracy_index': 6,  'accuracy': 0.86,  'head_removed': 161},
 {'noise_index': 9,  'accuracy_index': 6,  'accuracy': 0.88,  'head_removed': 161}]



# reason_index = [{'noise_index': 0,  'accuracy_index': 5,  'accuracy': 0.86,  'head_removed': 645},
#  {'noise_index': 1,  'accuracy_index': 2,  'accuracy': 0.95,  'head_removed': 448},
#  {'noise_index': 2,  'accuracy_index': 4,  'accuracy': 0.95,  'head_removed': 585},
#  {'noise_index': 3,  'accuracy_index': 6,  'accuracy': 0.85,  'head_removed': 685},
#  {'noise_index': 4,  'accuracy_index': 2,  'accuracy': 0.89,  'head_removed': 448},
#  {'noise_index': 5, 'accuracy_index': 1, 'accuracy': 0.9, 'head_removed': 270},
#  {'noise_index': 6,  'accuracy_index': 2,  'accuracy': 0.88,  'head_removed': 448},
#  {'noise_index': 7,  'accuracy_index': 6,  'accuracy': 0.84,  'head_removed': 685},
#  {'noise_index': 8, 'accuracy_index': 4, 'accuracy': 0.9, 'head_removed': 585},
#  {'noise_index': 9,  'accuracy_index': 3,  'accuracy': 0.89,  'head_removed': 538}]

reason_index = [{'noise_index': 0, 'accuracy_index': 2, 'accuracy': 1.0, 'head_removed': 475},
 {'noise_index': 1,  'accuracy_index': 3,  'accuracy': 0.93,  'head_removed': 554},
 {'noise_index': 2,  'accuracy_index': 4,  'accuracy': 0.96,  'head_removed': 617},
 {'noise_index': 3,  'accuracy_index': 4,  'accuracy': 0.97,  'head_removed': 617},
 {'noise_index': 4,  'accuracy_index': 3,  'accuracy': 0.99,  'head_removed': 554},
 {'noise_index': 5,  'accuracy_index': 2,  'accuracy': 0.93,  'head_removed': 475},
 {'noise_index': 6,  'accuracy_index': 2,  'accuracy': 0.94,  'head_removed': 475},
 {'noise_index': 7,  'accuracy_index': 4,  'accuracy': 0.88,  'head_removed': 617},
 {'noise_index': 8,  'accuracy_index': 4,  'accuracy': 0.95,  'head_removed': 617},
 {'noise_index': 9,  'accuracy_index': 5,  'accuracy': 0.91,  'head_removed': 663}]



# %%
def getPath(case, index):
    if(case == 'activationPatching'):
        pathAccuracy = f'../results/activationPatching/{index}/accuracy/circuit_results_histogram.pickle'
        pathMatrix = f'../results/activationPatching/{index}/kl_div_COT.pickle'
    if(case == 'decision'):
        pathAccuracy = f'../results/decision/part_2/combined/{index}/accuracy/circuit_results.pickle'
        pathMatrix = f'../results/decision/part_2/combined/combined_matrix.pkl'
    # if(case == 'copy_proj'):
    #     pathAccuracy = f'../results/copy/combined/{index}/accuracy_proj/circuit_results.pickle'
    #     pathMatrix = f'../results/copy/combined/combined_matrix_projection.pkl'
    if(case == 'copy'):
        pathAccuracy = f'../results/copy/combined/{index}/accuracy_prob/circuit_results.pickle'
        pathMatrix = f'../results/copy/combined/combined_matrix_attn_prob.pkl'
    if(case == 'reason'):
        pathAccuracy = f'../results/reasoning/combined/{index}/accuracy/circuit_results_histogram.pickle'
        pathMatrix = f'../results/reasoning/combined/normalised_combined_matrix.pkl'
    return pathAccuracy, pathMatrix




# %%
import pickle
def getAccuracyMatrix(accuracyPath, matrixPath):
    with open(accuracyPath, 'rb') as f:
        accuracy = pickle.load(f)
    with open(matrixPath, 'rb') as f:
        matrix = pickle.load(f)
    return accuracy, matrix

# %%
def getImportantHeads(threadShold, matrix):
    importantHeads = []
    for layer in range(len(matrix)):
        for head in range(len(matrix[layer])):
            if(matrix[layer][head] > threadShold[1] or matrix[layer][head] < threadShold[0]):
                importantHeads.append((layer, head))
    return set(sorted(importantHeads))

# %%
import argparse
parser = argparse.ArgumentParser()
# python3 IndividualHeadAccuracy.py --noiseIndex 0 --device "cuda:1" --numExamples 10 --alteranteExamples 10
parser.add_argument("-firstHead", "--firstHead")
parser.add_argument("-device", "--device", help = "device")
parser.add_argument("-secondHead", "--secondHead")
parser.add_argument("-mainHead", "--mainHead")
parser.add_argument("-noiseIndex", "--noiseIndex")
# parser.add_argument("-type", "--type")
args = parser.parse_args()

noise_index = int(args.noiseIndex)
first = args.firstHead
second = args.secondHead
main = args.mainHead
firstAccuracy, firstMatrix = getAccuracyMatrix(*getPath(first, noise_index))
secondAccuracy, secondMatrix = getAccuracyMatrix(*getPath(second, noise_index))
mainAccuracy, mainMatrix = getAccuracyMatrix(*getPath(main, noise_index))

if(first == 'reason'):
    first_index = reason_index
if(first == 'copy'):
    first_index = copy_index
if(first == 'decision'):
    first_index = decision_index

if(second == 'reason'):
    second_index = reason_index
if(second == 'copy'):
    second_index = copy_index
if(second == 'decision'):
    second_index = decision_index

if(main == 'reason'):
    main_index = reason_index
if(main == 'copy'):
    main_index = copy_index
if(main == 'decision'):
    main_index = decision_index
print(firstAccuracy[first_index[noise_index]['accuracy_index']])

if('range' not in firstAccuracy[first_index[noise_index]['accuracy_index']]):
    firstNumberOfHeads = firstAccuracy[first_index[noise_index]['accuracy_index']]['circuit']
    sorted_data = []
    for layer in range(len(firstMatrix)):
        for head in range(len(firstMatrix[layer])):
            sorted_data.append({'layer' : layer, 'head' : head, 'value' : firstMatrix[layer][head]})

    sorted_data = sorted(sorted_data, key=lambda x: x['value'])
    importantHeadData = sorted_data[1024 - firstNumberOfHeads:]
    firstImportantHeads = []
    for d in importantHeadData:
        firstImportantHeads.append((d['layer'], d['head']))
    firstImportantHeads = set(sorted(firstImportantHeads))

else:
    firstThresholdRange = firstAccuracy[first_index[noise_index]['accuracy_index']]['range']
    firstImportantHeads = getImportantHeads(firstThresholdRange, firstMatrix)


if('range' not in secondAccuracy[second_index[noise_index]['accuracy_index']]):
    secondNumberOfHeads = secondAccuracy[second_index[noise_index]['accuracy_index']]['circuit']
    sorted_data = []
    for layer in range(len(secondMatrix)):
        for head in range(len(secondMatrix[layer])):
            sorted_data.append({'layer' : layer, 'head' : head, 'value' : secondMatrix[layer][head]})
    sorted_data = sorted(sorted_data, key=lambda x: x['value'])
    # breakpoint()
    importantHeadData = sorted_data[1024 - secondNumberOfHeads:]
    secondImportantHeads = []
    for d in importantHeadData:
        secondImportantHeads.append((d['layer'], d['head']))
    secondImportantHeads = set(sorted(secondImportantHeads))

else:
    secondThresholdRange = secondAccuracy[second_index[noise_index]['accuracy_index']]['range']
    secondImportantHeads = getImportantHeads(secondThresholdRange, secondMatrix)     

if('range' not in mainAccuracy[main_index[noise_index]['accuracy_index']]):
    mainNumberOfHeads = mainAccuracy[main_index[noise_index]['accuracy_index']]['circuit']
    sorted_data = []
    for layer in range(len(mainMatrix)):
        for head in range(len(mainMatrix[layer])):
            sorted_data.append({'layer' : layer, 'head' : head, 'value' : mainMatrix[layer][head]})
    sorted_data = sorted(sorted_data, key=lambda x: x['value'])

    importantHeadData = sorted_data[1024 - mainNumberOfHeads : ]
    mainImportantHeads = []
    for d in importantHeadData:
        mainImportantHeads.append((d['layer'], d['head']))
    mainImportantHeads = set(sorted(mainImportantHeads))

else:
    mainThresholdRange = mainAccuracy[main_index[noise_index]['accuracy_index']]['range']
    mainImportantHeads = getImportantHeads(mainThresholdRange, mainMatrix)
len(firstImportantHeads), len(secondImportantHeads)

# %%
# type = args.type



# %%
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
import einops
from fancy_einsum import einsum
import tqdm.auto as tqdm
import random
from pathlib import Path
import plotly.express as px
from torch.utils.data import DataLoader

from jaxtyping import Float, Int
from typing import List, Union, Optional
from functools import partial
import copy

import itertools
from transformers import AutoModelForCausalLM, AutoConfig, AutoTokenizer
import dataclasses
import datasets
from IPython.display import HTML

# %%
import transformer_lens
import transformer_lens.utils as utils
from transformer_lens.hook_points import (
    HookedRootModule,
    HookPoint,
)  # Hooking utilities
from transformer_lens import HookedTransformer, HookedTransformerConfig, FactoredMatrix, ActivationCache

torch.set_grad_enabled(False)

import json
with open('data/activationPatching_llama2_false.json', 'r') as f:
    alternate_COTData = json.load(f)

import json
with open('data/activationPatching_llama2_clean.json', 'r') as f:
    COTData = json.load(f)

# %%
import sys
sys.path.append('../')
from utilsFile.fewShotConstants import TemplateCOT_fictional, TemplateCOT_false


# %%
device = args.device if torch.cuda.is_available() else "cpu"

# %%
from transformers import LlamaForCausalLM, LlamaTokenizer
import os
from utilsFile.loadModel import loadTransformerLensModel, runCacheActivationPatching
MODEL_PATH = '/home/models/Llama-2-7b-hf'
# modelPath='/home/models/vicuna-7b'
model, tokenizer = loadTransformerLensModel(MODEL_PATH)
model = model.to(device)

# %%
number_of_examples = 100
alternate_examples = 50

# %%
print(f"Noise index: {noise_index}")
print(f"Number of examples: {number_of_examples}")
prompts = [TemplateCOT_fictional.format(data['prompt']) + data[f'response_{noise_index}'] for data in COTData][:number_of_examples]
labels = [(data[f'response_{noise_index + 1}'].replace(data[f'response_{noise_index}'], "").strip()) for data in COTData][:number_of_examples]
alternate_prompts = [TemplateCOT_false.format(data['prompt']) + data[f'response_{noise_index}'] for data in alternate_COTData][:alternate_examples]
alternate_labels = [data['label'] for data in alternate_COTData][:alternate_examples]

input_ids = []
max_length = 0
for prompt in prompts:
    finalPrompt = prompt
    encoded_prompt = tokenizer.encode(finalPrompt, add_special_tokens=False, return_tensors="pt")
    max_length = max(max_length, encoded_prompt.size()[1])
    input_ids.append(encoded_prompt[0])

alternate_max_length = 0
alternate_input_ids = []
for prompt in alternate_prompts:
    finalPrompt = prompt
    encoded_prompt = tokenizer.encode(finalPrompt, add_special_tokens=False, return_tensors="pt")
    alternate_max_length = max(alternate_max_length, encoded_prompt.size()[1])
    alternate_input_ids.append(encoded_prompt[0])

max_seq_len = max(max_length, alternate_max_length)
print(f"max seq len {max_seq_len}")
pad_id = tokenizer.bos_token_id

for i in range(len(input_ids)):
    input_ids[i] = [pad_id] * (max_seq_len - len(input_ids[i])) + input_ids[i].detach().numpy().tolist()
input_ids = torch.tensor(input_ids)

for i in range(len(alternate_input_ids)):
    alternate_input_ids[i] = [pad_id] * (max_seq_len - len(alternate_input_ids[i])) + alternate_input_ids[i].detach().numpy().tolist()
alternate_input_ids = torch.tensor(alternate_input_ids)



# %%
def logit_accuracy(logits, patched_logits):
    next_token_logits = logits[:, -1, :]
    next_token_ids = torch.argmax(next_token_logits, dim=-1)
    next_token_ids = [[tokens.item()] for tokens in next_token_ids]
    accuracy = 0
    next_tokens = model.tokenizer.batch_decode(next_token_ids)

    next_token_patched_logits = patched_logits[:, -1, :]
    next_token_patched_ids = torch.argmax(next_token_patched_logits, dim=-1)
    next_token_patched_ids = [[tokens.item()] for tokens in next_token_patched_ids]
    next_patched_tokens = model.tokenizer.batch_decode(next_token_patched_ids)
    # print(next_tokens)
    # print(next_tokens)
    # print(next_patched_tokens)
    for i in range(len(next_tokens)):
        next_token = next_tokens[i].strip()
        next_patched_token = next_patched_tokens[i].strip()
        
        if(next_token == next_patched_token):
            accuracy += 1
    return accuracy / len(next_tokens)

# %%
print("RUNNING ORIGINAL LOGITS")
original_logits, cache = runCacheActivationPatching(model, input_ids)


print("RUNNING NOISE LOGITS")
alternate_logits, alternate_cache = runCacheActivationPatching(model, alternate_input_ids)

# %%
def patch_head_vector_avg(
        clean_head_vector: Float[torch.Tensor, "batch pos head_index d_head"],
        hook,
        head_index,
        alternate_cache):
    mean_alternate_cache = torch.mean(alternate_cache[hook.name][:, :, head_index, :], dim=0)
    zero_tensor_cache = torch.zeros_like(mean_alternate_cache)
    clean_head_vector[:, :, head_index, :] = mean_alternate_cache
    return clean_head_vector

# %%
types = ['common', 'only_main', 'only_other', 'other', 'common_only_main']
from tqdm import tqdm
for category in tqdm(types):
    if(category == 'main'):
        importantHeads = mainImportantHeads
    if(category == 'common'):
        importantHeads = mainImportantHeads.intersection(firstImportantHeads,secondImportantHeads)
    if(category == 'only_main'):
        importantHeads = mainImportantHeads.difference(firstImportantHeads).difference(secondImportantHeads)
    if(category == 'only_other'):
        importantHeads = firstImportantHeads.union(secondImportantHeads).difference(mainImportantHeads)
    if(category == 'other'):
        importantHeads = firstImportantHeads.union(secondImportantHeads)
    if(category == 'common_only_main'):
        importantHeads = mainImportantHeads.intersection(firstImportantHeads,secondImportantHeads).union(mainImportantHeads.difference(firstImportantHeads, secondImportantHeads))

    count = 0
    list_fwd_hooks = []
    for layer in range(32):
        for head in range(32):
            if((layer, head) in importantHeads):
                continue
            else:
                list_fwd_hooks.append((utils.get_act_name("z", layer, "attn"), partial(patch_head_vector_avg, head_index=head, alternate_cache=alternate_cache)))
    #                 # print(layer,head)
    #                 # print(patched_head[layer][head])
                count += 1
    print("Number of heads removed or patched: ", count)

    patched_logits = model.run_with_hooks(
                input_ids, 
                fwd_hooks = list_fwd_hooks, 
                return_type="logits"
            )

    patched_acc = logit_accuracy(original_logits, patched_logits)

    print(f"Accuracy of next token after patching {count} heads: {patched_acc}")
    print("Noise index: ", noise_index)
    print("Number of importantHeads: ", len(importantHeads))
    print("first head type: ", first)
    print("second head type: ", second)
    print("main head type: ", main)
    print("type: ", category)
# %%

# %%



