#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 14:02:38 2018

@author: clemonnier
"""

def letters_freq(my_string):
    """Paramètres passés en mode donnée: s
Paramètres passés en mode donnée/résultat: [aucun]
Paramètres passés en mode résultat: [aucun]
Préconditions: s est une chaîne de caractères
Postconditions: [aucune]
Résultat: un tableau associatif donnant le nombre d'occurrences de chaque caractère dans s
Variables locales : d, un tableau associatif ; c, un caractère"""
    dic={}##ou d=dict()
    for char in my_string:
        if char in dic:#ou dic.keys
            dic[char]=int(dic[char])+1
        else:
            dic[char]=1
    return dic

#Création du dictionnaire des mots du texte avec la valeur de leur occurrence dans le texte
"""
  Parameters passed in data mode: text
  Parameters passed in data/result mode: [none]
  Parameters passed in result mode: [none]
  Preconditions: the list of words contained in the text
  Result: a dictionary containing all of the words of the text. Each word is a key wich we correspond a value, their occurrency in the text
"""
def words_freq(texte):
	dicoOccurrences={}
	for w in texte : 
		if w in dicoOccurrences : 
			dicoOccurrences[w]=dicoOccurrences[w]+1
		else : 
			dicoOccurrences[w]=1
	return dicoOccurrences
  
def are_anagrams(s1,s2):
    """Paramètres passés en mode donnée: s 1 , s 2
Paramètres passés en mode donnée/résultat: [aucun]
Paramètres passés en mode résultat: [aucun]
Préconditions: s 1 et s 2 sont deux chaînes de caractères ne contenant pas de majuscules
Postconditions: [aucune]
Résultat: Vrai si s 1 et s 2 sont des anagrammes (comme par exemple "argent" et "grenat"), Faux sinon
Variables locales : d 1 et d 2 , deux tableaux associatifs"""
    d1=frequences_lettres(s1)
    d2=frequences_lettres(s2)
    if d1==d2:#!!!!fonctionne en pytohn mais pas en c++
        return True
    else:
        return False
 

def clean_lines(line):
		delimiters=["'","(",")","[","]","{","}","-","\n","_","/","*","+",".",",",";",":","!","?",'"','']
		j=""
		for l in line :
			if l in delimiters :
				j+=" "
			else :
				j+=l
		return j
      
def remove(to_remove,my_string):
    len_substring=len(to_remove)#longeur de la partie à supprimer
    if to_remove in my_string:
        first_pos=my_string.find(to_remove)
        my_string=my_string[:first_pos]+my_string[first_pos+len_substring:]
    return my_string
    

def remove_all(to_remove,my_string):
    len_substring=len(to_remove)#longeur de la partie à supprimer
    while to_remove in my_string:
        first_pos=my_string.find(to_remove)
        my_string=my_string[:first_pos]+my_string[first_pos+len_substring:]
    return my_string   
  
#print(sont_anam("marie","aimer"))
#print(sont_anam("",""))
####Un bon test unitaire est un test qui teste tt les fonctions et teste l'egalité entre résultat et resultat attendu
