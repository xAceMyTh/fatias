Fatias - cruzamentos de dados de servidores do executivo federal e filiados a partidos políticos.

![desenho fatia de bolo](fatia.jpeg)

Projeto desenvolvido no Open Data Day 2016 Brasília.

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

