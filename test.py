import re

def remove_repository_and_project_block_from_file(file_path, repository_name, project_name):
    try:
        # Lê o conteúdo do arquivo
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
        return
    except IOError:
        print(f"Erro: Não foi possível ler o arquivo '{file_path}'.")
        return

    # Define a regex para encontrar o bloco que contém "repository" e "project"
    pattern = re.compile(
        r'(\s*-\s*repository:\s*' + re.escape(repository_name) +
        r'\s*\n\s*team:.*?\n\s*project:\s*' + re.escape(project_name) +
        r'\s*\n(?:\s*.*\n)*?)(?=\s*-\s*repository:|\s*\Z)', 
        re.DOTALL
    )

    # Remove apenas o bloco correspondente
    updated_content = pattern.sub('', content)

    try:
        # Salva o conteúdo atualizado de volta no arquivo
        with open(file_path, 'w') as file:
            file.write(updated_content)
    except IOError:
        print(f"Erro: Não foi possível escrever no arquivo '{file_path}'.")
        return

    print(f"Bloco com repository '{repository_name}' e project '{project_name}' removido com sucesso.")

# Exemplo de uso
file_path = 'caminho/para/seu/arquivo.yaml'  # Substitua pelo caminho do seu arquivo
remove_repository_and_project_block_from_file(file_path, "SuperRepo", "Superprojeto")
