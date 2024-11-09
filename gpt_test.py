import openai
import os

def test_gpt_api():
    # Set your API key
    openai.api_key = "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"

    # Read background information and request content from a txt file
    with open("background.txt", "r", encoding="utf-8") as background_file:
        background_info = background_file.read().strip()

    with open("request.txt", "r", encoding="utf-8") as request_file:
        user_message = request_file.read().strip()

    # Build a request with background information
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": background_info},
            {"role": "user", "content": user_message}
        ]
    )

    # Print the content returned by the API
    print(response.choices[0].message["content"])

    # Save the generated code into a py file
    generated_code = response.choices[0].message["content"]
    with open("B.py", "w", encoding="utf-8") as code_file:
        code_file.write(generated_code)

# Set file names
a_filename = 'A.py'
b_filename = 'B.py'
c_filename = 'C.py'
d_filename = 'D.py'
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


# Run D.py
if os.system(f"python {d_filename}") != 0:
    print(f"Error occurred while running {d_filename}")

