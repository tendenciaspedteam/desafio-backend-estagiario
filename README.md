<h1 align="center">
  <img alt="Logo" src="./doc/img/logo.png" alt="Logo Tendencias">
</h1>

<h1 align="center">Desafios de Backend</h1>
<p align = "center">Lista de desafios para o processo seletivo para estagiário de backend</p>

## Desafio 1: Encontre a Mediana

### Problema

A mediana é o valor do meio em uma lista ordenada de inteiros. Se o tamanho da lista for par, não há um valor do meio, e a mediana é a média dos dois valores do meio.

- Por exemplo, para `arr = [2,3,4]`, a mediana é `3`.
- Por exemplo, para `arr = [2,3]`, a mediana é `(2 + 3) / 2 = 2,5`.

Implemente a classe `MedianFinder`:

- `MedianFinder()` inicializa o objeto `MedianFinder`.
- `void addNum(int num)` adiciona o inteiro `num` do fluxo de dados à estrutura de dados.
- `double findMedian()` retorna a mediana de todos os elementos até o momento. Respostas dentro de 10^-5 da resposta real serão aceitas.

**Exemplo 1:**

Entrada
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Saída
[null, null, null, 1.5, null, 2.0]

Explicação:

MedianFinder medianFinder = new MedianFinder();

medianFinder.addNum(1); // arr = [1]

medianFinder.addNum(2); // arr = [1, 2]

medianFinder.findMedian(); // retorna 1.5 (ou seja, (1 + 2) / 2)

medianFinder.addNum(3); // arr = [1, 2, 3]

medianFinder.findMedian(); // retorna 2.0


**Restrições:**

- `-10^5 <= num <= 10^5`
- Haverá pelo menos um elemento na estrutura de dados antes de chamar `findMedian`.
- No máximo 5 * 10^4 chamadas serão feitas para `addNum` e `findMedian`.
