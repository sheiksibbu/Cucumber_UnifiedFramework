import os
import subprocess

def generate_step_definitions(feature_file):
    # Run behave with the feature file to get undefined steps
    result = subprocess.run(['behave', feature_file], capture_output=True, text=True)
    
    # Output the raw result to debug
    print(result.stdout)

    step_definitions = []
    # Look for step definition snippets in the output
    for line in result.stdout.splitlines():
        if line.strip().startswith("@"):  # Looking for step definition snippets
            step_definitions.append(line.strip())

    if step_definitions:
        return step_definitions
    else:
        print("All steps are defined.")
        return []

def write_step_definitions(step_definitions, steps_file):
    with open(steps_file, 'w') as f:
        f.write("from behave import given, when, then\n\n")
        for snippet in step_definitions:
            f.write(f"{snippet}\n\n")

def main():
    feature_file = '/home/sheiksibgathulla/PycharmProjects/Cucumber_UnifiedFramework/features/steps/Flipkart.feature'
    
    
    # Update the path to save the generated step definitions in the correct location
    steps_file = '/home/sheiksibgathulla/PycharmProjects/Cucumber_UnifiedFramework/features/steps/Flipkart_steps.py'

    # Generate step definitions from the feature file
    step_definitions = generate_step_definitions(feature_file)

    if step_definitions:
        write_step_definitions(step_definitions, steps_file)
        print(f"Step definitions written to {steps_file}")
    else:
        print("No new step definitions were created.")

if __name__ == "__main__":
    main()
