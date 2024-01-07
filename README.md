# BrewMatch Project

## Overview

BrewMatch is a web application that allows users to find cafes in a specified city. It utilizes the Open Brewery DB API to fetch information about breweries and displays it in an easy-to-read format.

## Features

- Search for cafes by city name.
- Display cafe details such as name, address, type, website URL, phone number, and postal code.

## Deployment

The BrewMatch application is deployed and can be accessed at the following URL: [https://brewmatch.onrender.com](https://brewmatch.onrender.com)

## Local Setup

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation Steps

1. Clone the repository to your local machine.
    ```   git clone https://github.com/your-username/BrewMatch.git```

2. Navigate to the cloned directory.
    ```cd BrewMatch```

3. Install the required Python packages.
    ```pip install -r requirements.txt```

   Note: The requirements.txt should contain streamlit and requests.

4. Run the Streamlit application.
    ```streamlit run main.py```

5. The application should now be running on your local server, typically at [http://localhost:8501](http://localhost:8501).

## Usage

- Open the application in a web browser.
- Enter a city name into the input field.
- Click the 'Fetch Cafes' button to display the cafes in the specified city.

## Contributions

Contributions to the BrewMatch project are welcome. Please ensure to follow the project's contribution guidelines when submitting pull requests.
