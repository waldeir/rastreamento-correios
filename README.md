# Rastreamento Correios

## Rastreamento de encomendas a um comando de alcance

Este script simples serve para rastrear uma encomenda dos correios usando seu
código de rastreamento, imprimindo o resultado no terminal.

O comando pode ser usado com esta sintaxe:
```bash
./correios.py CÓDIGO_DE_RASTREAMENTO
```

Ele vai imprimir o caminho que o objeto fez até sua última localização atual, igual
aparece no site dos correios. O trabalho é feito usando esta
[API][correiosAPI].

Esse script requer o `python 3` e o `python-requests` para funcionar.


[correiosAPI]:https://github.com/chipytux/correiosApi 
