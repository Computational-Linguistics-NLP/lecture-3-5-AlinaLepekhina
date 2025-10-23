"""a = int(input())
if a <= 2:
    print("чудовищно мало")
elif 2<=a<=5:
    print("очень мало")
elif 5<=a<=10:
    print("мало")
elif 10<=a<=30:
    print("окей")
elif 30<=a<=100:
    print("много")
elif a>=100:
    print("чудовищно много")"""



    

    
a = int(input())
if a<=2:
    print("чудовищно мало")
else:
    if 2<=a<=5:
        print("очень мало")
    else:
        if 5<=a<=10:
            print("мало")
        else:
            if 10<=a<=30:
                print("окей")
            else:
                if 30<=a<=100:
                    print("много")
                else:
                    if a>=100:
                        print("чудовищно много")
            
            
