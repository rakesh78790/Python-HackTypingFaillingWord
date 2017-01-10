import keyboard


def send_keys_from_file(text_filepath):
    text_lines = []
    with open(text_filepath) as f:
        for line in f:
            cleaned_line = line.strip()
            if cleaned_line:
                text_lines.append(cleaned_line)

    if not text_lines:
        print('Extracted text is empty')
        return False

    for line in reversed(text_lines):
        print(line)
        keyboard.write(line.lower())

    print('Sending keys done')
    return True
