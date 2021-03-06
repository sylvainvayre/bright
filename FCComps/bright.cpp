// General Library 

#include "bright.h"

//Bright Globals

std::string bright::BRIGHT_DATA = "";

void bright::BrightStart()
{
#ifdef _WIN32
    char * tmpBRIGHT_DATA;
    size_t lenBRIGHT_DATA;
    errno_t errBRIGHT_DATA = _dupenv_s(&tmpBRIGHT_DATA, &lenBRIGHT_DATA, "BRIGHT_DATA");
    if (errBRIGHT_DATA) std::cout << "BRIGHT_DATA Enviromental Variable could not be found\n";
    BRIGHT_DATA = (std::string) tmpBRIGHT_DATA;
#else
    BRIGHT_DATA = getenv("BRIGHT_DATA");
#endif
    return;
};

//String Transformations
std::string bright::to_str (int t)
{
    std::stringstream ss;
    ss << t;
    return ss.str();
}

std::string bright::to_str (double t)
{
    std::stringstream ss;
    ss << t;
    return ss.str();
}

std::string bright::to_str (bool t)
{
    std::stringstream ss;
    ss << t;
    return ss.str();
}

int bright::to_int (std::string s)
{
    return atoi( s.c_str() );
}

double bright::to_dbl (std::string s)
{
    return strtod( s.c_str(), NULL );
}

std::string bright::ToUpper(std::string strToConvert)
{
    //change each element of the string to upper case.
    for(unsigned int i = 0; i < strToConvert.length(); i++)
    {
        strToConvert[i] = toupper(strToConvert[i]);
    }
    return strToConvert;
}

std::string bright::ToLower(std::string strToConvert)
{
    //change each element of the string to lower case
    for(unsigned int i=0;i<strToConvert.length();i++)
    {
        strToConvert[i] = tolower(strToConvert[i]);
    }
    return strToConvert;
}

std::string bright::getFlag(char line[], int max_l)
{
    char tempflag [10];
    for (int i = 0; i < max_l; i++)
    {
        if (line[i] == '\t' || line[i] == '\n' || line[i] == ' ' || line[i] == '\0')
        {
            tempflag[i] = '\0';
            break;
        }
        else
            tempflag[i] = line[i];
    }
    return std::string (tempflag);
}

std::string bright::Strip(std::string strToConvert, std::string strStrip)
{
    //change each element of the string to lower case
    int n_found = strToConvert.find(strStrip);
    while ( 0 <= n_found )
    {
        strToConvert.erase( n_found , strStrip.length() );
        n_found = strToConvert.find(strStrip);
    }
    return strToConvert;
}

std::string bright::MultiStrip(std::string strToConvert, std::string strMultiStrip)
{
    //change each element of the string to lower case
    for (int i = 0; i < strMultiStrip.length(); i++ )
    {
        strToConvert = Strip(strToConvert, strMultiStrip.substr(i, 1) );
    }
    return strToConvert;
}

std::string bright::LastChar(std::string s)
{
    //Returns the last character in a string.
    return s.substr(s.length()-1, 1);
}

std::string bright::SubFromEnd(std::string s, int n, int l)
{
    //Returns the splice of a string using negative indices.
    return s.substr(s.length()+n, l);
}

bool bright::ChainGreaterCompare(int a, int b, int c)
{
    //returns true id a <= b <= c and flase otherwise.
    return (a <= b && b <= c); 
}

bool bright::SubInString(std::string s, std::string sub)
{
    //Returns a boolean based on if the sub is in s.
    int n = s.find(sub);
    return ( 0 <= n && n < s.length() );
}

//Array Helpers
int bright::find_index_char(char * val, char ** arr, int arr_len)
{
    //Finds an element 'val' in array 'arr'
    //returns the index of val's first location
    //returns -1 if not found.
    //For Arrays of char strings

    if (arr_len < 0)
        arr_len = length_array(arr);

    for (int n = 0; n < arr_len; n++)
    {
        if (strcmp(arr[n], val) == 0)
            return n;
    };

    return -1;
};


//Math Helpers
const double bright::pi = 3.14159265359;
const double bright::N_A = 6.0221415 * pow(10.0, 23);
const double bright::bpcm2 = pow(10.0, -24); 

double bright::slope (double x2, double y2, double x1, double y1)
{
    //Finds the slope of a line.
    return (y2 - y1) / (x2 - x1);
};

double bright::SolveLine (double x, double x2, double y2, double x1, double y1)
{
    return (slope(x2,y2,x1,y1) * (x - x2)) + y2;
};

double bright::TANH(double x)
{
    return tanh(x);
};

double bright::COTH(double x)
{
    return 1.0 / tanh(x);
};
