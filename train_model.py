from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments
from datasets import load_dataset

# load GPT-2 model and tokenizer
model = GPT2LMHeadModel.from_pretrained('gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# load the dataset (personchat is placeholder! Replace it with your dataset if necessary!!!!)
dataset = load_dataset("personachat")

# define a function to tokenize the dataset
def tokenize_function(examples):
    return tokenizer(examples['text'], padding="max_length", truncation=True, max_length=128)

# tokenize the dataset
tokenized_datasets = dataset.map(tokenize_function, batched=True)

# select the training dataset
train_dataset = tokenized_datasets["train"]

# set up training arguments
training_args = TrainingArguments(
    output_dir='./results',            # where to store the model
    num_train_epochs=3,                # number of training epochs
    per_device_train_batch_size=4,     # batch size per device during training
    save_steps=10_000,                 # save model every 10,000 steps
    save_total_limit=2,                # limit total saved models to avoid filling up storage
)

# Initialize the Trainer object
trainer = Trainer(
    model=model,                       # GPT-2 model
    args=training_args,                # training arguments
    train_dataset=train_dataset,       # tokenized training dataset
)

# train model
trainer.train()

# save trained model
model.save_pretrained('path_to_save_model')
