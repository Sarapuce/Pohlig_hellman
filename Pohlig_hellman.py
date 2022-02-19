p = 7863166752583943287208453249445887802885958578827520225154826621191353388988908983484279021978114049838254701703424499688950361788140197906625796305008451719
h = 6289736695712027841545587266292164172813699099085672937550442102159309081155467550411414088175729823598108452032137447608687929628597035278365152781494883808
g = 2862392356922936880157505726961027620297475166595443090826668842052108260396755078180089295033677131286733784955854335672518017968622162153227778875458650593


print("\n\nCalculating prime number decomposition of p-1...")
p_1 = p - 1
d, factors = 2, []
while d*d <= p_1:
    while (p_1 % d) == 0:
        factors.append(d)
        p_1 //= d
    d += 1
if p_1 > 1:
    factors.append(p)

factors = [[x, factors.count(x)] for x in set(factors)]
print("Prime number decomposition of p-1 : \n{}\n\n".format(factors)) 

x = []
for factor in factors:
    print("┌──────────────\n│Searching xi for {}\n└──────────────".format(factor[0]))
    x_i_list = []
    for i in range(factor[1]):
        print("------\nSearching for power {}\n------".format(i))
        if i != 0:
            beta = (beta * pow(g, -(x_i_list[-1] * (factor[0] ** (i - 1))), p)) % p
        else:
            beta = h
        e1 = pow(beta, (p-1) // (factor[0] ** (i + 1)), p)
        e2 = pow(g, (p-1) // factor[0], p)
        print("e1 = {}".format(e1))
        print("e2 = {}".format(e2))
        for k in (range(factor[0])):
            if pow(e2, k, p) == e1:
                print("{}^{} = {} [p]".format(e1, k, e2))
                x_i_list.append(k)
                print("x = {}".format(k))
                break
    x.append(x_i_list)

print("\n\nCreation of congruence system...")
system = []
for i, factor in enumerate(factors):
    y = 0
    for j, x_j in enumerate(x[i]):
        y += x_j * (factor[0] ** j)
    y = y % (factor[0] ** factor[1])
    print("x = {} [p]".format(y))
    system.append(y)
    

result = 0
for i in range(len(factors)):
    p_i, e_i = factors[i]
    p_e = p_i ** e_i
    product = system[i]
    for j in range(len(factors)):
        if j == i:
            continue
        p_e_j = factors[j][0] ** factors[j][1]
        product *= p_e_j * pow(p_e_j, -1, p_e)
        product %= (p - 1)
    result += product
    result %= (p - 1)
    
print("\n\n┌──────────────\n│ x = {}\n└──────────────".format(result))

print("""   _____                                      
  / ___/____ __________ _____  __  __________ 
  \__ \/ __ `/ ___/ __ `/ __ \/ / / / ___/ _ \\
 ___/ / /_/ / /  / /_/ / /_/ / /_/ / /__/  __/
/____/\__,_/_/   \__,_/ .___/\__,_/\___/\___/ 
                     /_/                       (dit le king)
                     """)