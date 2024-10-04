import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# load GPT-2 model and tokenizer
def model_fn(model_dir):
    model = GPT2LMHeadModel.from_pretrained(model_dir)
    tokenizer = GPT2Tokenizer.from_pretrained(model_dir)
    return model, tokenizer

# process input and return prediction
def predict_fn(input_data, model_and_tokenizer):
    model, tokenizer = model_and_tokenizer
    inputs = tokenizer(input_data['message'], return_tensors='pt')
    outputs = model.generate(inputs.input_ids, max_length=50)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {'response': response}
