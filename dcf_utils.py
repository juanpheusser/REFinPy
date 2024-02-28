import pandas as pd
import numpy as np
from typing import Union

def create_dataframe(row_names: list[str], initial_year: int, num_years: int) -> pd.DataFrame:
  """
  Creates a pandas DataFrame with the given row names and columns representing consecutive years.

  Args:
      row_names: A list of strings representing the names of the rows.
      initial_year: An integer representing the starting year for the columns.
      num_years: An integer representing the number of years to include in the columns.

  Returns:
      A pandas DataFrame with the specified row and column names.
  """

  # Create the list of column names
  column_names = [str(year) for year in range(initial_year, initial_year + num_years)]

  # Create the DataFrame
  dcf = pd.DataFrame(columns=column_names, index=row_names)

  return dcf


def insert_data_into_row(dcf: pd.DataFrame, row_name: str, data: Union[list[float], pd.Series]) -> None:
  """
  Inserts a list of data into the specified row of a pandas DataFrame.

  Args:
      dcf: The pandas DataFrame containing the Discounted Cashflow Model.
      row_name: The name of the row to insert the data into.
      data: A list of data to insert.

  Returns:
      None. The data is inserted directly into the DataFrame.
  """

  # Check if the length of the data matches the number of columns
  if len(data) != len(dcf.columns):
    raise ValueError("The length of the data must match the number of columns in the DataFrame.")

  # Insert the data into the specified row
  dcf.loc[row_name] = data

def calculate_vacancy(dcf: pd.DataFrame, rates: pd.DataFrame) -> None:
  """
  Calculates vacancy by multiplying the Gross Revenue by the Vacancy Rate and inserts the result into the Vacancy row.

  Args:
      dcf: The pandas DataFrame containing the Discounted Cashflow Model.

  Returns:
      None. The vacancy values are inserted directly into the DataFrame.
  """

  # Get the Gross Revenue and Vacancy Rate rows
  gross_revenue = dcf.loc["Gross Revenue"]
  vacancy_rate = rates.loc["Vacancy Rate"]

  # Multiply the two rows to get vacancy
  vacancy = gross_revenue * vacancy_rate

  # Insert the vacancy values into the Vacancy row
  insert_data_into_row(dcf, "Vacancy", vacancy)


def calculate_effective_gross_income(dcf: pd.DataFrame) -> None:
  """
  Calculates the effective gross income by subtracting Vacancy from Gross Revenue and inserts the result into the Effective Gross Income row.

  Args:
      dcf: The pandas DataFrame containing the Discounted Cashflow Model.

  Returns:
      None. The effective gross income values are inserted directly into the DataFrame.
  """

  # Get the Gross Revenue and Vacancy rows
  gross_revenue = dcf.loc["Gross Revenue"]
  vacancy = dcf.loc["Vacancy"]

  # Calculate the effective gross income
  effective_gross_income = gross_revenue - vacancy

  # Insert the effective gross income values into the Effective Gross Income row
  insert_data_into_row(dcf, "Effective Gross Income", effective_gross_income)

def calculate_total_expenses(dcf: pd.DataFrame) -> None:
  """
  Calculates the total expenses by adding General Operating Expenses, Real Estate Taxes, Insurance, Property Management Fees and Structural Reserve and inserts the result into the Total Expense row.

  Args:
      dcf: The pandas DataFrame containing the Discounted Cashflow Model.

  Returns:
      None. The total expenses values are inserted directly into the DataFrame.
  """

  # Get the necessary rows
  general_operating_expenses = dcf.loc["General Operating Expenses"]
  real_estate_taxes = dcf.loc["Real Estate Taxes"]
  insurance = dcf.loc["Insurance"]
  property_management_fee = dcf.loc["Property Management Fee"]
  structural_reserve = dcf.loc["Structural Reserve"]

  # Calculate the total expenses
  total_expenses = general_operating_expenses + real_estate_taxes + insurance + property_management_fee + structural_reserve

  # Insert the total expenses values into the Total Expense row
  insert_data_into_row(dcf, "Total Expenses", total_expenses)

def calculate_net_operating_income(dcf: pd.DataFrame) -> None:
  """
  Calculates the net operating income by subtracting Total Expenses from Effective Gross Income and inserts the result into the Net Operating Income row.

  Args:
      dcf: The pandas DataFrame containing the Discounted Cashflow Model.

  Returns:
      None. The net operating income values are inserted directly into the DataFrame.
  """

  # Get the Effective Gross Income and Total Expenses rows
  effective_gross_income = dcf.loc["Effective Gross Income"]
  total_expenses = dcf.loc["Total Expenses"]

  # Calculate the net operating income
  net_operating_income = effective_gross_income - total_expenses

  # Insert the net operating income values into the Net Operating Income row
  insert_data_into_row(dcf, "Net Operating Income", net_operating_income)


def calculate_cash_flow_before_financing(dcf: pd.DataFrame) -> None:
  """
  Calculates the cash flow before financing by subtracting Tenant Improvements and Lease Commissions from Net Operating Income and inserts the result into the Cash Flow Before Financing row.

  Args:
      dcf: The pandas DataFrame containing the Discounted Cashflow Model.

  Returns:
      None. The cash flow before financing values are inserted directly into the DataFrame.
  """

  # Get the Net Operating Income, Tenant Improvements, and Lease Commissions rows
  net_operating_income = dcf.loc["Net Operating Income"]
  tenant_improvements = dcf.loc["Tenant Improvements"]
  lease_commissions = dcf.loc["Lease Commissions"]

  # Calculate the cash flow before financing
  cash_flow_before_financing = net_operating_income - tenant_improvements - lease_commissions

  # Insert the cash flow before financing values into the Cash Flow Before Financing row
  insert_data_into_row(dcf, "Cash Flow Before Financing", cash_flow_before_financing)

def calculate_cash_flow_after_financing(dcf: pd.DataFrame) -> None:
  """
  Calculates the cash flow after financing by subtracting Debt Service from Cash Flow Before Financing and inserts the result into the Cash Flow After Financing row.

  Args:
      dcf: The pandas DataFrame containing the Discounted Cashflow Model.

  Returns:
      None. The cash flow after financing values are inserted directly into the DataFrame.
  """

  # Get the Cash Flow Before Financing and Debt Service rows
  cash_flow_before_financing = dcf.loc["Cash Flow Before Financing"]
  debt_service = dcf.loc["Debt Service"]

  # Calculate the cash flow after financing
  cash_flow_after_financing = cash_flow_before_financing - debt_service

  # Insert the cash flow after financing values into the Cash Flow After Financing row
  insert_data_into_row(dcf, "Cash Flow After Financing", cash_flow_after_financing)


def insert_data_by_year(dcf: pd.DataFrame, data: dict) -> None:
  """
  Inserts data into the DataFrame based on the provided dictionary.

  Args:
      dcf: The pandas DataFrame containing the Discounted Cashflow Model.
      data: A dictionary with key-value pairs, where each key corresponds to a row in the DataFrame and the value is the data to insert for that row.

  Returns:
      None. The data is inserted directly into the DataFrame.
  """

  # Get the year from the data dictionary
  year = data['year']

  # Iterate over each key-value pair in the data dictionary
  for key, value in data.items():
    # Skip the 'year' key
    if key != 'year':
      # Insert the data into the DataFrame
      dcf.loc[key, year] = value

def replicate_first_column(dcf: pd.DataFrame) -> pd.DataFrame:
  """
  Replicates the first column of the DataFrame into every other column.

  Args:
      dcf: The pandas DataFrame containing the Discounted Cashflow Model.

  Returns:
      A new DataFrame with the first column replicated into every other column.
  """

  # Get the first column
  first_column = dcf.iloc[:, 0]

  # Create a new DataFrame with the first column replicated into every other column
  new_df = pd.DataFrame(np.tile(first_column.values, (len(dcf.columns), 1)).T, columns=dcf.columns, index=dcf.index)

  return new_df

def insert_data_from_dict_list(dcf: pd.DataFrame, data_list: list[dict]) -> None:
  """
  Inserts data into the DataFrame from a list of dictionaries.

  Args:
      dcf: The pandas DataFrame containing the Discounted Cashflow Model.
      data_list: A list of dictionaries, each containing data to be inserted into the DataFrame.

  Returns:
      None. The data is inserted directly into the DataFrame.
  """

  # Iterate over each dictionary in the list
  for data in data_list:
    # Call the insert_data_by_year function to insert the data
    insert_data_by_year(dcf, data)