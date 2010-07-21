import core.modules.module_registry
from core.modules.vistrails_module import Module, ModuleError
from core.system import list2cmdline
import os

version = "0.0.1"
name = "Reprocess"
identifier = "utexas.edu.vistrails.reprocess"

class ReprocessRun(object):
    """ReprocessRun is a class that runs the reprocess component"""
    
    _debug = True
    def run(self):
        cmd = [os.getenv("HOME") + '/bright/gui/bin/reprocess']
        cmdline = list2cmdline(cmd)
        if self._debug:
            print cmdline
        result = os.system(cmdline)
        if result != 0:
            raise ModuleError(self, "Execution failed") 

    def write_input(self):
        f = open("Rep_Input.txt", 'w')

        SE_U = self.getInputFromPort("SE_U")
        if 0.0 <= SE_U <= 1.0:
            f.write("SE_U {0}\n".format(SE_U))
            
        SE_PU = self.getInputFromPort("SE_PU")
        if 0.0 <= SE_PU <= 1.0:
            f.write("SE_PU {0}\n".format(SE_PU))
            
        SE_NP = self.getInputFromPort("SE_NP")
        if 0.0 <= SE_NP <= 1.0:
            f.write("SE_NP {0}\n".format(SE_NP)) 
        
        SE_CS = self.getInputFromPort("SE_CS")
        if 0.0 <= SE_CS <= 1.0:
            f.write("SE_CS {0}\n".format(SE_CS))                   
        
        SE_SR = self.getInputFromPort("SE_SR")
        if 0.0 <= SE_SR <= 1.0:
            f.write("SE_SR {0}\n".format(SE_SR))        
       
        SE_AM = self.getInputFromPort("SE_AM")
        if 0.0 <= SE_AM <= 1.0:
            f.write("SE_AM {0}\n".format(SE_AM))        
        
        SE_CM = self.getInputFromPort("SE_CM")
        if 0.0 <= SE_CM <= 1.0:
            f.write("SE_CM {0}\n".format(SE_CM))        
        
        IsosIn = self.getInputFromPort("IsosIn")
        f.write("IsosIn {0}\n".format(IsosIn))    
        
        IsosIn_type = self.getInputFromPort("IsosIn_type")
        f.write("IsosIn_type {0}\n".format(IsosIn_type))      
        
        PassNumber = self.getInputFromPort("PassNumber")
        if 0.0 <= PassNumber <= 10.0:
            f.write("PassNumber {0}\n".format(PassNumber))        
        
        f.close()

        
class Reprocess(Module, ReprocessRun):
    """Reprocess is a module that represents the Reprocessing component in the Bright Fuel Cycle"""
	
    def compute(self):
        self.write_input()
        self.run()
        result = "Rep.h5"
        self.setResult("Output_File", result)


def initialize(*args, **keywords):

    # We'll first create a local alias for the module registry so that
    # we can refer to it in a shorter way.
    reg = core.modules.module_registry.registry

    reg.add_module(Reprocess)
    
    reg.add_input_port(Reprocess, "SE_U",
        (core.modules.basic_modules.Float, 'Uranium Separation Efficiency'),
        defaults="1.0")
   
    reg.add_input_port(Reprocess, "SE_PU",
        (core.modules.basic_modules.Float, 'Plutonium Separation Efficiency'),
        defaults="1.0")
        
    reg.add_input_port(Reprocess, "SE_NP",
        (core.modules.basic_modules.Float, 'Neptunium Separation Efficiency'),
        defaults="1.0")
        
    reg.add_input_port(Reprocess, "SE_CS",
        (core.modules.basic_modules.Float, 'Cesium Separation Efficiency'),
        defaults="1.0")
        
    reg.add_input_port(Reprocess, "SE_SR",
        (core.modules.basic_modules.Float, 'Strontium Separation Efficiency'),
        defaults="1.0")
    
    reg.add_input_port(Reprocess, "SE_AM",
        (core.modules.basic_modules.Float, 'Americium Separation Efficiency'),
        defaults="1.0")  
    
    reg.add_input_port(Reprocess, "SE_CM",
        (core.modules.basic_modules.Float, 'Curium Separation Efficiency'),
        defaults="1.0")                   
    
    reg.add_input_port(Reprocess, "IsosIn",
        (core.modules.basic_modules.String, 'File which contains the mass details'))
    
    reg.add_input_port(Reprocess, "IsosIn_type",
        (core.modules.basic_modules.String, 'Type of the input mass file : text or hdf5'))
   
    reg.add_input_port(Reprocess, "PassNumber",
        (core.modules.basic_modules.Float, 'PassNumber'),
        defaults="0.0")
    
    reg.add_output_port(Reprocess, "Output_File",
	(core.modules.basic_modules.String, 'Name of the HDF5 file created by reprocess'))



