#include "helpers.h"
#include <stdlib.h>
#include <stdio.h>




void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    BYTE ZimaBlue;
    BYTE ChinaRed;
    BYTE NavyGreen;

    sscanf("5BC2E7", "%hhx", &ZimaBlue);
    sscanf("ff2121", "%hhx", &ChinaRed);
    sscanf("0A0A85", "%hhx", &NavyGreen);

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (image[i][j].rgbtRed == 0x00 && image[i][j].rgbtBlue == 0x00 && image[i][j].rgbtGreen == 0x00)
            {
                image[i][j].rgbtBlue = ZimaBlue;
                image[i][j].rgbtRed = ChinaRed;
                image[i][j].rgbtGreen = NavyGreen;
            }
        }
    }
}
