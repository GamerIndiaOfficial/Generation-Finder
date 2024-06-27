print("Generation Identifier Program")
yourage = int(input("Which year were you born?")) #Please do not use ABCD or demicals or special characters otherwise code may not work
print("----------")
print("So According to the data you are:-") #The data is collected from various sources across internet.
if yourage >= 1883 and yourage <= 1900:
  print("Lost Generation")
elif yourage >= 1901 and yourage <= 1927:
  print("Greatest Generation")
elif yourage >= 1928 and yourage <= 1945:
  print("Silent Generation")
elif yourage >= 1946 and yourage <= 1964:
  print("Baby Boomers")
elif yourage >= 1965 and yourage <= 1980:
  print("Generation X")
elif yourage >= 1981 and yourage <= 1996:
  print("Millennials")
elif yourage >= 1997 and yourage <= 2012:
  print("Generation Z") 
elif yourage >= 2012 and yourage <= 2023:
  print("Generation Alpha")
else:
  print("No information") #Currently no information 
print("----------")
print("Well, This program is created by @GamerIndiaOfficial on GitHub.")
input("") #The line 25 and 26 is madded so that the code will not immediately end.
exit(0) #Don't touch line 25 and 26
