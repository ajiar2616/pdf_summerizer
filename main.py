# Main Running File of the Project
from pdf_reader import extract_pdf_text
from summarizer import run_llama
from formatter import save_markdown

if __name__ == "__main__":
    pdf_path = "input.pdf"
    sections = extract_pdf_text(pdf_path)

    print(f"✅ Found {len(sections)} sections in the PDF\n")
    
    # Summarize each section
    summarized_sections = {}

    for title, content in sections.items():
        print(f"🔍 Summarizing {title}...")
        prompt = f"""
You are a helpful assistant. Summarize the following section of a document in 3-5 sentences:

{content[:2000]}
"""
        summary = run_llama(prompt)
        summarized_sections[title] = summary
        

    # Extract key topics from the full document
    full_text = "\n".join(sections.values())
    print("\n🔎 Extracting key topics...")

    topic_prompt = f"""
You are a smart assistant. Read this document and list the key topics or concepts it discusses, as bullet points:

{full_text[:3000]}
"""
    topic_response = run_llama(topic_prompt)
    topic_list = [line.strip("- ").strip() for line in topic_response.split("\n") if line.strip()]

    # Save as Markdown
    save_markdown(topic_list, summarized_sections)

    print("\n✅ Summary saved to summary.md 🎉")