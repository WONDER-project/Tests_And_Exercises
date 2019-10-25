import unittest, os, numpy

import orangecontrib.wonder.controller.fit.wppm.wppm_functions as wppm_functions

wulff_data_path = os.path.join(os.path.dirname(wppm_functions.__file__), "data")
wulff_data_path = os.path.join(wulff_data_path, "wulff_solids")

rows = numpy.loadtxt(os.path.join(wulff_data_path, "Cube_TruncatedCubeTriangularFace_L_FIT.data"), skiprows=2)

class WulffSolidsTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_coefficients_retrival(self):
        data_0 = rows[0]

        retrieved_data = wppm_functions.get_wulff_solid_Hj_coefficients(1, 0, 0, 0, wppm_functions.WulffCubeFace.TRIANGULAR)

        self.assertEqual(data_0[0], retrieved_data.h)
        self.assertEqual(data_0[1], retrieved_data.k)
        self.assertEqual(data_0[2], retrieved_data.l)
        self.assertEqual(data_0[3], retrieved_data.level)
        self.assertEqual(data_0[10], retrieved_data.a0)

if __name__ == '__main__':
    unittest.main()
