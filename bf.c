#include <stdio.h>

char tape[4000];
char *i;
int main(){
  i=tape;
  (*i)++;
  (*i)++;
  (*i)++;
  i++;
}
