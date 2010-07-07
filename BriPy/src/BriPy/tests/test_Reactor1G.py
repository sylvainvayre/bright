"""Reactor1G Component and Helper Class tests"""

from unittest import TestCase
import nose 

from nose.tools import assert_equal, assert_not_equal, assert_raises, raises, \
    assert_almost_equal, assert_true, assert_false

import os
import warnings
import tables as tb
import numpy as np

import BriPy


Reactor1G = BriPy.Reactor1G
FluencePoint = BriPy.FluencePoint
ReactorParameters = BriPy.ReactorParameters
MassStream = BriPy.MassStream

default_rp = BriPy.ReactorParameters()
default_rp.batches = 3
default_rp.flux = 2*(10**14)
default_rp.FuelForm = {"IHM": 1.0, "O16": 2.0}
default_rp.CoolantForm = {"H1": 2.0, "O16": 1.0}
default_rp.FuelDensity = 10.7
default_rp.CoolantDensity = 0.73
default_rp.pnl = 0.98
default_rp.BUt = 50.0
default_rp.useDisadvantage = True
default_rp.LatticeType = 'Cylindrical'
default_rp.HydrogenRescale = True
default_rp.Radius = 0.411
default_rp.Length = 0.7
default_rp.open_slots = 123
default_rp.total_slots = 180

def general_teardown():
    for f in os.listdir('.'):
        if "Isor1g.txt" in f:
            or1g.remove(f)
        elif "Paramr1g.txt" in f:
            os.remove(f)
        elif f in [".h5", "r1g.h5"]:
            os.remove(f)


class TestFluencePoint(TestCase):
    """Tests the fluence point Reactor1G helper clasr1g."""

    def test_constructor(self):
        fp = FluencePoint()
        assert_equal(fp.f, 0)
        assert_equal(fp.F, 0.0)
        assert_equal(fp.m, 0.0)

    def test_f(self):
        fp = FluencePoint()
        fp.f = 10
        assert_equal(fp.f, 10)

    def test_F(self):
        fp = FluencePoint()
        fp.F = 10.0
        assert_equal(fp.F, 10.0)

    def test_m(self):
        fp = FluencePoint()
        fp.m = 10.0
        assert_equal(fp.m, 10.0)


class TestReactorParameters(TestCase):
    """Tests the reactor parameters Reactor1G helper clasr1g."""

    def test_constructor(self):
        rp = ReactorParameters()
        assert_equal(rp.batches, 0)
        assert_equal(rp.flux, 0.0)
        assert_equal(rp.FuelForm, {})
        assert_equal(rp.CoolantForm, {})
        assert_equal(rp.FuelDensity, 0.0)
        assert_equal(rp.CoolantDensity, 0.0)
        assert_equal(rp.pnl, 0.0)
        assert_equal(rp.BUt, 0.0)
        assert_false(rp.useDisadvantage)
        assert_equal(rp.LatticeType, '')
        assert_false(rp.HydrogenRescale)
        assert_equal(rp.Radius, 0.0)
        assert_equal(rp.Length, 0.0)
        assert_equal(rp.open_slots, 0.0)
        assert_equal(rp.total_slots, 0.0)

    def test_batches(self):
        rp = ReactorParameters()
        rp.batches = 3
        assert_equal(rp.batches, 3)

    def test_flux(self):
        rp = ReactorParameters()
        rp.flux = 2*(10**14)
        assert_equal(rp.flux, 2*(10**14))

    def test_FuelForm(self):
        rp = ReactorParameters()
        rp.FuelForm = {"IHM": 1.0, "O16": 2.0}
        assert_equal(rp.FuelForm, {"IHM": 1.0, "O16": 2.0})

    def test_CoolantForm(self):
        rp = ReactorParameters()
        rp.CoolantForm = {"H1": 2.0, "O16": 1.0,
            "B10": 0.199 * 550 * 10.0**-6, 
            "B11": 0.801 * 550 * 10.0**-6}
        assert_equal(rp.CoolantForm, {"H1": 2.0, "O16": 1.0,
            "B10": 0.199 * 550 * 10.0**-6,
            "B11": 0.801 * 550 * 10.0**-6})

    def test_FuelDensity(self):
        rp = ReactorParameters()
        rp.FuelDensity = 10.7
        assert_equal(rp.FuelDensity, 10.7)

    def test_CoolantDensity(self):
        rp = ReactorParameters()
        rp.CoolantDensity = 0.73
        assert_equal(rp.CoolantDensity, 0.73)

    def test_pnl(self):
        rp = ReactorParameters()
        rp.pnl = 0.98
        assert_equal(rp.pnl, 0.98)

    def test_BUt(self):
        rp = ReactorParameters()
        rp.BUt = 50.0
        assert_equal(rp.BUt, 50.0)

    def test_useDisadvantage(self):
        rp = ReactorParameters()
        rp.useDisadvantage = True
        assert_true(rp.useDisadvantage)

    def test_LatticeType(self):
        rp = ReactorParameters()
        rp.LatticeType = 'Spherical'
        assert_equal(rp.LatticeType, 'Spherical')

    def test_HydrogenRescale(self):
        rp = ReactorParameters()
        rp.HydrogenRescale = True
        assert_true(rp.HydrogenRescale)

    def test_Radius(self):
        rp = ReactorParameters()
        rp.Radius = 0.411
        assert_equal(rp.Radius, 0.411)

    def test_Length(self):
        rp = ReactorParameters()
        rp.Length = 0.7
        assert_equal(rp.Length, 0.7)

    def test_open_slots(self):
        rp = ReactorParameters()
        rp.open_slots = 123
        assert_equal(rp.open_slots, 123)

    def test_total_slots(self):
        rp = ReactorParameters()
        rp.total_slots = 180
        assert_equal(rp.total_slots, 180)


class TestReactor1GConstructors(TestCase):
    """Tests that the Reactor1G component constructors work."""

    @classmethod
    def teardown_class(cls):
        general_teardown()

    def test_Reactor1G_1(self):
        r1g = Reactor1G()
        assert_equal(r1g.name, '')
        assert_equal(r1g.params2track, [])

    def test_Reactor1G_2(self):
        r1g = Reactor1G("r1g")
        assert_equal(r1g.name, 'r1g')
        assert_equal(r1g.params2track, [])

    def test_Reactor1G_3(self):
        r1g = Reactor1G(["Mass"])
        assert_equal(r1g.name, '')
        assert_equal(r1g.params2track, ["Mass"])

    def test_Reactor1G_4(self):
        r1g = Reactor1G(["Mass"], 'r1g')
        assert_equal(r1g.name, 'r1g')
        assert_equal(r1g.params2track, ["Mass"])

    def test_Reactor1G_5(self):
        rp = ReactorParameters()
        r1g = Reactor1G(rp, "r1g")
        assert_equal(r1g.name, 'r1g')
        assert_equal(r1g.params2track, [])
        assert_equal(r1g.B, 0)
        assert_equal(r1g.phi, 0.0)
        assert_equal(r1g.FuelChemicalForm, {})
        assert_equal(r1g.CoolantChemicalForm, {})
        assert_equal(r1g.rhoF, 0.0)
        assert_equal(r1g.rhoC, 0.0)
        assert_equal(r1g.P_NL, 0.0)
        assert_equal(r1g.TargetBU, 0.0)
        assert_false(r1g.useZeta)
        assert_equal(r1g.Lattice, '')
        assert_false(r1g.H_XS_Rescale)
        assert_equal(r1g.r, 0.0)
        assert_equal(r1g.l, 0.0)
        assert_equal(r1g.S_O, 0.0)
        assert_equal(r1g.S_T, 0.0)

    def test_Reactor1G_6(self):
        rp = ReactorParameters()
        r1g = Reactor1G(rp, ["Mass"], "r1g")
        assert_equal(r1g.name, 'r1g')
        assert_equal(r1g.params2track, ["Mass"])
        assert_equal(r1g.B, 0)
        assert_equal(r1g.phi, 0.0)
        assert_equal(r1g.FuelChemicalForm, {})
        assert_equal(r1g.CoolantChemicalForm, {})
        assert_equal(r1g.rhoF, 0.0)
        assert_equal(r1g.rhoC, 0.0)
        assert_equal(r1g.P_NL, 0.0)
        assert_equal(r1g.TargetBU, 0.0)
        assert_false(r1g.useZeta)
        assert_equal(r1g.Lattice, '')
        assert_false(r1g.H_XS_Rescale)
        assert_equal(r1g.r, 0.0)
        assert_equal(r1g.l, 0.0)
        assert_equal(r1g.S_O, 0.0)
        assert_equal(r1g.S_T, 0.0)
    


class TestReactor1GParameterAttributes(TestCase):
    """Tests that the Reactor1G parameter attributes work."""

    @classmethod
    def teardown_class(cls):
        general_teardown()

    def test_B(self):
        r1g = Reactor1G()
        r1g.B = 3
        assert_equal(r1g.B, 3)

    def test_phi(self):
        r1g = Reactor1G()
        r1g.phi = 2*(10**14)
        assert_equal(r1g.phi, 2*(10**14))

    def test_FuelChemicalForm(self):
        r1g = Reactor1G()
        r1g.FuelChemicalForm = {"IHM": 1.0, "O16": 2.0}
        assert_equal(r1g.FuelChemicalForm, {"IHM": 1.0, "O16": 2.0})

    def test_CoolantChemicalForm(self):
        r1g = Reactor1G()
        r1g.CoolantChemicalForm = {"H1": 2.0, "O16": 1.0,
            "B10": 0.199 * 550 * 10.0**-6, 
            "B11": 0.801 * 550 * 10.0**-6}
        assert_equal(r1g.CoolantChemicalForm, {"H1": 2.0, "O16": 1.0,
            "B10": 0.199 * 550 * 10.0**-6,
            "B11": 0.801 * 550 * 10.0**-6})

    def test_rhoF(self):
        r1g = Reactor1G()
        r1g.rhoF = 10.7
        assert_equal(r1g.rhoF, 10.7)

    def test_rhoC(self):
        r1g = Reactor1G()
        r1g.rhoC = 0.73
        assert_equal(r1g.rhoC, 0.73)

    def test_P_NL(self):
        r1g = Reactor1G()
        r1g.P_NL = 0.98
        assert_equal(r1g.P_NL, 0.98)

    def test_TargetBU(self):
        r1g = Reactor1G()
        r1g.TargetBU = 50.0
        assert_equal(r1g.TargetBU, 50.0)

    def test_useZeta(self):
        r1g = Reactor1G()
        r1g.useZeta = True
        assert_true(r1g.useZeta)

    def test_Lattice(self):
        r1g = Reactor1G()
        r1g.Lattice = 'Spherical'
        assert_equal(r1g.Lattice, 'Spherical')

    def test_H_XS_Rescale(self):
        r1g = Reactor1G()
        r1g.H_XS_Rescale = True
        assert_true(r1g.H_XS_Rescale)

    def test_r(self):
        r1g = Reactor1G()
        r1g.r = 0.411
        assert_equal(r1g.r, 0.411)

    def test_l(self):
        r1g = Reactor1G()
        r1g.l = 0.7
        assert_equal(r1g.l, 0.7)

    def test_S_O(self):
        r1g = Reactor1G()
        r1g.S_O = 123
        assert_equal(r1g.S_O, 123)

    def test_S_T(self):
        r1g = Reactor1G()
        r1g.S_T = 180
        assert_equal(r1g.S_T, 180)

    def test_VF(self):
        rp = ReactorParameters()
        rp.Radius = 0.5
        rp.Length = 1.0
        rp.open_slots = 0
        rp.total_slots = 1
        r1g = Reactor1G(rp, 'r1g')
        assert_almost_equal(r1g.VF, 3.14159265*0.25) 

    def test_VC(self):
        rp = ReactorParameters()
        rp.Radius = 0.5
        rp.Length = 1.0
        rp.open_slots = 0
        rp.total_slots = 1
        r1g = Reactor1G(rp, 'r1g')
        assert_almost_equal(r1g.VC, 1.0 - 3.14159265*0.25) 


class TestReactor1GBasicDataAttributes(TestCase):
    """Tests that the Reactor1G basic data attributes work."""

    @classmethod
    def setup_class(cls):
        libfile = os.getenv("BRIGHT_DATA") + '/LWR.h5'
        BriPy.load_isos2track_hdf5(libfile)
        cls.r1g = Reactor1G()
        cls.r1g.loadLib(libfile)

    @classmethod
    def teardown_class(cls):
        general_teardown()

    def test_libfile(self):
        self.r1g.libfile = "It's Ruth!"
        assert_equal(self.r1g.libfile, "It's Ruth!")

    def test_F(self):
        assert_equal(self.r1g.F[0], 0.0)
        assert(1 < len(self.r1g.F))
        for f in range(1, len(self.r1g.F)):        
            assert(self.r1g.F[f-1] < self.r1g.F[f])

    def test_BUi_F_(self):
        BUi_F_ = self.r1g.BUi_F_
        for i in BUi_F_.keys():
            assert_equal(BUi_F_[i][0], 0.0)
            assert_equal(len(self.r1g.F), len(BUi_F_[i]))
            for f in range(1, len(self.r1g.F)):        
                assert(BUi_F_[i][f-1] <= BUi_F_[i][f])

    def test_pi_F_(self):
        pi_F_ = self.r1g.pi_F_
        for i in pi_F_.keys():
            assert_equal(len(self.r1g.F), len(pi_F_[i]))

    def test_di_F_(self):
        di_F_ = self.r1g.di_F_
        for i in di_F_.keys():
            assert_equal(len(self.r1g.F), len(di_F_[i]))

    def test_Tij_F_(self):
        Tij_F_ = self.r1g.Tij_F_
        jsos   = BriPy.isos2track()
        for i in Tij_F_.keys():
            for j in jsos:
                assert_equal(len(self.r1g.F), len(Tij_F_[i][j]))


class TestReactor1GCalculatedWeightAttributes(TestCase):
    """Tests that the Reactor1G calculated weight attributes work."""

    @classmethod
    def setup_class(cls):
        libfile = os.getenv("BRIGHT_DATA") + '/LWR.h5'
        BriPy.load_isos2track_hdf5(libfile)
        cls.r1g = Reactor1G(default_rp, 'r1g')
        cls.r1g.loadLib(libfile)
        cls.r1g.IsosIn = MassStream({922350: 0.5, 922380: 0.5})
        cls.r1g.foldMassWeights()

    @classmethod
    def teardown_class(cls):
        general_teardown()

    def test_A_IHM(self):
        assert_almost_equal(self.r1g.A_IHM / 236.5, 1.0, 4)

    def test_MWF(self):
        assert_almost_equal(self.r1g.MWF / 268.5, 1.0, 4)

    def test_MWC(self):
        assert_almost_equal(self.r1g.MWC / 18.0, 1.0, 4)

    def test_niF(self):
        assert_equal(self.r1g.niF[80160],  2.0)
        assert_equal(self.r1g.niF[922350], 0.5)
        assert_equal(self.r1g.niF[922380], 0.5)

    def test_niC(self):
        assert_equal(self.r1g.niC[10010],  2.0)
        assert_equal(self.r1g.niC[80160],  1.0)

    def test_miF(self):
        assert_almost_equal(self.r1g.miF[80160],  2.0 * 16  / 236.5, 4)
        assert_almost_equal(self.r1g.miF[922350], 0.5 * 235 / 236.5, 4)
        assert_almost_equal(self.r1g.miF[922380], 0.5 * 238 / 236.5, 4)

    def test_miC(self):
        #First calculate the relative volume
        rel_Vol = (self.r1g.rhoC * 268.5 * self.r1g.VC) / (self.r1g.rhoF * 18.0 * self.r1g.VF)
        assert_almost_equal(self.r1g.miC[10010],  rel_Vol * 2.0 * 1   / 236.5, 4)
        assert_almost_equal(self.r1g.miC[80160],  rel_Vol * 1.0 * 16  / 236.5, 4)
        
    def test_NiF(self):
        assert_almost_equal(self.r1g.NiF[80160]  / (2.0 * self.r1g.rhoF * 6.022*(10**23) / 268.5), 1.0, 3)
        assert_almost_equal(self.r1g.NiF[922350] / (0.5 * self.r1g.rhoF * 6.022*(10**23) / 268.5), 1.0, 3)
        assert_almost_equal(self.r1g.NiF[922380] / (0.5 * self.r1g.rhoF * 6.022*(10**23) / 268.5), 1.0, 3)

    def test_NiC(self):
        assert_almost_equal(self.r1g.NiC[10010] / (2.0 * self.r1g.rhoC * 6.022*(10**23) / 18.0), 1.0, 3)
        assert_almost_equal(self.r1g.NiC[80160] / (1.0 * self.r1g.rhoC * 6.022*(10**23) / 18.0), 1.0, 3)


class TestReactor1GCalculatedDataAttributes(TestCase):
    """Tests that the Reactor1G calculated data attributes work."""

    @classmethod
    def setup_class(cls):
        libfile = os.getenv("BRIGHT_DATA") + '/LWR.h5'
        BriPy.load_isos2track_hdf5(libfile)
        cls.r1g = Reactor1G(default_rp, 'r1g')
        cls.r1g.loadLib(libfile)
        cls.r1g.IsosIn = MassStream({922350: 0.5, 922380: 0.5})
        cls.r1g.foldMassWeights()

    @classmethod
    def teardown_class(cls):
        general_teardown()

    def test_BU_F_(self):
        BU_F_ = self.r1g.BU_F_
        BUi_F_ = self.r1g.BUi_F_
        assert_equal(BU_F_[0], 0.0)
        for f in range(1, len(self.r1g.F)):
            tmp_BU = 0.0
            for i in self.r1g.miF.keys():
                tmp_BU = tmp_BU + (self.r1g.miF[i] * BUi_F_[i][f])
            assert_almost_equal(BU_F_[f] / tmp_BU, 1.0, 4)

    def test_P_F_(self):
        P_F_ = self.r1g.P_F_
        pi_F_ = self.r1g.pi_F_
        for f in range(len(self.r1g.F)):
            tmp_P = 0.0
            for i in self.r1g.miF.keys():
                tmp_P = tmp_P + (self.r1g.P_NL * self.r1g.miF[i] * pi_F_[i][f])
            assert_almost_equal(P_F_[f] / tmp_P, 1.0, 4)

    def test_dF_F_(self):
        dF_F_ = self.r1g.dF_F_
        di_F_ = self.r1g.di_F_
        for f in range(len(self.r1g.F)):
            tmp_dF = 0.0
            for i in self.r1g.miF.keys():
                tmp_dF = tmp_dF + (self.r1g.miF[i] * di_F_[i][f])
            assert_almost_equal(dF_F_[f] / tmp_dF, 1.0, 4)

    def test_dC_F_(self):
        dC_F_ = self.r1g.dC_F_
        di_F_ = self.r1g.di_F_
        zeta_F_ = self.r1g.zeta_F_
        for f in range(len(self.r1g.F)):
            tmp_dC = 0.0
            for i in self.r1g.miC.keys():
                if i == 10010 and self.r1g.H_XS_Rescale:
                    tmp_dC = tmp_dC + (self.r1g.miC[i] * di_F_[i][f] * (1.36927-(0.01119*self.r1g.BU_F_[f])) )
                else:
                    tmp_dC = tmp_dC + (self.r1g.miC[i] * di_F_[i][f])
            if self.r1g.useZeta:
                tmp_dC = tmp_dC * zeta_F_[f]
            assert_almost_equal(dC_F_[f] / tmp_dC, 1.0, 4)

    def test_D_F_(self):
        D_F_  = self.r1g.D_F_
        dF_F_ = self.r1g.dF_F_
        dC_F_ = self.r1g.dC_F_
        for f in range(len(self.r1g.F)):
            assert_almost_equal(D_F_[f] / (dF_F_[f] + dC_F_[f]), 1.0, 4)

    def test_k_F_(self):
        P_F_ = self.r1g.P_F_
        D_F_ = self.r1g.D_F_
        k_F_ = self.r1g.k_F_
        for f in range(len(self.r1g.F)):
            assert_almost_equal(k_F_[f] / (P_F_[f]/D_F_[f]), 1.0, 4)

    def test_Mj_F_(self):
        Mj_F_  = self.r1g.Mj_F_
        Tij_F_ = self.r1g.Tij_F_
        for j in Mj_F_.keys():
            for f in range(len(self.r1g.F)):
                tmp_Mj = 0.0
                for i in self.r1g.miF.keys():
                    tmp_Mj = tmp_Mj + (self.r1g.miF[i] * Tij_F_[i][j][f])
                assert_almost_equal(Mj_F_[j][f] / tmp_Mj, 1.0, 4)

    def test_zeta_F_(self):
        zeta_F_ = self.r1g.zeta_F_
        for f in range(len(self.r1g.F)):
            assert(1.0 <= zeta_F_[f])


class TestReactor1GDischargeAttributes(TestCase):
    """Tests that the Reactor1G discharge attributes are right."""

    @classmethod
    def setup_class(cls):
        libfile = os.getenv("BRIGHT_DATA") + '/LWR.h5'
        BriPy.load_isos2track_hdf5(libfile)
        cls.r1g = Reactor1G(default_rp, 'r1g')
        cls.r1g.loadLib(libfile)
        cls.r1g.IsosIn = MassStream({922350: 0.5, 922380: 0.5})
        cls.r1g.doCalc()

    @classmethod
    def teardown_class(cls):
        general_teardown()

    def test_fd(self):
        assert(0 <= self.r1g.fd)
        assert(self.r1g.fd <= len(self.r1g.F))

    def test_Fd(self):
        assert(self.r1g.F[self.r1g.fd] <= self.r1g.Fd)
        assert(self.r1g.Fd <= self.r1g.F[self.r1g.fd+1])

    def test_BUd(self):
        assert(self.r1g.BU_F_[self.r1g.fd] <= self.r1g.BUd)
        assert(self.r1g.BUd <= self.r1g.BU_F_[self.r1g.fd+1])

    def test_k(self):
        assert_almost_equal(self.r1g.k, 1.0)


class TestReactor1GSubStreamAndTruCRAttributes(TestCase):
    """Tests that the Reactor1G sub-stream and transuranic conversion ratio
    attributes are right."""

    @classmethod
    def setup_class(cls):
        libfile = os.getenv("BRIGHT_DATA") + '/LWR.h5'
        BriPy.load_isos2track_hdf5(libfile)
        cls.r1g = Reactor1G(default_rp, 'r1g')
        cls.r1g.loadLib(libfile)
        cls.r1g.IsosIn = MassStream({922350: 0.5, 922380: 0.5})
        cls.r1g.doCalc()
        cls.r1g.calcSubStreams()

    @classmethod
    def teardown_class(cls):
        general_teardown()

    def test_InU(self):
        assert_equal(self.r1g.InU.mass, 1.0)

    def test_InTRU(self):
        assert_equal(self.r1g.InTRU.mass, 0.0)

    def test_InLAN(self):
        assert_equal(self.r1g.InLAN.mass, 0.0)

    def test_InACT(self):
        assert_equal(self.r1g.InACT.mass, 1.0)

    def test_OutU(self):
        assert(self.r1g.OutU.mass < 1.0)

    def test_OutTRU(self):
        assert(0.0 < self.r1g.OutTRU.mass)

    def test_OutLAN(self):
        assert(0.0 < self.r1g.OutLAN.mass)

    def test_OutACT(self):
        assert(self.r1g.OutACT.mass < 1.0)

    def test_TruCR(self):
        self.r1g.calcTruCR()
        tmp_TruCR = (self.r1g.InTRU.mass - self.r1g.OutTRU.mass) / (self.r1g.BUd / 935.0)
        assert_almost_equal(self.r1g.TruCR / tmp_TruCR, 1.0)



class TestReactor1GThermalDisadvantageFactorAttributes(TestCase):
    """Tests that the Reactor1G calculated data attributes work."""

    @classmethod
    def setup_class(cls):
        libfile = os.getenv("BRIGHT_DATA") + '/LWR.h5'
        BriPy.load_isos2track_hdf5(libfile)
        cls.r1g = Reactor1G(default_rp, 'r1g')
        cls.r1g.loadLib(libfile)
        cls.r1g.IsosIn = MassStream({922350: 0.5, 922380: 0.5})
        cls.r1g.foldMassWeights()

    @classmethod
    def teardown_class(cls):
        general_teardown()

    def test_SigmaFa_F_(self):
        """Can not do full test do to private sigma_a_therm data member."""
        assert_equal(len(self.r1g.SigmaFa_F_), len( self.r1g.F))

    def test_SigmaFtr_F_(self):
        """Can not do full test do to private sigma_a_therm data member."""
        assert_equal(len(self.r1g.SigmaFtr_F_), len( self.r1g.F))

    def test_kappaF_F_(self):
        kappaF_F_ = self.r1g.kappaF_F_
        SigmaFa_F_ = self.r1g.SigmaFa_F_
        SigmaFtr_F_ = self.r1g.SigmaFtr_F_
        for f in range(len(self.r1g.F)):
            tmp_kappaF = np.sqrt(3.0 * SigmaFtr_F_[f] * SigmaFa_F_[f])
            assert_almost_equal(kappaF_F_[f] / tmp_kappaF, 1.0)

    def test_SigmaCa_F_(self):
        """Can not do full test do to private sigma_a_therm data member."""
        assert_equal(len(self.r1g.SigmaCa_F_), len( self.r1g.F))

    def test_SigmaCtr_F_(self):
        """Can not do full test do to private sigma_a_therm data member."""
        assert_equal(len(self.r1g.SigmaCtr_F_), len( self.r1g.F))

    def test_kappaC_F_(self):
        kappaC_F_ = self.r1g.kappaC_F_
        SigmaCa_F_ = self.r1g.SigmaCa_F_
        SigmaCtr_F_ = self.r1g.SigmaCtr_F_
        for f in range(len(self.r1g.F)):
            tmp_kappaC = np.sqrt(3.0 * SigmaCtr_F_[f] * SigmaCa_F_[f])
            assert_almost_equal(kappaC_F_[f] / tmp_kappaC, 1.0)

    #Test LatticeE_F_ here

    #Test LatticeF_F_ here


class TestReactor1GMethods(TestCase):
    """Tests that the fuel cycle component methods work."""

    @classmethod
    def teardown_class(cls):
        general_teardown()

"""
    def test_doCalc_1(self):
        BriPy.isos2track([922350, 922380, 942390])
        r1g = Reactor1G()
        r1g.decay_time = 0.0
        r1g.IsosIn = MassStream({942390: 1.0})
        r1g.doCalc()
        assert_equal(r1g.IsosOut.mass, 1.0)
        assert_almost_equal(r1g.IsosOut.comp[942390], 1.0) 

    def test_doCalc_2(self):
        BriPy.isos2track([922350, 922380, 942390])
        r1g = Reactor1G()
        r1g.decay_time = 0.0
        r1g.doCalc(MassStream({942390: 1.0}))
        assert_equal(r1g.IsosOut.mass, 1.0)
        assert_equal(r1g.IsosOut.comp[942390], 1.0) 

    def test_doCalc_3(self):
        BriPy.isos2track([922350, 922380, 942390])
        r1g = Reactor1G()
        r1g.IsosIn = MassStream({942390: 1.0})
        r1g.doCalc(24110*365.25*24*3600)
        assert(r1g.IsosOut.mass < 1.0)
        assert_almost_equal(r1g.IsosOut.comp[942390], 0.5, 3) 

    def test_doCalc_4(self):
        BriPy.isos2track([922350, 922380, 942390])
        r1g = Reactor1G()
        r1g.doCalc(MassStream({942390: 1.0}), 24110*365.25*24*3600)
        assert(r1g.IsosOut.mass < 1.0)
        assert_almost_equal(r1g.IsosOut.comp[942390], 0.5, 3) 

    def test_setParams(self):
        BriPy.isos2track([922350, 922380, 942390])
        r1g = Reactor1G()
        r1g.doCalc(MassStream({942390: 1.0}), 24110*365.25*24*3600)
        r1g.setParams()
        assert_equal(r1g.ParamsIn["Mass"],  1.00)
        assert(0.5 < r1g.ParamsOut["Mass"] < 1.0)
"""
        

if __name__ == "__main__":
    nose.main()