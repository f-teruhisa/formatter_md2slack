from bs4 import BeautifulSoup
import markdown
import os

md = markdown.Markdown()

def format_markdown_to_planetext(doc):
    html = md.convert(doc)
    text = ''.join(BeautifulSoup(html, features="html.parser").findAll(text=True))
    translate_checkbox_to_bullet(text)

def translate_checkbox_to_bullet(text):
    replaced_text = text.replace('[ ]', '-').replace('[x]', '-')
    output_txt_file(replaced_text)

def output_txt_file(text):
    with open('src/text.txt', mode='w') as t:
        t.write(text)

with open('src/document.md') as f:
    md_document = f.read()
    format_markdown_to_planetext(md_document)
