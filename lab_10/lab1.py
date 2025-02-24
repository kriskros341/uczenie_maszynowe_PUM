
from datasets import load_dataset
from transformers import AutoModelForSeq2SeqLM
from transformers import AutoTokenizer


def see_dataset(dataset):
    example_indices=[40,200]
    for i,index in enumerate(example_indices):
        print (dataset['test'][index])
        print ('***')
        print (dataset['test'][index]['dialogue'])
        print ('***')
        print (dataset['test'][index]['summary'])
        print ('---')

def see_decode_encode(tokenizer):
    sentence = 'A mouse is in the house.'
    sentence_encoded= tokenizer(sentence,return_tensors='pt')
    sentence_decoded = tokenizer.decode(sentence_encoded['input_ids'][0],skip_special_tokens=True)
    print (sentence_encoded)
    print (sentence_decoded)
    
if __name__ == '__main__':
    hf_dataset_name='knkarthick/dialogsum'
    dataset = load_dataset(hf_dataset_name)
    if False:
        see_dataset(dataset)
    model_name = 'google/flan-t5-base'
    tokenizer = AutoTokenizer.from_pretrained(model_name,use_fast=True)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)    
    if False:
        see_decode_encode(tokenizer)
    
    train_index = 400
    test_indices = [200]
    
    prompt = """

        I am dismayed by dogs

        sentiment: 
    """
    print(prompt)
    inputs = tokenizer(prompt, return_tensors='pt')
    gen_res = model.generate(inputs['input_ids'],max_new_tokens=50)
    output = tokenizer.decode(gen_res[0],skip_special_tokens=True)
    print(output)

    
    
    
