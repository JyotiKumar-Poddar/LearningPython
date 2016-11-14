'''
Created on 14-Nov-2016

@author: jyotipoddar
'''
i=1
for i in range(5):
    print(i+10)
    
# Here i is inclusive in 5 is exclusive    
for i in range(1,5):
    print(i*10)
    
    
   
def printCapitalizeString(st):
    """Print the value of the String in upper case 
        Args:
            st:String as an input
        Return: 
            Input in upper case
    """
    print("Actual String -->"+st)
    print("After Formating -->"+st.upper())
    
printCapitalizeString("jyoti kumar")