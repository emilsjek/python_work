def describe_city(name,country='ireland'):
    """name of city and country"""

    print(f"{name.title()} is in {country.title()}.")

describe_city('Cork')
describe_city('dublin')
describe_city('funchal','madeira')