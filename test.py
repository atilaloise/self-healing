import yaml
import re

def load_yaml_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_yaml_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def find_block(yaml_content, repository_value, project_value):
    # Regex para encontrar o bloco com as chaves e valores especificados
    pattern = re.compile(r"(\s*-\srepository:\s" + re.escape(repository_value) + r"\n(?:\s+\S+:\s[^\n]+\n)*)", re.MULTILINE)
    blocks = pattern.findall(yaml_content)

    for block in blocks:
        if f"project: {project_value}" in block:
            return block
    return None

def remove_block(yaml_content, block):
    if block:
        # Substitui o bloco encontrado por uma linha vazia
        yaml_content = yaml_content.replace(block, "\n", 1)
    return yaml_content

def process_yaml_file(file_path, repository_value, project_value):
    # Carrega o conteúdo do arquivo YAML
    yaml_content = load_yaml_from_file(file_path)

    # Encontra o bloco correspondente
    block_to_remove = find_block(yaml_content, repository_value, project_value)

    # Remove o bloco e atualiza o YAML
    updated_yaml_content = remove_block(yaml_content, block_to_remove)

    # Escreve o conteúdo atualizado de volta ao arquivo
    write_yaml_to_file(file_path, updated_yaml_content)

# Exemplo de uso:
file_path = 'caminho/para/seu/arquivo.yaml'
repository_value = "teste4"
project_value = "IAB"

#
