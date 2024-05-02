def counter(count):
    print("counter initialized...")

    while(count>0):
        yield count
        count-=1

for count in counter(10):
    print(count)