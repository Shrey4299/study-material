import logging
import datetime
import os

# Determine the path of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Set up logging
log_file_path = os.path.join(script_dir, "crontab_log.log")
logging.basicConfig(filename=log_file_path, level=logging.INFO)


def main():
    # Your code here
    logging.info(f"Script ran at {datetime.datetime.now()}")


if __name__ == "__main__":
    main()
