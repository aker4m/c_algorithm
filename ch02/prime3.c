#include<stdio.h>

#define N 1000000

int main(void)
{
		int i, n;
		int prime[N/2];
		int ptr = 0;
		unsigned long counter = 0;
		prime[ptr++] = 2;
		prime[ptr++] = 3;
		for(n = 5; n <= N; n +=2){
				int flag = 0;
				for(i = 1; counter++, prime[i] * prime[i] <= n; i++){
						counter++;
						if(n % prime[i] == 0) {
								flag = 1;
								break;
						}
				}
				if(! flag)
						prime[ptr++] = n;
		}
		for(i = 0; i < ptr; i++)
				printf("%d ", prime[i]);
		printf("곱셈과 나눗셈을 실행한 횟수 : %lu\n", counter);
		printf("%d까지의 소수의 갯수는 %d 입니다.\n", N, ptr);

		return 0;
}
