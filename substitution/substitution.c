#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
char cipher_char (char n, string intext);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    string key = argv[1];
    for (int i = 0; i < 26; i++)
    {
        if (!(isalpha(key[i])))
        {
            printf("Your input is not alphabetical.\n");
            return 1;
        }
    }
    for (int i = 0; i < 26; i++)
    {
        if isupper(key[i])
        {
            key[i] = tolower(key[i]);
        }
    }
    for (int i = 0; i < 25; i++)
    {
        for (int j = i + 1; j < 26; j++)
        {
            if (key[i] == key[j])
            {
                printf("same char in a key.");
                return 1;
            }
        }
    }
    string intext = get_string("plaintext: ");
    string outtext = intext;
    for(int i = 0; i < strlen(intext); i++)
    {
        outtext[i] = cipher_char(intext[i], key);
    }
    printf("ciphertext: %s\n", outtext);
    return 0;



}

char cipher_char (char n, string intext)
{
    string upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string lowerCase = "abcdefghijklmnopqrstuvwxyz";
    int index = 0;
    for (index = 0; index < 26; index++)
    {
        if (n == upperCase[index] || n == lowerCase[index])
        {
            if isupper(n)
            {
                return toupper(intext[index]);
            }
            else
            {
                return tolower(intext[index]);
            }
        }
    }
    return n;
}