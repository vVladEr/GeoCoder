import re


class AddressParser:
    def __init__(self):
        self.data = {"city": "", "street": "", "house_number": "", "house_ad_number": ""}
        self._addr = ""

    def general_addr_parse(self, addr):
        for key in self.data.keys():
            self.data[key] = ""
        self._addr = addr
        self.find_city_name()
        self.find_street_name()
        self.find_house_additional_number()
        self.find_house_number()

    def find_house_additional_number(self):
        re_house_ad_number = re.compile("(к\.? (?P<option1>\d+))|(корпус (?P<option2>\d+))|(/(?P<option3>\d+))")
        house_ad_number = re.search(re_house_ad_number, self._addr)
        if house_ad_number is not None:
            for i in range(1, 4):
                group_name = "option" + str(i)
                if house_ad_number.group(group_name):
                    self.data["house_ad_number"] = house_ad_number.group(group_name)
            self._addr = re.sub(re_house_ad_number, "", self._addr)

    def find_house_number(self):
        re_house_number = re.compile("(д\.? (?P<option1>\d+))|(дом (?P<option2>\d+))|((?P<option3>(\d+)))")
        house_number = re.search(re_house_number, self._addr)
        for i in range(1, 4):
            group_name = "option" + str(i)
            if house_number.group(group_name):
                self.data["house_number"] = house_number.group(group_name)
        self._addr = re.sub(re_house_number, "", self._addr)

    def find_street_name(self):
        re_street_name = re.compile("((ул\.?)|(улица) )?((?P<streetName>("
                                    "((?:(Мал)|(Больш)|(Верхн)|(Нижн)|(Стар)|(Нов))[a-я]{2} )?"
                                    "[ЁА-Я][ЁёА-я\-]+)))( |,)(?:\d|д|к)")
        street_name = re.search(re_street_name, self._addr)
        self.data["street"] = street_name.group("streetName")

    def find_city_name(self):
        re_city_name = re.compile("((?P<cityName>("
                                  "((?:(Мал)|(Больш)|(Верхн)|(Нижн)|(Стар)|(Нов))[a-я]{2} )?"
                                  "[ЁА-Я][ЁёА-я\-]+)))(( |,)(?:[ЁА-Я]|у|п|б| )|$)")
        city_name = re.search(re_city_name, self._addr)
        self.data["city"] = city_name.group("cityName")

