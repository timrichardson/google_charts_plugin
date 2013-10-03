

def plugin_google_chart():
    """used with the .load view to create a google chart
    Because this is used in a view LOAD, parameters are passed back from the browser as vars in the URL
    The complulsory vars include: 'type', a string defining the chart_type
        'data_url', which is a URL of the function which returns the data to be charted

    The use in the view is like this (including an example data URL

    {{ data_url = URL('plugin_google_chart','plugin_return_data.json',user_signature=True)}}
    ...
    {{=LOAD('plugin_google_chart','plugin_google_chart.load',ajax=True,
        user_signature=True,vars={'type':'bar','data_url':data_url})}}
    """
    chart_type = request.vars.type
    data_url = request.vars.data_url
    options_dict = request.vars.options_dict or ''
    if chart_type and data_url:
        return dict(chart_type=chart_type,data_url=data_url,
                    options_dict=options_dict)
    else:
        return dict()


def plugin_return_data():
    """ This is an example function to return a JSON-encoded array to the Google chart plugin.
    The URL should have a .json suffix
    This can also use the @auth.requires_signature() decorator
    """
    data = [['Year','Sales','Expenses'],["2004",1000,400],["2005",1100,440],["2006",1200,600],
            ["2007",1500,800],["2008",1600,850],["2009",1800,900]]
    return dict(data=data)


def plugin_usage_example():
    return dict()
