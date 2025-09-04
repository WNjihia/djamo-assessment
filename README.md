# Google Maps Appium Test Suite

## Overview

This repository contains an automated test suite for Google Maps, written using **Appium** and **pytest-bdd**. The test suite covers scenarios such as searching for destinations, starting itineraries, and verifying directions across multiple travel modes.

---

## Approach & Technical Choices

- **Framework**: Pytest with pytest-bdd for BDD-style scenarios.
- **Automation Tool**: Appium (UIAutomator2) for interacting with Android devices/emulators.
- **Page Object Model (POM)**: Implemented to separate test logic from UI interactions.
- **Device Setup**: Android emulator for testing. Configurable via `driver_setup.py`.
- **Locator Strategy**: Mix of `ID`, `Accessibility ID`, and `XPath`.
- **Travel Modes**: Driving, transit, walking, cycling are considered in assertions.
- **Assertions**: Flexible validations to account for dynamic elements such as duration or estimated time.

---

## Test Scenarios

Example scenario:

```gherkin
Scenario: When I launch the app, I can start an itinerary
    Given the Google Maps App is opened
    When I search for 'Abidjan'
    And I start an itinerary towards 'Abidjan'
    And I change the starting point to 'Dakar'
    Then the itinerary should show directions between starting point and destination
```


## How to Run the Test Suite

1. Clone the repository and navigate to project folder:
```
git clone https://github.com/WNjihia/djamo-assessment.git
cd djamo-assessment
```

2. Set up and activate virtual environment:
```
python -m venv <venv>
source venv/bin/activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Start the appium server:
```
appium
```

5. Start the emulator or connect physical device 
6. Run the test:
pytest -v step_definitions/test_itinerary.py


## Known Pitfalls

1. **Use of Try/Catch for Element Handling**  
   Some steps rely on try/catch blocks to handle cases where elements may not be immediately displayed or located. This can mask underlying issues and make tests less deterministic.

2. **Sign-In Screen**  
   Google Maps occasionally shows a sign-in screen, which can interrupt the test flow. Currently, this is mitigated using a try/catch block to dismiss or bypass the sign-in prompt if it appears.

3. **Dynamic Elements**  
   Certain UI elements, such as driving time, traffic updates, or estimated arrival, can change with each test run. Assertions based on these values may occasionally fail.

4. **Network Dependence**  
   The tests require an active internet connection to load Google Maps data. Slow or unstable connections can affect loading times and cause flaky test results.

5. **Appium Version Compatibility**  
   Some Appium versions may not support certain interactions on newer Android OS versions. Additionally, the driver setup does not currently account for different Android versions, which may lead to failures.

6. **Device Prompts**  
   Some devices may display unexpected prompts (e.g., stylus usage suggestions) that can interrupt the test flow and cause failures.


## Future Improvements

Support multiple device configurations via config.py and driver_setup.py.

Parameterize the city and starting points, travel mode and dynamically verify correct mode

Add screenshot capture for failed steps.

Implement retry mechanism for flaky network/UI interactions.

Integrate with cloud device farms (e.g., BrowserStack, Sauce Labs or Lambdatest).


## CI/CD Pipeline (Bitrise Integration)

Trigger: Run the pipeline on every pull request, nightly or when a new release build is created

Workflow:
(assumption - we are using Bitrise for the CI/CD integration)

Checkout code from repository.

Set up Python environment.

Install dependencies from requirements.txt.

Start Android emulator (Bitrise stack supports emulators).

Run test suite via pytest.

Generate test reports (HTML).

Store artifacts for inspection (screenshots, reports).

Notify team via Slack or email on failures.


Frequency: On every pull request and nightly for regression runs.

Report Visualization: Use pytest HTML reports plugin or Bitrise built-in test report parsing.
