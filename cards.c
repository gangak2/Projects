/*
John is playing a game with his friends. The game's rules are as follows: There is deck of N cards from which each person is dealt a hand of K cards. Each card has an integer value representing its strength. A hand's strength is determined by the value of the highest card in the hand. The person with the strongest hand wins the round. Bets are placed before each player reveals the strength of their hand.

John needs your help to decide when to bet. He decides he wants to bet when the strength of his hand is higher than the average hand strength. Hence John wants to calculate the average strength of ALL possible sets of hands. John is very good at division, but he needs your help in calculating the sum of the strengths of all possible hands.
Problem

You are given an array a with N ≤ 10 000 different integer numbers and a number, K, where 1 ≤ K ≤ N. For all possible subsets of a of size K find the sum of their maximal elements modulo 1 000 000 007.
Input

The first line contains the number of test cases T, where 1 ≤ T ≤ 25

Each case begins with a line containing integers N and K. The next line contains N space-separated numbers 0 ≤ a [i] ≤ 2 000 000 000, which describe the array a.
Output

For test case i, numbered from 1 to T, output "Case #i: ", followed by a single integer, the sum of maximal elements for all subsets of size K modulo 1 000 000 007.
Example
For a = [3, 6, 2, 8] and N = 4 and K = 3, the maximal numbers among all triples are 6, 8, 8, 8 and the sum is 30.
Example inputExample output

5
4 3
3 6 2 8 
5 2
10 20 30 40 50 
6 4
1 1 2 3 5 8 
2 2
1069 1122 
10 5
10386 10257 10432 10087 10381 10035 10167 10206 10347 10088 

Case #1: 30
Case #2: 400
Case #3: 103
Case #4: 1122
Case #5: 2621483
*/

#include<stdio.h>
#include<stdlib.h>

#define MODULO 1000000007


void Merge(long long int *array, int left, int mid, int right);

void MergeSort(long long int *array, int left, int right)
{
        long long int mid = (left+right)/2;
        if(left<right)
        {
                MergeSort(array,left,mid);
                MergeSort(array,mid+1,right);
                Merge(array,left,mid,right);
        }
}

void Merge(long long int *array, int left, int mid, int right)
{
        long long int tempArray[right-left+1];
        int pos=0,lpos = left,rpos = mid + 1;
        while(lpos <= mid && rpos <= right)
        {
                if(array[lpos] < array[rpos])
                {
                        tempArray[pos++] = array[lpos++];
                }
                else
                {
                        tempArray[pos++] = array[rpos++];
                }
        }
        while(lpos <= mid)  tempArray[pos++] = array[lpos++];
        while(rpos <= right)tempArray[pos++] = array[rpos++];
        int iter;
        for(iter = 0;iter < pos; iter++)
        {
                array[iter+left] = tempArray[iter];
        }
        return;
}

long long int modMultiplication(long long int a,long long int b, long long int m){
	long long int itermm,outmm=1;
	for(itermm=0;itermm<b;itermm++)
		outmm = outmm*(a-itermm)%m;
	//printf("%d\n",outmm);
	return outmm;
}

long long int power(long long int a, long long int b, long long int MOD) {
	long long int x = 1, y = a;
	    while(b > 0) {
	        if(b%2 == 1) {
	            x=(x*y);
	            if(x>MOD) x%=MOD;
	        }
	        y = (y*y);
	        if(y>MOD) y%=MOD;
	        b /= 2;
	    }
	   // printf("%d\n",x);
	    return x;
	}
	
long long int modInverse(long long int q, long long int r) {
	long long int itermi,outmi=1;
	for(itermi=1;itermi<=q;itermi++)
	    outmi = (outmi*power(itermi,r-2,r))%r;
	return outmi;
}

long long int permutedModInverse(long long int x, long long int y, long long int z){
	long long int t1,t2;
	if(y<=x/2){
		t1 = modMultiplication(x,y,z);
		t2 = modInverse(y,z);
	}
	else{
		t1 = modMultiplication(x,x-y,z);
		t2 = modInverse(x-y,z);
	}
	return (t1*t2)%z;
}

void print(long long int *array, int len){
	int j=0;
	for(j=0;j<len;j++){
		printf("%lld\t",array[j]);
	}
	printf("\n");
}

int main()
{
int T,L;
scanf("%d",&T);
L=T;
while(T--){
	int N,K,i;
	long long int a[10000],sum=1,temp1,temp2,out=0,temp3;
	scanf("%d %d", &N, &K);
	for(i=0;i<N;i++){
		scanf("%lld",&a[i]);
	}
	MergeSort(a,0,N-1);
	//print(a,N);
	for(i=N-1;i>=K-1;i--){
		temp1 = a[i]%MODULO;
		temp2 = permutedModInverse(i,K-1,MODULO);
		temp3 = (temp1*temp2)%MODULO;
		out = (out + temp3)%MODULO;
	}
	printf("Case #%d:\t%lld\n",L-T,out);
} 
}






























