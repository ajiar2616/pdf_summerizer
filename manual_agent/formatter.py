# Format and Save the summary as a Markdown file.
def save_markdown(topics, sections, output_file="summary.md"):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# 🧠 Key Topics\n")
        for topic in topics:
            f.write(f"- {topic.strip()}\n")

        f.write("\n---\n")

        for title, summary in sections.items():
            f.write(f"\n## {title}\n")
            f.write(f"{summary.strip()}\n")
