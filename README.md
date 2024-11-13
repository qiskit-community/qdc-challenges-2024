# IBM Quantum Developer Conference 2024

Welcome to the IBM Quantum Developer Conference 2024! These challenges are designed to test your quantum computing skills using the Qiskit product features announced during QDC. The competition spans three days and features two challenge tracks.

## Leaderboard

Want to see how you stack up against the competition? Search for your submission on the [Challenges Leaderboard](https://challenges.quantum.ibm.com/qdc-2024).

## Contest Rules

Please carefully review [the contest rules](./contest_rules.md) to ensure a smooth competition experience.

## Installation and Setup

To ensure you have the best challenge experience possible, please follow the preparation steps outlined in this GitHub README before the event. Please bring a laptop that can connect to the internet, as laptops will not be provided at the venue.

### Set up your IBM Quantum Platform Account
If you haven't already, create an account at the [IBM Quantum login page](https://quantum.ibm.com/login). **Be sure to sign up with the same email you used for event registration.** Your account will be linked to a specific [instance](https://docs.quantum.ibm.com/guides/instances) (in the form `hub/group/project`) for access to IBM Quantum services, and all attendees will be added to this instance for the conference.

### Create a Python Environment
Follow the steps [here](https://docs.quantum.ibm.com/guides/install-qiskit#install-the-qiskit-sdk-and-the-qiskit-runtime-client) to create a Python environment and install the Qiskit SDK and Qiskit Runtime. Since we will be using Jupyter notebooks, please complete step 4 in the guide to ensure Jupyter is installed.

Additionally, install these specific packages in your environment:
- The Qiskit Functions catalog client ([installation instructions here](https://docs.quantum.ibm.com/guides/functions#install-qiskit-functions-catalog-client))
- The Qiskit Transpiler Service client ([installation instructions here](https://docs.quantum.ibm.com/guides/qiskit-transpiler-service#install-the-qiskit-ibm-transpiler-package))

> **Alternative Option:**
If you are not able to set up a Python environment or run Jupyter notebooks on your laptop, you may use an online lab environment, such as Google Colab or qBraid. See [this guide](https://docs.quantum.ibm.com/guides/online-lab-environments) for more details.

## Preparing for the Challenge
To ensure your environment is up to date, update your installed packages right before the challenge.

---
If you are setting up a **local environment**, follow these steps:
1. Activate your Python environment to ensure packages are installed in the correct workspace.
2. Download this [requirements file](./requirements.txt) and save it in your workspace.
3. Run the following command to install or update all required packages:
    ```bash
    pip install -r path/to/requirements.txt --upgrade
    ```

    > **Tip:** Replace `path/to/requirements.txt` with the actual path to your `requirements.txt` file.

---
If you are using an **online lab environment** (e.g., Google Colab or qBraid), you can also use the `requirements.txt` file and `pip` command to install and update the required packages.

qBraid has also setup a special environment with all required packages installed. Please look for the environment "QDC 2024" in the [Environment tab](https://docs.qbraid.com/lab/user-guide/environments) to activate it. 

For specific instructions on adding the `requirements.txt` file and handling `pip` commands, please refer to your platform’s documentation, as some environments may require adjustments for notebooks or terminal interfaces.

## Challenges Topics

Every afternoon during QDC, attendees will have the opportunity to participate in hands-on coding challenges, where you will be able to practice using the latest tools and features highlighted in the morning seminars. You will be using Jupyter notebooks to complete the challenges, which can be found in this dedicated GitHub repository. To ensure you have the best challenge experience possible it is very important to follow the preparations steps outlined in the GitHub README prior to the event.

Every day there will be two challenges happening in parallel, and you may choose which one you would like to participate in based on your skills and interests. See below a summary of topics covered by each challenge:

### Day 1 - Circuits and Functions
- Track A: Introduction to Qiskit Functions and Qiskit addons
    - Get familiar with the IBM Functions catalogue
    - Learn how to use Circuit functions
    - Build your own function using Qiskit addons

- Track B: Utility-scale workload with sample-based quantum diagonalization (SQD)
    - Learn how to use SQD to improve results from a Hamiltonian simulation problem

### Day 2 - Transpilation
- Track A: Introduction to transpilation in Qiskit
    - Understand how to use `generate_preset_passmanager` with different options
    - Build custom pass managers
    - Get started with the Qiskit Transpiler Service

- Track B: Experiment with custom pass managers
    - Build the best possible custom pass manager
    - Optimize your circuit to reduce circuit depth and two-qubit gates

### Day 3 - Accuracy and Execution
- Track A: Introduction to noise learning and job debugging
    - Learn debugging techniques for error mitigation queries
    - Use noise learning helper programs to estimate noise
- Track B: Apply runtime error mitigation to a utility-scale problem
    - Choose the best error mitigation strategy based on learned noise

## Learning Resources

The seminars and challenges at QDC are designed to cover a broad range of advanced topics featuring Qiskit tools and capabilities. While participants are not expected to have a deep understanding of everything that will be covered we do recommend familiarizing yourself with the basics before attending the event. See below a collection of recommended resources for learning more about the topics prior to the event:

### Installation and Setup

- [Guide - Introduction to Qiskit](https://docs.quantum.ibm.com/guides)
- [Guide - Install Qiskit](https://docs.quantum.ibm.com/guides/install-qiskit)
- [Guide - Setup an IBM Quantum channel](https://docs.quantum.ibm.com/guides/setup-channel)
- [Guide - Qiskit Code Assistant](https://docs.quantum.ibm.com/guides/qiskit-code-assistant)

### Day 1 - Circuits and Functions

- [Guide - Hello World](https://docs.quantum.ibm.com/guides/hello-world)
- [Guide - Introduction to Qiskit Functions](https://docs.quantum.ibm.com/guides/functions)
- [Tutorial - Building workflows with the IBM Circuit function](https://learning.quantum.ibm.com/tutorial/building-workflows-with-the-ibm-circuit-function)
- [Tutorial - Compute dissociation curves for strong coupling systems with QunaSys QURI Chemistry](https://learning.quantum.ibm.com/tutorial/compute-dissociation-curves-for-strong-coupling-systems-with-quna-sys-qsci)
- [Tutorial - Solve higher-order binary optimization problems with Q-CTRL's Optimization Solver](https://learning.quantum.ibm.com/tutorial/solve-higher-order-binary-optimization-problems-with-q-ctrls-optimization-solver)
- [Guide - Qiskit addons](https://docs.quantum.ibm.com/guides/addons)

### Day 2 - Transpilation

- [Guide - Introduction to transpilation](https://docs.quantum.ibm.com/guides/transpile)
- [Guide - Transpiler stages](https://docs.quantum.ibm.com/guides/transpiler-stages)
- [Guide - Transpile with pass managers](https://docs.quantum.ibm.com/guides/transpile-with-pass-managers)
- [Guide - Transpile circuits remotely with the Qiskit Transpiler Service](https://docs.quantum.ibm.com/guides/qiskit-transpiler-service)

### Day 3 - Accuracy and Execution

- [Guide - Introduction to primitives](https://docs.quantum.ibm.com/guides/primitives)
- [Guide - Noise learning helper](https://docs.quantum.ibm.com/guides/noise-learning)
- [Guide - Error mitigation and suppression techniques](https://docs.quantum.ibm.com/guides/error-mitigation-and-suppression-techniques)
- [Tutorial - Combine error mitigation options with the estimator primitive](https://learning.quantum.ibm.com/tutorial/combine-error-mitigation-options-with-the-estimator-primitive)
