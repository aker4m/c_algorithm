#include<stdio.h>

#define N 1000000

int main(void)
{
		int i, n;
		int prime[N/2];
		int ptr = 0;
		unsigned long counter = 0;
		prime[ptr++] = 2;
		for(n = 3; n <= N; n += 2){
				for(i = 1; i < ptr; i++){
						counter++;
						if(n % prime[i] == 0)
								break;
				}
				if(ptr == i)
						prime[ptr++] = n;
		}
		for(i = 0; i < ptr; i++)
				printf("%d ", prime[i]);
		printf("나눗셈을 실행한 횟수 : %lu\n", counter);
		printf("%d까지의 소수의 갯수는 %d 입니다.\n", N, ptr);

		return 0;
}
