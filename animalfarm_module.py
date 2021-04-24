'''
양 - “메에에”
닭 - “꼬끼오”
개 - “크르릉”

animal.py 모듈 안에 동물들의 울음소리를 담은 리스트 animals 를 보고 각 동물이 몇 마리가 있는지 세어보.

'''

# 동물 변수(sheep, chicken, dog)를 선언하고, 
# animal 모듈의 animals 리스트 안의 동물 마리수를 동물 변수에 넣어봅시다.
import animal

ss = animal.animals
print(ss)

def cry(ss, cc):
    count = 0
    for i in ss:
        if i == cc:
            count = count + 1
    return count

# 변수 sheep, chicken, dog를 선언하고, animal 모듈의 animals 리스트 안의 동물 마리수를 각 변수에 저장
sheep = cry(ss, "메에에")
chicken = cry(ss, "꼬끼오")
dog = cry(ss, "크르릉")
