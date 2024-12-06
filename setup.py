import json
import re 
import copy
import os
import argparse
import datetime

def read_notebook(file_name:str) -> dict[str, any]:
    with open(file_name, 'r') as file:
        return json.load(file)

def write_notebook(file_name:str, notebook:dict[str, any]):
    with open(file_name, 'w') as file:
        json.dump(notebook, file)

def create_example_file(dir):
    with open(os.path.join(dir, 'example.txt'), 'w') as file:
        file.write('You should copy and paste the example provided for the problem here to test with!')

def create_dir(path):
    os.makedirs(path, exist_ok=True)

def update_notebook(notebook: dict[str, any], updates: dict[str, str]) -> dict[str, any]:
    # Clone the notebook to avoid modifying the original
    updated_notebook = copy.deepcopy(notebook)
    
    # Compile regex patterns for code cells
    code_patterns = {var: re.compile(rf"^\s*{var}\s*=\s*.*$", re.MULTILINE) for var in updates}
    
    # Compile regex patterns for Markdown placeholders for each variable
    markdown_patterns = {var: re.compile( r'\{var\}'.replace('var', var)) for var in updates}

    # Iterate over all cells in the cloned notebook
    for cell in updated_notebook.get('cells', []):
        if cell.get('cell_type') == 'code':
            # Process code lines in the cell
            updated_lines = []
            for line in cell.get('source', []):
                for var, value in updates.items():
                    if code_patterns[var].match(line):
                        line = f"{var} = {value}\n"
                updated_lines.append(line)
            cell['source'] = updated_lines

        elif cell.get('cell_type') == 'markdown':
            # Process Markdown cells for placeholders
            updated_lines = []
            for line in cell.get('source', []):
                for var, pattern in markdown_patterns.items():
                    line = pattern.sub(updates[var], line)
                updated_lines.append(line)
            
            cell['source'] = updated_lines

    return updated_notebook


def main():
    parser = argparse.ArgumentParser(description="Kickstart your Advent of Code with Skeleton code tailored to a particular day")

    today = datetime.datetime.now()
    parser.add_argument('--day', type=int,  default=today.day)
    parser.add_argument('--year', type=int, default=today.year)
    parser.add_argument('--template_path', default='./template.ipynb')
    parser.add_argument('--output_filename', default='solution.ipynb')
    parser.add_argument('--output_dir', default='Events')
    parser.add_argument('--create_all', action='store_true', help="Create all days from 0 to 25")

    args = parser.parse_args()

    if args.create_all:
        if input('Are you sure you want to create a template for each day?\n Y or N \n').lower() not in ('yes', 'y'):
            return 
        
        days_to_create = range(1, 26)  # Days 1 to 25
    else:
        days_to_create = [args.day]

    for day in days_to_create:
        updates = {'day': str(day), 'year': str(args.year)}

        # Make updates to template
        notebook = read_notebook(args.template_path)
        updated_notebook = update_notebook(notebook, updates)

        # Create new dir for this day 
        output_dir = f'{args.output_dir}/{args.year}/Day{day:02}'
        output_filename = args.output_filename if args.output_filename is not None else f"solution.ipynb"
        output_path = os.path.join(os.getcwd(), output_dir, output_filename)

        create_dir(output_dir)
        create_example_file(output_dir)

        write_notebook(output_path, updated_notebook)

        print(f'Created a solution template for day {day} at {output_dir}')


if __name__ == "__main__":
    main()
