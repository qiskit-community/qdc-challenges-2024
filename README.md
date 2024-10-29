# IBM Quantum Developer Conference 2024

Welcome to the **IBM Quantum Developer Conference 2024!** To ensure you have the best challenge experience possible, please follow the preparation steps outlined in this GitHub README before the event.

## Installation and Setup
Please bring a laptop that can connect to the internet, as laptops will not be provided at the venue.

### Set up your IBM Quantum Platform Account
If you haven't already, create an account at the [IBM Quantum login page](https://quantum.ibm.com/login). **Be sure to sign up with the same email you used for event registration.** Your account will be linked to a specific [instance](https://docs.quantum.ibm.com/guides/instances) (in the form `hub/group/project`) for access to IBM Quantum services, and all attendees will be added to this instance for the conference.

### Create a Python Environment
Follow the steps [here](https://docs.quantum.ibm.com/guides/install-qiskit#install-the-qiskit-sdk-and-the-qiskit-runtime-client) to create a Python environment and install the Qiskit SDK and Qiskit Runtime. Since we will be using Jupyter notebooks, please complete step 4 in the guide to ensure Jupyter is installed.

Additionally, install these specific packages in your environment:
- The Qiskit Functions catalog client ([installation instructions here](https://docs.quantum.ibm.com/guides/functions#install-qiskit-functions-catalog-client))
- The Qiskit Transpiler Service client ([installation instructions here](https://docs.quantum.ibm.com/guides/functions#install-the-qiskit-ibm-transpiler-package))

> **Alternative Option:**
If you are not able to set up a Python environment or run Jupyter notebooks on your laptop, you may use an online lab environment, such as Google Colab or qBraid. See [this guide](https://docs.quantum.ibm.com/guides/online-lab-environments) for more details.

## Preparing for the Challenge
To ensure your environment is up to date, update your installed packages right before the challenge.

---
If you are setting up a **local environment**, follow these steps:
1. Activate your Python environment to ensure packages are installed in the correct workspace.
2. Download this [requirements file](https://github.com/qiskit-community/qdc-challenges-2024/requirements.txt) and save it in your workspace.
3. Run the following command to install or update all required packages:
    ```bash
    pip install -r path/to/requirements.txt --upgrade
    ```

    > **Tip:** Replace `path/to/requirements.txt` with the actual path to your `requirements.txt` file.

---
If you are using an **online lab environment** (e.g., Google Colab or qBraid), you can also use the `requirements.txt` file and `pip` command to install and update the required packages.

For specific instructions on adding the `requirements.txt` file and handling `pip` commands, please refer to your platform’s documentation, as some environments may require adjustments for notebooks or terminal interfaces.
