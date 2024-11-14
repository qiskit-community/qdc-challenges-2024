# IBM Quantum Developer Conference 2024

Welcome to the IBM Quantum Developer Conference 2024! These challenges are designed to test your quantum computing skills using the Qiskit product features announced during QDC. The competition spans three days and features two challenge tracks.

## Contest Rules

Please carefully review [the contest rules](./contest_rules.md) to ensure a smooth competition experience.

## Installation and Setup

To participate, please complete the setup steps below. Remember to bring a laptop with internet access, as no devices will be provided at the venue.

### Step 1: Set up Your IBM Quantum Platform Account
1. [Create an IBM Quantum account](https://quantum.ibm.com/login) if you haven't already.
2. **Sign up using the same email address you registered with for this event**. Your account will be linked to a specific [instance](https://docs.quantum.ibm.com/guides/instances) for IBM Quantum services.

### Step 2: Create a Python Environment
1. Follow [this guide](https://docs.quantum.ibm.com/guides/install-qiskit#install-the-qiskit-sdk-and-the-qiskit-runtime-client) to create a Python environment and install the Qiskit SDK and Runtime. Ensure Jupyter is installed (Step 4 in the guide).
2. Install additional packages:
   - Qiskit Functions catalog client ([instructions](https://docs.quantum.ibm.com/guides/functions#install-qiskit-functions-catalog-client))
   - Qiskit Transpiler Service client ([instructions](https://docs.quantum.ibm.com/guides/qiskit-transpiler-service#install-the-qiskit-ibm-transpiler-package))

> **Alternative:** If setting up Python or Jupyter locally is difficult, consider using Google Colab or qBraid. See [this guide](https://docs.quantum.ibm.com/guides/online-lab-environments) for details.


## Preparing for the Challenge

To ensure all tools are up to date, please update your packages right before the challenge begins.

**If using a local environment:**
1. Activate your Python environment.
2. Download the [requirements file](./requirements.txt) to your workspace.
3. Run this command to install/update packages:

    ```bash
    pip install -r path/to/requirements.txt --upgrade
    ```

   > **Note:** Replace `path/to/requirements.txt` with your file's path.

**If using an online lab environment:**  
Use the same `requirements.txt` file and pip command to install/update packages. For qBraid, activate the "QDC 2024" environment under the [Environment tab](https://docs.qbraid.com/lab/user-guide/environments), which comes pre-configured.

## Challenge Notebooks

Each day, the challenge notebooks will be available in their respective "Day" folders within the GitHub repository. **Please download the notebooks for each day, open them, and run them to proceed with the challenges.**


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
