import ckanapi

dadosgovbr = ckanapi.RemoteCKAN('http://dados.gov.br', user_agent='fatias/1.0 (+http://github.com/augusto-herrmann/fatias)')

dataset_filiados = dadosgovbr.action.package_show(id='filiados-partidos-politicos')
