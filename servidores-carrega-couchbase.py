# -*- coding: utf-8 -*-
import io
import os
import csv
from couchbase.bucket import Bucket
from couchbase.exceptions import KeyExistsError

bucket = Bucket('couchbase://localhost/default')

# procura o nome da planilha de cadastro
cadastro_filename = [filename for filename in os.listdir('dados/servidores/') if os.path.isfile(os.path.join('dados/servidores/', filename)) and filename.split('.')[-1] == 'csv' and 'Cadastro' in filename][0]

print u'Processando {}...'.format(cadastro_filename)
with open(os.path.join('dados/servidores/', cadastro_filename)) as f:
    dados = f.read()
    # retira os bytes NUL (nao deveriam existir na planilha e dao erro)
    dados = dados.replace('\x00', '')
    planilha = csv.DictReader(io.BytesIO(dados), delimiter='\t')
    for linha in planilha:
        # definicao da chave
        # se o eleitor se filiou e se desfiliou mais de uma vez,
        # nao sera considerado (geralmente eh uma desfiliacao
        # a pedido e outra via judicial)
        chave = "-".join((
            linha['CPF'].decode('iso-8859-1'),
            linha['MATRICULA'].decode('iso-8859-1'),
            linha['FUNCAO'].decode('iso-8859-1'),
            linha['DATA_INGRESSO_CARGOFUNCAO'].decode('iso-8859-1'),
        ))
        dados = {
            'type': 'servidor',
            'cpf': linha['CPF'],
            'matricula': linha['MATRICULA'],
            'nome': linha['NOME'],
            'sigla_funcao': linha['SIGLA_FUNCAO'],
            'nivel_funcao': linha['NIVEL_FUNCAO'],
            'funcao': linha['FUNCAO'],
            'codigo_orgao_lotacao': linha['COD_ORG_LOTACAO'],
            'codigo_orgao_superior_lotacao': linha['COD_ORGSUP_LOTACAO'],
            'codigo_uorg_exercicio': linha['COD_UORG_EXERCICIO'],
            'codigo_orgao_exercicio': linha['COD_ORG_EXERCICIO'],
            'codigo_orgao_superior_exercicio': linha['COD_ORGSUP_EXERCICIO'],
            'tipo_vinculo': linha['TIPO_VINCULO'],
            'situacao_vinculo': linha['SITUACAO_VINCULO'],
            'regime_juridico': linha['REGIME_JURIDICO'],
            'data_ingresso_cargofuncao': linha['DATA_INGRESSO_CARGOFUNCAO'],
            'data_nomeacao_cargofuncao': linha['DATA_NOMEACAO_CARGOFUNCAO'],
        }
        
        # decodificar acentuacao, trocar para utf-8, exigido pelo couchbase
        dados = dict(((key, value.decode('iso-8859-1')) for key, value in dados.items()))
        
        # carregar somente os servidores que tem funcao
        if dados['funcao']:
            bucket.insert(chave, dados)

