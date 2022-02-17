# Calculadora do Cidadão

[![Build Status](https://travis-ci.org/bcfurtado/calculadoradocidadao.svg?branch=master)](https://travis-ci.org/bcfurtado/calculadoradocidadao)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fbcfurtado%2Fcalculadoradocidadao.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fbcfurtado%2Fcalculadoradocidadao?ref=badge_shield)

## what's it?
It's restful wrapper for `Calculadora do Cidadão` [website](https://www3.bcb.gov.br/CALCIDADAO/jsp/index.jsp).

## requirements
- python >= 3.10
- poetry

## install
```sh
poetry install
pre-commit
make tests
```

## how use
```sh
curl http://localhost:5000/corrigirpelaselic -d "dataInicial=30/09/2015" -d "dataFinal=05/12/2017" -d "valorCorrecao=2607,90" -X POST -v
```

## production
- https://calculadoradocidadao.herokuapp.com/

### production - how use
```sh
➜ curl https://calculadoradocidadao.herokuapp.com/corrigirpelaselic -d "dataInicial=30/09/2015" -d "dataFinal=05/12/2017" -d "valorCorrecao=2607,90" -X POST  | python -m json.tool
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


## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fbcfurtado%2Fcalculadoradocidadao.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fbcfurtado%2Fcalculadoradocidadao?ref=badge_large)