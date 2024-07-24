def custom_write(file_name, strings):
    strings_positions = {}
    line_number = 0
    line_bytes = []
    with open(file_name, mode='w', encoding="utf8") as file:
        for string in strings:
            line_bytes.append(file.tell())
            file.write(string + '\n')
    with open(file_name, mode='r', encoding='utf8') as reading_file:
        for line in reading_file:
            strings_positions[(line_number + 1, line_bytes[line_number])] = line.replace('\n', '')
            line_number += 1
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
