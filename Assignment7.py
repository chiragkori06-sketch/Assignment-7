# 1 total order value


order_amounts = [120, 250, 90, 310, 150]

total = 0

for amount in order_amounts:
    total += amount

print("Total order value:", total)

# output: Total order value: 920
 
# 2. cricket scrore with a while loop

scores = [45, 78, 102, 34, 67, 89]
i = 0

while i < len(scores) and scores[i] <= 100:
    print(scores[i])
    i += 1

    # output: 45, 78

    # 3.flipcart with  continue statement

    prices = [299, 499, 199, 999, 149]
total = 0

for price in prices:
    if price < 200:
        continue
    total += price

print("Total of remaining items:", total)

# output: Total of remaining items: 1797

# 4 playlist with enumerate

songs = ['Kesariya', 'Believer', 'Shape of You', 'Blinding Lights', 'Excuses']

for position, song in enumerate(songs, start=1):
    print(f"{position}. {song}")

    # output:
    # 1. Kesariya
    # 2. Believer
    # 3. Shape of You
    # 4. Blinding Lights
    # 5. Excuses

    # 5 instagram followers categories

    followers = [120, 1500, 23000, 800, 45000]

for count in followers:
    if count < 1000:
        print(count, "-> Micro")
    elif count <= 10000:
        print(count, "-> Influencer")
    else:
        print(count, "-> Celebrity")

        # output:
        # 120 -> Micro 
        # 1500 -> Influencer
        # 23000 -> Celebrity
        # 800 -> Micro
        # 45000 -> Celebrity