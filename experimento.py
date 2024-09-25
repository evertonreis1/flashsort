import time  # Biblioteca para medir o tempo de execução
import numpy as np  # Biblioteca para gerar listas aleatórias e manipulações numéricas

# Função FlashSort
def flash_sort(arr):
    n = len(arr)
    m = int(0.43 * n)
    min_val = min(arr)
    max_val = max(arr)

    if min_val == max_val:
        return arr, 0, 0

    count = [0] * m

    for num in arr:
        k = int((m - 1) * (num - min_val) / (max_val - min_val))
        count[k] += 1

    for i in range(1, m):
        count[i] += count[i - 1]

    i = 0
    nmove = 0
    k = m - 1
    num_swaps = 0

    while nmove < n:
        while i >= count[k]:
            i += 1
            k = int((m - 1) * (arr[i] - min_val) / (max_val - min_val))

        flash = arr[i]
        while i != count[k]:
            k = int((m - 1) * (flash - min_val) / (max_val - min_val))
            count[k] -= 1
            arr[count[k]], flash = flash, arr[count[k]]
            num_swaps += 1
            nmove += 1

    num_comparisons = 0

    for i in range(1, n):
        j = i
        while j > 0:
            num_comparisons += 1
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break
            j -= 1

    return arr, num_swaps, num_comparisons

# Função para executar o experimento com diferentes disposições de listas
def run_experiment(sizes):
    repetitions = 10  # Número de repetições para calcular a média

    for size in sizes:
        # Listas para armazenar os resultados
        for order_type in ['Crescente', 'Decrescente', 'Aleatória']:
            total_time = 0
            total_swaps = 0
            total_comparisons = 0

            for _ in range(repetitions):
                if order_type == 'Crescente':
                    arr = list(range(size))
                elif order_type == 'Decrescente':
                    arr = list(range(size, 0, -1))
                else:  # Aleatória
                    arr = np.random.randint(0, size, size).tolist()

                start_time = time.time()
                _, swaps, comparisons = flash_sort(arr)
                end_time = time.time()

                total_time += (end_time - start_time)
                total_swaps += swaps
                total_comparisons += comparisons

            # Calcula a média
            avg_time = total_time / repetitions
            avg_swaps = total_swaps / repetitions
            avg_comparisons = total_comparisons / repetitions

            print(f"Tamanho: {size}, Ordem: {order_type}, Tempo Médio: {avg_time:.6f} segundos, "
                  f"Trocas Médias: {avg_swaps}, Comparações Médias: {avg_comparisons}")

# Tamanhos das listas para o experimento
sizes = [1000, 10000, 100000, 1000000]

# Executar o experimento com diferentes disposições de listas
run_experiment(sizes)
