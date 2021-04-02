#include <stdio.h>
//#include <cs50.h>

int main(void)
{
    string answer = get_string("What's your name? ");
    printf("Hello %s", answer);
}

//Does not work in vs-code, but works in CS50 IDE