# Automação CAC Python



Este projeto é uma aplicação desenvolvida para automatizar o processamento e manipulação de PDFs, além de gerenciar fluxos administrativos.



## Estrutura do Projeto



- **`.idea/`**: Configurações do projeto para IDEs, como PyCharm.

- **`.python-version`**: Define a versão do Python utilizada no projeto.

- **`Pdfs.zip` e `Pdfs/`**: Arquivos e pastas contendo PDFs para processamento.

- **`erros.txt`**: Arquivo contendo logs ou mensagens de erro.

- **`main/`**: Diretório principal com os módulos e lógica do projeto.

- **`poetry.lock` e `pyproject.toml`**: Arquivos de configuração do Poetry para gerenciamento de dependências.



## Requisitos



- **Python 3.8+**

- **Poetry** instalado para gerenciar dependências e o ambiente virtual.



## Instalação



1. Certifique-se de ter o Poetry instalado:

   ```bash

   pip install poetry

    Instale as dependências do projeto:

Sempre exibir os detalhes

poetry install

Ative o ambiente virtual gerenciado pelo Poetry:

Sempre exibir os detalhes

    poetry shell

Como Executar

    Navegue até o diretório principal do projeto.
    Execute o script principal:

Sempre exibir os detalhes

    python main/<arquivo_principal>.py

    Substitua <arquivo_principal> pelo nome do arquivo principal na pasta main.

Funcionalidades

    Processamento automatizado de PDFs.
    Identificação e registro de erros em erros.txt.
    Configuração de ambiente simples com o Poetry.

Observações

    Verifique os PDFs na pasta Pdfs/ ou no arquivo ZIP Pdfs.zip antes de iniciar a execução.
    Certifique-se de que a versão do Python seja compatível com .python-version.

Contribuições

Contribuições são bem-vindas! Siga estas etapas:

    Faça um fork do repositório.
    Crie um branch com sua feature: git checkout -b feature/nova-feature.
    Faça commit das mudanças: git commit -m 'Adicionei uma nova feature'.
    Faça push para o branch: git push origin feature/nova-feature.
    Abra um Pull Request.
