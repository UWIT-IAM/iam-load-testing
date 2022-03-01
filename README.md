# IAM Load Testing

This package is simply a place to store [Locust] configurations
for IAM tools. Locust is an open-source tool for generating
requests against a server. 

Technically, you could wire up locust to do pretty much anything you 
wanted, but its out-of-the-box use case is for making http calls
to remote servers. Please read the [Locust] documentation for more details.

For more complex use cases, you can check out their
[write a client documentation](http://docs.locust.io/en/stable/testing-other-systems.html#testing-other-systems)

## First-time Users

Make sure [poetry] is installed on your system.

- Clone the repository and make sure you are in the repository directory. 
- Run `poetry install` to download dependencies.
- Then you can use `poetry run locust -f <locust-file-name>` to create a locust server.

Example output when creating the `husky_directory` locust server:

```text
❯ poetry run locust -f husky_directory.py
[2022-03-01 14:34:54,976] MacBook-Pro/INFO/locust.main: Starting web interface at http://0.0.0.0:8089 (accepting connections from all network interfaces)
[2022-03-01 14:34:55,052] MacBook-Pro/INFO/locust.main: Starting Locust 2.2.1
```

From here, you can visit http://0.0.0.0:8089 in your web browser to create 
request swarms and monitor them to your liking. Use `<CTRL>+C` to kill the server,
which also prints out some statistics from your test(s).

Use `poetry run locust --help` for a full list of runtime options.

[Locust]: https://locust.io/
[poetry]: https://python-poetry.org

## Contributing

Feel free to contribute to this as desired. Pull requests are not required, but if 
you are changing someone else's configuration, it might be a good courtesy to 
open a PR or let them know.

### General Maintenance

`poetry update` will bump dependencies to the next allowable version and update 
`poetry.lock`. 

`poetry add <package-name>` will add a new dependency to poetry. (For instance, you 
could do `poetry add uw-webdriver-recorder` if you wanted to write a client to flood 
using actual remote browser instances...as an idea.)
