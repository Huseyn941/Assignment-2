#import libraries here

def main():
  '''
  Kodunuzu buraya yazin.
  '''
  month=input("Enter a month: ")
day=int(input("Enter the day: "))
if 32>day>0:
    if month=='December' and 31>=day>=22 or month=='January' and 19>=day>=1:
        print("Your zodiac sign is Capricorn")
    elif month=='January' and 31>=day>=20 or month=='Feburary' and 18>=day>=1:
        print("Your zodiac sign is Aquarius")
    elif month=='Feburary' and 31>=day>=19 or month=='March' and 20>=day>=1:
        print("Your zodiac sign is Pisces")
    elif month=='March' and 31>=day>=21 or month=='April' and 19>=day>=1:
        print("Your zodiac sign is Aries")
    elif month=='April' and 30>=day>=20 or month=='May' and 20>=day>=1:
        print("Your zodiac sign is Taurus")
    elif month=='May' and 31>=day>=21 or month=='June' and 20>=day>=1:
        print("Your zodiac sign is Gemini")
    elif month=='June' and 30>=day>=21 or month=='July' and 22>=day>=1:
        print("Your zodiac sign is Cancer")
    elif month=='July' and 31>=day>=23 or month=='August' and 22>=day>=1:
        print("Your zodiac sign is Leo")
    elif month=='August' and 31>=day>=23 or month=='September' and 22>=day>=1:
        print("Your zodiac sign is Virgo")
    elif month=='September' and 30>=day>=23 or month=='October' and 22>=day>=1:
        print("Your zodiac sign is Libra")
    elif month=='October' and 31>=day>=23 or month=='November' and 21>=day>=1:
        print("Your zodiac sign is Scorpio")
    elif month=='November' and 30>=day>=22 or month=='December' and 21>=day>=1:
        print("Your zodiac sign is Sagittarius")
else:
    print("Either a month or a day is invalid!")
  pass

if __name__ == "__main__":
  main()
