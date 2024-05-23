# -*- coding: utf-8 -*-
import re
import io
import os
import urlparse
import zipfile
import requests
import ckanapi

dadosgovbr = ckanapi.RemoteCKAN('http://dados.gov.br', user_agent='fatias/1.0 (+http://github.com/augusto-herrmann/fatias)')
dataset_filiados = dadosgovbr.action.package_show(id='servidores-do-executivo-federal')
urls = [resource['url'] for resource in dataset_filiados['resources']]

resource_url = ''
# recupera o ultimo recurso referente a servidores civis
for url in reversed(urls):
    # procura uma url com a query string &d=C
    civil_ou_militar = urlparse.parse_qs(urlparse.urlparse(url).query).get('d', u'')[0]
    if civil_ou_militar == u'C':
        resource_url = url
        break

if not os.path.exists('dados'):
    print (u'Criando diretório "dados"...'
    os.mkdir('dados'))

if not os.path.exists('dados/servidores'):
    print u'Criando diretório "dados/servidores"...'
    os.mkdir('dados/servidores')

print u'Baixando a url %s' % resource_url
response = requests.get(resource_url, stream=True)
if response.ok:
    filename = re.match('attachment;filename="([^"]+)"',response.headers['Content-Disposition']).groups()[0]
    print u"Descompactando %s" % filename
    z = zipfile.ZipFile(io.BytesIO(response.content))
    z.extractall(path='dados/servidores')

