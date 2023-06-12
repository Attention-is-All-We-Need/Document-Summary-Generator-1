import os
from data_transformation import gen_para_pdf, gen_para_doc, gen_para_txt, gen_para_file
import torch
from transformers import pipeline
import sys
folder_path = os.getcwd()
sys.path.append(folder_path)

# file_path = os.path.join(folder_path, 'src')

# hf_name = 'pszemraj/led-base-book-summary'

# summarizer = pipeline(
#     "summarization",
#     hf_name,
#     device=0 if torch.cuda.is_available() else -1,
# )

    
file_name = '3_Hydrogen-Compressed-Natural-Gas_1.pdf"'
# file_path = os.path.join(file_path, file_name)
extracted_text = gen_para_file(file_name)
print(extracted_text)
    
# result = summarizer(
#            extracted_text,
#            min_length=8, 
#            max_length=256,
#            no_repeat_ngram_size=3, 
#            encoder_no_repeat_ngram_size=3,
#            repetition_penalty=3.5,
#            num_beams=4,
#            do_sample=False,
#            early_stopping=True,
#     )


    
