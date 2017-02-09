#include <iostream>
#include <csignal>

using namespace std;

void signalHandler( int signum )
{
	if(signum != SIGSEGV)
	{
		cout << "Signum: " << signum << '\n';
	}
	return;
}

int main()
{
	char a[10];
	int i = 0;

	signal(SIGINT, signalHandler);  // Interrupt
	signal(SIGABRT, signalHandler); // call to abort
	signal(SIGFPE, signalHandler);  // arithmatic error
	signal(SIGILL, signalHandler);  // illegal isntruction
	signal(SIGSEGV, signalHandler); // segfault
	signal(SIGTERM, signalHandler); // termination request


	while(true)
	{
		cout << a[i];
		if(!a[i]) // if a[i] is null
		{
			if(!(i%100))  // if i is divisible by 100
			{
				cout << i << '\n';
			}
		}

		i++;
	}
	return 0;
}
