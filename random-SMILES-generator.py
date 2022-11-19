import numpy as np
import random
import pubchempy as pcp


#Generating a random list of numbers later used as PubChem compound identifiers (CID).
random_numbers = random.sample(range(1,112406991),5000) #generating 5000 random numbers between 1 and 112406991 (number of Compounds on PubChem)
#print(random_numbers)

#Generating the list of SMILES through the previusly generated numbers
list_of_smiles = [] # opening an empty list

#The corresponding smiles is searched for every element in 'cid_list'
for x in random_numbers: 
    cid_list = pcp.Compound.from_cid(x) #eEements in 'random_numbers' are transferred to CIDs
    list_of_smiles.append (cid_list.isomeric_smiles) #CIDs are transferred to SMILES
    #print (len(list_of_smiles) #Just if the progress should be shown

#Creating a file with the generated SMILES
np.savetxt("List_of_SMILES.CSV", list_of_smiles, delimiter = ', ', fmt = '% s') #saving the SMILES in a CSV-file
