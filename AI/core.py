import time

viability = 100
def reflex():
    print("reflex")


r = []
r.append(reflex)

while viability > 5:
    # check viability
    print(viability)
    time.sleep(5)
    viability -= 1

    #
    r[0]()



