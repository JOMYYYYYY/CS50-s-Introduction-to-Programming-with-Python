#include <stdio.h>
#include <string.h>
#include <cs50.h>

int main (void)
{
    string a = get_string("a: ");
    string b = get_string("b: ");

    if (strcmp(a, b) == 0) {
        printf("same\n");
    } else {
        printf("different\n");
    }
}