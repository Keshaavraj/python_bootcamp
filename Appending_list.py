# step 1
beatles=[]
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 1:", beatles)

# step 2

for i in range(2):
    beatles.append(input("Enter the name: "))
print("Step 2:", beatles)

# step 3
del beatles[4]
del beatles[3]
print("Step 3:", beatles)

beatles.insert(0,"Ringo Starr")
# step 4
print("Step 4:", beatles)



# testing list legth
print("The Fab", len(beatles))
