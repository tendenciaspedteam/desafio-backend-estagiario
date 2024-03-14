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
        lista_grande = [random.randint(1, 1000) for _ in range(1002)]
        analise = AnaliseNumerica(lista_grande)
        lista_grande_ordenada = sorted(lista_grande)
        mediana_esperada = (lista_grande_ordenada[500] + lista_grande_ordenada[501]) / 2
        self.assertEqual(analise.findMedian(), mediana_esperada, "A mediana de uma lista grande deve ser calculada corretamente.")

    # Testes de Desempenho
    def test_desempenho_insercao(self):
        analise = AnaliseNumerica()
        inicio = time.time()
        for _ in range(1000000):  # 1 milhão de inserções
            analise.addNum(random.randint(1, 10000))
        fim = time.time()
        print("Tempo de inserção para 1.000.000 elementos:", fim - inicio)
        # Ajuste este limite conforme a eficiência esperada e a capacidade do seu sistema
        self.assertTrue(fim - inicio < 60, "Inserção deve ser eficiente para 1.000.000 de elementos.")

    def test_desempenho_mediana(self):
        analise = AnaliseNumerica([random.randint(1, 10000) for _ in range(1000000)])  # 1 milhão de elementos
        inicio = time.time()
        _ = analise.findMedian()
        fim = time.time()
        print("Tempo para calcular a mediana:", fim - inicio)
        self.assertTrue(fim - inicio < 1, "Cálculo da mediana deve ser eficiente para 1.000.000 de elementos.")
        
    def test_desempenho_insercao_e_mediana(self):
        analise = AnaliseNumerica()
        numero_elementos = 100000  # Número reduzido para balancear complexidade e tempo de execução
        numeros_aleatorios = [random.randint(1, 10000) for _ in range(numero_elementos)]
        
        # Testa a inserção
        inicio_insercao = time.time()
        for num in numeros_aleatorios:
            analise.addNum(num)
        fim_insercao = time.time()
        tempo_insercao = fim_insercao - inicio_insercao
        
        # Testa o cálculo da mediana
        inicio_mediana = time.time()
        mediana = analise.findMedian()
        fim_mediana = time.time()
        tempo_mediana = fim_mediana - inicio_mediana

        print(f"Tempo de inserção para {numero_elementos} elementos: {tempo_insercao} segundos.")
        print(f"Tempo para calcular a mediana: {tempo_mediana} segundos.")
        
        # Verificações
        # Ajuste esses limites conforme a eficiência esperada e a capacidade do seu sistema
        self.assertTrue(tempo_insercao < 30, "Inserção deve ser eficiente para o número de elementos.")
        self.assertTrue(tempo_mediana < 1, "Cálculo da mediana deve ser eficiente após inserções.")

if __name__ == '__main__':
    unittest.main()
