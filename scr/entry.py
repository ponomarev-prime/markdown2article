# Имя входного .md файла
input_md_file = 'text/index.md'  # Замените на путь к вашему .md файлу

def titleFinder(input_md_file):
    # Чтение содержимого .md файла
    with open(input_md_file, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()
    # Поиск первого вхождения символа '#'
    index_of_first_hash = md_content.find('#')
    if index_of_first_hash != -1:
        line_with_hash = md_content[:index_of_first_hash]
        # Находим позицию ближайшего символа переноса строки после символа '#'
        index_of_newline = md_content.find('\n', index_of_first_hash)
        if index_of_newline != -1:
            title = md_content[index_of_first_hash+2:index_of_newline]
            # print(title)
            return title
        else:
            print(f"Символ '#' найден, но нет символа переноса строки после него.")
            return 0
    else:
        print("Символ '#' не найден в .md файле")
        return 0


print(titleFinder(input_md_file))