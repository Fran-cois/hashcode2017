# /bin/python
import os

os.chdir("fichierIN/")

fichier_un = open("kittens.in", "r")
fichier_deux = open("me_at_the_zoo.in", "r")
fichier_trois = open("trending_today.in","r")
fichiers_quatre = open("videos_worth_spreading.in","r")
fichier = fichier_deux
first_line = fichier.readline() + " "
second_line = fichier.readline() + " "



def getSIMPLIER(s):
    j = 0
    ##str to int
    tab = []
    for i in range(len(s)):
        if current_endpoint[i] == " ":
            tab.append(int(s[j:i]))
            #print int(current_endpoint[j:i])
            j = i
    return tab




#print(fichier_un.readline())
#print(fichier_deux.readline())
#print(fichier_trois.readline())
#print(fichiers_quatre.readline())
#tableau du nb de chaque elmt du prob
elementsCardinal = []
videoTaille = []
j = 0

for i in range(len(first_line)):
    if first_line[i] == " ":
        elementsCardinal.append(int(first_line[j:i]))
        j = i

j = 0
for i in range(len(second_line)):
    if second_line[i] == " ":
        videoTaille.append(int(second_line[j:i]))
        j = i



#print len(videoTaille)
#print elementsCardinal

current_endpoint = fichier.readline() + " "
endpointS = []
endpoint_info = []
endpoint_n_cash_tab = []
j = 0
##str to int
for i in range(len(current_endpoint)):
    if current_endpoint[i] == " ":
        endpoint_info.append(int(current_endpoint[j:i]))
        #print int(current_endpoint[j:i])
        j = i
##
while(len(endpoint_info) == 2):
    
    endpoint_n_cash_tab.append(endpoint_info)
    for k in range(int(endpoint_info[1])):
        current_cash = []
        current_cash_line = fichier.readline() + " "
        j = 0
        #str to int
        for i in range(len(current_cash_line)):
            if current_cash_line[i] == " ":
                current_cash.append(int(current_cash_line[j:i]))
                j = i
        
        endpoint_n_cash_tab.append(current_cash)
                   
                   
                   
    endpointS.append(endpoint_n_cash_tab)
    endpoint_n_cash_tab= []
    #print endpointS
    endpoint_info = []
    j = 0
    current_endpoint = fichier.readline() + " "
    for i in range(len(current_endpoint)):
        if current_endpoint[i] == " ":
            endpoint_info.append(int(current_endpoint[j:i]))
            j = i





#print endpointS[0]


requestS = [endpoint_info]
## actualisation de current_endpoint
request_info_string = fichier.readline() + " "
current_request_tab =  getSIMPLIER(request_info_string)


while(len(current_request_tab) == 3):
    #print "test "
    requestS.append(current_request_tab)
    
    request_info_string = fichier.readline() + " "
    s = request_info_string
    #print request_info_string
    current_request_tab =[]
    j = 0
    if s != " ":
        for i in range(len(s)):
            if s[i] == " ":
                current_request_tab.append(int(s[j:i]))
                j = i

#print current_request_tab
#   print len(current_request_tab)

print requestS

    
    
    


T=[[]]
taille_cache=elementsCardinal[4]
TLine=[]

for(i in range(len(Request)):
    current_request=Request[i]
    matching_endpoint=enpoints[current_request[1]]
    
    for j in range(1,len(matching_endpoint[0][1])):
        temps_data=matching_endpoints[0][0]
        temps_cache=matching_endpoint[j][1]
        nb_request=current_request[2]
        taille_video=videoTaille[current_request[0]]
                
        a=(temps_data-temps_cache)*nb_request*taille_cache/taille_video
        TLine=[current_request[0],current_request[1],matching_endpoint[j][0],a,0]
        T.append[TLine]

T.sort(axis=3)
        
print(T)
        
        
        
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


	