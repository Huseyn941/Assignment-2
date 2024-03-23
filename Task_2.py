#import libraries here

def main():
  '''
  Kodunuzu buraya yazin.
  '''
  month=input("Enter name of the month: ")
day=int(input("Enter the day: "))
if 32>day>0:
    if month=='March' and 20<=day<32 or month=='April' and 31>day>0 or month=='May' and 32>day>0 or month=='June' and 0<day<21:
        print(f'{month} {day} is in Spring')
    elif month=='June' and 20<=day<31 or month=='July' and 32>day>0 or month=='August' and 32>day>0 or month=='September' and 0<day<22:
        print(f'{month} {day} is in Summer')
    elif month=='September' and 20<=day<31 or month=='October' and 31>day>0 or month=='November'and 31>day>0 or month=='December' and 0<day<21:
        print(f'{month} {day} is in Fall')
    elif month=='December' and 20<=day<31 or month=='January' and 32>day>0 or month=='Feburary' and 30>day>0 or month=='March' and 0<day<20:
        print(f'{month} {day} is in Winter')
else:
    print("error")

  pass

if __name__ == "__main__":
  main()
