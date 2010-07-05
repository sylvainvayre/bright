// MassStream.cpp
// The very central MassStream class

#include "MassStream.h"

/***************************/
/*** Protected Functions ***/
/***************************/

double MassStream::get_comp_sum ()
{
    //Sums the weights in the composition dictionary
    double sum = 0.0;
    for (CompIter i = comp.begin(); i != comp.end(); i++)
    {
        sum = sum + i->second;
    }
    return sum;
};

void MassStream::norm_comp_dict ()
{
    double sum = get_comp_sum();
    if (sum != 1.0) 
    {
        for (CompIter i = comp.begin(); i != comp.end(); i++)
        {
            i->second = i->second / sum;
        }
    }

    if (mass < 0.0) 
        mass = sum;

    return;
}

void MassStream::read_from_file (char * fchar)
{
    std::ifstream f;

    //Make sure that the file we are reading the mass stream from is reallyt there.
    try
    {
        f.open(fchar);
    }
    catch (...)
    {
        std::cout << "!!!Warning!!! Cannot find " << fchar << "!\n";
        return;
    }

    while ( !f.eof() )
    {
        std::string isostr, wgtstr;
        f >> isostr;
        if (0 < isostr.length())
        {
            f >> wgtstr;
            try 
            {
                comp[isoname::mixed_2_zzaaam(isostr)] = bright::to_dbl(wgtstr);
            }
            catch (isoname::NotANuclide e)
            {
                std::cout << "!!!Warning!!! " << isostr << " in " << fchar << " is not a nuclide!\n";
            }
        }
    }
    f.close();
    return;
}


/************************/
/*** Public Functions ***/
/************************/

/*--- Constructors ---*/

MassStream::MassStream()
{
    //Empty MassStream constructor
    mass = 0.0;
    name = "";
}

MassStream::MassStream(CompDict cd, double m, std::string s)
{
    //Initializes the mass stream based on an isotopic component dictionary.
    comp = cd;
    mass = m;
    name = s;

    norm_comp_dict();
}

MassStream::MassStream(char * fchar, double m, std::string s)
{
    //Initializes the mass stream based on an isotopic composition file with a (char *) name.
    mass = m;
    name = s;

    read_from_file(fchar);

    norm_comp_dict();
}

MassStream::MassStream(std::string fstr, double m, std::string s)
{

    //Initializes the mass stream based on an isotopic composition file with a (char *) name.
    mass = m;
    name = s;

    read_from_file( (char *) fstr.c_str() );

    norm_comp_dict();
}

/*--- Function definitions ---*/

void MassStream::Print()
{
    //Print the Mass Stream to stdout
    std::cout << "Mass Stream: " << name << "\n";
    std::cout << "\tMass: " << mass << "\n";
    std::cout << "\t---------\n";
        for( CompIter i = comp.begin(); i != comp.end(); i++)
        {
                std::cout << "\t" << isoname::zzaaam_2_LLAAAM(i->first) << "\t" << i->second << "\n";
        }
}

std::ostream& operator<<(std::ostream& os, MassStream ms)
{
    //Print the Mass Stream to stdout
    os << "Mass Stream: " << ms.name << "\n";
    os << "\tMass: " << ms.mass << "\n";
    os << "\t---------\n";
        for( CompIter i = ms.comp.begin(); i != ms.comp.end(); i++)
        {
        os << "\t" << isoname::zzaaam_2_LLAAAM( i->first ) << "\t" << i->second << "\n";
        };
    return os;
}


void MassStream::Normalize ()
{
    //Normalizes the mass
    mass = 1.0;
}

CompDict MassStream::multByMass()
{
    //bypass calculation if already normalized.
    if (mass == 1.0)
        return comp;
    
    CompDict cd;
    for (CompIter i = comp.begin(); i != comp.end(); i++)
    {
        cd[i->first] = (i->second) * mass;
    }
    return cd;
}

/*--- Stub-Stream Computation ---*/

MassStream MassStream::getSubStream (std::set<int> iset,  std::string n)
{
    //Grabs a substream from this stream based on a set of integers.
    //Integers can either be of zzaaam form -OR- they can be a z-numer (is 8 for O, 93 for Np, etc).
    //n is the name of the new stream.

    CompDict cd;
    for (CompIter i = comp.begin(); i != comp.end(); i++)
    {
        if ( 0 < iset.count(i->first) )
            cd[i->first] = (i->second) * mass;
        else if ( 0 < iset.count((i->first)/10000) )
            cd[i->first] = (i->second) * mass;
        else
            continue;
    }
    return MassStream (cd, -1, n);
}

MassStream MassStream::getSubStream (std::set<std::string> sset,  std::string n)
{
    //Grabs a substream from this stream based on a set of strings.
    //Strings can be of any form.
    using namespace isoname;

    std::set<int> iset;
    for (std::set<std::string>::iterator i = sset.begin(); i != sset.end(); i++)
    {
        //Is of form LL?
        if (0 < LLzz.count(*i) )
            iset.insert( LLzz[*i] );
        else
        {
            try
            {
                if (0 < zzLL.count( bright::to_int(*i)) )
                    //Is of form zz?
                    iset.insert( bright::to_int(*i) );
                else
                    //Is of a valid full nuclide form?
                    iset.insert( mixed_2_zzaaam(*i) );
            }
            catch (std::exception& e1)
            {
                try
                {
                    //Is of a valid full nuclide form?
                    iset.insert( mixed_2_zzaaam(*i) );
                }
                catch (std::exception& e2)
                {
                    std::cout << "Skipping the following which could not be converted to a nuclide nor an element: " << *i << ".\n"; 
                }
            }
        }
    }
    return getSubStream(iset, n);
}

MassStream MassStream::getU (std::string n)
{
    //Returns a mass stream of Uranium that is a subset of this mass stream.
    std::set<int> iso_set;
    iso_set.insert(92);
    return getSubStream (iso_set, n);
}

MassStream MassStream::getPU (std::string n)
{
    //Returns a mass stream of Plutonium that is a subset of this mass stream.
    std::set<int> iso_set;
    iso_set.insert(94);
    return getSubStream (iso_set, n);
}

MassStream MassStream::getLAN (std::string n)
{
    //Returns a mass stream of Lanthanides that is a subset of this mass stream.
    return getSubStream (isoname::lan, n);
}

MassStream MassStream::getACT (std::string n)
{
    //Returns a mass stream of Lanthanides that is a subset of this mass stream.
    return getSubStream (isoname::act, n);
}

MassStream MassStream::getTRU (std::string n)
{
    //Returns a mass stream of Lanthanides that is a subset of this mass stream.
    return getSubStream (isoname::tru, n);
}

MassStream MassStream::getMA (std::string n)
{
    //Returns a mass stream of Lanthanides that is a subset of this mass stream.
    return getSubStream (isoname::ma, n);
}

MassStream MassStream::getFP (std::string n)
{
    //Returns a mass stream of Lanthanides that is a subset of this mass stream.
    return getSubStream (isoname::fp, n);
}


/*--- Overloaded Operators ---*/

MassStream operator+ (MassStream x, double y)
{
    //Overloads x + y
    return MassStream (x.get_comp(), x.get_mass() + y, x.get_name());
}

MassStream operator+ (double x, MassStream y)
{
    //Overloads x + y
    return MassStream (y.get_comp(), x + y.get_mass(), y.get_name());
}

MassStream operator+ (MassStream x, MassStream y)
{
    //Overloads x + y
    CompDict cd;
    CompDict xwgt = x.multByMass();
    CompDict ywgt = y.multByMass();

    for (CompIter i = xwgt.begin(); i != xwgt.end(); i++)
    {
        if ( 0 < ywgt.count(i->first) )
            cd[i->first] = xwgt[i->first] + ywgt[i->first];
        else
            cd[i->first] = xwgt[i->first];
    }
    
    for (CompIter i = ywgt.begin(); i != ywgt.end(); i++)
    {
        if ( 0 == cd.count(i->first) )
            cd[i->first] = ywgt[i->first];			
    }
    
    return MassStream (cd);
}

MassStream operator* (MassStream x, double y)
{
    //Overloads x * y
    return MassStream (x.get_comp(), x.get_mass() * y, x.get_name());
}

MassStream operator* (double x, MassStream y)
{
    //Overloads x * y
    return MassStream (y.get_comp(), x * y.get_mass(), y.get_name());
}

MassStream operator/ (MassStream x, double y)
{
    //Overloads x / y
    return MassStream (x.get_comp(), x.get_mass() / y, x.get_name());
}
