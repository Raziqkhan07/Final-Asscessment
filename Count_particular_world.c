#include <stdio.h>
#include <stdlib.h>

int main()
{
int num =0;
char word[200];
char string[30];

FILE *in_file = fopen("File01.txt", "r");

if (in_file == NULL)
{
    printf("Error file missing\n");
    exit(-1);
}
printf("Enter the word You Want To Know: \t");
scanf("%s",word);
while(!feof(in_file))
{
    fscanf(in_file,"%s",string);
    if(!strcmp(string,word))
    num++;
}
printf("we found the word %s in the file %d times\n",word,num );
return 0;
}
