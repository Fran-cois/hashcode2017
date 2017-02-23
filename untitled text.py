V

C

T

##
"initialise C"

C=[taille_cache for i in range(nb_cache)]


##

R=[[] for i in range (nb_cache)]
for i in range(nb_poss):
	if ((C[T[i][2]]> V[T[i][0]]) and (T[T[i][4]]==0)):
		R[T[i][2]].append(T[i][0])
		T[i][4]=1
		for k in range(i+1,nb_poss):
			if ((T[i][0]==T[k][0] and T[i][1]==T[k][1]) or (T[i][0]==T[k][0] and T[i][2]==T[k][2])):
				T[i][4]==1
##
"on calcule l"
l=0
for i in range(nb_cache):
	if len(R[i])>1:
		l+=1
##
"on, cree le fichier".
l=4
f=open('test.txt','w')
f.write(str(l)+" \n")
for i in range(len(R)):
	if (len(R[i])>1):
		for j in range(1,len(R[i])):
			f.write(str(R[i][j]+" ")
		f.write("\n")

	
##
