def make_pwm(motif):
    k=len(motif[0])
    pwm=[]
    for i in range(k):
        count={"A":1,"C":1,"G":1,"T":1}
        for m in motif:
            count[m[i]]+=1
        total=sum(count.values())
        prob={}
        for x in "ATGC":
            prob[x]=count[x]/total
        pwm.append(prob)
    return pwm
motif=["AGC","AGC","TGC"]
pwm=make_pwm(motif)
for i ,row in enumerate(pwm):
    print("position",i+1,row)