gadgets = [ ("Explosive Batarangs", 3, True),
            ("Batarangs", 5, True),
            ("Smoke Pellets", 0, False),
            ("Tear Gas Grenades", 2, True),
            ("Night Vision Goggles", 1, True), 
            ("Batclaw", 0, False), 
            ("Grapple Gun", 3, True), 
            ("Batsignal", 0, False), 
            ("Utility Belt", 1, True), 
            ("Batmobile Tires", 4, True) ]
#instock items->first then next priority most quantitiy and if same then alphabetical

gadgets.sort(key=lambda a:(not a[2],-a[1],a[0]))

#firstly dekha ki a[2] could be true or false jisme true ka value 1 and false ka 0
#Therefore after negating it hamne usko sort kiya that is 0 sabse upar aayega cuz ascending order 
# and since hamne negate kiya tha therefore True is 0 now jo sabse upar aayega jaisa hame chahiye tha

#secondly dekha a[1] that is the quantity usko we have turned into negative so that it is sorted in increasing order
#but in reality is decreasing which satisfies the purpose

#lastly a[0] is sorted in alphabetical order 

#This was the priority list according to which we have done the sorting

print(gadgets)

