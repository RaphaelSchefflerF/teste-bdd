# Projeto de Testes Automatizados com Behave e Selenium

Este projeto utiliza o **Behave** (BDD) e o **Selenium** para automatizar uma coleta de dados no Google Acadêmico. O processo inclui a navegação pelo Google, acesso ao Google Acadêmico, busca por um termo específico e coleta de títulos e links de múltiplos artigos acessíveis, que são salvos em um arquivo CSV.

## Requisitos

- **Python 3.x** instalado
- **Google Chrome** instalado
- **ChromeDriver** compatível com sua versão do Google Chrome (instalado automaticamente pelo `webdriver-manager`)

## Configuração do Ambiente

### 1. Clonar o Repositório

Clone este repositório e navegue até a pasta do projeto:

```bash
git clone https://github.com/seuusuario/seuprojeto.git
cd seuprojeto
```

### 2. Instalar Dependências

Instale as dependências do projeto com o comando:

```bash
pip install behave selenium webdriver-manager
```

## Estrutura do Projeto

A estrutura do projeto é organizada conforme abaixo:

```
.
├── features
│   ├── busca_google_academico.feature   # Cenários de testes em BDD para busca no Google Acadêmico
│   └── steps
│       └── busca_google_steps.py        # Passos dos cenários implementados em Python
└── artigos_google_academico.csv         # Arquivo CSV que armazena os títulos e links coletados
```

## Executando os Testes

### 1. Navegar até a pasta de testes

Entre na pasta `features`, onde estão os cenários de teste:

```bash
cd features
```

### 2. Rodar os Testes

Para executar os testes, utilize o comando:

```bash
python -m behave
```

## Saída dos Testes

Após a execução, o arquivo `artigos_google_academico.csv` será criado com as seguintes informações para cada artigo coletado:

- **Título**: O título de cada artigo acessível encontrado na busca.
- **Link**: A URL de cada artigo.

### Exemplo de `artigos_google_academico.csv`

```csv
Título,Link
"PHP: Hypertext Preprocessor","https://link_do_artigo1.com"
"Desenvolvimento de aplicações com PHP","https://link_do_artigo2.com"
```

## Observações

- Verifique se a versão do Chrome instalada é compatível com o ChromeDriver gerenciado pelo `webdriver-manager`.
- O arquivo `artigos_google_academico.csv` será sobrescrito a cada execução. Renomeie o arquivo ou mova-o para outra pasta caso deseje manter um histórico dos artigos coletados.
- O teste coleta até cinco páginas de artigos por padrão, para evitar sobrecarga. Esse limite pode ser ajustado no código, se necessário.
