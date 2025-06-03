import pygetwindow as gw
import re
import time

def find_docx_from_browser():
    windows = gw.getAllTitles()
    for title in windows:
        match = re.search(r"([\w\s\-]+\.docx)", title)
        if match:
            return match.group(1)
    return None

# 
while True:
    filename = find_docx_from_browser()
    if filename:
        print("📄 the Name of opened file is:", filename)
    else:
        print("❌  .docx file not finded")

    time.sleep(5)  # 
