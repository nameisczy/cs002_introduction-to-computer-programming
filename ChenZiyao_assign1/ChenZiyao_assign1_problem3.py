#ziyao chen, 9/13/2022, section 011, Math Expressions

print("-"*60) #print text
print(format("mL to US Fluid Volume Units","^"+str(60)+"s")) #Align the text to the center and print it
print("-"*60) #print text
      
mL=250.0 #define variable mL
tsp=mL*0.202884 #define variable tsp
tbsp=tsp/3 #define variable tbsp
cup=tbsp/16 #define variable cup
pint=cup/2 #define variable pint
quart=pint/2 #define variable quart
gallon=quart/4 #define variable gallon
floz=mL/29.5735 #define variable floz

print(format("mL:",">"+str(11)+"s"), format(mL,".1f"),sep="             ") #Align the text to the right, format mL to show exactly 1 decimal places
print(format("tsp:",">"+str(12)+"s"), format(tsp,".15f"),sep="            ") #Align the text to the right, format mL to show exactly 15 decimal places
print(format("tbsp:",">"+str(13)+"s"), format(tbsp,".3f"),sep="           ") #Align the text to the right, format mL to show exactly 3 decimal places
print(format("cup(s):",">"+str(15)+"s"), format(cup,".7f"),sep="         ") #Align the text to the right, format mL to show exactly 7 decimal places
print(format("pint(s):",">"+str(16)+"s"), format(pint,".8f"),sep="        ") #Align the text to the right, format mL to show exactly 8 decimal places
print(format("quart(s):",">"+str(17)+"s"), format(quart,".9f"),sep="       ") #Align the text to the right, format mL to show exactly 9 decimal places
print(format("gallon(s):",">"+str(18)+"s"), format(gallon,".11f"),sep="      ") #Align the text to the right, format mL to show exactly 11 decimal places
print(format("fl oz:",">"+str(14)+"s"), format(floz,".15f"),sep="          ") #Align the text to the right, format mL to show exactly 15 decimal places
print("-"*60) #print text
