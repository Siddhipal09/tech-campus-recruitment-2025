import sys
import os

def is_valid_date(date):
    """Validate the date format (YYYY-MM-DD)."""
    return len(date) == 10 and date[4] == '-' and date[7] == '-' and date.isdigit()

def extract_logs_by_date(log_file_path, date, output_file_path):
    """Extract logs for the specific date and write them to an output file."""
    try:
        with open(log_file_path, 'r') as log_file, open(output_file_path, 'w') as output_file:
            line_count = 0
            matched_line_count = 0

           
            for line in log_file:
                line_count += 1
               
                if line.startswith(date):
                    output_file.write(line)
                    matched_line_count += 1

           
            print(f"Total lines processed: {line_count}")
            print(f"Total lines written: {matched_line_count}")

    except Exception as e:
        print(f"Error processing the log file: {e}")

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py <YYYY-MM-DD>")
        sys.exit(1)

    input_date = sys.argv[1]

   
    if not is_valid_date(input_date):
        print("Invalid date format. Please use YYYY-MM-DD.")
        sys.exit(1)

   
   
    log_file_path = 'src/logs_2024.log'  
    output_file_path = f'../output/output_{input_date}.txt'

   
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

   
    extract_logs_by_date(log_file_path, input_date, output_file_path)

if __name__ == "__main__":
    main()