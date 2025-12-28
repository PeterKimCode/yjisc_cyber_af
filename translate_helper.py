
import os
import glob

def is_korean(text):
    return any(u'\uac00' <= char <= u'\ud7a3' for char in text)

def find_html_files(directory):
    html_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
    return html_files

def main():
    root_dir = "c:/Users/ABC/Documents/yjisc_cyber_af/yjisc_cyber_af"
    all_html_files = find_html_files(root_dir)
    exclude = ["header.html", "footer.html", "index.html"]
    
    korean_files = []
    
    for file_path in all_html_files:
        basename = os.path.basename(file_path)
        if basename in exclude:
            continue
            
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                if is_korean(content) or 'lang="ko"' in content:
                    korean_files.append(file_path)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    korean_files.sort()
    
    # Print the first 10 files
    print("Files to translate:")
    for f in korean_files[:10]:
        print(f)
        
    print(f"\nTotal remaining files: {len(korean_files)}")

if __name__ == "__main__":
    main()
