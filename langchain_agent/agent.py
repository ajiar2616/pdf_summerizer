from tools.pdf_reader_tool import extract_pdf_pages
from tools.summarizer_tool import summarize_text
from tools.formatter_tool import write_markdown
from langchain_ollama import OllamaLLM

def run_pdf_summarizer_agent(file_path):
    print("📄 Extracting sections from PDF...")
    sections = extract_pdf_pages(file_path)

    summarized_sections = {}
    for title, content in sections.items():
        print(f"✏️ Summarizing {title}...")
        summary = summarize_text(content, title)
        summarized_sections[title] = summary

    # Extract overall key topics
    full_text = "\n".join(sections.values())
    llm = OllamaLLM(model="llama3")
    topic_prompt = f"""
You are a helpful assistant. Read this document and list the key topics it covers as bullet points:

{full_text[:3000]}
"""
    print("🧠 Extracting key topics...")
    topics_raw = llm.invoke(topic_prompt)
    topics = [line.strip("-• ").strip() for line in topics_raw.split("\n") if line.strip()]

    print("📝 Writing markdown summary...")
    write_markdown(topics, summarized_sections)
    print("✅ Summary saved as summary.md!")
