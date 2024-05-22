def parse_input_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read().strip()
    
    entries = content.split('\n\n')  # Split entries by blank lines
    parsed_data = []

    for entry in entries:
        lines = entry.strip().split('\n')
        question = lines[0]
        correct_answer_index = int(lines[1]) - 1  # Convert to 0-based index
        answers = lines[2:]
        
        if not 0 <= correct_answer_index < len(answers):
            print("[ERROR] Invalid correct answer index")
            exit(1)
        
        parsed_data.append({
            'question': question,
            'correct_answer_index': correct_answer_index + 1,  # Convert back to 1-based index
            'answers': answers
        })
    
    return parsed_data

# Example usage
file_path = 'input.txt'
parsed_data = parse_input_file(file_path)
for entry in parsed_data:
    print(f"Question: {entry['question']}")
    print(f"Correct Answer Index: {entry['correct_answer_index']}")
    print("Answers:")
    for answer in entry['answers']:
        print(f"- {answer}")
    print()
