# 등장하는 알파벳의 개수 -> dict 결과 만들기
# Dict Comprehension 사용 
# 대소문자 구분 하지 않기, 1개 이상 등장하는 알파벳만
# hint : 알파벳 리스트 , lower, upper, count 

word = "Alice in wonderland"

# {'a': 2,
#  'c': 1,
#  'd': 2,
#  'e': 2,
#  'i': 2,
#  'l': 2,
#  'n': 3,
#  'o': 1,
#  'r': 1,
#  'w': 1}

word = word.lower()
result = {
    i : word.count(i)
    for i in sorted(set(word.replace(' ', '')))
}
print(result)

# collections 사용
import collections
word1 = word.replace(' ', '').lower()
print(collections.Counter(word1))