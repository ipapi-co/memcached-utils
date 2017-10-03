
#!/usr/bin/python

import argparse
import memcache
import sys

def main(argv=None):    
    argv = argv or sys.argv[1:]
    parser = argparse.ArgumentParser(description='Utility to get or set memcached values')
    parser.add_argument('-c', '--client', dest='client', help='memcached client address:port', default='127.0.0.1:11211') 
    parser.add_argument('-k', '--key', dest='key', help='get/set value for given key', default=None) 
    parser.add_argument('-v', '--val', dest='val', help='set this value (if omitted, just print the existing value)', default=None)
    parser.add_argument('-f', '--fmt', dest='fmt', help='format of value to be set (options : int or str))', default='int')
    args = parser.parse_args(argv)

    mc = memcache.Client([args.client])

    if args.key is None:
        sys.exit('Key is required')

    print 'Value of "{}" = {}'.format(args.key, mc.get(args.key))
    if args.val is not None:
        print 'Replacing this...'
        val = str(args.val) if args.fmt == 'str' else int(args.val)
        mc.set(args.key, val)
        print 'Value of "{}" = {}'.format(args.key, mc.get(args.key))


if __name__ == "__main__":       
    sys.exit(main())   

