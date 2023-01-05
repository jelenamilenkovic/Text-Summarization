import PyPDF2
from tkinter import *
import re
import urllib.request
import bs4 as bs
import sys

def file_Reader(file_path):
    with open(file_path) as f:
        text = f.read().replace("\n", '')
        return text

def wikipedia_Reader(url):
    scrap_data = urllib.request.urlopen(url)
    article = scrap_data.read()
    parsed_article = bs.BeautifulSoup(article,'lxml')
    
    paragraphs = parsed_article.find_all('p')
    article_text = ""
    
    for p in paragraphs:
        article_text += p.text
    
    article_text = re.sub(r'\[[0-9]*\]', '', article_text)
    return article_text

def pdf_Reader(pdf_path):
    with open(pdf_path, 'rb') as pdfFileObject:
        pdfReader = PyPDF2.PdfReader(pdfFileObject)
        count = len(pdfReader.pages)
        print("\nTotal Pages in pdf = ", count)
        start_page = 0
        end_page = count-1

        for i in range(start_page,end_page+1):
            page = pdfReader.pages[i]

        return page.extract_text()


    