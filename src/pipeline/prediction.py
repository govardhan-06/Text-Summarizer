from transformers import AutoModelForSeq2SeqLM,AutoTokenizer
from transformers import pipeline
from datasets import load_from_disk
from src.config.configuration import ConfigurationManager

class PredictionPipeline:
    def __init_(self):
        self.config=ConfigurationManager().get_model_evaluation_config()

    def predict(self,text):
        #loading data
        dataset_samsum_pt=load_from_disk(self.config.data_path)

        ##Load tokenzier
        tokenizer=AutoTokenizer.from_pretrained("pegasus-samsum-tokenizer")
        model=AutoModelForSeq2SeqLM.from_pretrained("pegasus-samsum-model")

        #Prediction
        gen_kwargs={"length_penalty":0.8,"num_beams":8,"max_length":128}

        pipe=pipeline("summarization",model=self.config.model_path,tokenizer=tokenizer)
        print("Dialogue:")
        print(text)

        output=pipe(text,**gen_kwargs)[0]['summary_text']
        print("\nModel Summary:")
        print(output)

        return output