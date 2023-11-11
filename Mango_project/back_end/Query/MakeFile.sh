	g++ -c  -O2 -Wall -Wextra  -Wno-sign-compare -std=c++17 Clothes.cc 

	g++ -c  -O2 -Wall -Wextra  -Wno-sign-compare -std=c++17 Outfit.cc 

	g++ -c  -O2 -Wall -Wextra  -Wno-sign-compare -std=c++17 main.cc

	g++ -o program.exe main.o Outfit.o Clothes.o


rm -f *.o
#rm -f *.exe # Do not comment if you want to test