"""Usage:
    iterate.py -n [NUM]

Arguments:
  NUM        Number to iterate
Options:
  -h --help  Shows these options
  -n           Specify the number to iterate

"""
from docopt import docopt


if __name__ == '__main__':
    args = docopt(__doc__)


def iterate(n):
    for i in range(1,n+1):
        print(i)
        if i%3 == 0 and i%5==0:
            print(str(i) + ' - multiple of 3 and 5')
        elif i%3 == 0:
            print(str(i)+ ' - multiple of 3')
        elif i%5 == 0:
            print(str(i) +' - multiple of 5')
        else:
            print(i)

n = int(args['NUM'])
iterate(n)
