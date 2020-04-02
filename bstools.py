#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 14:02:38 2018

@author: clemonnier
"""

def char_freq(s,cs=True):
    """
        :param s: string of characters (could be a word or a set of words separated by delimiters)
        :type s: str
        :param cs: Indicates if whether or not case should be taken into account.
        :type cs: bool
        :returns: associative array giving the number of occurrences of each character in s
        :rtype: dict

	
        :Example:

        >>> import bstools
        >>> a = "Kiwi"
        >>> bstools.char_freq(a)
        {'K': 1, 'i': 2, 'w': 1}

        .. note:: If s is an empty string, an empty dictionnary is returned 
        .. warning:: By default,the char_freq function is case-sensitive (cs=True). Setting cs=False allows a non-case-sensitive behaviour.     
        """
    if (cs==False):
      s=s.lower()
      
    dic={}##ou d=dict()
    for char in s:
        if char in dic:#ou dic.keys
            dic[char]=int(dic[char])+1
        else:
            dic[char]=1
    return dic

  
def are_anagrams(s1,s2):
  """
  :param s1: string of characters (could be a word or a set of words separated by delimiters) 
  :type s1: str
  :param s2: string of characters (could be a word or a set of words separated by delimiters) 
  :type s2: str
  :returns: True is s1 and s2 are anagrams, False if they are not
  :rtype: bool

  :Example:

  >>> import bstools
  >>> bstools.are_anagrams("Elections results","Lies let's recount")
  True
  
  

  .. note:: This function is not case-sensitive and does not take delimeters and punctuation into account (cf Example)
  """
  d1=char_freq(letters_only(s1),False)
  d2=char_freq(letters_only(s2),False)
  if d1==d2:#!!!!fonctionne en pytohn mais pas en c++
      return True
  else:
      return False
 

def letters_only(s):
  """
  :param s: string of characters (could be a word or a set of words separated by delimiters) \
  :type s: str \
  :returns:  s without any delimiter, space, or punctuation \
  :rtype:str
    

  :Example:
    
  >>> import bstools
  >>> a = "Hello World !"
  >>> letters_only(a)
  'HelloWorld'
  
  ...seealso:: bstools.remove(), bstools.remove_all()

  """
  delim=["'","(",")","[","]","{","}","-","\n","_","/","*","+",".",",",";",":","!","?",'"','','\'',' ']
  j=""
  for l in s :
    if (l in delim) :
      pass
    else:
      j+=l
  return j
      
def remove(rm,s):
  """
  :param s: string of characters (could be a word or a set of words separated by delimiters) \
  :type s: str \
  :returns:  s without the first occurence of rm \
  :rtype:str
    

  :Example:
    
  >>> import bstools
  >>> bstools.remove("na","bananas")
  'banas'
  
  ...note:: The remove function is case-sensitive
  ...seealso:: bstools.remove_all()
  """
  len_substring=len(rm)#longeur de la partie à supprimer
  if rm in s:
      first_pos=s.find(rm)
      s=s[:first_pos]+s[first_pos+len_substring:]
  return s
    

def remove_all(rm, s):
  """
  :param s: string of characters (could be a word or a set of words separated by delimiters) \
  :type s: str \
  :returns:  s without all the possible occurences of rm \
  :rtype:str
    

  :Example:
    
  >>> import bstools
  >>> bstools.remove_all("na","bananas")
  'bas'
  
  ...note:: The remove function is case-sensitive
  ...seealso:: bstools.remove()
  """
  len_substring=len(rm)#longeur de la partie à supprimer
  while rm in s:
      first_pos=s.find(rm)
      s=s[:first_pos]+s[first_pos+len_substring:]
  return s   
