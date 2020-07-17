ItemsInCart =0
#2 items will be added to cart

if ItemsInCart !=2:
    #raise Exception("Products cart count not matching")
    pass
#assert(ItemsInCart == 2)

try:
    with open('filelog.txt','r')as reader:
        reader.read()

#except:
    #print(" Some how i reahced this block")

except Exception as e:
    print(e)

finally:
    print("cleaning")