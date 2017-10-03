
# Python utility to get / set (read/write) values from memcached 
(requires package python-memcached)

#### Install 
pip install memcached-utils

#### Print the value of key `foo` from memcached
```
memcached-utils.py -k "foo"
```

#### Get the value of key `foo` for memcached client running on `127.0.0.1:11211` (default)

```
memcached-utils.py -k "foo" -v bar -f str
```

#### Set the value of key `foo` to `bar` (integer)

```
memcached-utils.py -k "foo" -v bar -f int
```

#### Set the value of key `foo` to `bar` (string)

```
memcached-utils.py -k "foo" -v bar -f str
```


