# Company Payroll System

A robust, object-oriented payroll management system built with **Python 3.14.0**. This project demonstrates clean architecture using the **Separation of Concerns** principle to handle various types of payables, including different employee categories, volunteers, and external invoices with validation rules.

## 📝 Description

The **Company Payroll System** is designed to calculate and manage payments for a diverse set of entities. Unlike simple payroll scripts, this system treats every payable entity (staff or invoice) polymorphically, allowing for flexible extension.

**Key Features:**
* **Employee Management:** distinct logic for Hourly, Salaried, and Commission-based employees.
* **Volunteer Support:** handles unpaid or stipend-based staff members.
* **Invoice Processing:** comprehensive system for processing invoices containing items like Books and Food.
* **Validation Logic:** a pluggable validation system for invoices (e.g., Mandatory vs. Complete validation rules).
* **Architecture:** modular design split into `employees`, `inventory`, `finance`, and `validators`.

## 🛠️ Technologies Used

* **Language:** Python 3.14.0
* **Paradigms:** Object-Oriented Programming (OOP), Polymorphism, Composition.

## 🚀 Installation Instructions

### Prerequisites
* Ensure you have **Python 3.14.0** (or newer) installed on your machine.

### Steps
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/company-payroll.git](https://github.com/yourusername/company-payroll.git)
    cd company-payroll
    ```

2.  **Verify Python Version:**
    ```bash
    python --version
    # Output should be Python 3.14.0
    ```

3.  **No external dependencies:** This project uses the Python Standard Library, so no `pip install` is required.

## 💻 Usage Examples

### Running the Default Simulation
The project comes with a `main.py` file that populates the system with dummy data and prints the payroll summary.

```bash
python company_payroll/main.py
