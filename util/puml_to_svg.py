import os
import subprocess

# Caminho absoluto do arquivo JAR (corrigido)
plantuml_jar = r"C:\Users\pedro\Downloads\pweb1\APS-documents\util\plantuml-1.2022.12.jar"

# Caminho da pasta raiz onde os arquivos .puml estão
root_dir = os.getcwd()

# Função para converter arquivos .puml em .svg
def convert_puml_to_svg(file_path):
    command = ['java', '-jar', plantuml_jar, '-tsvg', file_path]
    
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode == 0:
        print(f'Convertido: {file_path}')
    else:
        print(f'Erro ao converter {file_path}: {result.stderr.decode()}')

# Percorre a pasta raiz em busca de arquivos .puml
for dirpath, _, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith('.puml'):
            file_path = os.path.join(dirpath, filename)
            convert_puml_to_svg(file_path)
