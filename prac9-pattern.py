'''def pattern(n):
    for i in range(n):
        for j in range (n):
            print((i+j)%n + 1 ,end="")
        print()
pattern(eval(input("enter number: ")))

output
---------
enter number: 5
12345
23451
34512
45123
51234


c=1
for i in range(5):
    print(" "*(4-i),end="")
    for j in range(i+1):
        if j%2==0:
            print(" *",end="")
        else:
            print(f" {c}",end="")
            c+=1
    print()
c=1

output
-----------------
     *
    * 1
   * 2 *
  * 3 * 4
 * 5 * 6 *'''
