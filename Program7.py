def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def get_unique_words(text):
    words = text.split()
    cleaned_words = [word.strip('.,!?').lower() for word in words]
    unique_words = set(cleaned_words)
    return sorted(unique_words)

def main():
    file_path = 'input.txt'
    text = read_file(file_path)
    
    unique_words = get_unique_words(text)
    
    print("Unique words in alphabetical order:")
    for word in unique_words:
        print(word)

if __name__ == "__main__":
    main()
