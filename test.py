   pattern = re.compile(
        r'(\s*-\s*repository:\s*' + re.escape(repository_name) +
        r'\s*\n(?:\s+[^\n]*\n)*?' +
        r'\s*project:\s*' + re.escape(project_name) +
        r'\s*(?:\n\s+[^\n]*)*)\n(?=\s*-\s*repository:|\Z)', 
        re.DOTALL
    )