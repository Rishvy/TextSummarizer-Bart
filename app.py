from flask import Flask, request, render_template
from transformers import BartForConditionalGeneration, BartTokenizer
import torch

app = Flask(__name__)

# Load BART model and tokenizer once at startup
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')

@app.route('/', methods=['GET', 'POST'])
def summarize():
    summary = ""
    if request.method == 'POST':
        text = request.form['input_text']
        if text.strip():
            # Tokenize and generate summary
            inputs = tokenizer.encode(text, return_tensors='pt', max_length=1024, truncation=True)
            summary_ids = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
            summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)