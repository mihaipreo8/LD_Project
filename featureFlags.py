# -----------------------------------------------------------------------------
# featureFlags.py
# Created: December 17, 2023
# Author: Mihai Preoteasa
#
# Description: Using LaunchDarkly's Python SDK to access Feature Flags
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

    # Create a Context object with attributes
    context = Context.builder("context-key-mihaipreo") \
                     .set("firstName", "Mihai") \
                     .set("lastName", "Preoteasa") \
                     .set("email", "mihaipreo@gmail.com") \
                     .set("groups", ["LaunchDarkly", "MihaiCompany"]) \
                     .build()
    # context = Context.builder("context-key-rmartin") \
    #                  .set("firstName", "Rachel") \
    #                  .set("lastName", "Martin") \
    #                  .set("email", "rmartin@launchdarkly.com") \
    #                  .set("groups", ["LaunchDarkly"]) \
    #                  .build()

    # Use the Context object in the variation call
    is_flag_enabled = ld_client.variation("kill-switch-mihai-1", context , False)

    if is_flag_enabled:
        print("Kill switch is ENABLED")
    else:
        print("Kill switch is DISABLED")

    # Close the client before exiting the main function
    ld_client.close()

if __name__ == "__main__":
    main()
