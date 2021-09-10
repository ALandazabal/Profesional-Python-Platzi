import time

def fibo_gen(max=None):
    n1 = 0
    n2 = 1
    counter = 0

    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            if aux <= max:
                yield aux
            else:
                return StopIteration

if __name__ == '__main__':
    max = int(input("Por favor ingrese el max: "))
    fibonacci = fibo_gen(max)
    for element in fibonacci:
        print(element)
        time.sleep(1)