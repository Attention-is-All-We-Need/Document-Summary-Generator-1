import os
from data_transformation import gen_para_pdf, gen_para_doc, gen_para_txt
import torch
from transformers import pipeline

hf_name = 'pszemraj/led-base-book-summary'

summarizer = pipeline(
    "summarization",
    hf_name,
    device=0 if torch.cuda.is_available() else -1,
)

def extract_text(file_path):
    if file_path.endswith('.pdf'):
        text = gen_para_pdf(file_path)
        return text
    elif file_path.endswith('.doc') or file_path.endswith('.docx'):
        text = gen_para_doc(file_path)
        return text
    elif file_path.endswith('.txt'):
        text = gen_para_txt(file_path)
        return text
    else:
        raise ValueError("Unsupported file type.")
    
directory = r'C:\Users\Anwesh\Desktop\SnT Hackathon\Document-Summary-Generator-1\UPLOAD_FOLDER'
file_name = '3_Hydrogen-Compressed-Natural-Gas_1.pdf"'
file_path = os.path.join(directory, file_name)
extracted_text = extract_text(file_path)
    
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


    
