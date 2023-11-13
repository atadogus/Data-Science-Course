import pandas


def sort_csv(csv_file, column_name):
    dataFrame = pandas.read_csv(csv_file)
    dataFrame.sort_values(column_name, axis=0, ascending=True, inplace=True, na_position="first")
    dataFrame.to_csv(csv_file)


def remove_zero_values(csv_file, column_name, column_var_to_change):
    dataFrame = pandas.read_csv(csv_file)
    dataFrame.drop(dataFrame[dataFrame[column_name] == column_var_to_change].index, inplace=True)
    dataFrame.to_csv(csv_file)


def remove_comas_and_signs(csv_file, column):
    dataFrame = pandas.read_csv(csv_file)
    dataFrame[column] = dataFrame[column].str.replace(",", "")
    dataFrame[column] = dataFrame[column].str.replace("$", "")
    dataFrame.to_csv(csv_file)

