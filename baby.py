from random import choice


questions=["why is the sky blue?:","why is the sun so hot?:","how do we breathe?:"]
question=choice(questions)
answer=input(question).strip().lower()
while answer!="just because":
      answer=input("why?: ").strip().lower()
    
print("ah okay")
    
    
                           
