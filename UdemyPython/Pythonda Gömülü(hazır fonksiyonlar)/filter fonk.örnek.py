#def ucgenmi(demet):
 #   if(demet[0]+demet[1]>demet[2]and demet[0]+demet[2]>demet[1]and demet[1]+demet[2]>demet[3]):
  #      return True
   # else:
     #   return False
#liste=[(3,4,5),(6,8,10),(3,10,7)]
#print(list(filter(ucgenmi,liste)))
def ucgenmi(demet):
    if(demet[0]+demet[1]>demet[2]and demet[0]+demet[2]>demet[1]and demet[1]+demet[2]>demet[0]):
        return True
    else:
        return False
liste=[(3,4,5),(6,8,10),(3,10,7)]
print(list(filter(ucgenmi,liste)))
