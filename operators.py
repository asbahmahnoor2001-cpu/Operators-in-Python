#Storing Values
'''
tree1 = float(input("Tree1"))
tree2 = float(input("Tree2"))
tree3 = float(input("Tree3"))
tree4 = float(input("Tree4"))
tree5 = float(input("Tree5"))

sum = tree1+tree2+tree3+tree4+tree5
print("The sum of all the trees is:", sum)
average = sum/5
print("The average of the 5 trees is:", average) 
'''

amount = int(input("Enter an Amount: "))

note_1000 = amount//1000
amount = amount%1000
note_500 = amount//500
amount = amount%500
note_200 = amount//200
amount = amount%200
note_100 = amount//100
amount = amount%100
note_50 = amount//50
amount = amount%50
note_20 = amount//20
amount = amount%20
note_10 = amount//10
amount = amount%10
note_5 = amount//5
amount = amount%5
note_2 = amount//2
amount = amount%2

print("Notes 1000:", note_1000)
print("Notes 500:", note_500)
print("Notes 200:", note_200)
print("Notes 100:", note_100)
print("Notes 50:", note_50)
print("Notes 20:", note_20)
print("Notes 10:", note_10)
print("Notes 5:", note_5)
print("Notes 2:", note_2)
print("Remaining Amount:", amount)

print("Enter marks for 4 subjects")

math = int(input("Maths: "))
science = int(input("Science: "))
bangla = int(input("Bangla: "))
geography = int(input("Geography: "))

sum = math+science+bangla+geography
print("Sum of all the subjects:", sum)

perc = (sum/400)*100
print(end="Percentage Mark = ")
print(perc)
