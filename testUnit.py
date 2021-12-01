import unittest
import requests
import time
from statistics import mean
 
class TestApp(unittest.TestCase):
    def test_outputs(self):
        list=[3,4,5]
        URL = "http://127.0.0.1:4000/?vals="
        first = True
        for value in list:
            if first:
                URL += str(value)
                first = False
            else:
                URL += ',' + str(value)
        self.assertEqual(float(str(requests.get(URL).text).split('=')[1].strip()),mean([3,4,5]))

    def testconnection(self):
        URL = "http://127.0.0.1:4000/"
        self.assertEqual(float(str(requests.get(URL).text).split(',')[0].strip()),200)

    def testreports(self):
        nb_test = 1000
        tab = []
        for i in range(nb_test):
            t_rstart = time.process_time()
            requests.get("http://127.0.0.1:4000/")
            t_rend = time.process_time()
            tab.append(t_rend - t_rstart)
        if mean(tab) <= 0.1:
            re = True
        else :
            re = False
        self.assertEqual(re,True)
    


if (__name__ == '__main__'):
    unittest.main()
