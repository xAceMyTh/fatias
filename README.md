Fatias - cruzamentos de dados de servidores do executivo federal e filiados a partidos políticos.

![desenho fatia de bolo](fatia.jpeg)

Projeto desenvolvido no Open Data Day 2016 Brasília.

# Objetivo

Fornecer um ambiente para análise de dados e visualizações para a distribuição
dos cargos de confiança no poder executivo federal entre os partidos políticos.

São exemplos de perguntas que o projeto pretende responder:

* Quais são os partidos cujos filiados mais ocupam cargos de confiança no poder
  executivo federal, e com quais percentuais?
* Quais órgãos públicos são predominantemente loteados para quais partidos?
* Como estão distribuídos entre os filiados a partidos políticos os Jetons
  (remuneração percebida em razão da participação em conselhos de administração
  e fiscal de empresas controladas pela União)?

# Fontes de dados

* Dataset dos [servidores do executivo federal](http://dados.gov.br/dataset/servidores-do-executivo-federal)
* Dataset dos [filiados a partidos políticos](http://dados.gov.br/dataset/filiados-partidos-politicos)

# Instalação

1. Clonar o repositório

`git clone https://github.com/augusto-herrmann/fatias.git`

2. Para usar os scripts em Python, criar e ativar um [ambiente virtual](https://virtualenv.readthedocs.org/en/latest/)

```
cd fatias
virtualenv --no-site-packages pyenv
source pyenv/bin/activate
```
3. Instalar as dependências do script que deseja usar. Use o comando

`pip install -r requirements.txt`

4. Para executar o script e baixar os dados, use

`python download-dados.py`

