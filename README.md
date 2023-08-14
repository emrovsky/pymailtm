# mail.tm Python Library

The `mailtm` library is a simple Python wrapper for interacting with the [mail.tm](https://mail.tm) API. It provides easy-to-use functions to create temporary email accounts, retrieve available domains, and obtain tokens for these accounts. This is useful for testing and development purposes where you need temporary email addresses.

## Installation

You can install the mailtm.py from repo

## Usage

Here's how you can use the `mailtm` library to perform various actions:

### Importing the Library

```python
import mailtm
```

### Creating a Temporary Email Account

```python
account = create_account(domain) -> you need to get <domain> value from get_domain()
print(account["mail"])
print(account["password"])
```

### Getting Available Domains

```python
# Get a list of available domain
domain = get_domain()["domain"]
print("Available Domain:", domain)
```

### Getting Tokens for Accounts

```python
# Get a token from a account's username and password
token = get_token_of_account(mail="mail",password="password")
print(token)
```



## Contributing

Contributions are welcome! If you find a bug or want to add a new feature, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

**Disclaimer:** This library is designed to interact with the [mail.tm](https://mail.tm) service. Use it responsibly and in accordance with the terms of use of the service. The `mailtm` library and its developers are not responsible for any misuse or violation of terms.
