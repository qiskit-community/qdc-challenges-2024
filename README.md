# IBM Quantum Developer Conference 2024

Welcome to the **IBM Quantum Developer Conference 2024**! To ensure you have the best challenge experience possible it is very important to follow the preparations steps outlined in this GitHub README prior to the event.

## Installation and Setup
Please bring your own laptop that you can connect to the internet. Laptops will not be provided at the venue.

### Have your IBM Quantum Platform account
To get one, go to the [IBM Quantum login page](https://quantum.ibm.com/login). **You must sign up with the same email you used to register for the event.** Your user account is associated with one or more [instances](https://docs.quantum.ibm.com/guides/instances) (in the form `hub/group/project`) that gives access to IBM Quantum services, and all event attendees will be added to a specific instance for the duration of QDC.

### Set up a Python enviornment
Follow the steps [here](https://docs.quantum.ibm.com/guides/install-qiskit#install-the-qiskit-sdk-and-the-qiskit-runtime-client) to create a Python environment and install the Qiskit SDK and Qiskit Runtime. We will be using Jupyter notebooks for the challenges, so please make sure to follow step 4 of the install guide.

Make sure to also install these additional packages in your Python environment:
- The Qiskit Functions catalog client (see install instructions [here](https://docs.quantum.ibm.com/guides/functions#install-qiskit-functions-catalog-client))
- The Qiskit Transpiler Service client (see install instructions [here](https://docs.quantum.ibm.com/guides/functions#install-the-qiskit-ibm-transpiler-package))

**Alternative environment option:**
If you are not able to set up a Python environment or run Jupyter notebooks directly on your laptop, you may use an online lab environment (such as Google Colab or QBraid instead). See [here](https://docs.quantum.ibm.com/guides/online-lab-environments) for more information. If you opt for this method, ensure that your online lab environment has the latest version of the following packages: `qiskit`, `qiskit-ibm-runtime`, `qiskit-ibm-transpiler`, and `qiskit-ibm-catalog`.

### Before the challenge
Make sure your installed packages are up to date with the latest versions:
```
pip install <packag_name> -U
```
You may run the command above for each package in your python environment.
