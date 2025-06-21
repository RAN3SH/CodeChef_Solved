# Job Application Tracker - DEVWEEKEND Skill Test Report

## Author: Ranesh

This text covers my solution attempts for the three cases in the CodeChef DEVWEEKEND Skill Test.

---

## ✅ Case 1: CLI Job Application (Basic Input & Validation)

- Implemented a Python program with a command-line menu to:
  - Add job applications with input fields: name, email, job role, and experience.
  - Validate that:
    - Name and job role are not empty.
    - Email contains "@" and "." in valid positions.
    - Experience is a non-negative number.

- If all inputs are valid, the application is added successfully and saved to a file `applications.txt`.

- The format used in the file:
  Name: Alice
  Email: alice@example.com
  Job Role: Backend Developer
  Experience: 2 years


---

## ✅ Case 2: List Applications from File

- Implemented the `list_applications()` function that:
- Opens `applications.txt` in read mode.
- If the file is empty or missing, prints: `No applications found.`
- Otherwise, prints all saved applications clearly to the console.

- Ensured the file is opened only once, as required by the test case.

---

## ❌ Case 3: Django Job Application Form (Web App)

- I started implementing a Django-based web application, but was not able to complete it.

---

## Conclusion

- Case 1 and Case 2 were fully implemented and passed all requirements.
- Case 3 (Django project) was not finished.

Thank you!
