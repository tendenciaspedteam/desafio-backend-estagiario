import unittest
import random
import time

# Certifique-se de que o caminho até a sua classe AnaliseNumerica está correto
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

    def teste_de_desempenho_insercao(self):
        analise = AnaliseNumerica()
        inicio_insercao = time.time()
        for _ in range(1000000):  # Corrigido para 1.000.000 inserções
            analise.addNum(random.randint(1, 10000))
        fim_insercao = time.time()
        tempo_insercao = fim_insercao - inicio_insercao
        print(f"Tempo de inserção para 1.000.000 elementos: {tempo_insercao:.2f} segundos.")
        # Ajuste a expectativa de desempenho conforme necessário
        self.assertTrue(tempo_insercao < 1, "Inserção deve ser eficiente para 1.000.000 de elementos.")

    def teste_de_desempenho_calculo_mediana(self):
        analise = AnaliseNumerica()
        # Prepara o cenário com 1.000.000 inserções
        for _ in range(1000000):
            analise.addNum(random.randint(1, 10000))

        inicio_mediana = time.time()
        _ = analise.findMedian()
        fim_mediana = time.time()
        tempo_mediana = fim_mediana - inicio_mediana
        print(f"Tempo para calcular a mediana: {tempo_mediana:.2f} segundos.")
        # Ajuste a expectativa de desempenho conforme necessário
        self.assertTrue(tempo_mediana < 1, "Cálculo da mediana deve ser rápido após 1.000.000 de inserções.")

if __name__ == '__main__':
    unittest.main()
