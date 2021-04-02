#include <stdio.h>
#include <cs50.h>

void buildPyramidRightAligned(int);

/*
void buildPyramidLeftAligned(int);
void buildPyramidRightAlignedWithDots(int);
*/

int main(void)
{
    int height;

    do
    {
        height = get_int("Define height of pyramid: ");
    } while (height > 8 || height < 1);

    buildPyramidRightAligned(height);

    /**
    buildPyramidLeftAligned(height);
    buildPyramidRightAlignedWithDots(height);
    **/
}

void buildPyramidRightAligned(int height)
{
    int v = 1;
    // Building pyramid
    for (int a = 0; a < height; a++)
    {
        // Print " " (height - 1) number of times
        for (int i = 0; i < height - v; i++)
        {
            printf(" ");
        }

        // Print "#" v number of times -->
        //the variable "v" is here the difference between the height (e.g. 8) and the spaces that got printed in the first for-loop (spaces: 7 --> diff: 1)
        for (int j = 0; j < v; j++)
        {
            printf("#");
        }

        printf("\n"); // Get into the new line

        v++;
    }
}

/*
void buildPyramidLeftAligned(int height)
{
    int v = height - 1;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < height - v; j++)
        {
            printf("#");
        }
        v--;
        printf("\n");
    }
}

void buildPyramidRightAlignedWithDots(int height)
{
    int v = 1;
    // Building pyramid
    for (int a = 0; a < height; a++)
    {
        // Print " " (height - 1) number of times
        for (int i = 0; i < height - v; i++)
        {
            printf(".");
        }

        // Print "#" v number of times -->
        //the variable "v" is here the difference between the height (e.g. 8) and the spaces that got printed in the first for-loop (spaces: 7 --> diff: 1)
        for (int j = 0; j < v; j++)
        {
            printf("#");
        }

        printf("\n"); // Get into the new line

        v++;
    }
}
*/