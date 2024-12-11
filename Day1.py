#ans1
print("Hello, World!")
#ans2
x = 10
def func():
    x = 50
    print("Local x:", x)
func()
print("Global x:", x)
#ans3
# print("Hello World") this code will not execute because of identation error because there is a space before print.
#ans4
x="I am a global variable"
def exm_fun():
    x = "I am a local variable"
print("x=" ,x)
exm_fun()
print("x=" ,x)
#ans5
name=input("Enter your name: ") 
age=int(input("Enter your age: "))
height=float(input("Enter your height in cm: "))
print("\nHere is the information you provided:")
print("Name:", name)
print("Age:", age)
print("Height:", height,"cm")





