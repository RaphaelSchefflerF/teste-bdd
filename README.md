Aqui está a versão aprimorada do README pronta para uso em um repositório Git, com formatação Markdown adequada:

---

# Projeto de Testes Automatizados com Behave e Selenium

Este projeto utiliza o **Behave** (BDD) e o **Selenium** para automatizar uma busca no Google Acadêmico. O processo inclui a navegação pelo Google, acesso ao Google Acadêmico e busca de um termo específico, salvando o título e o link do último resultado acessível em um arquivo CSV.

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
└── resultados_google_academico.csv      # Arquivo CSV que armazena o último resultado acessível
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

Após a execução, o arquivo `resultados_google_academico.csv` será criado com as seguintes informações:

- **Busca**: O termo pesquisado no Google Acadêmico.
- **Último Resultado Acessível**: O título do último artigo acessível encontrado.
- **Link**: A URL do último artigo acessível.

### Exemplo de `resultados_google_academico.csv`

```csv
Busca,Último Resultado Acessível,Link
PHP,"Título do último artigo","https://link_do_ultimo_artigo.com"
```

## Observações

- Verifique se a versão do Chrome instalada é compatível com o ChromeDriver gerenciado pelo `webdriver-manager`.
- A cada execução, o arquivo `resultados_google_academico.csv` é sobrescrito. Renomeie o arquivo ou mova-o para outra pasta caso queira manter históricos das buscas.

---

Com este README, seu repositório Git estará documentado de forma clara e prática para que outros usuários possam configurar e executar os testes automatizados facilmente.
