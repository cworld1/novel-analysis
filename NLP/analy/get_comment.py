import json
import os

def extract_comments(json_directory, output_directory):
    """
    Extracts comments from JSON files and saves them into text files grouped by book ID.
    
    Args:
    json_directory (str): The directory where the JSON files are stored.
    output_directory (str): The directory where the output text files will be saved.
    """
    # Ensure output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Process each file in the JSON directory
    for filename in os.listdir(json_directory):
        if filename.endswith(".json"):
            file_path = os.path.join(json_directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                # Safely access the book ID
                book_id = data.get('bookInfo', {}).get('bookId', 'unknown_book_id')
                comments = data.get('commentInfo', {}).get('items', [])
                
                # Open or create a text file for each book ID and append comments
                output_file_path = os.path.join(output_directory, f"{book_id}.txt")
                with open(output_file_path, 'a', encoding='utf-8') as output_file:
                    for comment in comments:
                        content = comment.get('content', '')
                        if content:  # Only write non-empty content
                            output_file.write(content + '\n')

# Example usage
json_directory = '/root/HanLP/data/book_info'
output_directory = '/root/HanLP/output_comment'
extract_comments(json_directory, output_directory)
