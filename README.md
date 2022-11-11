# Garage API
An API to control garage doors with a Raspberry Pi and some relays.

---

## Running
Install the requirements with `pip install -r requirements.txt`.
Run the API with `uvicorn garage:api`.

### Authentication
The API is expecting a valid API key in the form of a bearer token. See configuration below to see where to set it up.

## Configuration
Create a `garage.json` file using the provided example. Configure your garage doors accordingly, the `control_pin` is the GPIO pin on your Raspberry Pi for that garage door. Configure as many unique API keys as you like, one of them will be required for the API calls (with the exception of the `ping` endpoint).