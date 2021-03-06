"""Storage Component tests"""

from unittest import TestCase
import nose 

from nose.tools import assert_equal, assert_not_equal, assert_raises, raises, \
    assert_almost_equal, assert_true, assert_false

import os
import warnings
import tables as tb
import numpy as np

import BriPy
Storage = BriPy.Storage
MassStream = BriPy.MassStream

class TestStorageConstructors(TestCase):
    """Tests that the storage component constructors work."""

    @classmethod
    def teardown_class(cls):
        for f in os.listdir('.'):
            if "Isos.txt" in f:
                os.remove(f)
            elif "Params.txt" in f:
                os.remove(f)
            elif f in [".h5", "s.h5"]:
                os.remove(f)

    def test_Storage_1(self):
        s = Storage()
        assert_equal(s.name, '')
        assert_equal(s.params2track, ["Mass"])

    def test_Storage_2(self):
        s = Storage("s")
        assert_equal(s.name, 's')
        assert_equal(s.params2track, ["Mass"])


class TestStorageAttributes(TestCase):
    """Tests that the fuel cycle component attributes work."""

    @classmethod
    def teardown_class(cls):
        for f in os.listdir('.'):
            if "Isos.txt" in f:
                os.remove(f)
            elif "Params.txt" in f:
                os.remove(f)
            elif f in [".h5", "s.h5"]:
                os.remove(f)

    def test_decay_time(self):
        s = Storage()
        s.decay_time = 0.0
        assert_equal(s.decay_time, 0.0)
        s.decay_time = 628        
        assert_equal(s.decay_time, 628.0)

    def test_params2track(self):
        s = Storage()
        assert_equal(s.params2track, ["Mass"])
        s.params2track = ["Om nom nom"]
        assert_equal(s.params2track, ["Om nom nom"])
                        

class TestStorageMethods(TestCase):
    """Tests that the fuel cycle component methods work."""

    @classmethod
    def teardown_class(cls):
        for f in os.listdir('.'):
            if "Isos.txt" in f:
                os.remove(f)
            elif "Params.txt" in f:
                os.remove(f)
            elif f in [".h5", "s.h5"]:
                os.remove(f)

    def test_doCalc_1(self):
        BriPy.isos2track([922350, 922380, 942390])
        s = Storage()
        s.decay_time = 0.0
        s.IsosIn = MassStream({942390: 1.0})
        s.doCalc()
        assert_equal(s.IsosOut.mass, 1.0)
        assert_almost_equal(s.IsosOut.comp[942390], 1.0) 

    def test_doCalc_2(self):
        BriPy.isos2track([922350, 922380, 942390])
        s = Storage()
        s.decay_time = 0.0
        s.doCalc(MassStream({942390: 1.0}))
        assert_equal(s.IsosOut.mass, 1.0)
        assert_equal(s.IsosOut.comp[942390], 1.0) 

    def test_doCalc_3(self):
        BriPy.isos2track([922350, 922380, 942390])
        s = Storage()
        s.IsosIn = MassStream({942390: 1.0})
        s.doCalc(24110*365.25*24*3600)
        assert(s.IsosOut.mass < 1.0)
        assert_almost_equal(s.IsosOut.comp[942390], 0.5, 3) 

    def test_doCalc_4(self):
        BriPy.isos2track([922350, 922380, 942390])
        s = Storage()
        s.doCalc(MassStream({942390: 1.0}), 24110*365.25*24*3600)
        assert(s.IsosOut.mass < 1.0)
        assert_almost_equal(s.IsosOut.comp[942390], 0.5, 3) 

    def test_setParams(self):
        BriPy.isos2track([922350, 922380, 942390])
        s = Storage()
        s.doCalc(MassStream({942390: 1.0}), 24110*365.25*24*3600)
        s.setParams()
        assert_equal(s.ParamsIn["Mass"],  1.00)
        assert(0.5 < s.ParamsOut["Mass"] < 1.0)
        

if __name__ == "__main__":
    nose.main()
