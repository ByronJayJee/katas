'''
Camel Case Kata Challenge
Example camel_case('hello case') => 'HelloCase'

Written by ByronJayJee
Dec 4, 2018
'''

def find_first_word(svar,dlim):
   # Let's start by removing any leading white space
   stChar=-1
   for x in range(0,len(svar)):
      if svar[x]!=dlim and stChar==-1:
         stChar=x
         svar_nlws = svar[x:]
         break
      if x==len(svar)-1: # Return empty strings if input string is only whitespace
         return '', ''

   word_end = -1
   # Next, find the white space after the first word
   #print(svar_nlws)
   for x in range(0,len(svar_nlws)):
      if svar_nlws[x]==dlim:
         word_end = x
         #print(word_end)
         #print(x)
         break
      if x==len(svar_nlws)-1:
         word_end = x+1
   sword = svar_nlws[0:word_end]
   rest = svar_nlws[word_end+1:]

   return sword, rest

def camel_case(svar,dlim):
   # I'm going to assume there is no more that 10 words in the string
   #    Therefore, I'll make an array of size (10*2 + 1) = 21 ... one entry 
   #    for the number of words found, one entry for the start position of 
   #    each word, and one entry for the end position of each word.
   
   # JK, this is python, no need to pre-initialize arrays

   print('input: ' + svar)

   # Make string lower case
   svar = svar.lower()

   wcount = 0;
   
   ccword = ''
   lrest = len(svar)
   
   
   while lrest > 0:
      sword2, rest2 = find_first_word(svar,dlim)
      #print(sword2)
      #print(rest2)
      if len(sword2) > 0:
         wcount += 1
      if len(sword2) == 0:
          break
      #print(wcount)
      #print(sword2)
      if(wcount==1):
         ccword += sword2
      if(wcount!=1):
         ccword += sword2[0].upper() + sword2[1:]

      svar = rest2
      lrest = len(svar)

   print('output: ' + ccword)


delim=' '
camel_case('  Hello world    ', delim)
