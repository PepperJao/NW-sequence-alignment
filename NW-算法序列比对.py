'''def introduce():
    print("*********************************************")
    print("                Author : 赵雨晴               ")
    print("input1: first sequence")
    print("input2: second sequence")
    print("*********************************************")
    '''

seq2 = "VGAWAD"   #初始变量预设
seq1 = "IPGAWD"

#seq1 = input("Please input first sequence:")#SHORT
#seq2 = input("Please input second sequence:")#LONG
# seq1 = "IPGAWD"
# seq2 = "VGAWAD"

def matrix(seq1, seq2):
    input_1 = []
    input_2 = []
    for i in range(len(seq1)):
        input_1.append(i * -4)
    for i in range(len(seq2)):
        input_2.append(i * -4)
    return input_1, input_2


def matchBase(base1, base2):
    if base1 == base2:
        return "match"
    else:
        return "mismatch"


def getScore(i, j, result_match):
    num_s1 = "(" + str(j - 1) +"," +str(i - 1) + ")"
    num_si = "(" + str(j - 1) +"," + str(i) + ")"
    num_sj = "(" + str(j) + "," + str(i - 1) + ")"

    if result_match == "match":
        score1 = score[num_s1] + 4
    else:
        score1 = score[num_s1] - 3
    score_i = score[num_si] - 4
    score_j = score[num_sj] - 4
    score_max = max(score1, score_i, score_j)
    a = "(" + str(j) +"," +str(i) + ")"

    if score_max == score1:
        con[a] = score_max
    elif score_max == score_i:
        a_i[a] = score_max
    else:
        b_j[a] = score_max

    score[a] = score_max


def getPath(j, i,seq1, seq2,flag):
    a = "(" + str(j) + "," + str(i) + ")"
    score_res1 = con.get(a)
    score_res2 = a_i.get(a)
    score_res3 = b_j.get(a)

    if score_res1 != None:
        res1.append(seq1[i])
        res2.append(seq2[j])
        if j == 0:
            return res2
        res_j = getPath(j - 1, i - 1,seq1, seq2,flag)
    elif score_res2:
        res1.append("-")
        res2.append(seq2[j])
        if j == 0 :
            return res2
        res_j = getPath(j - 1, i ,seq1, seq2,flag)
    else:

        if score_res3 != None:
            res2.append("-")
            res1.append(seq1[i])
            flag = False
        else:
            res2.append(seq2[j])
            res1.append(seq1[i])
            flag = True
        if j == 0:
            return res2
        res_j = getPath(j,i- 1,seq1, seq2,flag)
    return res_j




def run(seq1, seq2):   #回溯
    input_1, input_2 = matrix(seq1, seq2)
    for i in range(len(input_1)):
        s = "(0," + str(i) + ")"
        score[s] = input_1[i]
    for i in range(len(input_2)):
        s = "(" + str(i) + ",0)"
        score[s] = input_2[i]
    for j in range(len(seq2) - 1):
        j += 1
        for i in range(len(seq1) - 1):
            i += 1
            result_match = matchBase(seq1[i],seq2[j])
            getScore(i, j, result_match)
    flag = True
    res_j = getPath(len(seq2) - 1, len(seq1) - 1,seq1, seq2,flag)
    return res_j


if __name__ == "__main__":#主函数

    flag = True
    while(flag):
        #   introduce()
        res1 = []
        res2 = []
        con = {}
        a_i = {}
        b_j = {}

        score = {}

        seq1 = "0" + seq1.upper()
        seq2 = "0" + seq2.upper()

        res_j = run(seq1, seq2)
        res_j.reverse()
        res1.reverse()
        print("  ".join(res1))
        print("  ".join(res_j))
        flag = False
        
'''
       tmp = input("是否继续判断：[y/n]") #重复运行

        if tmp.strip() == "n":
            flag = False
        else:
            flag = True
'''
