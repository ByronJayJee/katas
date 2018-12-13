'''
 ip address validation kata challenge

Instructions: Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

Examples:

Valid inputs:
1.2.3.4
123.45.67.89

Invalid inputs:
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089

**Note that leading zeros (e.g. 01.02.03.04) are considered invalid.

Written by ByronJayJee
Dec 13, 2018
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

def ip_valid(svar,dlim):

   print('input: ' + svar)

   ocount = 0;
   valid_flag=0
   lrest = len(svar)
   
   
   while ocount < 4 and lrest > 0:
      sword2, rest2 = find_first_word(svar,dlim)
      #print(sword2)
      #print(rest2)
      octet=int(sword2)
      if sword2[0] != '0' and octet<=255:
         valid_flag += 1
      if len(sword2) == 0:
          break
      #print(wcount)
      #print(sword2)

      svar = rest2
      lrest = len(svar)
      ocount += 1

   if lrest>0:
       valid_flag=-1

   if valid_flag==4:
      print('Success - Valid IPv4 address')
   else:
      print('Error - Invalid IPv4 address')

   #print('output: ' + str(valid_flag))


delim='.'

ip_valid('123.45.67.89', delim) #valid
#ip_valid('123.045.67.89', delim) #invalid
