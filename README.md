# Rastreamento Correios

Esse script simples serve para rastrear uma encomenda usando seu código de
rastreamento.

O comando pode ser usado com essa sintaxe:
```bash
./correios.py CODIGO_DE_RASTREAMENTO
```

Ele vai imprimir o caminho que o objeto fez até sua última localização, igual
aparece no site dos correios. O trabalho é feito usando esta
[API][correiosAPI].

Esse script requer o `python 3` e o `python-requests` para funcionar.


[correiosAPI]:https://github.com/chipytux/correiosApi 
