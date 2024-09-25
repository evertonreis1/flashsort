import time  # Biblioteca para medir o tempo de execuao

# Funcao FlashSort
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


# Exemplo de uso da funcao FlashSort
arr = [4, 2, 9, 6, 1, 8, 3, 7, 5]
start_time = time.time()
sorted_arr, swaps, comparisons = flash_sort(arr)
end_time = time.time()

print(f"Array Ordenado: {sorted_arr}")
print(f"Trocas: {swaps}, Comparacoes: {comparisons}")
print(f"Tempo de Execucao: {end_time - start_time:.6f} segundos")