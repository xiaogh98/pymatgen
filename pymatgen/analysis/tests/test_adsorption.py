from __future__ import absolute_import
from __future__ import print_function

import unittest2 as unittest
import os

import numpy as np
from pymatgen.util.testing import PymatgenTest
from pymatgen.core.surface import generate_all_slabs
from pymatgen.analysis.adsorption import *
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen import Structure, Lattice
import json
from six.moves import zip

test_dir = os.path.join(os.path.dirname(__file__), "..", "..", "..", "..",
                        'test_files')


class AdsorbateSiteFinderTest(PymatgenTest):
    def setUp(self):
        #self.bcc_struct = Structure.from_spacegroup("Im-3m", Lattice.cubic(2.8),
        #                                            ["Fe"], [[0, 0, 0]])
        self.structure = Structure.from_spacegroup("Fm-3m", Lattice.cubic(3.5),
                                                ["Ni"], [[0, 0, 0]])

        #self.hcp_struct = Structure.from_spacegroup("")
        slabs = generate_all_slabs(self.structure, max_index=1,
                                   min_slab_size=6.0, min_vacuum_size=15.0,
                                   max_normal_search=1, center_slab=True)
        self.slab_dict = {''.join([str(i) for i in slab.miller_index]):
                          slab for slab in slabs}
        self.asf_100 = AdsorbateSiteFinder(self.slab_dict["100"])
        self.asf_111 = AdsorbateSiteFinder(self.slab_dict["111"])
        self.asf_110 = AdsorbateSiteFinder(self.slab_dict["110"])

    def test_init(self):
        asf_100 = AdsorbateSiteFinder(self.slab_dict["100"])
        asf_111 = AdsorbateSiteFinder(self.slab_dict["111"])
        pass

    def test_find_adsorption_sites(self):
        sites = self.asf_100.find_adsorption_sites()
        self.assertEquals(len(sites), 3)
        sites = self.asf_111.find_adsorption_sites()
        self.assertEquals(len(sites), 4)
        sites = self.asf_110.find_adsorption_sites()
        self.assertEquals(len(sites), 4)

    def test_functions(self):
        pass

if __name__ == '__main__':
    unittest.main()
