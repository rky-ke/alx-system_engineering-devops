#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

extern char **environ;

void exitfunc(void)
{
	printf("\n Clean-up function called\n");
}
int main(int argc, char *argv[])
{
	int count = 0;

	atexit(exitfunc);

	printf("\n");

	while(environ[count++] != NULL)
	{
		//Does some stuff
	}

	_exit(0);
}
