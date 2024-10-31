# language: pt
Funcionalidade: Pesquisa no Google Acadêmico e abertura do último resultado acessível
    Como usuário
    Quero realizar uma busca pelo Google Acadêmico e abrir o último resultado acessível

Cenário: Pesquisar no Google e depois no Google Acadêmico
    Dado que o usuário está na página inicial do Google
    Quando o usuário buscar por "Google Acadêmico"
    E o usuário abre o Google Acadêmico nos resultados
    E o usuário buscar por "PHP" no Google Acadêmico
    Então o usuário deve abrir o último resultado acessível para "PHP" e salvar no arquivo
