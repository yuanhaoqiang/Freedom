#include <stdio.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <unistd.h>
#include <wait.h>

//#include "hardware.h"

int main(void)
{
	int pid, child;
	char *args[] = {"\bin\echo", "hello world!", NULL};


//	if(sys_init() == 1){
//		printf("sys_init success!\r\n");
//	}else{
//		printf("sys_inte error!\r\n");
//		exit(1);
//	}

	if((child = fork()) == -1){
		perror("fork");
		exit(EXIT_FAILURE);
	}else if(child == 0){
		printf("child pid = %d\r\n", getpid());
	
	//	execlp("echo","sh", "hello world!", NULL);
		execlp("python", "sh", "main.py", NULL);
		//		execve("\\bin\\sh", args, NULL);
//		sleep(2);
		printf("error! child cant come here!!!\r\n");

	}else{
		printf("parent pid =%d\r\n", getpid());
//		sleep(1);
	
//		execlp("echo", "hello world!", NULL);
		execlp("ps", "-a", NULL);
		wait(&child);
//		exit(EXIT_SUCCESS);
	}
	wait(&child);
	//sleep(2);
	exit(EXIT_SUCCESS);
}
