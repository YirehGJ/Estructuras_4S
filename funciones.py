d = {} #{"key": "value": 123:True}
s = {} #[1,2,3,4,5] => (1,2,3,4)

for i in range (0,10,2): #for (int i = 0; i < 10)
    d[i]=i*i
print (d)

cont = 10
while (cont >-5):
    print("Aun no")
    cont -= 1    #  -= 1 es lo mismo que += -1

    if (not cont):
        break 