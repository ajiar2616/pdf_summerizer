from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")

def summarize_text(text, page_title="Section"):
    prompt = f"""
You are a helpful assistant. Summarize the following content from {page_title} in 3-5 sentences:

{text[:2000]}
"""
    return llm.invoke(prompt)
