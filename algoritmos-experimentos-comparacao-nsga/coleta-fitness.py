import os
a = 0
b = 0
caminho = os.path.expanduser('~/Documentos/mestrado/disciplina-topicos/coleta/NSGA-II-AGM1-ACLASS-COE-CM-FM-EXT-ELEG/1/')
caminhoarquivo = caminho + 'fitness.txt'

conc = []
pastas = []
pastas = os.listdir(str(caminho))

for i in pastas:
	posicao = pastas[b-1]	
	hy = open(str(caminho) + str(posicao) +'/fitness/fitness.txt', 'r')
	conc.append(hy.readlines())
	b = b+1
	hy.close()	

criar = open(str(caminhoarquivo), 'w')
criar.close()
for j in conc:
	semilista = j
	r = open(str(caminhoarquivo), 'r')
	texto = r.readlines()	
	texto.append('\n')	
	arquivo = open(str(caminhoarquivo), 'w')
	arquivo.writelines(texto)
	arquivo.close()
	for k in semilista:
		 r = open(str(caminhoarquivo), 'r')
		 texto = r.readlines()	
		 texto.append(str(k))	
		 arquivo = open(str(caminhoarquivo), 'w')
		 arquivo.writelines(texto)
		 arquivo.close()	
