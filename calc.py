
while True:
# Coletar os números que o usuário deseja utilizar
	num1 = float(input("digite por favor o primeiro número:  "))
	num2 = float(input("agora digite o segundo número:  "))

# Operções alvo
	soma = num1 + num2
	subtracao = num1 - num2
	multiplicacao = num1 * num2
	divisao = num1 / num2
#Solicitar a operação desejada pelo usuário
	print("\nSelecione a opção desejada")
	print("1. soma")
	print("2. subtração")
	print("3. multiplicação")
	print("4. divisão")
	print("5. sair")
	escolha = input("Digite sua escolha (1/2/3/4/5): ")

	if escolha not in ['1', '2', '3', '4', '5']:
		print('Opção inválida! Por favor, escolha uma opção válida')
		num1 = (input('digite por favor o primeiro número:'))
		num2 = (input('agora digite o segundo número: '))

	if escolha == '1':
		resultado = num1 + num2
		operacao = 'soma'
	elif escolha == '2':
		resultado = num1 - num2
		operacao = 'subtração'
	elif escolha == '3':
		resultado = num1 * num2
		operacao = 'multiplicação'
	elif escolha == '4':
		if num2 == 0:
		  print('Erro. Divisão por zero não permitida!')
		resultado = num1 / num2
		operacao = 'divisão'
# Exibir o resultadoda operação escolhida
	print(f'O resultado da {operacao} é: {resultado}\n')
