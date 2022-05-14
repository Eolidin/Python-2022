def palindrom(x):
    if len(x) < 2:
        return (True)
    elif (x[0]).lower() != (x[-1]).lower():
        return(False)
    else:
        return(palindrom(x[1:-1]))

print(palindrom("Jannik"))
print(palindrom("Anna"))
print(palindrom("rentner"))