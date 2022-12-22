with open("data/en_US_cleaned.txt", "r") as f:
    input_set = set()
    output_set = set()
    maxword = (None, 0)
    maxipa = (None, 0)
    for line in f:
        word, ipa = line.rstrip().split("\t")
        if len(word) > maxword[1]:
            maxword = (word, len(word))
        if len(ipa) > maxipa[1]:
            maxipa = (ipa, len(ipa))
        for c in word:
            input_set.add(c)
        for c in ipa:
            output_set.add(c)
print(input_set)
print(output_set)
print(maxword)
print(maxipa)