with open("data/en_US.txt", "r") as src, open("data/en_US_cleaned.txt", "w") as dst:
    for line in src:
        word, ipa = line.rstrip().split("\t")
        ipa = ipa.split(",")[0]  # take only first pronunciation
        dst.write(f"{word}\t{ipa}\n")