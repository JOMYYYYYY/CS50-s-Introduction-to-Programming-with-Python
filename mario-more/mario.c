#include <cs50.h>
#include <stdio.h>
void print_space(int n);
void print_grid(int n);

int main(void)
{
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);

    // print_space(n);
    // print_grid(n);
    for (int i = 0; i < n; i++)
    {
        print_space(n - i - 1);
        print_grid(i + 1);
        print_space(2);
        print_grid(i + 1);
        printf("\n");
    }
}

void print_space(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf(" ");
    }
}

void print_grid(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("#");
    }
}