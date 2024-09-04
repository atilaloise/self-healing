import yaml
import re

def load_yaml(yaml_content):
    return yaml.safe_load(yaml_content)

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

# Exemplo de uso:
yaml_content = """
__mobile_ios_modules: &mobile_ios_modules
  team: ios
  template: mobile/ios
  project: iba

pipelines:
  - repository: teste1
    template: xpto
    team: decv
    project: IAB

  - template: xpto
    repository: teste4
    project: IAB
    team: decv

  - repository: teste_mobile
    <<: *mobile_ios_modules

  - repository: teste2
    team: decv
    project: IAB
    template: xpto
"""

repository_value = "teste4"
project_value = "IAB"

# Carrega o conteúdo do YAML
yaml_loaded = load_yaml(yaml_content)

# Encontra o bloco correspondente
block_to_remove = find_block(yaml_content, repository_value, project_value)

# Remove o bloco e atualiza o YAML
updated_yaml_content = remove_block(yaml_content, block_to_remove)

print(updated_yaml_content)
