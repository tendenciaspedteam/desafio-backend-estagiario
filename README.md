<h1 align="center">
  <img alt="Logo" src="./doc/img/logo.png" alt="Logo Tendencias">
</h1>

<h1 align="center">Desafios de Backend</h1>
<p align = "center">Lista de desafios para o processo seletivo para estagiário de backend</p>

## Desafio 1: Implemente uma classe de análise numérica

### Problema

O objetivo deste desafio é implementar uma classe em Python chamada `AnaliseNumerica`. Esta classe será capaz de realizar operações básicas de análise em um conjunto de números, incluindo a adição de novos números ao conjunto e o cálculo da mediana, mantendo o conjunto de números sempre ordenado.

### Requisitos do Desafio

1. **Inicialização da Classe:**

   - A classe `AnaliseNumerica` deve ser inicializada com uma lista de números. Se nenhuma lista for fornecida no momento da inicialização, a classe deve começar com uma lista vazia.
   - A lista de números deve ser mantida ordenada em ordem crescente desde o início.

2. **Adicionar Números:**

   - Implemente um método `addNum` que recebe um número como parâmetro e adiciona esse número à lista de números da classe, garantindo que a lista continue ordenada após cada adição. **Importante:** Implemente sua própria função de ordenação para manter a lista ordenada, sem utilizar métodos de ordenação embutidos do Python (como `sort()` ou `sorted()`).

3. **Calcular Mediana:**

   - Implemente um método `findMedian` que retorna a mediana dos números na lista. A mediana é o valor que separa a metade maior da metade menor da lista. Se a lista for de tamanho par, a mediana deve ser a média dos dois números do meio. Se a lista estiver vazia, o método deve retornar `None`.

### Instruções para o Candidato

- Seu código deve ser escrito em Python.
- Assegure-se de que sua classe `AnaliseNumerica` atenda a todos os requisitos acima.
- Escreva seu código de forma clara e organizada. Comente seu código quando necessário para explicar a lógica utilizada.
- Após completar a implementação, inclua exemplos de uso da sua classe, demonstrando a adição de números e o cálculo da mediana, mantendo a lista de números ordenada sem utilizar métodos de ordenação embutidos.

#### Observações:

- **Otimização da Inserção:** Embora a inserção em uma lista ordenada possa ter uma complexidade de tempo $O(n)$devido à necessidade de deslocar elementos, é possível localizar a posição de inserção em $O(\log n)$.
- **Otimização do Cálculo da Mediana:** O cálculo da mediana pode ser otimizado para tempo constante $O(1)$ após cada inserção.

