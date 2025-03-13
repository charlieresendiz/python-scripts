import os

def configure_wireguard_split_clients(directory):
    """
    Adds 'XXX.XX.X.X/XX' to AllowedIPs in Wireguard config files with 'split' in their names.

    Args:
        directory: The directory containing the Wireguard configuration files.
    """

    for filename in os.listdir(directory):
        if "split" in filename and filename.endswith(".conf"):
            file_path = os.path.join(directory, filename)
            try:
                with open(file_path, 'r') as file:
                    lines = file.readlines()

                with open(file_path, 'w') as file:
                    allowed_ips_found = False
                    for line in lines:
                        if line.startswith("AllowedIPs = "):
                            allowed_ips_found = True
                            ips = line.split("= ")[1].strip()
                            if "XXX.XX.X.X/XX" not in ips:
                                if ips:
                                    new_ips = ips + ", XXX.XX.X.X/XX"
                                else:
                                    new_ips = "XXX.XX.X.X/XX"
                                file.write(f"AllowedIPs = {new_ips}\n")
                            else:
                                file.write(line)
                        else:
                            file.write(line)
                    if not allowed_ips_found:
                        print(f"Warning: AllowedIPs not found in {file_path}. Adding it to the end of the file.")
                        with open(file_path, 'a') as file:
                            file.write("\nAllowedIPs = XXX.XX.X.X/XX\n")

                print(f"Successfully configured {file_path}")

            except FileNotFoundError:
                print(f"Error: File not found: {file_path}")
            except Exception as e:
                print(f"An error occurred while processing {file_path}: {e}")

# --- Implementation ---
directory = "/path/to/your/files"
configure_wireguard_split_clients(directory)
