import yaml
import argparse

from distance_invite import InviteCustomers

def run(conf_path, customer_overwrite):
    try:
        with open(conf_path, 'r') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
    except Exception as e:
        # something went wrong with loading config.
        # raise the error and move on.
        raise e
    office = config.get('office')
    if customer_overwrite:
        # user specified a different file from the one in our
        # config
        file_name = customer_overwrite
    else:
        file_name = config.get('customer_filepath')

    max_distance = config.get('max_distance')
    new_invites = InviteCustomers(office, file_name, max_distance)
    results = new_invites.run()
    results_format = "{user_id} - {name}"
    print("\nUsers To Invite:")
    for r in results:
        print(results_format.format(user_id=r['user_id'], name=r['name']))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Allow a user to define some'
                                    ' config files & customer.txt files')
    parser.add_argument('--config_path', help='file path for config',
                        default='./config.yml')
    parser.add_argument('--customer_overwrite',
                        help='file path for a different customers.txt',
                        default=False)

    args = parser.parse_args()
    run(args.config_path, args.customer_overwrite)
