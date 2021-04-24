'''
AI의 암호가 주어질 때, 이에 매칭되는 번호로 바꾸는 프로그램을 작성해봅시다.

AI의 암호와 이에 매칭하는 번호는 다음과 같습니다.

AI의 암호	번호
에릭	1
김동완	2
전진	3
이민우	4
앤디	5
AI의 암호 모음이 리스트로 주어질 때, 이에 해당하는 번호 모음이 담긴 리스트를 반환하는 함수 skyCastle() 를 작성해봅시다.

ex) skyCastle(["에릭", "이민우", "김동완", "전진"]) > 함수 반환 예시 [1, 4, 2, 3]

'''

def skyCastle(my_list):
    matching = {"에릭":1, "김동완":2, "전진":3, "이민우":4, "앤디":5}
    m_list = []
    for i in my_list:
        m_list.append(matching[i])
    return m_list
    
skyCastle(["에릭", "이민우", "김동완", "전진"])