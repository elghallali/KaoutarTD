def validation(chaine):
    result = False
    for i in chaine:
        if i in "acgt":
            result = True
        else:
            result = False
    return result

x = validation("actgcattcggtagt")
print(x)
