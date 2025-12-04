position = 50
val1 = 0
val2 = 0

with open('input.txt','r') as input:
    for line in input:
        direction = line[0]
        distance = int(line[1:].strip())  

        step = 1 if direction == 'R' else -1

        for _ in range(distance):
            position = (position + step) % 100
            
            if position == 0:
                val2 += 1

        if position == 0:
            val1 += 1

print("The password for part 1 is:", val1)
print("The password for part 2 is:", val2)