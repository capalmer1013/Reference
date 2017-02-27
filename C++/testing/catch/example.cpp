#define CATCH_CONFIG_MAIN  // this tells catch to provide a main() - only do this in once cpp file
#include "catch.hpp"

unsigned int Factorial( unsigned int number) {
	if(number == 0) return 1;
	return number <= 1 ? number: Factorial(number-1) * number;
}

TEST_CASE( "Factorials are computed", "[factorial]") {
	REQUIRE( Factorial(0) == 1);
	REQUIRE( Factorial(1) == 1);
	REQUIRE( Factorial(2) == 2);
	REQUIRE( Factorial(3) == 6);
	REQUIRE( Factorial(10) == 3628800);
}

