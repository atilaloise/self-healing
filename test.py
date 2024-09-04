import re

def remove_pipeline_block(yaml_content, repository_name, project_name):
    # Regex para identificar blocos de pipelines que contêm as chaves repository e project em qualquer ordem
    pattern = re.compile(
        r'(\s*-\s*(?:\w+:\s*.*\n)+?'  # Início do bloco, capturando qualquer chave e valor
        r'(?=.*?\brepository:\s*' + re.escape(repository_name) + r'\b)'  # Condição: deve conter a chave repository com o valor correspondente
        r'(?=.*?\bproject:\s*' + re.escape(project_name) + r'\b)'  # Condição: deve conter a chave project com o valor correspondente
        r'(?:\s+\w+:\s*.*\n)*)',  # Continua capturando até o final do bloco
        re.MULTILINE
    )
    
    # Substitui o bloco encontrado por uma linha vazia para evitar sobreposição
    new_yaml_content = re.sub(pattern, '\n', yaml_content)
    
    return new_yaml_content.strip()

# Exemplo de uso
yaml_content = """
pipelines:
  - team: decv
    repository: teste1
    template: xpto
    project: IAB

  - template: xpto
    repository: teste4
    project: IAB
    team: decv

  - repository: teste2
    team: decv
    project: IAB
    template: xpto
"""

repository_name = "teste4"
project_name = "IAB"

new_yaml_content = remove_pipeline_block(yaml_content,
