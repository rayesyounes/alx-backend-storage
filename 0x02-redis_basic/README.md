# Project: 0x02. Redis basic

## Resources

### Read or watch:

* [Redis Crash Course Tutorial](https://intranet.alxswe.com/rltoken/hJVo3XwMMFFoApyX8zPXvA)
* [Redis commands](https://intranet.alxswe.com/rltoken/oauvbRmxM12SxvimzqhrOg)
* [Redis python client](https://intranet.alxswe.com/rltoken/imfgFhAZPlg7YMZ_tHvFZw)
* [How to Use Redis With Python](https://intranet.alxswe.com/rltoken/7SluvFvgckwVgsvrfOf1CQ)

### General

* All of your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
* All of your files should end with a new line
* A <code>README.md</code> file, at the root of the folder of the project, is mandatory
* The first line of all your files should be exactly <code>#!/usr/bin/env python3</code>
* Your code should use the <code>pycodestyle</code> style (version 2.5)
* All your modules should have documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)
* All your classes should have documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)
* All your functions and methods should have documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* All your functions and coroutines must be type-annotated.

### Installation
- Install Redis on Ubuntu 18.04:
  ```
  $ sudo apt-get -y install redis-server
  $ pip3 install redis
  $ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
  ```

### Use Redis in a container
- Redis server is stopped by default - when you are starting a container, you should start it with:
  ```
  service redis-server start
  ```

## Tasks

### 0. Writing strings to Redis (Mandatory)
- Create a Cache class.
- In the `__init__` method, store an instance of the Redis client as a private variable named `_redis` (using `redis.Redis()`) and flush the instance using `flushdb`.
- Create a `store` method that takes a `data` argument and returns a string. The method should generate a random key (e.g., using uuid), store the input data in Redis using the random key, and return the key.
- Type-annotate `store` correctly. Remember that `data` can be a str, bytes, int, or float.

### 1. Reading from Redis and recovering the original type (Mandatory)
- Create a `get` method that takes a key string argument and an optional Callable argument named `fn`. This callable will be used to convert the data back to the desired format.
- Remember to conserve the original Redis.get behavior if the key does not exist.
- Also, implement 2 new methods: `get_str` and `get_int` that will automatically parameterize `Cache.get` with the correct conversion function.

### 2. Incrementing values (Mandatory)
- Define a `count_calls` decorator that takes a single method Callable argument and returns a Callable.
- As a key, use the qualified name of the method using the `__qualname__` dunder method.
- Create and return a function that increments the count for that key every time the method is called and returns the value returned by the original method.

### 3. Storing lists (Mandatory)
- Define a `call_history` decorator to store the history of inputs and outputs for a particular function.
- Every time the original function will be called, add its input parameters to one list in Redis and store its output into another list.
- In `call_history`, use the decorated function’s qualified name and append ":inputs" and ":outputs" to create input and output list keys, respectively.

### 4. Retrieving lists (Mandatory)
- Implement a `replay` function to display the history of calls of a particular function.
- Use keys generated in previous tasks to generate the following output.

### 5. Implementing an expiring web cache and tracker (Advanced)
- Implement a `get_page` function (prototype: `def get_page(url: str) -> str:`).
- The core of the function is very simple. It uses the requests module to obtain the HTML content of a particular URL and returns it.

| Task | File |
| ---- | ---- |
| 0. Writing strings to Redis | [exercise.py](./exercise.py) |
| 1. Reading from Redis and recovering original type | [exercise.py](./exercise.py) |
| 2. Incrementing values | [exercise.py](./exercise.py) |
| 3. Storing lists | [exercise.py](./exercise.py) |
| 4. Retrieving lists | [exercise.py](./exercise.py) |
| 5. Implementing an expiring web cache and tracker | [web.py](./web.py) |

