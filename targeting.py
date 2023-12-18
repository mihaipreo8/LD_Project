# -----------------------------------------------------------------------------
# targeting.py
# Created: December 17, 2023
# Author: Mihai Preoteasa
#
# Description: Using LaunchDarkly's Python SDK to determine whether an email 
# address has access to the feature flag or not. 
# -----------------------------------------------------------------------------

import ldclient
from ldclient.config import Config
from ldclient import Context
from config import LD_SDK_KEY

# Initialize the LaunchDarkly client
def initialize_ld_client():
    ldclient.set_config(Config(LD_SDK_KEY))
    return ldclient.get()

def main():
    ld_client = initialize_ld_client()

    # Prompt the user for their email address
    user_email = input("Enter your email address: ")

    # Create a Context object with the provided email
    context = Context.builder("user-key") \
                     .set("email", user_email) \
                     .build()

    # Use the Context object in the variation call
    is_flag_enabled = ld_client.variation("kill-switch-mihai-1", context, False)

    if is_flag_enabled:
        print("Feature flag 'kill-switch-mihai-1' is ENABLED for the email:", user_email)
    else:
        print("Feature flag 'kill-switch-mihai-1' is DISABLED for the email:", user_email)

    # Close the client before exiting the main function
    ld_client.close()

if __name__ == "__main__":
    main()
