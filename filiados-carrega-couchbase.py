# -*- coding: utf-8 -*-
import os
import csv
from couchbase.bucket import Bucket
from couchbase.exceptions import KeyExistsError

bucket = Bucket('couchbase://localhost/filiados')

csv_filenames = [filename for filename in os.listdir('dados/filiados/') if os.path.isfile(os.path.join('dados/filiados/', filename)) and filename.split('.')[-1] == 'csv']
total = len(csv_filenames)

for num, filename in enumerate(csv_filenames):
    print u'({:d}/{:d}) Processando {}...'.format(num+1, total, filename)
    with open(os.path.join('dados/filiados/', filename)) as f:
        planilha = csv.DictReader(f, delimiter=';')
        for linha in planilha:
            # definicao da chave
            # se o eleitor se filiou e se desfiliou mais de uma vez,
            # nao sera considerado (geralmente eh uma desfiliacao
            # a pedido e outra via judicial)
            chave = "-".join((
                linha['NUMERO DA INSCRICAO'],
                linha['DATA DA FILIACAO'],
                linha['SITUACAO DO REGISTRO'],
            ))
            dados = {
                'type': 'filiado',
                'titulo_eleitor': linha['NUMERO DA INSCRICAO'],
                'nome': linha['NOME DO FILIADO'],
                'sigla_partido': linha['SIGLA DO PARTIDO'],
                'situacao_registro': linha['SITUACAO DO REGISTRO'],
                'tipo_registro': linha['TIPO DO REGISTRO'],
                'zona_eleitoral': linha['SECAO ELEITORAL'],
                'secao_eleitoral': linha['ZONA ELEITORAL'],
                'codigo_municipio': linha['CODIGO DO MUNICIPIO'],
                'uf': linha['UF'],
                'data_filiacao': linha['DATA DA FILIACAO'],
            }
            if linha['DATA DO CANCELAMENTO']:
                dados['data_cancelamento'] = linha['DATA DO CANCELAMENTO']
            if linha['DATA DA DESFILIACAO']:
                dados['data_desfiliacao'] = linha['DATA DA DESFILIACAO']
            try:
                bucket.insert(chave, dados)
            except KeyExistsError:
                # pula o registro
                continue

