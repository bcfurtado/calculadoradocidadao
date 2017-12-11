# calculadora do cidadao

## requirements
- python >= 3.6

## install
```sh
mkvirtualenv calculadoradocidadao -p $(which python3)
pip install -r requirements.txt
```

## how use
```sh
curl http://localhost:5000/corrigirpelaselic -d "dataInicial=30/09/2015" -d "dataFinal=05/12/2017" -d "valorCorrecao=2607,90" -X POST -v
```
