// FCComp Test File
//Compile with:
//	g++ -o reprocess reprocess.cpp ../FCComps/Reprocess.cpp ../FCComps/FCComp.cpp ../FCComps/MassStream.cpp ../FCComps/isoname.cpp ../FCComps/genlib.cpp

#include "../../FCComps/Reprocess.h"
#include "../../FCComps/isoname.h"
#include <map>
#include <iostream>
#include <string>
#include <set>

using namespace std;

void Print( string s)

{
	cout << s << "\n";
}



int main()
{
	Print("Test Initialize Empty Reprocessing Facility:");
	Reprocess repempty;
	Print("\tName\t\t\t" + repempty.name);
	Print("");

	int itrack_arr [] = {922350, 922360, 922380, 942390, 952421};
	set<int> itrack (itrack_arr, itrack_arr+5); 	

	Print("Test Initialize SepEffDict Reprocessing Facility:");
	SepEffDict sed; 
	sed[92] = 0.999;
	sed[942390] = 0.99;
	

	return 0;
}
