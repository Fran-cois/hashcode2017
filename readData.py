# /bin/python
import os

os.chdir("fichierIN/")

fichier_un = open("kittens.in", "r")
fichier_deux = open("me_at_the_zoo.in", "r")
fichier_trois = open("trending_today.in","r")
fichiers_quatre = open("videos_worth_spreading.in","r")
fichier = fichier_un
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



## actualisation de current_endpoint
request_info_string = fichier.readline() + " "
request_info_tab =  getSIMPLIER(request_info_string)
print request_info




#while(len(endpoint_info) == 3):


    
    
    

fichier.close()
