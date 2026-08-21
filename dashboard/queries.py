"""
This function is used to store the time filter queries and to run them based
on the users choice
"""
def get_query(time_filter):

    if time_filter == "Last 24 Hours":
        return """
        Select * from raw
        where from_iso8601_timestamp(timestamp) >= current_timestamp - interval '1' day
        order by timestamp desc"""
    
    elif time_filter == "Last 7 Days":
        return """
        Select * from raw
        where from_iso8601_timestamp(timestamp) >= current_timestamp - interval '7' day
        order by timestamp desc
        """
    
    elif time_filter == "Last 30 Days":
        return """
        Select * from raw
        where from_iso8601_timestamp(timestamp) >= current_timestamp - interval '30' day
        order by timestamp desc
        """
    
    elif time_filter == "All Data":
        return """
        Select * from raw
        order by timestamp desc
        """

