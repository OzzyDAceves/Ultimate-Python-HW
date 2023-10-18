# And, Or, Not

print('Does your car have gasoline?, write "yes" or "not"')
Gasoline = input()
print('Is your car running?, write "yes" or "not"')
Power_on = input()

Gasoline = True if 0 == Gasoline.find("y") else False
Power_on = True if 0 == Power_on.find("y") else False

if Gasoline and Power_on:
    print("You can move forward")
elif Gasoline == True and Power_on != True:
    print("You need power on the car")
elif Gasoline != True and Power_on == True:
    print("You need gasoline")
elif Gasoline != True and Power_on != True:
    print("Can't move")
