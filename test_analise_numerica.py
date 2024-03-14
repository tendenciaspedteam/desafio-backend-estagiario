import unittest
import random
import time

from analiseNumerica import AnaliseNumerica


class TestAnaliseNumerica(unittest.TestCase):

    def test_lista_vazia(self):
        analise = AnaliseNumerica()
        self.assertIsNone(analise.findMedian(), "A mediana de uma lista vazia deve ser None.")

    def test_lista_um_elemento(self):
        analise = AnaliseNumerica()
        analise.addNum(5)
        self.assertEqual(analise.findMedian(), 5, "A mediana de uma lista com um elemento deve ser o elemento.")

    def test_lista_dois_elementos(self):
        analise = AnaliseNumerica()
        analise.addNum(5)
        analise.addNum(2)
        self.assertEqual(analise.findMedian(), 3.5, "A mediana de uma lista com dois elementos deve ser a média deles.")

    def test_adicionar_elementos_mantem_ordem(self):
        analise = AnaliseNumerica()
        analise.addNum(10)
        analise.addNum(1)
        analise.addNum(100)
        self.assertEqual(analise.findMedian(), 10, "A mediana após adicionar elementos deve ser correta.")

    def test_lista_grande_aleatoria(self):
        analise = AnaliseNumerica()
        lista_grande = [random.randint(1, 1000) for _ in range(1002)]
        for num in lista_grande:
            analise.addNum(num)
        lista_grande_ordenada = sorted(lista_grande)
        mediana_esperada = (lista_grande_ordenada[500] + lista_grande_ordenada[501]) / 2
        self.assertEqual(analise.findMedian(), mediana_esperada, "A mediana de uma lista grande deve ser calculada corretamente.")

    # Testes de Desempenho adaptados para serem mais realistas
    def test_desempenho(self):
        analise = AnaliseNumerica()
        inicio = time.time()
        for _ in range(10000):  # Reduzido para 10.000 inserções para teste mais rápido
            analise.addNum(random.randint(1, 10000))
        fim = time.time()
        print("Tempo de inserção para 10.000 elementos:", fim - inicio)
        self.assertLess(fim - inicio, 1, "Inserção deve ser eficiente para 10.000 de elementos.")

if __name__ == '__main__':
    unittest.main()
