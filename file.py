def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num*0.5) + 1):
        if num % i == 0:
            return False
    return True

def display(strt, lst, file):
    with open(file, 'w') as file:
        for num in range(strt, lst + 1):
            if prime(num):
                file.write(str(num) + '\n')

# Display prime numbers and store in results.txt
display(1, 250, 'results.txt')
