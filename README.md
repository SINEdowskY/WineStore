# Wine Store

Welcome to Wine Store, an online platform built with Django for purchasing and exploring a variety of wines.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Authentication**: Allow users to register, login, and manage their accounts.
- **Product Catalog**: Browse through a wide selection of wines with detailed descriptions.
- **Shopping Cart**: Add wines to the cart and proceed to checkout for purchase.
- **Order Management**: Users can view their order history and track the status of their orders.
- **Admin Panel**: Administrators can manage products, orders, and users easily through the admin interface.

## Installation

1. Clone the repository:

    ```bash
    git clone git@github.com:SINEdowskY/WineStore.git
    ```

2. Navigate to the project directory:

    ```bash
    cd WineStore
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv env
    ```

4. Activate the virtual environment:

    - On Windows:

    ```bash
    env\Scripts\activate
    ```

    - On macOS and Linux:

    ```bash
    source env/bin/activate
    ```

5. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Run migrations:

    ```bash
    python manage.py migrate
    ```

7. Start the development server:

    ```bash
    python manage.py runserver
    ```

8. Open your browser and navigate to `http://localhost:8000` to access the application.

## Usage

1. **Register/Login**: Create a new account or log in with existing credentials.
2. **Explore Wines**: Browse through the collection of wines available in the catalog.
3. **Add to Cart**: Select wines and add them to your shopping cart.
4. **Checkout**: Proceed to checkout, review your order, and provide necessary details for delivery.
5. **Manage Orders**: Users can view their order history and track the status of their current orders.
6. **Admin Interface**: Administrators can access the admin panel at `/admin` to manage products, orders, and users.

## Contributing

Contributions are welcome! If you have any suggestions, enhancements, or bug fixes, feel free to open an issue or create a pull request.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
