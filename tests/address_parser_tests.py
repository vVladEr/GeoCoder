import addr_parser
import unittest

SIMPLE_TEST_ADDRESSES = ["Екатеринбург Тургенева 4", "Екатеринбург, ул. Тургенева д. 4",
                "Екатеринбург, ул. Тургенева дом 4"]

TEST_ADDRESSES_WITH_AD_NUMBER = ["Екатеринбург, ул. Тургенева д. 4 к. 1",
                "Екатеринбург, ул. Тургенева д. 4/1",
                "Екатеринбург, ул. Тургенева д. 4 корпус 1",
                "Екатеринбург, ул. Тургенева дом 4 к. 1",
                "Екатеринбург, ул. Тургенева дом 4/1",
                "Екатеринбург, ул. Тургенева дом 4 корпус 1",
                "Екатеринбург, ул. Тургенева корпус 1 дом 4 "]
PARSER = addr_parser.AddressParser()


class TestAddrParser(unittest.TestCase):
    def testHouseNumber(self):
        for addr in SIMPLE_TEST_ADDRESSES:
            PARSER.general_addr_parse(addr)
            self.assertEqual(PARSER.data["house_number"], "4")

    def testWithoutAdditionalHouseNumber(self):
        for addr in SIMPLE_TEST_ADDRESSES:
            PARSER.general_addr_parse(addr)
            self.assertEqual(PARSER.data["house_ad_number"], "")

    def testWithAdditionalHouseNumber(self):
        for addr in TEST_ADDRESSES_WITH_AD_NUMBER:
            PARSER.general_addr_parse(addr)
            self.assertEqual(PARSER.data["house_ad_number"], "1")


if __name__ == '__main__':
    unittest.main()