import json
from math import radians, sin, cos, acos


class InviteCustomers(object):
    '''
    Class to load up a list of customers from a given file
    path, and using the Great Circle Distance formula, find out
    which customers are within some given distance between their
    long/lat and their office
    '''
    def __init__(self, office, customer_file_path, max_distance):
        self.office = office
        self.customer_file_path = customer_file_path
        self.max_distance = max_distance
        self.customers = []

    def calculate_distance(self, user):
        '''
        office - tuple of longitude, latitude for the dubin office
        user - tuple of longitude, latitude for a given customer

        returns distance between the given two.
        '''
        office_lon, office_lat = self.office
        user_lon, user_lat = user
        radius = 6371
        '''
        6371 - magic number explained:
        So long as a spherical Earth is assumed, any single formula for
        distance on the Earth is only guaranteed correct within 0.5%
        (though better accuracy is possible if the formula is only intended
        to apply to a limited area).
        Using the mean earth radius, R 1 = 1 3 ( 2 a + b ) ≈ 6371 km
        https://en.wikipedia.org/wiki/Great-circle_distance#Radius_for_spherical_Earth
        Probably need to refactor if we ever move planet
        '''
        # step #1, convert to radians
        to_convert = [float(office_lon), float(office_lat),
                      float(user_lon), float(user_lat)]
        office_lon, office_lat, user_lon, user_lat = map(radians, to_convert)
        # step #2: next, apply formula fro m wiki:
        # r * (acos(sin(a0) * sin(v0) + cos(a0) * cos(v0) * cos(a1 - v1)))
        final_resp = 6371 * (acos(sin(office_lat) * sin(user_lat)
                             + cos(office_lat) * cos(user_lat) *
                             cos(office_lon - user_lon)))
        return final_resp

    def get_customer_file(self):
        try:
            with open(self.customer_file_path, 'r') as f:
               customers = f.readlines()
            self.customers = customers
        except FileNotFoundError as e:
            print("No file found at {}".format(self.customer_file_path))
            raise e

    def is_close(self, d):
        if d <= self.max_distance:
            return True
        else:
            return False

    def find_valid_invites(self):
        '''
        Iterate through users, pull lat and long from each users
        entry and pass into the calc distance function, building up a
        list of valid invites as we go.
        '''
        valid_invites = []
        for u in self.customers:
            json_d = json.loads(u)
            this_c = (json_d['latitude'], json_d['longitude'])
            d = self.calculate_distance(this_c)
            if self.is_close(d):
                valid_invites.append(json.loads(u))
        return valid_invites

    def prepare_response(self, valid_invites):
        '''
        Sort a list of invites by user_id
        '''
        valid_invites.sort(key=lambda y: y['user_id'])
        return valid_invites

    def run(self):
        '''
        1. load customers from the file
        2. find the list of users who are within boundaries
        3. format the response and print it out.
        '''
        self.get_customer_file()
        valid_invites = self.find_valid_invites()
        return self.prepare_response(valid_invites)
