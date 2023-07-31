import addr_parser
import unittest

SIMPLE_TEST_ADDRESSES = ["Екатеринбург Тургенева 4", "Екатеринбург, ул. Тургенева д. 4",
                "Екатеринбург, ул. Тургенева дом 4", "Тургенева 4, Екатеринбург", "Тургенева дом 4 Екатеринбург"]

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

    def testOneWordStreetName(self):
        for addr in SIMPLE_TEST_ADDRESSES and TEST_ADDRESSES_WITH_AD_NUMBER:
            PARSER.general_addr_parse(addr)
            self.assertEqual(PARSER.data["street"], "Тургенева")

    def testOneWordCityName(self):
        for addr in SIMPLE_TEST_ADDRESSES and TEST_ADDRESSES_WITH_AD_NUMBER:
            PARSER.general_addr_parse(addr)
            self.assertEqual(PARSER.data["city"], "Екатеринбург")

    def testTwoWordStreetName(self):
        addrs = ["Москва Новый Арбат 23", "Новый Арбат 23, Москва"]
        for addr in addrs:
            PARSER.general_addr_parse(addr)
            self.assertEqual(PARSER.data["street"], "Новый Арбат")

    def testTwoWordCityName(self):
        addrs = ["Нижний Тагил Ленина 23", "Ленина 23, Нижний Тагил"]
        for addr in addrs:
            PARSER.general_addr_parse(addr)
            self.assertEqual(PARSER.data["city"], "Нижний Тагил")

    def testTwoWordCityWithTwoWordStreet(self):
        addrs = ["Нижний Тагил Малая Конная 23", "Малая Конная 23, Нижний Тагил"]
        for addr in addrs:
            PARSER.general_addr_parse(addr)
            self.assertEqual(PARSER.data["city"], "Нижний Тагил")
            self.assertEqual(PARSER.data["street"], "Малая Конная")


if __name__ == '__main__':
    unittest.main()