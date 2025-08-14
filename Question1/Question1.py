import json

def word_cnt(text):
    words = text.split()
    result = dict(zip(set(words), map(words.count, set(words))))
    
    # Inner helper function to use 'with' for safe file writing
    def write_file(i):
        with open(f"result_{i}.json", "w") as f:
            json.dump(result, f, indent=4)
    
    list(map(write_file, range(1, 101)))
    
    return result

# Example usage
input_text = "data engineering is awesome"
result = word_cnt(input_text)
