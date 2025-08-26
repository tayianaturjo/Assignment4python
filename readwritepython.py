# file_assignment.py

def main():
    # Ask the user for a filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Try reading the file
        with open(filename, "r", encoding="utf-8") as infile:
            content = infile.read()

        # Modify content (example: convert to uppercase)
        modified_content = content.upper()

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w", encoding="utf-8") as outfile:
            outfile.write(modified_content)

        print(f"✅ Success! Modified file saved as '{new_filename}'")

    # Handle errors gracefully
    except FileNotFoundError:
        print(f"⚠️ Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"⚠️ Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
