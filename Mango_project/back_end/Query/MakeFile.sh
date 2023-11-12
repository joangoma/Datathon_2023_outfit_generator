	g++ -c  -O2 -Wall -Wextra  -Wno-sign-compare -std=c++17 Clothes.cc 

	g++ -c  -O2 -Wall -Wextra  -Wno-sign-compare -std=c++17 Query.cc

	g++ -o Query.exe Query.o Clothes.o


rm -f *.o
#rm -f *.exe # Do not comment if you want to test