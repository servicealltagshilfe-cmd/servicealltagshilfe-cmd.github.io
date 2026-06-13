#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut die EPUB-Datei 'Herzenssache' aus content.py und dem Cover."""
import os
from ebooklib import epub
import content as C

OUT = "build/Herzenssache.epub"

book = epub.EpubBook()
book.set_identifier("servicealltagshilfe-herzenssache-2026")
book.set_title(C.BOOK_TITLE)
book.set_language(C.LANG)
book.add_author(C.AUTHOR)
book.add_metadata("DC", "description",
                  "Ein ehrlicher, praxisnaher Beziehungsratgeber für alle: "
                  "Singles, Paare, Verheiratete und jede Form der Liebe. "
                  "Mit vielen Beispielen und konkreten Tipps.")
book.add_metadata("DC", "subject", "Beziehung")
book.add_metadata("DC", "subject", "Partnerschaft")
book.add_metadata("DC", "subject", "Liebe")
book.add_metadata("DC", "publisher", C.AUTHOR)

# --- Cover ---
with open("build/cover.jpg", "rb") as f:
    book.set_cover("cover.jpg", f.read())

# --- Stylesheet ---
css = epub.EpubItem(uid="style", file_name="style/main.css",
                    media_type="text/css", content=C.CSS)
book.add_item(css)

# --- Titelseite ---
title_html = f"""
<div class="cover-page">
<h1 style="border:none;font-size:2.2em;margin-top:2em;">{C.BOOK_TITLE}</h1>
<p style="font-size:1.3em;font-style:italic;color:#b8430f;">{C.BOOK_SUBTITLE}</p>
<p style="margin-top:1.5em;font-size:1.05em;">Ein ehrlicher Beziehungsratgeber</p>
<p style="margin-top:0.3em;">für Singles &middot; Paare &middot; Verheiratete &middot; jede Liebe</p>
<p style="margin-top:3em;font-family:Helvetica,Arial,sans-serif;color:#555;">{C.AUTHOR}</p>
<p style="margin-top:4em;font-size:3em;color:#c0392b;">&#10084;</p>
</div>
"""
title_page = epub.EpubHtml(title="Titel", file_name="title.xhtml", lang=C.LANG)
title_page.content = title_html
title_page.add_item(css)
book.add_item(title_page)

# --- Kapitel ---
chapters = []
for i, (title, html) in enumerate(C.CHAPTERS, start=1):
    ch = epub.EpubHtml(title=title, file_name=f"chap_{i:02d}.xhtml", lang=C.LANG)
    ch.content = html
    ch.add_item(css)
    book.add_item(ch)
    chapters.append(ch)

# --- Navigation / TOC ---
book.toc = tuple(chapters)
book.add_item(epub.EpubNcx())
nav = epub.EpubNav()
nav.add_item(css)
book.add_item(nav)

# Lesereihenfolge: Cover -> Titel -> Inhaltsverzeichnis -> Kapitel
book.spine = ["cover", title_page, nav] + chapters

os.makedirs("build", exist_ok=True)
epub.write_epub(OUT, book)
size = os.path.getsize(OUT)
print(f"EPUB erstellt: {OUT} ({size/1024:.0f} KB, {len(chapters)} Kapitel)")
