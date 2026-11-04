# log-parser

A solução foi desenvolvida em Python 3 (somente biblioteca padrão).

O script lê o arquivo de log e exibe:

- as 3 URLs (`request_to`) mais chamadas;
- os 3 status de resposta (`response_status`) mais frequentes.

## Executar

```
python3 log.py            # usa log.txt
python3 log.py outro.log  # ou informe outro arquivo
```

Saída esperada para o `log.txt` incluído:

```
Top 3 URLs:
https://eagerhaystack.com - 750
https://surrealostrich.com.br - 734
https://grimpottery.net.br - 732

Top 3 status codes:
404 - 1474
503 - 1451
400 - 1440
```

## Testes

```
python3 -m unittest
```
