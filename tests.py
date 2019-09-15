import unittest
import json
from distance_invite import InviteCustomers


class TestInvites(unittest.TestCase):
    '''
    Testing the InviteCustomers class.
    '''
    def test_valid_input(self):
        '''
        basic test, one user with valid in range distance.
        '''
        c = self.get_new_customer_invites()
        one_customer = json.dumps({"latitude": "53.2451022", "user_id": 4,
                                   "name": "Ian Kehoe", "longitude": "-6.238335"})
        c.customers = [one_customer]
        x = c.find_valid_invites()
        self.assertEqual(len(x), 1, 'only one valid response')

    def test_valid_input_no_matches(self):
        '''
        no user in the list is under max_distance away.
        '''
        c_invites = self.get_new_customer_invites()
        c_invites.max_distance = -1
        one_customer = json.dumps({"latitude": "53.2451022", "user_id": 4,
                           "name": "Ian Kehoe", "longitude": "-6.238335"})
        c_invites.customers = [one_customer]
        x = c_invites.find_valid_invites()
        self.assertEqual(len(x), 0)

    def test_user_ids_in_order(self):
        '''
        test that order of valid anwers is corrects
        '''
        c_invites = self.get_new_customer_invites()
        one_customer = json.dumps({"latitude": "53.2451022", "user_id": 4,
                           "name": "Ian Kehoe", "longitude": "-6.238335"})

        two_customer = json.dumps({"latitude": "53.2451022", "user_id": 2,
                           "name": "Ian Kehoe", "longitude": "-6.238335"})

        c_invites.customers = [one_customer, two_customer]
        x = c_invites.find_valid_invites()
        sorted_ans = c_invites.prepare_response(x)
        self.assertEqual(sorted_ans[0]['user_id'], 2)
        self.assertEqual(sorted_ans[1]['user_id'], 4)

    def test_user_ids_in_order(self):
        '''
        test that users with no user_id throws KeyError
        '''
        c_invites = self.get_new_customer_invites()
        one_customer = json.dumps({"latitude": "53.2451022", "user_id": 4,
                                  "name": "Ian Kehoe", "longitude": "-6.238335"})

        # this one will break it.
        two_customer = json.dumps({"latitude": "53.2451022",
                                   "name": "Ian Kehoe", "longitude": "-6.238335"})

        c_invites.customers = [one_customer, two_customer]
        x = c_invites.find_valid_invites()
        with self.assertRaises(KeyError) as f_err:
            c_invites.prepare_response(x)
        exception = f_err.exception
        self.assertEqual(('user_id',), exception.args)

    def test_empty_data(self):
        '''
        test if customers list is empty
        '''
        c_invites = self.get_new_customer_invites()
        res = c_invites.find_valid_invites()
        self.assertEqual(res, [])

    def test_customers_file_does_not_exist(self):
        '''
        If a customers file does, raise a file not found error.
        '''
        c_invites = self.get_new_customer_invites()
        c_invites.customer_file_path = './ccc.txt'
        with self.assertRaises(FileNotFoundError) as f_err:
            c_invites.get_customer_file()
        exception = f_err.exception
        self.assertEqual(exception.strerror, 'No such file or directory')

    def test_basic_run(self):
        '''
        test a basic run returns the expected results
        '''
        c_invites = self.get_new_customer_invites()
        results = c_invites.run()
        self.assertEqual(12, len(results))
        self.assertEqual(results[0]['user_id'], 4)
        self.assertEqual(results[-1]['user_id'], 39)

    def get_new_customer_invites(self):
        '''
        Helper func to return stock new invite customers obj
        '''
        office = [53.339428, -6.257664]
        customer_file_path = './test_customers.txt'
        max_distance = 100
        return InviteCustomers(office, customer_file_path, max_distance)


if __name__ == '__main__':
    unittest.main()

