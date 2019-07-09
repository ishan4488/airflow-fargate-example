import logging

from argparse import ArgumentParser

parser = ArgumentParser(description='Airflow Fargate Example')
parser.add_argument('name', help='name', type=str)

if __name__ == '__main__':
    args = parser.parse_args()
    name = args.name
    print("Printing Name: " + name)
