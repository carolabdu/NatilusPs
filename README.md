# NatilusPs

Python Básico: 

Os problemas estão com a mesma numeração do slide com a explicação dp exercício

1. Para o primeiro exercício duas listas são recebidadas sepradamente. Depois disso apenas é feita uma comparação entre o primeir0 elemento das duas e o último elemento das duas. 

2. No segundo exercício é recebido um inteiro. No código fiz uma função que identifica se um número é primo testando se esse número é divisível por algum inteiro entre 2 e n**(1/2)+1. Com a função pronta fui testando em ordem descrescente o número, menor que n, que era primo, o primeiro que fosse achado, era o número pedido. 

3. No terceiro exercício é recebido um número inteiro (mas para facilitar ele é recebido como uma string). Depois é checado a sua quantidade de algarismos. Se ela for par são criadas duas fatias de tamanhos iguais: a primeira fatia tem a primeira metade dos algarismos e a segunda tem a outra metade, mas escrita na ordem inversa, caso essas fatias sejam iguais, o número é uma palíndromo. Caso a quantidade de algarismos seja ímpar é usado o mesmo raciocínio, mas é ignorado o algarismo 'central', pois ele não irá interferir no resultado. 

4. No exercício 4 foi usada a mesma função de verificar se é primo (exercício 2). Comecei com uma soma=0 , e depois testei cada número de 2 até 999, se fosse primo era somado com o resultado anterior. 
