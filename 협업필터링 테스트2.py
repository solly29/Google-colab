from matplotlib import font_manager, rc # 한글나오게
from math import sqrt
import matplotlib.pyplot as plt

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


critics = {
    '차현석': {
        '택시운전사': 2.5,
        '남한산성': 3.5,
        '킹스맨:골든서클': 3.0,
        '범죄도시': 3.5,
        '아이 캔 스피크': 2.5,
        'The Night Listener': 3.0,
    },
    '황해도': {
        '택시운전사': 1.0,
        '남한산성': 4.5,
        '킹스맨:골든서클': 0.5,
        '범죄도시': 1.5,
        '아이 캔 스피크': 4.5,
        'The Night Listener': 5.0,
    },
    '김미희': {
        '택시운전사': 3.0,
        '남한산성': 3.5,
        '킹스맨:골든서클': 1.5,
        '범죄도시': 5.0,
        'The Night Listener': 3.0,
        '아이 캔 스피크': 3.5,
    },
    '김준형': {
        '택시운전사': 2.5,
        '남한산성': 3.0,
        '범죄도시': 3.5,
        'The Night Listener': 4.0,
    },
    '이은비': {
        '남한산성': 3.5,
        '킹스맨:골든서클': 3.0,
        'The Night Listener': 4.5,
        '범죄도시': 4.0,
        '아이 캔 스피크': 2.5,
    },
    '임명진': {
        '택시운전사': 3.0,
        '남한산성': 4.0,
        '킹스맨:골든서클': 2.0,
        '범죄도시': 3.0,
        'The Night Listener': 3.5,
        '아이 캔 스피크': 2.0,
    },
    '심수정': {
        '택시운전사': 3.0,
        '남한산성': 4.0,
        'The Night Listener': 3.0,
        '범죄도시': 5.0,
        '아이 캔 스피크': 3.5,
    },
    '박병관': {'남한산성': 4.5,
            '아이 캔 스피크': 1.0,
            '범죄도시': 4.0},
}


plt.figure(figsize=(14,8))
plt.plot([1,2,3],[1,2,3],'g^') #각각의 값과 점의 모양설정
plt.text(1,1,'사과') #텍스트 찍기
plt.text(2,2,'바나나')
plt.text(3,3,'포도')
#각 축의 크기 설정
plt.axis([0,6,0,6]) # 그래프의 x축,y축 크기설정
plt.show()


def drawGraph(data, name1, name2):
    plt.figure(figsize=(14,8)) # 크기

    li = []
    li2 = []

    for i in data[name1]:
        if i in data[name2]:
            li.append(data[name1][i])
            li2.append(data[name2][i])
            # 텍스트 찍기 (x,y,텍스트)
            plt.text(data[name1][i], data[name2][i], i)

    plt.plot(li,li2,'ro') # 각각의 값과 점의 모양설정

    plt.axis([0,6,0,6])   # 그래프의 x축,y축 크기설정
    # x,y축 이름 설정 
    plt.xlabel(name1)
    plt.ylabel(name2)
    plt.show()


def sim_pearson(data, name1, name2): # 두 사람간의 상관 계수를 구한다.
    sumX = 0
    sumY = 0
    sumPowX = 0
    sumPowY = 0
    sumXY = 0
    count = 0

    for i in data[name1]: # i = key
        if i in data[name2]: # 같은 영화를 평가했을때만
            sumX+=data[name1][i]
            sumY+=data[name2][i]
            sumPowX+=pow(data[name1][i],2)
            sumPowY+=pow(data[name2][i],2)
            sumXY+=data[name1][i]*data[name2][i]
            count+=1
            
    return (sumXY - ((sumX*sumY) / count)) / sqrt(
        (sumPowX-(pow(sumX,2)/count)) * (sumPowY - (pow(sumY,2) / count)))
    

def top_match(data, name, index=3, sim_function=sim_pearson):
    li = []
    for i in data:
        if i != name:
            li.append((sim_function(data,name,i), i))
    li.sort()
    li.reverse()
    
    return li[:index] # 처음부터 index까지의 리스트를 반환


def getRecommendation(data,person,sim_function=sim_pearson):
    result = top_match(critics, person, len(data))

    simSum = 0
    score=0
    li = []
    score_dic={}
    sim_dic={}

    for sim,name in result:
        if sim<0 : continue
        for movie in data[name]:
            if movie not in data[person]:
                score_dic.setdefault(movie,0)   # 기본적으로 value값에 0을 준다.
                score_dic[movie] += sim*data[name][movie] # 유사도와 영화평점은 곱함

                sim_dic.setdefault(movie,0)
                sim_dic[movie] += sim           # 사람들의 유사도를 더한다.

            score = 0

    for key in score_dic:
        # 추측 영화 평점의 합 / 유사도의 합이 예상평점이다.
        score_dic[key] = score_dic[key] / sim_dic[key] 
        li.append((score_dic[key],key))
    li.sort()
    li.reverse()
    return li

#drawGraph(critics,'황해도','임명진')
#print(sim_pearson(critics,'심수정','차현석'))
print(getRecommendation(critics, '박병관'))

