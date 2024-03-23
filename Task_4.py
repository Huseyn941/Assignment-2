#import libraries here

def main():
  '''
  Kodunuzu buraya yazin.
  '''
  year = int(input("Enter the year: "))
if year>0:
    if year%12==8:
        print(f'{year} is the year of Dragon')
    elif year%12==9:
        print(f'{year} is the year of Snake')
    elif year%12==10:
        print(f'{year} is the year of Horse')
    elif year%12==11:
        print(f'{year} is the year of Sheep')
    elif year%12==0:
        print(f'{year} is the year of Monkey')
    elif year%12==1:
        print(f'{year} is the year of Rooster')
    elif year%12==2:
        print(f'{year} is the year of Dog')
    elif year%12==3:
        print(f'{year} is the year of Pig')
    elif year%12==4:
        print(f'{year} is the year of Rat')
    elif year%12==5:
        print(f'{year} is the year of Ox')
    elif year%12==6:
        print(f'{year} is the year of Tiger')
    elif year%12==7:
        print(f'{year} is the year of Hare')
else:
    print("Invalid year!")
  pass

if __name__ == "__main__":
  main()
