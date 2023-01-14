def viralAdvertising(n):
    likes = 0
    share = 5
    for _ in range(n):
        daily_like = share // 2
        share = daily_like * 3
        likes += daily_like
        
    return likes

print(viralAdvertising(5))
