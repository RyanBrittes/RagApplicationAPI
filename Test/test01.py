phrase = "O ceu tem a cor azul de dia mas de noite ele é preto. O mar tem a cor azul também, mas rios podem ter cor transparente. O sal tem a cor branca, mas também pode ser vermelha."

overlap = ""
count = 0
overlap_size = 2
index_letter = 0
index_start = 0
chunks = []
index_list = 0
index_overlap = 1

while index_letter < len(phrase):

    if phrase[index_letter] == ".":
        chunk = phrase[index_start:index_letter + 1]
        index_start = index_letter + 2
        chunks.append(overlap + chunk)

        while count < overlap_size:
            #print(index_overlap)
            if chunk[-index_overlap] in [" ", ","]:
                count += 1

            index_overlap += 1

        overlap = chunk[-index_overlap + 1:]
        count = 1
        index_overlap = 0

    index_letter += 1

print(chunks)
