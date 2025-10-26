from openai import OpenAI
import os
from dotenv import load_dotenv
from utils.database_utils import fetch_merged_text
from utils.database_utils import fetch_ICL

# Load environment variables
load_dotenv()

def test_gpt_api():
    # Initialize OpenAI client with API key from environment variable
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")
    
    client = OpenAI(api_key=api_key)

    # Get database paths from environment variables
    db_path_ICL = os.getenv("ICL_DB_PATH", "data/ICL.db")
    db_path_request = os.getenv("REQUEST_DB_PATH", "data/request.db")
    
    # Test Example Number from environment variables
    ICL_num = int(os.getenv("ICL_NUM", "1"))
    test_num = int(os.getenv("TEST_NUM", "1"))

    user_message = fetch_merged_text(db_path_request, test_num, 1)

    # Get model from environment variable
    model = os.getenv("OPENAI_MODEL", "gpt-4o-2024-11-20")
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": user_message}
        ]
    )


    # Print the content returned by the API
    print(response.choices[0].message.content)

    # Save the generated code into a py file
    generated_code = response.choices[0].message.content
    with open("config/param_config.py", "w", encoding="utf-8") as code_file:
        code_file.write(generated_code)

    # Read background information and request content from a db file
    background_info = fetch_ICL(db_path_ICL, ICL_num)
    user_message = fetch_merged_text(db_path_request, test_num, 2)

    # Build a request with background information
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": background_info},
            {"role": "user", "content": user_message}
        ]
    )

    # Print the content returned by the API
    print(response.choices[0].message.content)

    # Save the generated code into a py file
    generated_code = response.choices[0].message.content
    with open("src/structural_analysis.py", "w", encoding="utf-8") as code_file:
        code_file.write(generated_code)


    user_message = fetch_merged_text(db_path_request, test_num, 3)

    # Build a request with background information
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": user_message}
        ]
    )

    # Print the content returned by the API
    print(response.choices[0].message.content)

    # Save the generated code into a py file
    generated_code = response.choices[0].message.content
    with open("src/post_proc.py", "w", encoding="utf-8") as code_file:
        code_file.write(generated_code)

# Set file names
a_filename = 'config/param_config.py'
b_filename = 'src/structural_analysis.py'
c_filename = 'src/post_proc.py'
d_filename = 'src/full_program.py'
def merge_files(a_file, b_file, c_file, d_file):
    try:
        # Open A, B, C files, and read their content
        with open(a_file, 'r') as file_a:
            content_a = file_a.read()
        with open(b_file, 'r') as file_b:
            content_b = file_b.read()
        with open(c_file, 'r') as file_c:
            content_c = file_c.read()

        # Open D file and write content
        with open(d_file, 'w') as file_d:
            file_d.write(content_a)  # Write content of file A
            file_d.write('\n')
            file_d.write(content_b)  # Write content of file B
            file_d.write('\n')
            file_d.write(content_c)  # Write content of file C

        print(f"Successfully merged {a_file}, {b_file}, {c_file} into {d_file}")
    except Exception as e:
        print(f"Error occurred during merging: {e}")

if __name__ == "__main__":
    test_gpt_api()
    merge_files(a_filename, b_filename, c_filename, d_filename)


# Run full_program.py
if os.system(f"python {d_filename}") != 0:
    print(f"Error occurred while running {d_filename}")

