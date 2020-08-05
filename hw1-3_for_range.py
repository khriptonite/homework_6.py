# o aplicatie care afiseaza primele 5 numere care se impart la 3 dintr-un diapazon dat

#HW1: utilizati functia inputInt() 

def inputInt(message):
    num = input(message)
    return int(num)

start_value = inputInt("Start: ?")
end_value  = inputInt("End: ?")

#HW2: creati din codul asta o functie
def print_f (text):
    print("\n")
    print("#"*100)
    print("-"*20, text, "-"*20)
    print("#"*100)

#HW3: rezolvati aceeasi problema doar ca algoritmul 
      # trebuie sa lucreze in ambele directii
      
      #input : 1.....20 -> 3, 6, 9, 12, 15
      #input : 20....1 -> 18, 15, 12, 9, 6
if start_value < end_value:
    step = 1
else:
    step = -1

#################################################
print_f("Diapazon of values")

for x in range(start_value, end_value, step):
        print(x, end=" ")
        
print_f("Divide by 3")      
    
for x in range(start_value, end_value, step):
    if x % 3 == 0:
        print(x, end=" ")
        
print_f("First 5 values that Divides by 3")      
n = 0 
    
for x in range(start_value, end_value, step):
    if x % 3 == 0 and n < 5:
        print(x, end=" ")
        n += 1