import csv
import requests

# Jira Cloud REST API endpoint
api_url = "your_site_url"

# Jira credentials
username = "your_username"
api_token = "your_api_token"

# Function to remove groups from issue security scheme levels
def remove_groups_from_security_scheme(scheme_id, level_id, memberId):
    # Construct the URL to remove groups from the security scheme level
    remove_groups_url = f"{api_url}/rest/api/3/issuesecurityschemes/{scheme_id}/level/{level_id}/member/{memberId}"

    # Send a DELETE request to remove the groups
    response = requests.delete(remove_groups_url, auth=(username, api_token))
    if response.status_code == 204:
        print(f"Groups removed from security scheme level {level_id} in scheme {scheme_id}")
    else:
        print(f"Failed to remove groups from security scheme level {level_id} in scheme {scheme_id}")

# Read the CSV file and process each row
with open("files/remove-member-testmigration_2023-11-23T11 57 41.605Z.csv") as file:
    reader = csv.reader(file)
    next(reader)

# Initialize a counter variable
    row_count = 0

    # Iterate over the rows
    for row in reader:
        # Increment the counter
        row_count += 1
        print("Sad smo tu: " + str(row_count))
        scheme_id = row[1]
        level_id = row[2]
        memberId = row[0]
        remove_groups_from_security_scheme(scheme_id, level_id, memberId)

        # Check if it's the second row
        if row_count == 6:
            # Process the second row
            print(row)

            # Break the loop after processing the second row
            break


