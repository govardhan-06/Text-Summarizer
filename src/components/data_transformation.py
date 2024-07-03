import os
from src.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
from entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config=config
        self.tokenizer=AutoTokenizer.from_pretrained(config.tokenizer_name)

    def preprocess_Data(self,batch):
        input_encoding=self.tokenizer(batch["dialogue"],max_length = 1024, truncation = True )
        with self.tokenizer.as_target_tokenizer():
            target_encoding=self.tokenizer(batch["summary"],max_length = 1024, truncation = True )

        return {
            "input_ids":input_encoding["input_ids"],
            "attention_mask":input_encoding["attention_mask"],
            "labels":target_encoding["input_ids"]
        }
    
    def convert(self):
        dataset_samsum=load_from_disk(self.config.data_path)
        dataset_samsum_pt=dataset_samsum.map(self.preprocess_Data,batched=True)
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir,"samsum_dataset"))