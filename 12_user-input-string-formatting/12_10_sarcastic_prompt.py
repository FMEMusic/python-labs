# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.
opinion = input("Please insert your honest opinion about Kanye West---->")
opinion2 =" "
for i in range(0,len(opinion)):
    if i % 2:
        opinion2 += opinion[i].lower()
    elif i == 0 :
        opinion2 += opinion[0]
    else:
        opinion2 += opinion[i]
print(opinion2)
    