#include <stdio.h>

int main(int argc, char *argv[]) {
	int array[500];
	for (int i=0; i<500; i++) {
		array[i] = 500-i;
	}

	for (int i = 499; i >= 0; i--) {
		printf("%i\n", array[i]+7);
		printf("%i\n", array[i] - 5);
		printf("%i\n", array[i] + 20);
	}


	return 0;
}
