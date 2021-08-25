def matchingWords(sentence1, sentence2):
    words1 = sentence1.strip().split(" ")
    words2 = sentence2.strip().split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score += 1
    return score

if __name__ == "__main__":
    sentences = ["Python is good", "This is snake", "Manav is a good boy"]
    query = input("Please enter the query string: ")
    scores = [matchingWords(query, sentence) for sentence in sentences]
    sortedSentScore = [sentScore for sentScore in sorted(zip(scores, sentences), reverse=True) if sentScore[0] != 0]
    # print(sortedSentScore) #It prints the list of scores and sentence

    print(f"{len(sortedSentScore)} results found!")
    for score, item in sortedSentScore:
        print(f" \"{item}\" with score of {score}") 