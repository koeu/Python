'''
절사평균은 최댓값과 최솟값을 제외한 값들의 평균
어떤 리스트가 주어질 때, 우리는 그 리스트의 절사평균을 구하려고 합니다. 절사평균을 구하는 함수 myMean()를 만들어봅시다.

숫자를 담고 있는 리스트를 매개변수로 넣으면 그 리스트의 절사평균을 반환하는 함수 myMean()을 구현하세요.
ex) myMean([1, 2, 3, 4, 5]) > 3.0
'''
def myMean(mylist):
    mylist.remove(max(mylist))
    mylist.remove(min(mylist))
    avg = sum(mylist)/len(mylist)
    return avg
    
myMean([1, 2, 3, 4, 5])