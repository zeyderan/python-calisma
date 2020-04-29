name = 'aykut bayraktar'
# for letter in name:
#     if letter == 'a':
#         break # ilk harf 'a' olduğu için döngü başlamadan biter
#     print(letter)
# for letter in name:
#     if letter == 'a':
#         continue # 'a' harfine denk gelince o anki döngü es geçer
#     print(letter)
    
# x = 0
# while x < 5:
#     x+=1 # buraya almazsak x sürekli 2 de takılı kalır
#     if x == 2:
#         continue
#     print(x)

x = 1
result = 0
while x <= 100:
    x+=1
    if x % 2 == 0:
        continue
    result+=x
print(result)    
    
    