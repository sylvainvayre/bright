/* FCComp Test File
Compile with:
         g++ -o ../bin/Template2 template2.cpp -lhdf5 -lz -lm -lhdf5_hl -lhdf5_cpp -lhdf5_hl_cpp ../../FCComps/Reprocess.cpp ../../FCComps/FCComp.cpp ../../FCComps/MassStream.cpp ../../FCComps/isoname.cpp ../../FCComps/bright.cpp
*/

#include "Template.h"


/*-------------------------------------------*/
/*------------Public Functions---------------*/
/*-------------------------------------------*/


// Function allowing us to get the value of a string only
//   composed by numbers.
double Template::GetFloatVal(string str)
{
	double num;
	num = atof(str.c_str());
	return(num);
}


// Function reading a file from its name and returning
//   a standard map which type is <string, string>.
mapType Template::readFile(File name)
{
    
	ifstream file;
	file.open(name, ios::in);
	int i=0;

// Testing the opening of the file :
  	if(file.is_open())
	  {
      
		string* tab = NULL;
		tab = new string[100];
		int rank;

     
		while (file.eof() == false)			// Putting the strings from the file to a tab.
		  {
			file >> tab[i];
			rank = i;
			i++;
		  }

		int k=0;
		mapType itab;
      
		for ( k=0 ; k < rank + 1 ; k++)		// Convert the previous tab into the standard map.
		  {
			itab[tab[2*k]] = tab[2*k+1];
		  }	
 
		return (itab);
      
	  }
	else
	  {
		cout << "Error : File not found!" << endl;	// Error message if the specified file is wrong.
		mapType n;
		n[""]="";
		return n;
	  }

}


// Print function
void Template::Print(mapType m)
{
	mapType::iterator mapIterator;
  	for(mapIterator = m.begin() ; mapIterator != m.end() ; mapIterator++)
	  {
		cout << mapIterator->first << " \t \t " << mapIterator->second << endl;
	  }
}


