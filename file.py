import unittest
from requests.exceptions import Timeout
from unittest.mock import Mock

print("this extra line added")

requests=Mock()

def get_holidays():
   r=requests.get("httpL://localhost/api/holidays")
   if r.status_code==200:
       return r.json()
   return None

class TestCalender(unittest.TestCase):
    def test_get_holidays_timeout(self):
        requests.get.side_effect=Timeout
        with self.assertRaises(Timeout):
            get_holidays()

if __name__=='__main__':
    unittest.main()
print("this line added in firstbranch")