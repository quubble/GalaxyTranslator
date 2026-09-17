# 🌌 Galaxy Translator

A beautiful **AI-powered multilingual language translation web application** built with **Python, Streamlit, PyTorch, and Hugging Face Transformers**.

Supports **190+ languages** through Meta AI's **NLLB-200 distilled 600M** pretrained neural machine translation model.

Some supported languages include:

✅ English
✅ Marathi
✅ Hindi
✅ Telugu
✅ Tamil
✅ Bengali
✅ French
✅ German
✅ Arabic
✅ And many more…

---

## ✨ Features

* 🌍 Multilingual text translation
* 🤖 Powered by **NLLB-200 distilled 600M**
* 🔤 Uses NLLB technical language codes such as `eng_Latn`, `mar_Deva`, and `tel_Telu`
* 🔎 Searchable source and target language selection
* 📝 Simple and user-friendly text input
* 🎨 Custom lavender / galaxy-inspired interface
* ✨ Animated translation output card
* ⚡ Powered by PyTorch
* 💻 Supports CPU inference
* ☁️ Suitable for Streamlit-based deployment
* 🚫 No model training required
* 🧠 Uses a pretrained Neural Machine Translation model

---

## 🛠 Tech Stack

* **Frontend:** Streamlit
* **AI / NLP Model:** NLLB-200 distilled 600M
* **Model:** `facebook/nllb-200-distilled-600M`
* **Backend:** PyTorch
* **NLP Framework:** Hugging Face Transformers
* **Tokenization:** SentencePiece
* **Model File Format:** Safetensors
* **Model Loading / Device Management:** Accelerate
* **Styling:** Custom CSS

---

## 📂 Project Structure

```bash
GalaxyTranslator/
├── app.py
├── image.png
├──config.toml
├── requirements.txt
└── README.md
```

### File Description

* `app.py` → Main Streamlit application
* `image.png` → Background image
* `requirements.txt` → Python dependencies
* `README.md` → Project documentation

> The `venv/` virtual environment is used for local development and should not be uploaded to GitHub.

---

## ✅ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/quubble/GalaxyTranslator.git
cd GalaxyTranslator
```

### 2️⃣ Create Virtual Environment

Creating a virtual environment is recommended to keep the project's dependencies isolated.

```bash
python -m venv venv
```

Activate it on Windows:

```bash
.\venv\Scripts\activate
```

After successful activation, the terminal should show:

```text
(venv)
```

---

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

Main dependencies:

```text
streamlit
torch
transformers
sentencepiece
safetensors
accelerate
```

---

### 4️⃣ Add Background Image

Make sure the background image is present in the project directory:

```bash
image.png
```

Your project should look like:

```bash
GalaxyTranslator/
├── app.py
├── image.png
├── requirements.txt
└── README.md
```

---

### 5️⃣ Run the App

```bash
streamlit run app.py
```

The application will normally be available at:

```text
http://localhost:8501
```

---

# 🌍 How to Use

* **Enter your text in the input box**
* **Select Source Language**
* **Select Target Language**
* **Click 🚀 Translate**
* **View your translation in the animated output card**

The application converts the selected languages into their corresponding NLLB language codes and uses the pretrained NLLB-200 model to generate the translation.

---

# 🧠 Model Details

* **Model Used:** `facebook/nllb-200-distilled-600M`
* **Model:** NLLB-200 distilled 600M
* **Developed By:** Meta AI
* **NLLB:** No Language Left Behind
* **Language Coverage:** 190+ languages
* **Model Type:** Multilingual Neural Machine Translation
* **Inference Mode:** No training required
* **Framework:** Hugging Face Transformers + PyTorch
* **Hardware:** CPU supported; GPU can provide faster inference

The `distilled-600M` version is a distilled NLLB model containing approximately **600 million parameters**, providing a practical balance between translation capability and computational requirements.

NLLB-200 is primarily intended for machine translation research and supports single-sentence translation across its supported languages.

---

# 🔤 Language Codes

NLLB uses technical language and script codes internally.

| Language | NLLB Code  |
| -------- | ---------- |
| English  | `eng_Latn` |
| Marathi  | `mar_Deva` |
| Hindi    | `hin_Deva` |
| Telugu   | `tel_Telu` |
| Tamil    | `tam_Taml` |
| Bengali  | `ben_Beng` |
| French   | `fra_Latn` |
| German   | `deu_Latn` |
| Arabic   | `arb_Arab` |

The model contains language/script codes for its supported language set, including multiple scripts and language variants.

---

# 🔄 Translation Workflow

```text
User enters text
       ↓
Select Source Language
       ↓
Select Target Language
       ↓
Convert selected languages to NLLB codes
       ↓
Set source language in tokenizer
       ↓
Tokenizer converts text into tokens
       ↓
Tokens are converted into PyTorch tensors
       ↓
NLLB-200 model performs translation
       ↓
Target language token is specified
       ↓
Model generates translated tokens
       ↓
Tokenizer decodes tokens into text
       ↓
Translated text is displayed
```

---

# 💻 Hardware Requirements

The application can run on a **CPU**, although inference can be faster when a suitable GPU is available.

### Recommended Development Environment

* Python 3.13 or 3.14
* 8 GB or more RAM recommended
* Modern CPU
* GPU is optional

Actual performance depends on the hardware and deployment environment.

---

# ⚠️ Limitations

* Translation quality can vary between different languages.
* Complex sentences may produce imperfect translations.
* Idioms and cultural expressions can be difficult to translate.
* Technical terminology may not always be translated correctly.
* Long input text can increase processing time and memory usage.
* The model was trained with input lengths not exceeding 512 tokens, so longer inputs may experience quality degradation.
* CPU inference can be slower than GPU inference.
* Translation quality depends on the model's training data and language coverage.
* The model is intended primarily for general-domain machine translation and is not intended for specialized medical or legal translation.
* Translations should not be treated as certified professional translations.

Therefore, the application should be considered an **AI-assisted translation system** rather than a replacement for professional human translation.

---

# 🔮 Future Scope

Extend the NLLB-200 text translation system into a voice-based multilingual translator by integrating Speech-to-Text, 
language identification, and Text-to-Speech, enabling spoken translation across NLLB-200's supported languages.

* **NLLB-200 is the translation engine, while speech recognition, language identification, and speech synthesis are separate modules. 
Meta itself describes NLLB as a machine-translation system for written text.**

🎤 Voice Input
↓
🗣️ Speech-to-Text
↓
🔍 Language Identification
↓
🤖 NLLB-200 — Text Translation
↓
🔊 Text-to-Speech
↓
🎧 Translated Voice Output

### ⚡ Model Optimization

Improve application performance through:

* Quantization
* Faster inference
* GPU acceleration
* Memory optimization
* Efficient model loading

### 🌐 Language Coverage

Make better use of the model's multilingual capabilities by expanding the application's language selection to cover more of the **190+ supported languages**.

### ✂️ Long-Text Processing

Implement intelligent text segmentation so longer inputs can be divided into suitable segments before translation, helping the application work more effectively with text beyond the model's recommended input length.

### 🎨 UI Enhancements

Continue improving the galaxy-inspired interface with additional animations, themes, responsive design, and accessibility features.

---

# ☁️ Streamlit Deployment

The application can be deployed as a Streamlit web application.

The deployment workflow is:

```text
Galaxy Translator
       ↓
GitHub Repository
       ↓
Streamlit Deployment
       ↓
Install requirements.txt
       ↓
Download NLLB-200 Model
       ↓
Load Model
       ↓
Deploy Application
       ↓
Public Streamlit App
```

Because the NLLB-200 distilled 600M model is relatively large and requires significant memory for inference, available CPU/RAM resources should be considered when choosing a cloud deployment environment.

---

# 📜 Model License

The `facebook/nllb-200-distilled-600M` model is released under the **CC-BY-NC 4.0** license. Users should review the model's license and usage restrictions before using it in commercial applications.

---

# 🎯 Concepts Demonstrated

* Artificial Intelligence
* Natural Language Processing
* Neural Machine Translation
* Transformer Architecture
* Sequence-to-Sequence Models
* Tokenization
* PyTorch
* Hugging Face Transformers
* Streamlit
* Python
* Cloud Deployment

---

# ⭐ Acknowledgements

This project makes use of the following open-source technologies and research:

* Hugging Face Transformers
* Meta AI NLLB
* PyTorch
* Streamlit
* SentencePiece
* Safetensors
* Accelerate

---

## 🌌 Galaxy Translator

**AI-powered multilingual translation with a simple and interactive Streamlit interface.**
