import unittest
import random
import time

from analiseNumerica import AnaliseNumerica


class TestAnaliseNumerica(unittest.TestCase):

    def test_lista_vazia(self):
        analise = AnaliseNumerica()
        self.assertIsNone(analise.findMedian(), "A mediana de uma lista vazia deve ser None.")

    def test_lista_um_elemento(self):
        analise = AnaliseNumerica([5])
        self.assertEqual(analise.findMedian(), 5, "A mediana de uma lista com um elemento deve ser o elemento.")

    def test_lista_dois_elementos(self):
        analise = AnaliseNumerica([5, 2])
        self.assertEqual(analise.findMedian(), 3.5, "A mediana de uma lista com dois elementos deve ser a média deles.")

    def test_adicionar_elementos_mantem_ordem(self):
        analise = AnaliseNumerica([10])
        analise.addNum(1)
        analise.addNum(100)
        self.assertEqual(analise.findMedian(), 10, "A mediana após adicionar elementos deve ser correta.")

    def test_lista_grande_aleatoria(self):
        lista_grande = [random.randint(1, 1000) for _ in range(1001)]
        analise = AnaliseNumerica(lista_grande)
        lista_grande_ordenada = sorted(lista_grande)
        mediana_esperada = (lista_grande_ordenada[500] + lista_grande_ordenada[501]) / 2
        self.assertEqual(analise.findMedian(), mediana_esperada, "A mediana de uma lista grande deve ser calculada corretamente.")

    # Testes de Desempenho
    def test_desempenho_insercao(self):
        analise = AnaliseNumerica()
        inicio = time.time()
        for _ in range(10000):
            analise.addNum(random.randint(1, 1000))
        fim = time.time()
        self.assertTrue(fim - inicio < 5, "Inserção deve ser eficiente para 10000 elementos.")

    def test_desempenho_mediana(self):
        analise = AnaliseNumerica([random.randint(1, 1000) for _ in range(10000)])
        inicio = time.time()
        _ = analise.findMedian()
        fim = time.time()
        self.assertTrue(fim - inicio < 1, "Cálculo da mediana deve ser eficiente para 10000 elementos.")

if __name__ == '__main__':
    unittest.main()
