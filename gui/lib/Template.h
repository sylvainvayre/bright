/*-------------------------------------------*/
/*------------Includes & Typedef-------------*/
/*-------------------------------------------*/

#include <iostream>
#include <stdlib.h> 
#include <string>
#include <fstream>
#include "../../FCComps/Reprocess.h"
#include "../../FCComps/isoname.h"
#include <map>
#include <set>
#include "../../FCComps/bright.h"


using namespace std;
typedef map<string, string> mapType;
typedef char * File;


/*-------------------------------------------*/
/*--------------Template Class---------------*/
/*-------------------------------------------*/

class Template : public FCComp
{

// Public functions :
public:
	double GetFloatVal(string);				//  Get the value of a string

	mapType readFile(File);				// Convert a text file into a <string, double> map.

	void Print(mapType);

};
