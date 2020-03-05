def pairSummingToPowerOfTwo(a):

    int_Power = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384]

    intCheck = 0

    for i in range(len(a)):

        for j in range(len(a)):

            if ( i < j ) and ( (a[i] + a[j]) in int_Power ):
                print("(",i,",",j,") - a[",i,"] + [",j,"] = ", a[i], " + ", a[j], " = ", a[i] + a[j])
                intCheck += 1

    return intCheck

if __name__ == '__main__':
    ans = pairSummingToPowerOfTwo([1,1,-1,2,3])
    print(ans)
    ans = pairSummingToPowerOfTwo([2,2,2,2])
    print(ans)
    ans = pairSummingToPowerOfTwo([-2,-1,0,1,2])
    print(ans)