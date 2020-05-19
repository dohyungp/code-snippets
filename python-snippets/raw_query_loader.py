import os


def read_query(query_name):
    """Read raw sql from sub directory called queries
    """
    working_dir = os.path.dirname(os.path.abspath(__file__))
    queries_dir = os.path.join(working_dir, 'queries')
    query_fn = os.path.join(queries_dir, query_name)
    with open(query_fn, 'r') as f:
        sql = f.read()

    return sql
