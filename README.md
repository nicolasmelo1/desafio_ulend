# desafio_ulend
Desafio para a vaga de Full-stack developer na Ulend


## Descrição
Na Ulend, um empréstimo para uma empresa pode ser financiado por diversos investidores.
As vezes, para totalizarmos um empréstimo de R$ 100.000,00, podemos ter investimentos de até 
50 investidores, dado que cada investidor pode investir a partir de R$ 2.000,00. 

## Teste
Dado a base de investimentos "json" e utilizando a linguaguem Python, crie lotes de investimentos que totalizem os valores 
de cada lote de empréstimo (loan) abaixo. Os Lotes não podem conter investimentos com o status 2

Empréstimo 147
    - Lote 1 R$ 226.000,00
    - Lote 2 R$ 164.000.00
Empréstimo 148
    - Lote 1 R$ 94.000,00
    - Lote 2 R$ 26.000,00

Exibir os investimentos na tela, separados por lotes, ordernados pelo campo uuid, conforme estrutura
abaixo:

--- 
Empréstimo 147
Lote 1 R$ 226.000,00
Investimento LsXfRsmEEeuY3WD4HcD05A
Investimento LsXfAMmEEeuY3WD4HcD05A
---
--- 
Empréstimo 148
Lote 1 R$ 94.000,00
Investimento LsXo4smEEeuY3WD4HcD05A
Investimento LsXrlMmEEeuY3WD4HcD05A
---

Assim que finalizado, enviar, via e-mail, o código criado.