#include <stdio.h>
#include <stdlib.h>

void win(){
    puts("I'm in");
    FILE *file = fopen("flag.txt", "r");
    if (file) {
        char ch;
        while ((ch = fgetc(file)) != EOF) putchar(ch);
        fclose(file);
    }
	exit(0);
}


int main() {
    char buffer[60];
    puts("Hello world, this is my first C program");
    printf("Address of buffer: %p\n", (void*) buffer);
    printf("Address of win() function: %p\n", (void*) win);
    printf("Address of instruction pointer: %p\n", __builtin_return_address(0));

    void * ptr = __builtin_return_address(0);
    printf("the other ptr = %p\n", ptr);
    fgets(buffer, 0x60, stdin);
    return 0;
}
