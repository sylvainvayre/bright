/* FCComp Test File
Compile with:
         g++ -o ../bin/Input Input.cpp -lhdf5 -lz -lm -lhdf5_hl -lhdf5_cpp -lhdf5_hl_cpp ../../FCComps/Reprocess.cpp ../../FCComps/FCComp.cpp ../../FCComps/MassStream.cpp ../../FCComps/isoname.cpp ../../FCComps/bright.cpp
*/

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
typedef map<int, double> mapType;


void Print(string s)
{
	cout << s << "\n";
}

double GetFloatVal(string str)
{
  double num;
  num = atof(str.c_str());
  return(num);
}



mapType GetTab(string path)
{
    
  ifstream file;
  file.open("./txt/input.txt", ios::in);
  int i=0;

  if(file.is_open())
    {
      int rank;
      string* tab = NULL;
      tab = new string[100];
     
      while (file.eof() == false)
	{
	  file >> tab[i];
	  i++;
	}

      
      int k=0;
      mapType itab;
      
      for ( k=0 ; k < sizeof(tab) ; k++)
	{
	  itab[isoname::LLAAAM_2_zzaaam(tab[2*k])] = GetFloatVal(tab[2*k+1]);
	}	 
      return (itab);
      

    }
  else
    {
      cout << "Error : File not found!" << endl;
      mapType n;
      n[0]=0;
      return n;
    }

  }




int main()
{
  	Print("Test Initialize Empty Reprocessing Facility:");
  	Reprocess repempty;
  	Print("\tName\t\t\t" + repempty.name);
  	Print("");

  	int itrack_arr [] = {922350, 922360, 922380, 942390, 952421};
  	set<int> itrack (itrack_arr, itrack_arr+5);
  
 	 string path1 = "../txt/input.txt";
  	mapType MyTab;
	
  	MyTab = GetTab(path1);

 

  	map<int,float>::const_iterator
  	  mapBegin (MyTab.begin()),
  	  mapEnd(MyTab.end());
  	for(;mapBegin!=mapEnd;++mapBegin) std::cout << mapBegin->first << '\t' << mapBegin->second << std::endl;

 
  return 0;

}

