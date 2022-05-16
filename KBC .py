from numpy import quantile


print("welcome to Kaun Banega Crorepati")
print("So let's start")
print("You have  life line \n (1).50/50 life line"  )
question_list = [
"How many continents are there?",  # pehla question
"What is the capital of India?",# doosra question
"NG mei kaun se course padhaya jaata hai?"# teesra question
"The latest version of Consumer Protection Act was passed in which year",#fourth quation
"China has recently released a list of “standardised names” for 15 places in which Indian state",#FIFTH QUATION
"Which state signed MoU with Singapore-based LNG Alliance Company, to set up its first LNG Terminal"# sixth quation
]
options_list = [
#pehle question ke liye options
["[A] Four",
"[B] Nine",
"[C] Seven",
"[D] Eight",
],
#second question ke liye options
["[A] Chandigarh",
"[B] Bhopal",
"[C] Chennai",
"[D] Delhi"],
#third question ke liye options
["[A] Software Engineering",
"[B] Counseling",
"[C] Tourism",
"[D] Agriculture"],
#fourth quation ka liya options
["[A] 2010",
"[B] 2015",
"[C] 2019",
"[D] 2021"
],
#fifth  quation ka liya options
["[A] Sikkim",
"[B] Uttarakhand",
"[C] Aruchanal Pradesh",
"[D] Assam"],
#sixth quation ka liya options
["[A] Kerala",
"[B] Karnataka",
"[C] Telangana",
"[D] Gujarat]"
]]
s=["[B] Nine","[C] Seven","[C] Chennai","[D] Delhi","[A] Software Engineering","[B] Counseling","[B] 2015","[C] 2019","[C] Aruchanal Pradesh","[D] Assam""[B] Karnataka","[C] Telangana"]

solution_list = [3,4,1,3,3,3]  
count=0
count1=1
amount=0
ch=0
wrong_answer =0 
i=0
while i<len(question_list):
    print("ye rha aap ka  quation 👉")
    print(question_list[i])
    j=0
    while j<len(options_list[i]):
        print(options_list[i][j])
        j+=1  
    life_line=input("do you wont life line\n(1). yes \n(2) no 👉")
    if ch==0:       
        if life_line=="yes":    
            print(s[count])
            print(s[count1])    
            f=int(input("enter the answer👉"))
        
            if solution_list[i]== f :
                amount=amount+1000
                print("😄yes this aright answer ")
                print("you win👉",amount)
            else:
                wrong_answer=wrong_answer+1
                print("🤦Sorry this is wrong Answer") 
          
            ch=ch+1
        elif life_line=="no":
            f1=int(input("enter the answer👉"))
            if solution_list[i]== f1 :
                amount=amount+1000
                print("😄yes this aright answer:-")
                print("you win",amount)
            else:
                wrong_answer=wrong_answer+1
                print("🤦‍♂️Sorry this is wrong Answer")         
    elif ch==1:
        print("🤦‍♂️sorry you dont have life line")
        f=int(input("enter the answer👇"))
        if solution_list[i]== f :
            amount=amount+1000
            print("😄yes this aright answer")
            print("you win",amount)
        else:
            wrong_answer=wrong_answer+1
            print("🤦‍♂️Sorry this is wrong Answer:-") 
    count+=2
    count1+=2
    i=i+1 
    if wrong_answer==1:
                    print("Your Game Is Over😩") 
                    print("You Win 👉",amount)
                    add_quatios=input("enter the permetion if you want to add quation 👉")
                    new_options=[]
                    if add_quatios=="yes":
                        quation=input("enter the quation")    
                        s=1
                        while s<=4:
                            options=input("enter the new options")
                            s=s+1
                        new_options.append(options)

                    break    
        


     
           

   

   
    
           









