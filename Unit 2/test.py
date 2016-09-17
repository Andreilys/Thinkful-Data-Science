def fizzbuzz_test(f):
    output = []
    for n in range(100):
        output.append(str(f(n) + "\n"))

    expected = open("fizzbuzz-output.txt, "r")
    i = 0
    for line in expected:
        if line == output[i]:
            print("Success!")
            i += 1
        else:
            print("Nope. Try again.")

# print(weather_data[1][2])

def fizzbuzz(n):
    ret = ""
    if not (n%3):
        ret += "fizz"
    if not (n%5):
        ret += "buzz"
    return ret or str(n)

fizzbuzz_test(fizzbuzz)
