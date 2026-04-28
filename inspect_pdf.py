import fitz

doc = fitz.open("Ассоциация Героев (Мир One-Punch Man).pdf")
print("Total pages:", doc.page_count)

for i in range(min(50, doc.page_count)):
    text = doc.load_page(i).get_text()
    if "Глава" in text or "Сеттинг" in text or "сеттинг" in text:
        lines = text.split('\n')
        for line in lines:
            if "Глава" in line or "Сеттинг" in line or "сеттинг" in line:
                print(f"Page {i}: {line}")
