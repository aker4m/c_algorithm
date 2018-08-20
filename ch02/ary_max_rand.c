#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int maxof(const int a[], int n)
{
		int i;
		int max = a[0];
		for(i = 1; i < n; i++){
				if(a[i] > max) max = a[i];
		}
		return max;
}

int main(void)
{
		int i;
		int *height;
		int number;
		do{
				printf("사람 수 : ");
				scanf("%d", &number);
		}while(number <= 0);

		height = calloc(number, sizeof(int));
		srand(time(NULL));
		for(i = 0; i < number; i++){
				height[i] = 100 + rand() % 90;
				printf("height[%d] = %d\n", i, height[i]);
		}
		printf("최댓값은 %d 입니다.\n", maxof(height, number));
		free(height);

		return 0;
}
