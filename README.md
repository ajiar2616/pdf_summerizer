# 🤖 PDF Summarizer Agent (Local Agentic AI)

This project is a **local agentic AI workflow** that reads a multi-page PDF, extracts key topics, summarizes each section intelligently using a local LLM, and outputs the results as a clean Markdown file — all **offline**.

---

## 🔧 Tech Stack

- **Python 3**
- **Ollama + LLaMA 3 (Local LLM)**
- **PyMuPDF** for reading PDF content
- **Markdown** file writer
- Modular project structure (Reader ➜ Summarizer ➜ Formatter)

---

## 🎯 Features

- ✅ Reads and parses a multi-page PDF file
- ✅ Breaks it into logical sections (by page)
- ✅ Uses a local LLM (via Ollama) to summarize each section
- ✅ Extracts key topics from the full document
- ✅ Outputs a `summary.md` file with clean structure
- ✅ No cloud APIs — runs 100% locally

---

## 🚀 How to Run

### 1. **Clone the Repository**

```bash
git clone https://github.com/YOUR_USERNAME/pdf-summarizer-agent.git
cd pdf_summarizer
```

### 2. Choose the Agentic (Manual/LangChain)
Before installing all the dependencies choose the right agentic. We have built this with both manual which is completely setup belongs to local or with an Agentic Library (LangChain). Once you navigate to the specific folder you can continue with the below mentioned steps.

### 2. **Install Python dependencies**

```bash
pip install -r requirements.txt
```


### 3. Install Ollama (Local AI Runtime)
Download & install from https://ollama.com

Then run this to download the model:

```bash
ollama pull llama3
```

And start the Ollama server (in a separate terminal):

```bash
ollama serve
```

This will run a local API server on http://localhost:11434

To verify the Ollam is running type the command on another terminal:

```bash
curl http://localhost:11434
```


### 4. Add Your PDF
Place your PDF file in the root folder and name it `input.pdf`.

### 5. Run the Summarizer
```bash
python3 main.py
```

This will:

- Read the PDF

- Summarize each page using LLaMA 3

- Extract key topics

- Save everything to summary.md


## 📁 Folder Structure

```graphql
pdf_summarizer/
├── manual_agent/
│   ├── main.py               ← Manual version
│   ├── pdf_reader.py
│   ├── summarizer.py
│   ├── formatter.py
│   ├── requirements.py
│
├── langchain_agent/
│   ├── main.py                ← LangChain version
│   ├── agent.py
│   ├── tools/
│   │   ├── pdf_tool.py
│   │   ├── summarize_tool.py
│   │   └── formatter_tool.py
│   ├── requirements.txt
│   ├── agent.py
│   ├── main.py
│   ├── agent.py
└── input.pdf
```

---
