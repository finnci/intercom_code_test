import yaml
from distance_invite import InviteCustomers


def run():
    try:
        with open('./config.yml', 'r') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
    except Exception as e:
        # something went wrong with loading config.
        # raise the error and move on.
        raise e
    office = config.get('office')
    file_name = config.get('customer_filepath')
    max_distance = config.get('max_distance')
    new_invites = InviteCustomers(office, file_name, max_distance)
    new_invites.run()


if __name__ == "__main__":
    run()
