def write_markdown(topics, summaries, filename="summary.md"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("# 🧠 Key Topics\n")
        for topic in topics:
            f.write(f"- {topic.strip()}\n")
        f.write("\n---\n")

        for title, summary in summaries.items():
            f.write(f"\n## {title}\n")
            f.write(f"{summary.strip()}\n")