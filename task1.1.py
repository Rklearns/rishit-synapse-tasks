from itertools import combinations
dictionary = {
    "Kevin": {"Halsey", "Taylor Swift", "Mitski", "Joji", "Shawn Mendes", "Sabrina Carpenter",
              "Nicky Minaj", "Conan Gray", "One Direction", "Justin Bieber"},

    "Stuart": {"Kendrick Lamar", "Steve Lacy", "Tyler The Creator",
               "Joji", "TheWeeknd", "Coldplay", "Kanye West",
               "Travis Scott", "Frank Ocean", "Brent Faiyaz"},

    "Bob": {"Conan Gray", "Joji", "Dove Cameron", "Mitski",
            "Arctic Monkeys", "Steve Lacy", "Kendrick Lamar",
            "Isabel LaRosa", "Shawn Mendes", "Coldplay"},

    "Edith": {"Metallica", "Billie Eillish", "TheWeeknd", "Mitski",
              "NF", "Conan Gray", "Kendrick Lamar", "Nicky Minaj",
              "Kanye West", "Coldplay"}
}
percentlist=[]
list1=[]
list2=[]
keylist=list(dictionary.keys())#list of all keys of dictionary is made
permutation=list(combinations(keylist,2))#tuple is printed here jiske paas unique combinations  hai of names of the dj in pairs

for i,j in permutation: #since tuple of the list has 2 elements in it therefore a and b will start from 0th index of the tuple
  set1=dictionary[i]# yaha we are basically accesing the values of the keys of dictionary
  set2=dictionary[j]
  percent1=(len(set1.intersection(set2))/len(set1)*100)
  percent2=(len(set1.intersection(set2))/len(set2)*100)
  totalpercent=float(((percent1+percent2)/2))

  if (percent1>=30 and percent2>=30 and totalpercent>=30):#checks if total percent is ABOVE 30 OR NOT...also individually
   percentlist.append(totalpercent)
   list1.append(i)#I AM MAKING A LIST OF ALL NAMES OF PAIRS SO THAT I CAN ZIP LATER
   list2.append(j)
   percentlist.sort()

  else:
   continue  

  zippedlist=list(zip(list1,list2,percentlist))#ZIPS THE DJ PAIR AND ITS OVERLAPPING LIST
  zippedlist.sort(key=lambda a:a[-1], reverse=True)#HERE USED LAMBDA FUNCTION AND INDEX
  #WILL START FROM THE LAST ELEMENT OF THE ZIPPED LIST TOH BASICALLY LAST INDEX OF TUPLE WILL BE SORTED 
  #IN DECREASING ORDER


print("Therefore the list of DJ Pairs having highest overlapping percentage is ")
print(zippedlist)
       








