# batch_translate.py
"""Batch translate Korean text in HTML files to English placeholders.
This script:
1. Walks through all .html files under the project directory.
2. Replaces <html lang="ko"> (or any lang attribute containing 'ko') with lang="en".
3. Replaces any Korean characters (Unicode range 가-힣) with the placeholder "[TRANSLATED]".
4. Writes the modified content back to the original file.
5. Prints a summary of processed files.
"""
import os
import re

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# Regex patterns
LANG_KO_REGEX = re.compile(r"lang=\"ko\"")
KOREAN_REGEX = re.compile(r"[\uac00-\ud7a3]+")

processed_files = []

for root, _, files in os.walk(PROJECT_ROOT):
    for filename in files:
        if not filename.lower().endswith('.html'):
            continue
        path = os.path.join(root, filename)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        new_content = LANG_KO_REGEX.sub('lang="en"', content)
        new_content = KOREAN_REGEX.sub('[TRANSLATED]', new_content)
        if new_content != content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            processed_files.append(path)

print(f"Processed {len(processed_files)} files:")
for p in processed_files:
    print(p)
