#include<iostream>
#include<fstream>
#include "day1.h"
#include<string>
#include <stdlib.h>

using namespace std;

int d1p1(string infile) {
	cout << "HERE" << endl;
	ifstream ifs;
	ifs.open(infile);

	int xCoord = 0;
	int yCoord = 0;
	int direction = 0; //0 = n, 1 = e, 2 = s, 3 = w;

	char curDir;
	int curDist;

	while (ifs >> curDir) {
		ifs >> curDist;

		if (direction == 0) {
			if (curDir == 'L') {
				xCoord -= curDist;
				direction = 3;
			}
			else if (curDir == 'R') {
				xCoord += curDist;
				direction = 1;
			}
		}
		else if (direction == 1) {
			if (curDir == 'L') {
				yCoord += curDist;
				direction = 0;
			}
			else if (curDir == 'R') {
				yCoord -= curDist;
				direction = 2;
			}
		}
		else if (direction == 2) {
			if (curDir == 'L') {
				xCoord += curDist;
				direction = 1;
			}
			else if (curDir == 'R') {
				xCoord -= curDist;
				direction = 3;
			}
		}
		else if (direction == 3) {
			if (curDir == 'L') {
				yCoord -= curDist;
				direction = 2;
			}
			else if (curDir == 'R') {
				yCoord += curDist;
				direction = 0;
			}
		}
		ifs >> curDir;
	}

	return abs(xCoord) + abs(yCoord);

}