# -*- coding: utf-8 -*-
import io
import os
import urlparse
import zipfile
import requests
import ckanapi

dadosgovbr = ckanapi.RemoteCKAN('http://dados.gov.br', user_agent='fatias/1.0 (+http://github.com/augusto-herrmann/fatias)')
dataset_filiados = dadosgovbr.action.package_show(id='filiados-partidos-politicos')
urls = [resource['url'] for resource in dataset_filiados['resources']]

if not os.path.exists('dados'):
    print u'Criando diretório "dados"...'
    os.mkdir('dados')

for url in urls:
    filename = os.path.basename(urlparse.urlparse(url).path)
    if os.path.exists('dados/%s.csv' % filename.split('.')[0]):
        print u'Pulando arquivo existente: %s' % filename
        continue
    print u'Baixando a url %s' % url
    response = requests.get(url, stream=True)
    if response.ok:
        z = zipfile.ZipFile(io.BytesIO(response.content))
        # queremos apenas o arquivo csv, e nao queremos o sub judice
        planilhas = [name for name in z.namelist() if os.path.splitext(name)[-1] == '.csv' and not 'sub_jud' in name]
        if not planilhas:
            print u'Aviso: O arquivo %s não contém planilhas.' % filename
            # pula para a proxima url
            continue
        path_planilha = planilhas[0] # le a primeira planilha
        nome_planilha = os.path.basename(path_planilha)
        with z.open(path_planilha) as p, open('dados/%s' % nome_planilha, 'w') as f:
            print u'Gravando arquivo %s' % nome_planilha
            f.write(p.read())
    else:
        print 'ERRO: Código %d ao acessar a url.' % response.status_code

