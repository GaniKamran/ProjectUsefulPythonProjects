L=[[1,3,4],[54,23,13],[45,3,52]]
EagleRose=[["Cabir","Elmanoglu","Baku"],["Huseyn","Raufov","Xacmaz"],["Nadir","Zeynalov","Berde"]]
N=[3,2,5,6,74]
N.sort()
N.reverse()
print(N)
print(L[2][0])
c=0
for i in EagleRose:
 print(EagleRose[c][0])
 c=c+1

for i in EagleRose:
  for l in i:
   if l=="Cabir":
    print("Tapildi")
   continue
   print("new rise")
  else:
   print("Ra")
print("Rise")