# This code for getting some properties of list of numbers taken from user.
lst = list()
# Assigning some used varaibles to inital values.
c,c_1,c_2,v,w,x,y,z = 0,0,0,0,0,0,0,0

print ("\n\n>>> >>> >>>  Enter Numbers then, write  done : \n\n")

# Loop of taking valid numbers from user.
while True:
    nums = input()
    if nums == "done":
        break
    elif nums.isnumeric():
        lst.append(int(nums))
    else:
        print ("\n\n***** Invalid Input, please enter valid numbers *****\n\n")
        continue
# Getting median according to lenght on numbers list.
exact = sorted(lst)
if len(exact) % 2 == 0:
    c_1 = (len(exact) / 2)
    c_2 = ((len(exact) / 2) + 1)
    w = (int(c_1) - 1)
    x = (int(c_2) - 1)
    y = int((exact[w] + exact[x]) / 2)
    print ("\n\n**** The Median is -->  {median}  ****\n".format(median = y))
elif len(exact) % 2 != 0:
    c = (len(exact) / 2)
    v = int(c)
    z = exact[v]
    print ("\n\n**** The Median is -->  {median}  ****\n".format(median = z))

# Getting mean of numbers.
mean = (sum(exact) / len(exact))
print ("\n**** The Mean is -->  {:.1f}  ****\n".format(mean))

# Getting Max. number.
_max = max(exact)
print ("\n**** The Maximum Number is -->  {ma}  ****\n".format(ma = _max))

# Getting Min. number.
_min = min(exact)
print ("\n**** The Minimum Number is -->  {mi}  ****\n\n".format(mi = _min))
