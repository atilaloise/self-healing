import re

def remove_pipeline_block(yaml_content, repository_name, project_name):
    # Regex para identificar blocos de pipelines
    pattern = re.compile(
        r'(\s*- repository:\s*' + re.escape(repository_name) + r'\s*\n'
        r'(?:\s+.+\n)*?'  # Pega todas as linhas dentro do bloco
        r'\s*project:\s*' + re.escape(project_name) + r'\s*\n'
        r'(?:\s+.+\n)*)',  # Continua pegando todas as linhas dentro do bloco
        re.MULTILINE
    )
    
    # Substitui o bloco encontrado por uma linha vazia para evitar sobreposição
    new_yaml_content = re.sub(pattern, '\n', yaml_content)
    
    return new_yaml_content.strip()

# Exemplo de uso
yaml_content = """
pipelines:
  - repository: teste1
    template: xpto
    team: decv
    project: IAB

  - repository: teste4
    template: xpto
    project: IAB
    team: decv

  - repository: teste2
    team: decv
    project: IAB
    template: xpto
"""

repository_name = "teste4"
project_name = "IAB"

new_yaml_content = remove_pipeline_block(yaml_content, repository_name, project_name)
print(new_yaml_content)
