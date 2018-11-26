import requests
import json

_URL = "http://www.mocky.io/v2/581335f71000004204abaf83"


class PhoneBook(object):
    """"""

    def __init__(self):
        self._url_api = _URL
        self._contacts = self._get_data()

    def get_by_name(self, name):
        """get_by_name(str) -> return json dict"""
        return self._filter_by_query(query=name, query_by="name")

    def get_by_phone_number(self, phone_number):
        """get_by_phone_number(str) -> return json dict"""
        return self._filter_by_query(query=phone_number, query_by="phone_number")

    def get_by_address(self, address):
        """get_by_address(str) -> return json dict"""
        return self._filter_by_query(query=address, query_by="address")

    def display_contacts(self):
        """Displays all the contacts details of a given phonebook"""

        for idx, contact in enumerate(self._contacts):
            print("-"*80)
            print("{}) Name: {}, Address: {}, number: {}".format(idx, contact['name'],
                                                                      contact['address'],
                                                                      contact['phone_number']
                                                           )
                  )
            print("-"*80)
            print()

    def _get_data(self):
        """Returns a list of phone number contacts in JSON format"""

        phone_data = requests.api.get(self._url_api)
        return self._sort_data(data=self._to_json(phone_data.content))

    def _to_json(self, data):
        """_to_json(bytes) -> json
           Takes a given data and returns that data in json format
        """

        return json.loads(data.decode())

    def _filter_by_query(self, query, query_by):
        """filter_by_query(str, str) -> return dict or None"""

        for contact in self._contacts:
            if query.lower() == contact[query_by].lower():
                return contact
        return None

    def _sort_data(self, data, by_address=False, by_number=False):
        """_sort_data(dict, boolean, boolean) -> return json dict"""

        data = data['contacts']

        if by_address:
            data = [contact for contact in sorted(data, key=lambda d: d.get('address'))]
        elif by_number:
            data = [contact for contact in sorted(data, key=lambda d: d.get('phone_number'))]
        else:
            data = [contact for contact in sorted(data, key=lambda d: d.get('name'))]
        return data



