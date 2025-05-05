# 📚 Text Summarizer using BART

This repository implements a text summarization tool using the `facebook/bart-large-cnn` model from Hugging Face. It takes long-form English text and returns a concise, meaningful summary using state-of-the-art transformer architecture.

---

## 🚀 Features

- ✅ Abstractive summarization with `BART`
- ✅ CLI and Jupyter Notebook interfaces
- ✅ Easy parameter customization
- ✅ Lightweight and extensible
- ✅ Basic experiment tracking

---

## 🧠 Model Information

- **Model**: `facebook/bart-large-cnn`
- **Type**: Encoder-decoder transformer
- **Task**: Abstractive Text Summarization
- **Source**: [HuggingFace Model Card](https://huggingface.co/facebook/bart-large-cnn)

---

## 🛠 Installation

1. Clone the repository:

```bash
git clone https://github.com/Rishvy/TextSummarizer-Bart.git
cd TextSummarizer-Bart
pip install -r requirements.txt
python summarizer.py --text "Your long text goes here"
