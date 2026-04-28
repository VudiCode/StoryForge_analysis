import fitz
import os
import re

def extract_pdf_chapters(pdf_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    doc = fitz.open(pdf_path)

    current_chapter = None
    current_content = []

    def save_chapter():
        if current_chapter and current_content:
            safe_name = re.sub(r'[\\/*?:"<>|]', "", current_chapter)
            filepath = os.path.join(output_dir, f"{safe_name}.txt")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write("\n".join(current_content))

    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text = page.get_text()

        lines = text.split('\n')
        for line in lines:
            line_stripped = line.strip()

            if line_stripped == "Сеттинг":
                save_chapter()
                current_chapter = "Сеттинг"
                current_content = [line]
                continue

            chapter_match = re.match(r'^(Глава \d+)$', line_stripped)
            if chapter_match:
                save_chapter()
                current_chapter = chapter_match.group(1)
                current_content = []
                continue

            if current_chapter is not None:
                current_content.append(line)

    save_chapter()

if __name__ == "__main__":
    pdf_path = "Ассоциация Героев (Мир One-Punch Man).pdf"
    output_dir = "adventure"
    extract_pdf_chapters(pdf_path, output_dir)
