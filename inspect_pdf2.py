import fitz

doc = fitz.open("Ассоциация Героев (Мир One-Punch Man).pdf")
for i in range(5):
    text = doc.load_page(i).get_text()
    print(f"--- Page {i} ---")
    print(text[:500])
