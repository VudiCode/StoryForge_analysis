import fitz

doc = fitz.open("Ассоциация Героев (Мир One-Punch Man).pdf")
for i in range(doc.page_count):
    text = doc.load_page(i).get_text()
    lines = text.split('\n')
    for line in lines:
        if line.strip() == "Сеттинг":
            print(f"Page {i}: {line}")
        elif line.strip().startswith("Глава") and len(line.strip().split()) <= 2:
            print(f"Page {i}: {line}")
