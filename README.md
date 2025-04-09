# 🧪 BDD Automation Framework - Python + Selenium + Behave

This project is a Behavior-Driven Development (BDD) automation testing framework built using **Python**, **Selenium WebDriver**, and **Behave** (Cucumber for Python). It is designed for functional UI test automation and follows best practices in test structure and maintainability.

---

## 📁 Project Structure

```
project-root/
│
├── features/
│   ├── steps/                  # Step Definitions
│   ├── environment.py          # Hooks (setup & teardown)
│   ├── *.feature               # Gherkin feature files
│
├── logs/                       # Log files
├── reports/                    # Test reports (Allure/HTML)
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
```

---

## ⚙️ Tools & Technologies

- **Language:** Python 3.11.5 
- **Test Framework:** Behave (BDD)
- **Automation:** Selenium WebDriver  
- **Design Pattern:** Page Object Model (POM)  
- **Reporting:** Allure
- **Logging:** Python’s logging module  
- **Others:** ConfigParser, time, os, etc.

---

## 🚀 How to Run Tests

1. **Clone the repository:**
   ```bash
   git clone https://github.com/VishalPommedi/PractiesSelenium.git
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run tests:**
   ```bash
   behave
   ```

4. *(Optional)* **Generate Allure Report:**
   ```bash
   behave -f allure_behave.formatter:AllureFormatter -o reports/ features/
   allure serve reports/
   ```

---

## 🧪 Sample Feature File

```gherkin
Feature: Login Functionality

  Scenario: Valid login
    Given the user is on the login page
    When the user enters valid credentials
    Then the user should be redirected to the dashboard
```

---

## ✍️ Author

- **Name:** Vishal Pommedi  
- **LinkedIn:** [[www.linkedin.com/in/vishal-pommedi](www.linkedin.com/in/vishal-pommedi)] 
- **GitHub:** [[github.com/yourusername](https://github.com/VishalPommedi)]

---

## 📌 Notes

- You can customize `environment.py` to include setup/teardown hooks.
- Add environment-specific config using `.ini` or `.env` files.
- Extend this framework to integrate with CI tools like Jenkins or GitHub Actions.

---

## ✅ To Do (Optional)

- [ ] Add Docker support  
- [ ] Integrate CI/CD pipeline  
- [ ] Add parallel test execution  
- [ ] Expand test coverage