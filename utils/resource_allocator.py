def resource_status(inflow):

    if inflow > 300:
        return "High Resource Demand"

    elif inflow > 150:
        return "Medium Resource Demand"

    else:
        return "Low Resource Demand"