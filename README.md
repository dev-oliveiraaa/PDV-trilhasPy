# (Desafio 01) Trilhas Back-end: Lógica de PDV em Python

## 📌 Sobre o projeto

Este projeto consiste no desenvolvimento de um sistema de **Ponto de Venda (PDV)** utilizando Python, como parte do Desafio 01 do Trilhas Back-end.

O sistema permite registrar compras, calcular descontos de acordo com as regras estabelecidas e armazenar um histórico resumido das operações realizadas.

## ⚙️ Funcionalidades

- **Registro de compras:** permite informar o valor de cada compra.
- **Desconto por idade:** aplica 20% de desconto para clientes com 65 anos ou mais.
- **Desconto por valor:** aplica 10% de desconto em compras acima de R$ 100,00.
- **Desconto por quantidade (Extra):** aplica 5% de desconto para compras com mais de 3 unidades.
- **Cupom de fidelidade (Extra):** aplica 10% de desconto adicional quando o cupom `FIDELIDADE10` é informado.
- **Validação de cupom (Extra):** exibe uma mensagem de erro caso o cupom informado seja inválido.
- **Histórico de compras (Extra):** registra um resumo das operações no arquivo `resumo.txt`.

## 🧪 Casos de teste concluídos

Os casos de teste abaixo foram executados para verificar os cálculos dos descontos por idade e por valor, conforme os resultados esperados.

| # | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
|---:|---:|---:|---:|---:|---:|
| 1 | 50,00 | 30 | 0% | 0% | R$ 50,00 |
| 2 | 100,00 | 30 | 0% | 0% | R$ 100,00 |
| 3 | 80,00 | 65 | 20% | 0% | R$ 64,00 |
| 4 | 100,00 | 70 | 20% | 0% | R$ 80,00 |
| 5 | 125,00 | 70 | 20% | 0% | R$ 100,00 |
| 6 | 200,00 | 30 | 0% | 10% | R$ 180,00 |
| 7 | 101,00 | 30 | 0% | 10% | R$ 90,90 |
| 8 | 200,00 | 65 | 20% | 10% | R$ 144,00 |
| 9 | 1.000,00 | 80 | 20% | 10% | R$ 720,00 |
| 10 | 200,00 | 64 | 0% | 10% | R$ 180,00 |

**Status:** casos de teste concluídos, com os resultados esperados registrados em `resumo.txt`.

## 🛠️ Tecnologias utilizadas

- **Python 3**
- Manipulação de listas
- Estruturas condicionais (`if` e `else`)
- Estruturas de repetição (`while` e `for`)
- Manipulação de arquivos com `open()`

## ▶️ Como executar

1. Certifique-se de ter o Python 3 instalado.
2. Clone este repositório:

   ```bash
   git clone https://github.com/dev-oliveiraaa/PDV-trilhasPy.git
   ```

3. Acesse a pasta do projeto:

   ```bash
   cd nivel_1
   ```

4. Execute o programa:

   ```bash
   python3 pdv.py
   ```

## 📂 Arquivos do projeto

- `pdv.py`: código-fonte do sistema de PDV.
- `resumo.txt`: arquivo gerado pelo programa para armazenar o resumo das compras e os resultados dos casos de teste.

---

**Projeto desenvolvido como parte do Desafio 01 — Trilhas Inova Back-end Python.**
