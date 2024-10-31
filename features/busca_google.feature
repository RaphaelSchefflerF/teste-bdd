# language: pt
Funcionalidade: Coleta de Artigos no Google Acadêmico para Revisão de Literatura
    Como pesquisador
    Quero buscar artigos sobre PHP no Google Acadêmico
    Para coletar títulos e links de artigos para uso em uma revisão de literatura

Cenário: Coletar múltiplos artigos sobre PHP no Google Acadêmico e salvar em CSV
    Dado que o usuário está na página inicial do Google
    Quando o usuário buscar por "Google Acadêmico"
    E o usuário abre o Google Acadêmico nos resultados
    E o usuário buscar por "PHP" no Google Acadêmico
    Então o usuário deve coletar títulos e links de artigos em múltiplas páginas e salvar no arquivo CSV
