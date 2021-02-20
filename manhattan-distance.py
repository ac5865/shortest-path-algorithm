def distance_sum(x,y,n):
    sum=0
    for i in range(n):
        for j in range(i+1,n):
            sum+= (abs(x[i]-x[j]))+(abs(y[i]-y[j]))
            return sum

x=[1.5, 3.8, 6, 7.2]
y=[2.3, 4.5, 7.2, 9]
n=len(x)

print(distance_sum(x,y,n))
