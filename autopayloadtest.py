#encoding: utf-8
import requests
import unittest
import ddt

@ddt.ddt
class testClass(unittest.TestCase):
    def setUp(self):
        print("starting...")
        self.base_url='http://preview.airwallex.com:30001/bank'


    @ddt.data(
        ( "payment_method1",{"payment_method": "SWIFT","bank_country_code": "US","account_name": "John Smith","account_number": "123","swift_code": "ICBCUSBJ","aba": "11122233A"}, 200),

        ("payment_method2",{"payment_method": "LOCAL", "bank_country_code": "US", "account_name": "John Smith", "account_number": "123","swift_code": "ICBCUSBJ", "aba": "11122233A"},200),

        ("payment_method3",{"payment_method": "", "bank_country_code": "US", "account_name": "John Smith", "account_number": "123", "swift_code": "ICBCUSBJ", "aba": "11122233A"}, 400),

        ("payment_method4",{"payment_method": "INVALID", "bank_country_code": "US", "account_name": "John Smith", "account_number": "123","swift_code": "ICBCUSBJ", "aba": "11122233A"}, 400),

        ("bank_country_code5",{"payment_method": "SWIFT", "bank_country_code": "AU", "account_name": "John Smith", "account_number": "123","swift_code": "ICBCUSBJ", "aba": "11122233A"}, 200),

        ("bank_country_code6",{"payment_method": "SWIFT", "bank_country_code": "CN", "account_name": "John Smith", "account_number": "123","swift_code": "ICBCUSBJ", "aba": "11122233A"}, 200),

        ("bank_country_code7",{"payment_method": "SWIFT", "bank_country_code": "INVALID", "account_name": "John Smith", "account_number": "123","swift_code": "ICBCUSBJ", "aba": "11122233A"}, 400),

        ("account_name8", {"payment_method": "SWIFT", "bank_country_code": "US","account_number": "123", "swift_code": "ICBCUSBJ", "aba": "11122233A"}, 400),

        ("account_name9",{"payment_method": "SWIFT", "bank_country_code": "US", "account_number": "123", "swift_code": "ICBCUSBJ","aba": "11122233A"}, 400),

        ("account_name10",{"payment_method": "SWIFT", "bank_country_code": "INVALID", "account_name": "John","account_number": "123", "swift_code": "ICBCUSBJ","aba": "11122233A"}, 400),

        ("account_number11",{"payment_method": "SWIFT", "bank_country_code": "INVALID", "account_name": "John", "account_number": "123","swift_code": "ICBCUSBJ", "aba": "11122233A"}, 400),

        ("account_number12",{"payment_method": "SWIFT", "bank_country_code": "US","account_name": "John Smith","account_number": "","swift_code": "ICBCUSBJ","aba": "123456789"}, 400),

        ("account_number13", {"payment_method": "SWIFT", "bank_country_code": "US", "account_name": "John Smith","account_number": "123456789012345678", "swift_code": "ICBCUSBJ", "aba": "123456789"},400),
        ("account_number14", {"payment_method": "SWIFT", "bank_country_code": "AU", "account_name": "John Smith","account_number": "123456", "swift_code": "ICBCUSBJ", "aba": "123456789"}, 200),
        ("account_number15", {"payment_method": "SWIFT", "bank_country_code": "AU", "account_name": "John Smith", "account_number": "123456789", "swift_code": "ICBCUSBJ", "aba": "123456789"}, 200),

        ("account_number16",{"payment_method": "SWIFT", "bank_country_code": "AU", "account_name": "John Smith", "account_number": "12345","swift_code": "ICBCUSBJ", "aba": "123456789"}, 400),

        ("account_number17",{"payment_method": "SWIFT", "bank_country_code": "AU", "account_name": "John Smith", "account_number": "12345","swift_code": "ICBCUSBJ", "aba": "123456789"}, 400),

        ("account_number18", {"payment_method": "SWIFT", "bank_country_code": "AU", "account_name": "John Smith","account_number": "1234567890", "swift_code": "ICBCUSBJ", "aba": "123456789"}, 200),

        ("account_number19", {"payment_method": "SWIFT", "bank_country_code": "CN", "account_name": "John Smith","account_number": "12345678901234567890", "swift_code": "ICBCUSBJ", "aba": "123456789"},200),

        ("account_number20", {"payment_method": "SWIFT", "bank_country_code": "CN", "account_name": "John Smith","account_number": "1234567", "swift_code": "ICBCUSBJ", "aba": "123456789"}, 400),

        ("account_number21", {"payment_method": "SWIFT", "bank_country_code": "CN", "account_name": "John Smith","account_number": "123456789012345678901", "swift_code": "ICBCUSBJ", "aba": "123456789"}, 400),

        ("account_number22", {"payment_method": "SWIFT", "bank_country_code": "US", "account_name": "John Smith","account_number": "123", "swift_code": "ICBCUSBJ", "aba": "123456789"},400),

        ("account_number23", {"payment_method": "SWIFT", "bank_country_code": "US", "account_name": "John Smith", "account_number": "123","swift_code": "ICBCUSBJ123", "aba": "123456789"}, 200),

        ("account_number24",{"payment_method": "SWIFT", "bank_country_code": "US", "account_name": "John Smith", "account_number": "123","swift_code": "ICBCUSBJ123", "aba": "123456789"}, 200),

    )
    @ddt.unpack


    def testPost(self,casename_data,boday_data, statuscode_data):
        #print(type(statuscode_data) )
        formdata = boday_data

        headers_data = {
    'Content-Type': "application/json",
    'Cache-Control': "no-cache",
    }

        res = requests.post(url=self.base_url, json=formdata,headers = headers_data)
        #print( type(res.status_code))
        #print(res.text)
        print("casename:"+casename_data,res.status_code, res.json())
        self.assertTrue(statuscode_data == res.status_code)
        #self.assertTrue(message_data == res.json()['success'])

    def tearDown(self):
        print("close...")

if __name__ == "__main__":
    unittest.main()
