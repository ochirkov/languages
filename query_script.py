import requests
import time
import argparse
import random
from requests.exceptions import ConnectionError as conn_err


parser = argparse.ArgumentParser()
parser.add_argument('--count', type=int,
                    help='number of reqs per sec', default=2)
parser.add_argument('--ip', type=str,
                    help='ip addr of load balancer', required=True)
args = parser.parse_args()


langs = ('cs', 'da', 'de', 'el', 'en',
         'es', 'it', 'nl', 'pl', 'ru'
        )

def run():

    print(f"New iteration with {args.count} repeats")
    for i in range(args.count):

        lang = random.choice(langs)

        try:

            res = requests.get(f"http://{args.ip}/lw/xmas/{lang}")

            if res.status_code == 200:
                print(res.text)
            else:
                print(f"Failured response with status {res.status_code}")

        except conn_err as e:
            print(e)

    time.sleep(1)


if __name__ == "__main__":

    while True:
        run()

