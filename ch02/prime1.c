#include<stdio.h>

#define N 1000000

int main(void)
{
		int i, n;
		int cnt = 0;
		unsigned long counter = 0;
		for(n = 2; n <= N; n++){
				for(i = 2; i < n; i++){
						counter++;
						if (n % i == 0)
								break;
				}
				if (n == i){
						printf("%d ", n);
						cnt++;
				}
		}
		printf("나눗셈을 실행한 횟수 : %lu\n", counter);
		printf("%d까지의 소수의 갯수는 %d 입니다.\n", N, cnt);

		return 0;
}
