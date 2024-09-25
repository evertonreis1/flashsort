# Experimento sobre Algoritmos de Ordenação: Análise do FlashSort

Autor: Everton Reis de Souza  
Instituição: Universidade Federal de Alagoas - Campus Arapiraca  
Endereço: Av. Manoel Severino Barbosa - Bom Sucesso, Arapiraca - AL, 57309-005  
E-mail: everton.reis@arapiraca.ufal.br

## Resumo
Este trabalho apresenta um experimento sobre o algoritmo de ordenação FlashSort, analisando seu desempenho em termos de tempo de execução e número de operações realizadas. O estudo avalia diferentes condições iniciais dos dados e tamanhos variados de conjuntos, executado em um ambiente de computação local. Os resultados obtidos demonstram a eficiência do FlashSort em comparação com algoritmos de ordenação tradicionais, destacando suas vantagens e limitações.

## 1. Introdução
A ordenação de dados é uma operação fundamental em diversas áreas da computação, impactando diretamente a eficiência de algoritmos subsequentes e a performance de sistemas. Com o crescimento exponencial dos dados gerados diariamente, a escolha do algoritmo de ordenação adequado torna-se crucial para otimizar recursos computacionais e reduzir tempos de processamento.

Entre os algoritmos de ordenação, existem aqueles que são amplamente utilizados devido à sua eficiência comprovada, como QuickSort, MergeSort e HeapSort. No entanto, também existem algoritmos que apresentam abordagens diferentes para a ordenação de dados, explorando paradigmas alternativos e oferecendo vantagens específicas em determinados cenários. O FlashSort é um desses algoritmos, conhecido por sua eficiência em tempo de execução para conjuntos de dados com distribuição uniforme.

Este trabalho visa analisar o desempenho do FlashSort em diferentes cenários, destacando suas vantagens e limitações em comparação com algoritmos de ordenação mais tradicionais. Além disso, o estudo reforça a importância da compreensão da complexidade algorítmica e da escolha adequada de métodos de ordenação conforme os requisitos de desempenho.

## 2. Fundamentação

### 2.1. Paradigma
O FlashSort segue o paradigma de distribuição (distribution-based), combinando técnicas de classificação por distribuição com características de ordenação in-place. O algoritmo divide o conjunto de dados em classes (bins) baseadas na distribuição dos valores, permitindo uma ordenação eficiente ao restringir a operação de permutação a segmentos específicos da lista. Esta abordagem reduz significativamente o número de comparações necessárias, especialmente para conjuntos de dados com distribuição uniforme.

### 2.2. Ordenação Interna/Externa
O FlashSort é um algoritmo de ordenação interna, operando diretamente na memória principal. Ele é projetado para ser eficiente em termos de uso de memória, utilizando espaço adicional mínimo além da lista original para armazenar índices e contadores de classes. Devido à sua eficiência e baixo uso de memória, o FlashSort é adequado para conjuntos de dados que cabem na memória RAM disponível, sendo especialmente eficaz para grandes volumes de dados com distribuição uniforme.

### 2.3. Algoritmo In-place
O FlashSort é um algoritmo in-place, pois realiza a ordenação diretamente na lista original sem a necessidade de estruturas de dados auxiliares significativas. A única memória extra utilizada é para armazenar índices e contadores de classes durante o processo de distribuição. Esta característica torna o FlashSort preferível em ambientes com restrições de memória, permitindo a ordenação de grandes conjuntos de dados sem a necessidade de alocação adicional significativa.

### 2.4. Estabilidade
O FlashSort não é um algoritmo estável, ou seja, ele pode alterar a ordem relativa de elementos iguais durante o processo de distribuição e permutação. Embora a estabilidade não seja uma exigência em todas as aplicações, ela pode ser importante em cenários onde a ordem original dos elementos possui significado semântico. A falta de estabilidade no FlashSort é uma das suas limitações, especialmente em aplicações que requerem preservação da ordem original de elementos iguais.

### 2.5. Recorrência do Algoritmo
A complexidade temporal do FlashSort é considerada linear (O(n)) para conjuntos de dados com distribuição uniforme, o que o torna altamente eficiente para grandes volumes de dados. No entanto, sua complexidade pode degradar para O(n²) em casos de distribuição não uniforme, onde o número de classes não está bem balanceado.

## 3. Implementação do FlashSort
Nesta seção, o algoritmo FlashSort foi implementado em Python e utilizado nos experimentos.

## 4. Método do Experimento

### 4.1. Disposição Prévia dos Algoritmos nas Ordens
O experimento foi conduzido aplicando o *FlashSort* em três tipos de ordenação inicial dos dados:

1. Ordem 1: Crescente – Dados já ordenados em ordem crescente.
2. Ordem 2: Decrescente – Dados ordenados em ordem decrescente.
3. Ordem 3: Desordenado – Dados gerados de forma aleatória.

### 4.2. Tamanhos dos Dados
Os tamanhos dos conjuntos de dados foram escolhidos para avaliar a escalabilidade do FlashSort, considerando a sua complexidade linear para distribuições uniformes:

- 1.000 elementos
- 10.000 elementos
- 100.000 elementos
- 1.000.000 elementos

### 4.3. Parâmetros de Avaliação
Os seguintes parâmetros foram medidos para cada execução do algoritmo:

- **Tempo médio de execução**: Medido em milissegundos, representando o tempo total médio gasto pelo algoritmo para ordenar o conjunto de dados.
- **Trocas médias**: Contagem média de trocas realizadas durante o processo de ordenação.
- **Comparações médias**: Contagem média de comparações realizadas durante o processo de ordenação.

### 4.4. Especificação do Ambiente do Experimento
Os experimentos foram executados localmente em um computador pessoal, com a seguinte configuração:

- Processador: AMD Ryzen 5 3500U @2.10 GHz
- Memória RAM: 8 GB
- Sistema Operacional: Windows
- Linguagem de Programação: Python 3.12.4

### 4.5. Procedimento Experimental
Para cada tamanho de conjunto de dados e cada tipo de ordenação inicial, o experimento foi conduzido da seguinte forma:

1. **Preparação dos Dados**: Para cada tamanho de lista especificado, três tipos de listas foram criadas: Crescente, Decrescente ou Desordenado.
2. **Execução do FlashSort**: Aplicar o algoritmo FlashSort à lista e medir o tempo de execução, o número de trocas (swaps) e comparações.
3. **Repetição**: Para cada combinação de tamanho de lista e tipo de ordenação (Crescente, Decrescente e Aleatória), a execução foi realizada apenas uma vez.
4. **Registro dos Resultados**: Os resultados foram impressos na tela com as seguintes informações para cada combinação de tamanho e tipo de lista: Tamanho da lista, tipo de ordenação inicial, tempo de execução em segundos, número de trocas realizadas e comparações.

## 5. Resultados e Análises

### 5.1. Tabela Geral
A tabela apresenta os resultados do experimento que avalia o desempenho do algoritmo FlashSort em listas de diferentes tamanhos organizadas em três ordens distintas: crescente, decrescente e aleatória.
![Dados](https://github.com/evertonreis1/flashsort/blob/main/dadosLATEX.png?raw=true "Imagem dos Dados em LaTeX")


### 5.2. Análise dos Resultados
Os resultados indicam que o FlashSort possui uma complexidade temporal O(n) para conjuntos de dados com distribuição uniforme, o que o torna altamente eficiente para grandes volumes de dados. Observa-se que o tempo de execução cresce linearmente com o aumento do número de elementos, corroborando a análise teórica da complexidade do algoritmo.

### 5.2.1. Comparação com Algoritmos Tradicionais
Ao comparar o FlashSort com algoritmos tradicionais como QuickSort, MergeSort e HeapSort, observa-se que o FlashSort pode superar esses algoritmos em termos de tempo de execução para grandes conjuntos de dados com distribuição uniforme.

### 5.2.2. Impacto das Condições Iniciais
As condições iniciais dos dados (Crescente, Decrescente ou Desordenado) não influenciam significativamente o desempenho do FlashSort, desde que a distribuição dos dados permaneça uniforme.

### 5.2.3. Limitações do FlashSort
Embora o FlashSort seja altamente eficiente para conjuntos de dados com distribuição uniforme, sua eficiência pode diminuir para distribuições não uniformes. Além disso, a falta de estabilidade pode ser uma limitação em cenários onde a ordem relativa de elementos iguais é importante.

## 6. Considerações Finais
O experimento realizado evidencia que o FlashSort é altamente eficiente para a ordenação de grandes conjuntos de dados com distribuição uniforme devido à sua complexidade temporal O(n). Comparado com algoritmos de ordenação tradicionais como QuickSort e MergeSort, o FlashSort apresenta vantagens significativas em cenários específicos, permitindo uma ordenação mais rápida e eficiente.

No entanto, o FlashSort possui limitações, como a dependência da distribuição uniforme dos dados e a falta de estabilidade, o que pode restringir sua aplicabilidade em certos contextos onde essas características são importantes. Além disso, para distribuições não uniformes, a eficiência do FlashSort pode ser comprometida, tornando-o menos vantajoso em comparação com algoritmos mais robustos.

Este estudo reforça a importância da compreensão das características e complexidades dos algoritmos de ordenação, destacando a necessidade de escolher o algoritmo adequado conforme os requisitos específicos de desempenho e distribuição dos dados. Futuras pesquisas poderão explorar a implementação de variações do FlashSort que busquem mitigar suas limitações, bem como comparar seu desempenho em diferentes ambientes computacionais e com diferentes distribuições de dados.

## 7. Referências
1. Knuth, D. E. (1998). The Art of Computer Programming, Volume 3: Sorting and Searching. Addison-Wesley.
2. Neubert, Karl-Dietrich. Flash-Sort: Classificação por permutação in situ. euroFORTH.
3. Nilsson, Martin; Tanaka, Hidehiko. Rumo a um Flashsort Realizável. pp. 261-264, 1988.
4. Blelloch, Guy E. et al. Uma comparação de algoritmos de classificação para a máquina de conexão CM-2. Em: Anais do terceiro simpósio anual da ACM sobre algoritmos e arquiteturas paralelas, 1991. pp. 3-16.
