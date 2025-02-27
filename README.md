Trabalho Individual 1 — Algoritmo de Karatsuba

Implementação do Algoritmo de Karatsuba em Python.

1. Descrição do Projeto

O Algoritmo de Karatsuba é um método eficiente para multiplicar números inteiros grandes. Desenvolvido por Anatolii Karatsuba na década de 1960, ele reduz a complexidade da multiplicação tradicional de O(n²) para aproximadamente O(n^1.585), tornando-se mais rápido para números de muitos dígitos.

1.1 Objetivos

Implementar o Algoritmo de Karatsuba em Python (arquivo main.py).
Permitir a inserção de dois números inteiros pelo usuário.
Apresentar o resultado da multiplicação no terminal.
Gerar diagramas de fluxo para visualização do processo (códigos em Python com Graphviz).
Documentar de forma clara o funcionamento e as análises do algoritmo.

2. Como Executar o Projeto

2.1 Pré-Requisitos

Python 3 instalado (versão 3.7 ou superior).
Sistema operacional Linux, Windows ou macOS.
Acesso ao terminal (ou prompt de comando).
(Opcional) Graphviz para gerar diagramas.

2.2 Passo a Passo de Execução

Clonar o Repositório:

git clone https://github.com/MF300175/trabalho_individual_1_FPAA.git
cd trabalho_individual_1_FPAA
Executar o Código Principal (Karatsuba):
Arquivo main.py contém o Algoritmo de Karatsuba e solicita dois números do usuário:
python main.py

Exemplo de execução:

Digite o primeiro número: 12345678
Digite o segundo número: 87654321
O resultado da multiplicação de 1234 por 5678 é: 1082152022374638

Gerar Diagrama de Fluxo (Genérico):

Arquivo karatsuba_diagram.py gera um diagrama estático (sem input do usuário) ilustrando o fluxo.

Execute:

python karatsuba_diagram.py
Isso criará um arquivo PNG (por exemplo, Karatsuba_Fluxogram.png).
Abra-o no Windows (se estiver usando WSL) com:
explorer.exe "$(wslpath -w Karatsuba_Fluxogram.png)"

Gerar Diagrama de Fluxo (Dinâmico):

Arquivo karatsuba_diagram_dinamic.py solicita valores de x e y do usuário e os injeta no diagrama.
Execute:
python karatsuba_diagram_dinamic.py
Responda aos inputs:

Digite o valor de x: 123456789
Digite o valor de y: 987654321
Fluxograma gerado: Karatsuba_Fluxogram_Dinamico.png

Abra o arquivo PNG gerado no seu sistema.

3. Lógica do Algoritmo (Passo a Passo)

Caso Base: Se um dos números tiver apenas 1 dígito (x < 10 or y < 10), retorna x * y diretamente.
Divisão: Se ambos são grandes, dividimos cada número em duas partes: high e low.

Recursão:

z0 = karatsuba(x_low, y_low)
z1 = karatsuba((x_low + x_high), (y_low + y_high))
z2 = karatsuba(x_high, y_high)

Combinação:

resultado = z2 * 10^(2*m) + (z1 - z2 - z0) * 10^m + z0

4. Relatório Técnico

4.1 Análise da Complexidade Ciclomática

Grafo de fluxo:

Representa o fluxo de controle do algoritmo com nós e arestas.

Fórmula:

M = E - N + 2P
E: Número de arestas
N: Número de nós
P: Número de componentes conexos (em geral, 1)

Exemplo de Cálculo (ilustrativo)

Suponha que o fluxograma tenha 9 nós e 10 arestas:

M = 10 - 9 + 2*1 = 3

### 4.2 Análise da Complexidade Assintótica

- **Tempo**: O algoritmo Karatsuba roda em aproximadamente \\(O(n^{1.585})\\).  
  Para ilustrar, considere os números **12345678** e **87654321**, cada um com **8 dígitos**.  
  Se definirmos \\(n = 8\\), temos:
  \\[
    O(n^{1.585}) = O(8^{1.585}) \\approx O(25.3)
  \\]
  enquanto a **multiplicação tradicional** teria \\(O(n^2) = O(64)\\).  
  Assim, o Karatsuba requer **menos operações** que o método tradicional para esses 8 dígitos.

- **Espaço**: O armazenamento de chamadas recursivas e strings para conversão ficam em \\(O(n)\\).  
  No exemplo com 8 dígitos, \\(O(8)\\) é modesto, mas conforme \\(n\\) cresce, esse custo aumenta linearmente.

#### Melhores, Médios e Piores Casos

- **Melhor caso**: Quando um dos números é pequeno (1 dígito). Complexidade \\(O(1)\\).  
- **Caso médio/pior caso**: Números de \\(n\\) dígitos, com múltiplas chamadas recursivas, resultando em \\(O(n^{1.585})\\). Para \\(n = 8\\), estimamos \\(\\sim25\\) unidades de operação, enquanto o método tradicional (\\(O(n^2)\\)) levaria \\(64\\).

5. Diagrama de Fluxo

Abaixo, um diagrama que ilustra o fluxo do algoritmo (exemplo genérico):

![Fluxo Karatsuba](./Karatsuba_Fluxogram.png)

Para gerar um diagrama dinâmico usando valores de x e y, use o arquivo karatsuba_diagram_dinamic.py.

6. Observações Finais

O algoritmo de Karatsuba traz ganhos significativos para números grandes em comparação à multiplicação tradicional.
Recomenda-se testar com diferentes valores para validar a performance.

7. Referências

Repositório Exemplo: https://github.com/joaopauloaramuni/fundamentos-de-projeto-e-analise-de-algoritmos/tree/main/PROJETOS
Aula e PDF de Complexidade: https://github.com/joaopauloaramuni/fundamentos-de-projeto-e-analise-de-algoritmos/tree/main/PDF
Karatsuba (1960): Método de multiplicação de inteiros grandes.

8. Licença

Este projeto está licenciado sob a MIT License.