import pypandoc
import sys

# using: $ python3 convert_md_to_html.py index.md index.html
args = sys.argv[1:]
inputFile = args[0]
outputFile = args[1]

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
            return title
        else:
            print(f"Символ '#' найден, но нет символа переноса строки после него.")
            return 0
    else:
        print("Символ '#' не найден в .md файле")
        return 0

def convMarkdownToHtml(inputFile, outputFile):
    # Имя входного .md файла, выходного файла html, путь к изображениям и заголовок
    input_md_file = f'text/{inputFile}'
    image_path = 'text/.img/'  # Укажите путь к вашим изображениям
    output_html_file = outputFile 
    # Чтение содержимого .md файла
    with open(input_md_file, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()
    # Замена пути к изоюражениям в прочитаном md файле
    md_content = md_content.replace('./.img/', f'{image_path}')
    # Конвертация .md в .html с внедрением изображений
    htmlTitle=titleFinder(input_md_file) # Загловок html
    metaTitle = f"pagetitle={htmlTitle}"
    html_content = pypandoc.convert_text(md_content, 'html', format='md', extra_args=['--standalone', '--embed-resources', '--metadata', metaTitle])
    # Записываем .html в выходной файл
    with open(output_html_file, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

if __name__ == "__main__":
    convMarkdownToHtml(inputFile, outputFile)