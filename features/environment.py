# from selenium import webdriver
#
# def before_scenario(context, driver):
#     """Launches the Flipkart URL before each scenario."""
#     context.driver = webdriver.Chrome()
#     context.driver.maximize_window()
#     context.driver.get("https://www.saucedemo.com/v1/")
#
# def after_scenario(context, driver):
#     """Quits the Chrome browser after each scenario."""
#     if context.driver:
#         context.driver.quit()



# import openpyxl
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
#
#
# def before_scenario(context, scenario):
#     """Launches the Flipkart URL with detailed Chrome options before each scenario."""
#
#     # Setup Chrome options
#     chrome_options = Options()
#
#     # Block notifications and pop-ups
#     prefs = {
#         "profile.default_content_setting_values.notifications": 2,
#         "profile.default_content_setting_values.popups": 2,
#         "credentials_enable_service": False,
#         "profile.password_manager_enabled": False
#     }
#     chrome_options.add_experimental_option("prefs", prefs)
#
#     # Additional Chrome configurations
#     chrome_options.add_argument("--start-maximized")
#     chrome_options.add_argument("--disable-popup-blocking")
#     chrome_options.add_argument("--incognito")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     chrome_options.add_argument("--remote-allow-origins=*")
#
#     # Initialize the Chrome driver with options
#     # service = Service(executable_path='/path_to_chromedriver')
#     # context.driver = webdriver.Chrome(service=service, options=chrome_options)
#
#     context.driver = webdriver.Chrome(options=chrome_options)
#
#     # Load the website
#     url = "https://www.saucedemo.com/v1/"
#     context.driver.get(url)
#     print(f"Scenario '{scenario.name}' started, opened {url}.")
#
#
# def after_scenario(context, scenario):
#     """Quits the Chrome browser after each scenario."""
#     if context.driver:
#         context.driver.quit()
#         print(f"Scenario '{scenario.name}' ended, browser closed.")




#########   New Feature File with Auto Triage Mechanism


# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# # Global result list to track test results
# test_results = []
#
#
# def before_scenario(context, scenario):
#     """Launches the Flipkart URL with detailed Chrome options before each scenario."""
#     chrome_options = Options()
#     chrome_options.add_argument("--start-maximized")
#     chrome_options.add_argument("--disable-notifications")
#     chrome_options.add_argument("--incognito")
#     chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
#
#     context.driver = webdriver.Chrome(options=chrome_options)
#     context.test_name = scenario.name
#     context.module_name = "Sample Module"
#
#
# def after_scenario(context, scenario):
#     """Captures test status and reason for failure after each scenario."""
#     test_status = "Pass" if scenario.status == "passed" else "Fail"
#     reason = scenario.exception if scenario.exception else "N/A"
#
#     # Append test result to global list
#     test_results.append({
#         "Test Case Name": context.test_name,
#         "Module": context.module_name,
#         "Status": test_status,
#         "Reason of Failure": str(reason)
#     })
#
#     if context.driver:
#         context.driver.quit()
#
#
# def after_all(context):
#     """Write test results to an Excel file after all scenarios."""
#     df = pd.DataFrame(test_results)
#     output_file = "test_results.xlsx"
#     df.to_excel(output_file, index=False, engine='openpyxl')
#     print(f"Test results saved to '{output_file}'.")





########  new file for csv test results  --- This code is Working


# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# # Global result list to track test results
# test_results = []
#
#
# def before_scenario(context, scenario):
#     """Launches the Flipkart URL with detailed Chrome options before each scenario."""
#     chrome_options = Options()
#     chrome_options.add_argument("--start-maximized")
#     chrome_options.add_argument("--disable-notifications")
#     chrome_options.add_argument("--incognito")
#     chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
#
#     context.driver = webdriver.Chrome(options=chrome_options)
#     # context.driver = webdriver.Chrome()
#
#     context.test_name = scenario.name
#     context.module_name = "Login Module"
#
#
#     ############  ------------------------------------->>>>>>>>>>>>>
#
#     context.driver = webdriver.Chrome()
#     context.driver.maximize_window()
#     context.driver.get("https://www.saucedemo.com/v1/")
#
#     ###########  -------------------------------------->>>>>>>>>>>>>
#
#
# def after_scenario(context, scenario):
#     """Captures test status and reason for failure after each scenario."""
#     test_status = "Pass" if scenario.status == "passed" else "Fail"
#     reason = scenario.exception if scenario.exception else "N/A"
#
#     # Append test result to global list
#     test_results.append({
#         "Test Case Name": context.test_name,
#         "Module": context.module_name,
#         "Status": test_status,
#         "Reason of Failure": str(reason)
#     })
#
#     if context.driver:
#         context.driver.quit()
#
#
# def after_all(context):
#     """Write test results to a CSV file after all scenarios."""
#     df = pd.DataFrame(test_results)
#     output_file = "/home/sheiksibgathulla/PycharmProjects/Cucumber_UnifiedFramework/AutomationResults_Triage.csv"
#     df.to_csv(output_file, index=False)
#     print(f"Test results saved to '{output_file}'.")












##################3   this is the new code which iam trying now


# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# # Global result list to track test results
# test_results = []
#
#
# def before_scenario(context, scenario):
#     """Launches the Flipkart URL with detailed Chrome options before each scenario."""
#     chrome_options = Options()
#     chrome_options.add_argument("--start-maximized")
#     chrome_options.add_argument("--disable-notifications")
#     # chrome_options.add_argument("--incognito")
#     chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
#     # chrome_options.add_argument("--headless")
#     chrome_options.add_experimental_option("useAutomationExtension", True)
#     # chrome_options.add_argument("--window-size=768x1024")
#     context.driver = webdriver.Chrome(options=chrome_options)
#
#     context.test_name = scenario.name
#     context.module_name = "Login Module"
#
#     context.driver.maximize_window()
#     context.driver.get("https://www.saucedemo.com/v1/")
#
#
# def after_scenario(context, scenario):
#     """Captures test status and reason for failure after each scenario."""
#     test_status = "Pass" if scenario.status == "passed" else "Fail"
#
#     # Check if there's a failure reason set from the step
#     reason = context.failure_reason if hasattr(context, "failure_reason") else "N/A"
#
#     # Append test result to global list
#     test_results.append({
#         "Test Case Name": context.test_name,
#         "Module": context.module_name,
#         "Status": test_status,
#         "Reason of Failure": str(reason)
#     })
#
#     # Clear failure reason after scenario
#     if hasattr(context, "failure_reason"):
#         del context.failure_reason
#
#     if context.driver:
#         context.driver.quit()
#
#
# def after_all(context):
#     """Write test results to a CSV file after all scenarios."""
#     df = pd.DataFrame(test_results)
#     output_file = "/home/sheiksibgathulla/PycharmProjects/Cucumber_UnifiedFramework/AutomationResults_Triage.csv"
#     df.to_csv(output_file, index=False)
#     print(f"Test results saved to '{output_file}'.")









# import pandas as pd
#
#
# def after_all(context):
#     """Write test results to an Excel file after all scenarios with styling."""
#     df = pd.DataFrame(test_results)
#
#     # Specify the output Excel file path
#     output_file = "/home/sheiksibgathulla/PycharmProjects/Cucumber_UnifiedFramework/AutomationResults_Triage.xlsx"
#
#     # Create a Pandas Excel writer using openpyxl
#     with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
#         # Write the DataFrame to the Excel file
#         df.to_excel(writer, index=False, sheet_name="Test Results")
#
#         # Get the workbook and the sheet
#         workbook = writer.book
#         sheet = writer.sheets["Test Results"]
#
#         # Apply style to the header
#         header = sheet[1]  # First row is the header
#         for cell in header:
#             cell.fill = openpyxl.styles.PatternFill(start_color="0000FF", end_color="0000FF",
#                                                     fill_type="solid")  # Blue background
#             cell.font = openpyxl.styles.Font(color="FFFFFF")  # White text
#
#
#         # Optionally, you can adjust column width to fit the content
#         for col in sheet.columns:
#             max_length = 0
#             column = col[0].column_letter  # Get column name
#             for cell in col:
#                 try:
#                     if len(str(cell.value)) > max_length:
#                         max_length = len(cell.value)
#                 except:
#                     pass
#             adjusted_width = (max_length + 2)
#             sheet.column_dimensions[column].width = adjusted_width
#
#     print(f"Test results saved to '{output_file}'.")





# import pandas as pd
# import openpyxl
# from openpyxl.styles import PatternFill, Font
#
#
# def after_all(context):
#     """Write test results to an Excel file after all scenarios with styling."""
#     df = pd.DataFrame(test_results)
#
#     # Specify the output Excel file path
#     output_file = "/home/sheiksibgathulla/PycharmProjects/Cucumber_UnifiedFramework/AutomationResults_Triage.xlsx"
#
#     # Create a Pandas Excel writer using openpyxl
#     with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
#         # Write the DataFrame to the Excel file
#         df.to_excel(writer, index=False, sheet_name="Test Results")
#
#         # Get the workbook and the sheet
#         workbook = writer.book
#         sheet = writer.sheets["Test Results"]
#
#         # Apply style to the header (First row)
#         header = sheet[1]  # First row is the header
#         for cell in header:
#             # Apply blue background and white text color
#             cell.fill = PatternFill(start_color="0000FF", end_color="0000FF", fill_type="solid")
#             cell.font = Font(color="FFFFFF", bold=True)  # White text and bold font
#
#         # Optionally, you can adjust column width to fit the content
#         for col in sheet.columns:
#             max_length = 0
#             column = col[0].column_letter  # Get column name
#             for cell in col:
#                 try:
#                     if len(str(cell.value)) > max_length:
#                         max_length = len(cell.value)
#                 except:
#                     pass
#             adjusted_width = (max_length + 2)
#             sheet.column_dimensions[column].width = adjusted_width
#
#     print(f"Test results saved to '{output_file}'.")


# def after_all(context):
#     """Write test results to a CSV file after all scenarios."""
#     df = pd.DataFrame(test_results)
#
#     # Calculate the total number of tests
#     total_tests = len(df)
#
#     # Calculate the number of passed and failed tests
#     passed_tests = len(df[df["Status"] == "Pass"])
#     failed_tests = len(df[df["Status"] == "Fail"])
#
#     # Calculate pass and fail percentages
#     pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
#     fail_percentage = (failed_tests / total_tests) * 100 if total_tests > 0 else 0
#
#     # Add the percentages to the DataFrame (as a new row)
#     summary = {
#         "Test Case Name": "Summary",
#         "Module": "Login Module",
#         "Status": f"Pass: {pass_percentage:.2f}% | Fail: {fail_percentage:.2f}%",
#         "Reason of Failure": "N/A"
#     }
#     df = df.append(summary, ignore_index=True)
#
#     # Write the DataFrame with the summary to CSV
#     output_file = "/home/sheiksibgathulla/PycharmProjects/Cucumber_UnifiedFramework/AutomationResults_Triage.csv"
#     df.to_csv(output_file, index=False)
#
#     print(f"Test results saved to '{output_file}'.")









###################--------------- >>>>>>>>>>    This is Working












# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import psutil
# import time

# # Global result list to track test results
# test_results = []

# # Global variable to track system resource usage
# resource_usage = []


# def log_resource_usage():
#     """Log CPU and Memory usage during each scenario."""
#     cpu_usage = psutil.cpu_percent(interval=1)
#     memory_usage = psutil.virtual_memory().used / (1024 * 1024)
#     resource_usage.append({"CPU %": cpu_usage, "Memory MB": memory_usage})


# def before_scenario(context, scenario):
#     """Launch the Flipkart URL with Chrome options and start resource monitoring."""
#     chrome_options = Options()
#     chrome_options.add_argument("--start-maximized")
#     chrome_options.add_argument("--disable-notifications")
#     chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
#     context.driver = webdriver.Chrome(options=chrome_options)

#     context.test_name = scenario.name
#     context.module_name = "Login Module"

#     context.driver.maximize_window()
#     context.driver.get("https://www.saucedemo.com/v1/")

#     # Log initial resource usage
#     log_resource_usage()


# def after_scenario(context, scenario):
#     """Capture test status and log resource usage after each scenario."""
#     test_status = "Pass" if scenario.status == "passed" else "Fail"
#     reason = getattr(context, "failure_reason", "N/A")

#     # Append test result
#     test_results.append({
#         "Test Case Name": context.test_name,
#         "Module": context.module_name,
#         "Status": test_status,
#         "Reason of Failure": str(reason)
#     })

#     # Log final resource usage
#     log_resource_usage()

#     # Quit driver after scenario
#     if context.driver:
#         context.driver.quit()


# def after_all(context):
#     """Write test results and resource usage to CSV files."""
#     # Write test results to CSV
#     results_file = "/home/sheiksibgathulla/PycharmProjects/Cucumber_UnifiedFramework/AutomationResults_Triage.csv"
#     pd.DataFrame(test_results).to_csv(results_file, index=False)
#     print(f"Test results saved to '{results_file}'.")

#     # Write resource usage logs to CSV
#     usage_file = "/home/sheiksibgathulla/PycharmProjects/Cucumber_UnifiedFramework/ResourceUsageLogs.csv"
#     pd.DataFrame(resource_usage).to_csv(usage_file, index=False)
#     print(f"Resource usage logs saved to '{usage_file}'.")











#############    This is Working as expected code




import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import psutil
import time
import tempfile
import os
import shutil

# Global result list to track test results
test_results = []

# Global variable to track system resource usage
resource_usage = []

def log_resource_usage():
    """Log CPU and Memory usage during each scenario."""
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().used / (1024 * 1024)
    resource_usage.append({"CPU %": cpu_usage, "Memory MB": memory_usage})

def before_scenario(context, scenario):
    """Launch the Flipkart URL with Chrome options and start resource monitoring."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    
    # Create a unique temporary directory for the user data
    context.user_data_dir = os.path.join(tempfile.gettempdir(), f"chrome_user_data_{os.getpid()}")
    chrome_options.add_argument(f"--user-data-dir={context.user_data_dir}")
    
    context.driver = webdriver.Chrome(options=chrome_options)
    context.test_name = scenario.name
    context.module_name = "Login Module"

    context.driver.maximize_window()
    context.driver.get("https://www.saucedemo.com/v1/")

    # Log initial resource usage
    log_resource_usage()

def after_scenario(context, scenario):
    """Capture test status and log resource usage after each scenario."""
    test_status = "Pass" if scenario.status == "passed" else "Fail"
    reason = getattr(context, "failure_reason", "N/A")

    # Append test result
    test_results.append({
        "Test Case Name": context.test_name,
        "Module": context.module_name,
        "Status": test_status,
        "Reason of Failure": str(reason)
    })

    # Log final resource usage
    log_resource_usage()

    # Quit driver after scenario
    if context.driver:
        context.driver.quit()
    
    # Clean up the user data directory
    if context.user_data_dir and os.path.exists(context.user_data_dir):
        shutil.rmtree(context.user_data_dir)

def after_all(context):
    """Write test results and resource usage to CSV files."""
    # Write test results to CSV
    results_file = "/home/sheiksibgathulla/PycharmProjects/Cucumber_UnifiedFramework/AutomationResults_Triage.csv"
    pd.DataFrame(test_results).to_csv(results_file, index=False)
    print(f"Test results saved to '{results_file}'.")

    # Write resource usage logs to CSV
    usage_file = "/home/sheiksibgathulla/PycharmProjects/Cucumber_UnifiedFramework/ResourceUsageLogs.csv"
    pd.DataFrame(resource_usage).to_csv(usage_file, index=False)
    print(f"Resource usage logs saved to '{usage_file}'.")




