import scipy.stats as stats
##################################################################
### Q1-Binomail-probability
n=10
p=0.5
x=7
prob=stats.binom.pmf(x,n,p)
print(f'Answer for Q-1: P(X=7)= {prob:.4f}')
##################################################################
### Q2-Binomail-probability
# A
n=5
p=2/3
x=5
prob=stats.binom.pmf(x,n,p)
print(f'Answer for Q-2A: P(X=5)= {prob:.4f}')

# B
n=5
p=2/3
x=[3,4,5]
probs=0
for i in x:
    prob=stats.binom.pmf(i,n,p)
    probs+=prob
    # print(f'P(X={i}): {prob:.4f}')
print(f'Answer for Q-2B: P(X={x})= {probs:.4f}')

# C
n=5
p=2/3
x=2
prob=stats.binom.pmf(x,n,p)
print(f'Answer for Q-2C: P(X={x})= {prob:.4f}')
##################################################################
### Q3- Geometric probability distribution
x=6
p=3/75
prob=stats.geom.pmf(x,p)
print(f'Answer for Q-3: P(X={x})= {prob:.4f}')
##################################################################
### Q4 Poisson probability distribution
#A
lamda=1
x=0
poisson_prob=stats.poisson.pmf(x,mu=lamda)
print(f'Answer for Q-4A: P(X={x})= {poisson_prob:.4f}')

#B
lamda=1
x=1
poisson_prob=stats.poisson.pmf(x,mu=lamda)
print(f'Answer for Q-4B: P(X={x})= {poisson_prob:.4f}')

#C
lamda=1
x=2
poisson_prob=stats.poisson.pmf(x,mu=lamda)
print(f'Answer for Q-4C: P(X={x})= {poisson_prob:.4f}')

#D
lamda=1
x=3
poisson_prob=stats.poisson.pmf(x,mu=lamda)
print(f'Answer for Q-4D: P(X={x})= {poisson_prob:.4f}')
