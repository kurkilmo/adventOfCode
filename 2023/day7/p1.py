import functools
import statistics as stat

lines = open("testinput.txt").readlines()

pict_dict = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}

def comp(hand1, hand2):
    h1 = hand1[0]
    h2 = hand2[0]
    
    max1 = h1.count(stat.mode(h1))
    max2 = h2.count(stat.mode(h2))
    
    if (max1 != max2):
        return max1 - max2

    if (max1 == 3 & ):

def main():
    hands = []
    for line in lines:
        line = line.strip()
        spl = line.split(" ")
        hand = []
        for c in spl[0]:
            try:
                hand.append(int(c))
            except:
                hand.append(int(pict_dict[c]))
        hands.append((hand, int(spl[1])))
    for h in hands:
        print(h)
    sorted_hands = sorted(hands, key=functools.cmp_to_key(comp))
    for h in sorted_hands:
        print(h)

if __name__ == "__main__":
    main()