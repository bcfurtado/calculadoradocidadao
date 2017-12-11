# Calculadora do Cidadão

## what's it?
It's restful wrapper for `Calculadora do Cidadão` [website](https://www3.bcb.gov.br/CALCIDADAO/jsp/index.jsp).

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

## how deploy
```sh
heroku login
heroku create
git push heroku master
```

## production
- https://calculadoradocidadao.herokuapp.com/

### production - how use
```sh
➜  Projects  curl https://calculadoradocidadao.herokuapp.com/corrigirpelaselic -d "dataInicial=30/09/2015" -d "dataFinal=05/12/2017" -d "valorCorrecao=2607,90" -X POST  | python -m json.tool
{
    "dataFinal": "05/12/2017",
    "dataInicial": "30/09/2015",
    "valorCorrecao": "2607,90",
    "valorCorrigido": "R$ 3.364,58 (REAL)"
}
```


## roadmap

| Endpoint                                   | Status  |
|--------------------------------------------|---------|
| Aplicação com depósitos regulares          | Pending |
| Financiamento com prestações fixas         | Pending |
| Valor futuro de um capital                 | Pending |
| Correção de valores > Índices de preços    | Pending |
| Correção de valores > TR                   | Pending |
| Correção de valores > Poupança             | Pending |
| Correção de valores > Selic                | Done    |
| Correção de valores > CDI                  | Pending |
| Cartão de Crédito: financiamento da fatura | Pending |
