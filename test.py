import re

def remove_pipeline_block(yaml_content, repository_name, project_name):
    # Define a expressão regular para encontrar blocos com 'repository' e 'project' específicos
    pattern = re.compile(
        r'-\s*repository:\s*{}\n\s*[^-]*?project:\s*{}\n(?:\s+[^-]*\n)*'.format(re.escape(repository_name), re.escape(project_name)),
        re.MULTILINE
    )
    
    # Substitui o bloco encontrado por uma linha em branco (para evitar sobreposição)
    modified_yaml = re.sub(pattern, '\n', yaml_content)

    return modified_yaml

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

modified_yaml = remove_pipeline_block(yaml_content, repository_name, project_name)
print(modified_yaml)
