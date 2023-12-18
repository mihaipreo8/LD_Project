# LD_Project

Instructions:

Step 1: Clone the GitHub Repository and Overview of Contents
	Open a terminal or Command Prompt.
	Run git clone https://github.com/mihaipreo8/LD_Project.git.
	The repository contains 4 files:
		config.py: Contains the SDK key for LaunchDarkly.
		featureFlags.py: Uses LaunchDarkly's Python SDK to access Feature Flags.
		targeting.py: Uses LaunchDarkly's Python SDK to determine if an email address has access to the feature flag.
		readme.md: Provides information and instructions about the project.

Step 2: Install and Set Up Python
	Check if Python is Installed
		On Linux/MacOS: In terminal, run python --version or python3 --version.
		On Windows: In Command Prompt, run python --version.
	Install Python if Not Present
		Linux: Use package manager, e.g., sudo apt-get install python3.
		MacOS: Install via Homebrew: brew install python.
		Windows: Download from Python's website and install with "Add Python to PATH" option.
	Add Python to PATH if Needed
		Windows: Through 'Environment Variables' in 'System Properties', add Python's install path (e.g., C:\Python39) to 'Path'.
		Linux/MacOS: Usually automatic. If manual addition is needed, edit .bashrc or .bash_profile to include export PATH="/path/to/python:$PATH".

Step 3 (Optional): Initialize a Python Virtual Environment
Using a Python virtual environment allows for isolated project dependencies, avoiding conflicts with the global Python installation. It's essential for maintaining a consistent development environment across different machines and projects.
	Quick Steps
		Navigate to Project Directory:
			In terminal or Command Prompt, use cd path/to/project.
		Create Virtual Environment:
			Run python -m venv venv (or python3 -m venv venv on Linux/MacOS). This creates a venv directory in your project folder.
		Activate Virtual Environment:
			Windows: venv\Scripts\activate.
			Linux/MacOS: source venv/bin/activate.
			
Step 4: Install LaunchDarkly SDK
	In your virtual environment, install the LaunchDarkly SDK using pip:
		Run 'pip install launchdarkly-server-sdk'

Step 5: Impersonate User for Review
	As a LaunchDarkly reviewer, impersonate the user mihaipreo@gmail.com on the LaunchDarkly platform.
	Test the submission with the feature flag turned both On and Off.

Step 6: Run Feature Flag Test Script
	In Terminal or Command Prompt, run the script to test feature flags:
		Use python featureFlags.py or python3 featureFlags.py.
	This will display the status (Enabled/Disabled) of the feature flag, considering the set targeting rules.
	In the Python script, two context objects are assigned, one commented out. Feel free to swap commenting between these two to observe different outcomes.

Step 7: Test Targeting with Email Input
	Run a targeting test script in Terminal or Command Prompt:
		Use python targeting.py or python3 targeting.py.
	You'll be prompted to input an email address.
	According to LaunchDarkly platform rules, only the email mihaipreo@gmail.com will return ENABLED, while any other email will result in DISABLED.
	
	