import matplotlib.pyplot as plt
from math import sqrt

critics={
    'hhd' : {'guardians of the galaxy 2':5, 'christmas in august':4, 'boss baby':1.5},
    'chs' : {'christmas in august':5, 'boss baby':2},
    'kmh' : {'guardians of the galaxy 2':2.5, 'christmas in august':2, 'boss baby':1},
    'leb' : {'guardians of the galaxy 2':3.5, 'christmas in august':4, 'boss baby':5}
}

def sim(i, j): # 두 점사이의 유사도(피타고라스)
	return sqrt(pow(i,2)+pow(j,2))

def sim_distance(data, name1, name2): # 두 사람 사이의 거리(유클리디안 유사도)
    sum = 0
    for i in data[name1]:
        if i in data[name2]: # 같은 영화를 봤으면, 포함되어 있으면
            sum += pow(data[name1][i] - data[name2][i], 2)
            
    return 1/(1+sqrt(sum))

def top_match(data, name, index=3, sim_function=sim_distance):
    li = []
    for i in data:
        if i != name:
            li.append((sim_function(data,name,i), i))
    li.sort()
    li.reverse() # 반대로
    
    return li[:index] # 처음부터 index까지의 리스트를 반환

def barchart(data, labels):
    positions = range(len(data)) # 사람 수 만큼
    # 그래프의 설정(항목 개수, 데이터, 그래프의 높이, 색)
    plt.barh(positions, data, height=0.5, color='r')
    plt.yticks(positions, labels) # y축 라벨 이름
    plt.xlabel('similarity')
    plt.ylabel('name')
    plt.show()

li = top_match(critics,'chs')
print(li)
score = []
names = []
for i in li:
    score.append(i[0])
    names.append(i[1])
    
barchart(score, names)
