#import libraries here

def main():
  a=int(input("Enter the wavelenght in nm: "))
if 750>a>=620:
    print(f'The relevant color is Red')
elif 620>a>=590:
    print(f'The relevant color is Orange')
elif 590>a>=570:
    print(f'The relevant color is Yellow')
elif 570>a>=495:
    print(f'The relevant color is Green')
elif 495>a>=450:
    print(f'The relevant color is Blue')
elif 450>a>=380:
    print(f'The relevant color is Violet')
else:
    print("Invalid input!")
  pass

if __name__ == "__main__":
  main()
