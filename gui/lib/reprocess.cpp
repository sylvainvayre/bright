/* FCComp Test File
Compile with:
         g++ -o ../bin/reprocess reprocess.cpp -lhdf5 -lz -lm -lhdf5_hl -lhdf5_cpp -lhdf5_hl_cpp ../../FCComps/Reprocess.cpp ../../FCComps/FCComp.cpp ../../FCComps/MassStream.cpp ../../FCComps/isoname.cpp ../../FCComps/bright.cpp Template.cpp
*/
#include "../../FCComps/MassStream.h"
#include "../../FCComps/Reprocess.h"
#include "Template.h"

/*-------------------------------------------*/
/*----------------Functions------------------*/
/*-------------------------------------------*/

void PrintS(SepEffDict s)
{
	SepEffDict::iterator SepEffIterator;
  	for(SepEffIterator = s.begin() ; SepEffIterator != s.end() ; SepEffIterator++)
	  {
		cout << SepEffIterator->first << " \t " << SepEffIterator->second << endl;
	  }
}


SepEffDict getSepEff(Template temp, File name)
{		
	mapType m;
	m=temp.readFile(name);

	SepEffDict sep;
	
	mapType:: iterator mapBegin = m.begin();
	
	while( mapBegin!=m.end() )
	  {
	    if ( mapBegin->first.find("SE_") == 0 )
	      {	
		sep[isoname::LLzz[(mapBegin->first.substr(mapBegin->first.find_first_not_of( "SE_")))]] = temp.GetFloatVal(mapBegin->second);
	      }		
	    mapBegin++;
	  }

	return(sep);
}
	

/*-------------------------------------------*/
/*-------------------Main--------------------*/
/*-------------------------------------------*/
int main()
{
	//(char*)(PWD + (string)"Rep_Input.txt").c_str()
	string PWD = getenv("PWD");

	FCComps::write_text = 0;
	FCComps::write_hdf5 = 1;
	
// Get and display special parameters for Reprocess :
	File repInput = "Rep_Input.txt";
	Template temp;
	mapType m;
	m=temp.readFile(repInput);
	SepEffDict sepeff = getSepEff(temp, repInput);

	cout << endl;
	cout << "Separation Efficiency Dictionnary :" << endl;
	cout << endl;
	PrintS(sepeff);
	cout << endl;

	File load = "load.txt";
	FCComps::load_isos2track_text(load);

// Get the MassStream :

	MassStream inStream;	

	if (m["IsosIn_type"].compare("text") == 0)
		{
			//(char*)m["IsosIn"].c_str())
			inStream.load_from_text((char*)m["IsosIn"].c_str());
		}
	else if (m["IsosIn_type"].compare("hdf5") == 0)
		{	
			//m[PWD + "IsosIn"]
			inStream.load_from_hdf5(m["IsosIn"], "/IsosOut");
		}

	inStream.mass = -1;
	inStream.norm_comp_dict();
	
	cout << endl;
	inStream.Print();
	cout << endl;

	Reprocess rep(sepeff,"Rep");
	rep.PassNum = atoi((char*)m["PassNumber"].c_str());
	rep.doCalc(inStream);
	
	rep.writeout();

	return 0;
}
