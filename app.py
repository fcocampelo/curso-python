# python/app.py
# -*- coding: UTF-8 -*-
def cadastrar(nomes):
	print 'Digite: o nome:'
	nome = raw_input()
	nomes.append(nome)

def listar(nomes):
	print 'Listando nomes:'
	for nome in nomes:
		print nome

def remover(nomes):
	print 'Qual nome voce gostaria de remover'
	nome_remover = raw_input()
	nomes.remove(nome_remover)

def menu():
	nomes = [] #nao podemos esquecer de inicializar a lista
	escolha = ''
	while(escolha != '0'):    
		print 'Digite: 1 para cadastrar, 2 para listar, 3 para remover nome, 0 para terminar'
		escolha = raw_input()
		if(escolha == '1'):
			cadastrar(nomes)

		if(escolha == '2'):
			listar(nomes) 

		if(escolha == '3'):
			remover(nomes)
			
menu()