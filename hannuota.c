#include <stdio.h>
int g_num = 0;

void hanoi(int n,char A,char B, char C){
	if(n == 1){
		printf("Move sheet %d from %c to %c\n",n,A,C);
		g_num += 1;
	}
	else{
		hanoi(n-1,A,C,B);
		printf("Move sheet %d from %c to %c\n", n, A, C);
		g_num += 1;
		hanoi(n-1,B,A,C);
	}
}

int main(){
	int n;
	printf("请输入盘数:");
	scanf("%d", &n);
	hanoi(n, 'A', 'B', 'C');
	printf("共计 %d 步\n", g_num);
	return 0;
}
