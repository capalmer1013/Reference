#include <iostream>

using namespace std;

int main(){
	char ref = 'a';
	char *ch = &ref;

	while(true){
		cout << *ch;
		ch += 1;
	}
	return 0;
}
