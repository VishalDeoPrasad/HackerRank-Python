def designerPdfViewer(h, word):
    word_height = [h[ord(c)-97] for c in word]
    return max(word_height)*len(word)

h = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7]
print(designerPdfViewer(h, "zaba"))