import unittest
import re

def parsedhcpleases(in_file):
    leases = []
    pattern = r'static-mapping (.*?) \{\n\s+ip-address ((\d{1,3}\.){3}\d{1,3})\n\s+mac-address (.{17})\n\s+\}'

    with open(in_file) as uni:
        temp_list = re.findall(pattern, uni.read())   
        for punkt in temp_list:
            string = 'dhcp-host='
            comma = ','
            macaddr = punkt[3]
            name = punkt[0].replace('_','-')
            ipaddr = punkt[1]
            string += comma.join([macaddr, name, ipaddr])
            leases.append(string)
    return leases


class TestLeases(unittest.TestCase):
    def test_regexp_cutter(self):
        cases = {1: ['''dhcp_uni.txt''', ['dhcp-host=7c:2f:80:5f:e3:c3,A510-IP,192.168.88.151']]}
        for key in cases.keys():
            data = cases[key][0]
            target = cases[key][1]
            result = [parsedhcpleases(data)[0]]
            self.assertEqual(result, target)
 
if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
