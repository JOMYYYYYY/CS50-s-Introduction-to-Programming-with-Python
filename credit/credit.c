#include <cs50.h>
#include <stdio.h>
int length(long n);
int sum_digit(int n);
int start_number_1(long n);
int start_number_2(long n);

int main(void)
{
    long n = get_long("Number: ");
    const long number = n;
    int sum1 = 0;
    int sum2 = 0;
    while(n > 0)
    {
        sum2 = sum2 + n % 10;
        n = n / 10;
        //printf("sum2 = %d\n", sum2);
        sum1 = sum1 + sum_digit((n % 10)*2);
        n = n / 10;
    }
    int sum = sum1 + sum2;
    //printf("%d", sum);
    if (sum % 10 == 0)
    {
        if ((start_number_1(number) == 4 ) && (13 <= length(number) && length(number) <= 16))
        {
            printf("VISA\n");
            return 0;
        }
        if ((start_number_2(number) == 34 || start_number_2(number) == 37) && (length(number) == 15))
        {
            printf("AMEX\n");
            return 0;
        }
        if ((start_number_2(number) == 51 || start_number_2(number) == 52 || start_number_2(number) == 53 || start_number_2(number) == 54 || start_number_2(number) == 55) && (length(number) == 16))
        {
            printf("MASTERCARD\n");
            return 0;
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }


}

int length(long n)
{
    int i = 0;
    while(n > 0)
    {
        n = n / 10;
        i++;
    }
    return i;
}

int sum_digit(int n)
{
    int sum = 0;
    while(n > 0)
    {
        sum = sum + (n % 10);
        n = n / 10;
    }
    return sum;
}
int start_number_1(long n)
{
    while(n >= 10)
    {
        n = n / 10;
    }
    return n;
}

int start_number_2(long n)
{
    while(n >= 100)
    {
        n = n / 10;
    }
    return n;
}