#baby_simulator
#while loop
#Aswering randon questions froma a baby until the answer starts with "just because"

from random import choice


questions=["why is the sky blue?:","why is the sun so hot?:","how do we breathe?:"]
question=choice(questions)
answer=input(question).strip().lower()
while answer!="just because":
      answer=input("why?: ").strip().lower()
    
print("ah okay")
    
    
                           
