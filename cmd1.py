import sys
print("This is the name of the script:", sys.argv[0]) 
print("Number of words:", len(sys.argv) - 1)
for i in range(1,len(sys.argv)):

    print(f"Word {i}:",str(sys.argv[i]))


print ("Done by Vishal")
