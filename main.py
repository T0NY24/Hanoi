# Problema De Las torres de Hannoi

def TowerOfHanoi(n , source, destination, auxiliary):
	if n==1:
		print ("Mover el disco 1 desde la fuente",source,"A destino",destination)
		return
	TowerOfHanoi(n-1, source, auxiliary, destination)
	print ("Mover Disco",n,"de la fuente",source,"A destino",destination)
	TowerOfHanoi(n-1, auxiliary, destination, source)
		

n = 4
TowerOfHanoi(n,'A','B','C') 
# A, C, B are the name of rods


