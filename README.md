# Cucumber Unified Framework

A unified automation framework built using [Cucumber](https://cucumber.io/) and [Behave](https://behave.readthedocs.io/en/stable/) for behavior-driven testing of web applications, demonstrated with login flows for OrangeHRM and Flipkart.

## 🚀 Features

- **Gherkin Syntax:** Test scenarios are written in human-readable language.
- **Python Automation:** Uses Behave with Selenium WebDriver.
- **Sample Feature Files:**
  - OrangeHRM Login validation ([features/Login.feature](features/Login.feature))
  - Flipkart Login ([features/steps/Flipkart.feature](features/steps/Flipkart.feature))
- **Auto-Triage Mechanism:** Captures test results and failure reasons, with output to Excel or CSV.
- **Continuous Integration:** Includes GitHub Actions CI for automated test runs.

## 🛠 Technologies Used

- Python (Behave, Selenium)
- Gherkin
- GitHub Actions
- Pandas (for result files)
- Chrome WebDriver

## 📂 Repository Structure

```
features/
├── steps/
│   ├── login.py             # Step definitions for login scenarios
│   ├── Flipkart.feature     # Flipkart login feature
│   ├── Login.feature        # OrangeHRM login feature
│   └── generate_steps.py    # Tool to auto-generate Python step definitions
├── environment.py           # Hooks for test lifecycle and result tracking
.github/
└── workflows/
    └── cicd.yaml            # CI workflow for scheduled/manual/test runs
```

## ⚡️ Getting Started

### Prerequisites

- Python 3.8+
- Chrome WebDriver
- Google Chrome installed

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sheiksibbu/Cucumber_UnifiedFramework.git
   cd Cucumber_UnifiedFramework
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Includes: behave, selenium, pandas, openpyxl, etc.)*

3. **Set up ChromeDriver:**
   - Make sure ChromeDriver matches your Chrome version and is in your PATH.

### Running Tests

- **Via Behave (local):**
   ```bash
   behave features --tags=@Smoke12345
   ```

- **Via GitHub Actions (CI):**
   - Tests are automatically triggered for pushes, PRs, and on schedule. See [.github/workflows/cicd.yaml](.github/workflows/cicd.yaml).

### Test Results

- Results and failure reasons are captured and exported to Excel automatically (see `after_all` hook in `features/environment.py`).

## 📝 Example Scenarios

**OrangeHRM Login:**  
```gherkin
Scenario: Successsful login and home page verification
  Given the user navigates to the OrangeHRM login page
  When the user enters valid credentails
  And clicks the Login button
  Then the user should be redirected to the home page
  And the page title should be OrangeHRM
  And the dashboard should display OrangeHRM Logo
```

**Flipkart Login:**  
```gherkin
Scenario: Successful login with valid credentials
  Given I open the Flipkart login page
  When I enter the valid username "testuser@example.com" and password "testpassword"
  And I click the login button
  Then I should be redirected to the homepage
  And I should see the user's name "Test User" on the homepage
```

## 🤝 Contributing

Contributions are welcome!  
Fork the repo, create a feature branch, and open a pull request.

## 📄 License

_This project does not specify a license yet. Please add one for open source usage._

## 🔗 Links

- [Behave Documentation](https://behave.readthedocs.io/en/stable/)
- [Cucumber Reference](https://cucumber.io/)
- [Selenium WebDriver](https://selenium.dev/documentation/webdriver/)
- [GitHub Actions](https://docs.github.com/en/actions)

---

*Maintained by [sheiksibbu](https://github.com/sheiksibbu)*