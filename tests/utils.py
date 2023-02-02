
number = (int, float, complex)

def schema_checker(schema, data, path=[]):
    if isinstance(schema, dict):
        assert isinstance(data, dict)
        for key, sub_schema in schema.items():
            new_path = [*path, key]
            if "*" == key:
                for field, value in data.items():
                    assert isinstance(field, str), f".{'.'.join(new_path)}.{field} is not a string"
                    schema_checker(sub_schema, value, new_path)
            else:
                assert key in data, f"key .{'.'.join(new_path)} does not exist"
                schema_checker(sub_schema, data[key], new_path)

    elif isinstance(schema, list):
        assert isinstance(data, list), f".{'.'.join(path)} is not a list"

        if len(schema) > 1:
            raise NotImplementedError("Cannot check schema with multiple item types in a list")

        for row in data:
            schema_checker(schema[0], row, path)

    elif "Dict[str, number]" == schema:
        assert isinstance(data, dict), f".{'.'.join(path)} is not a dict"
        assert all(isinstance(key, str) for key in data.keys()), f".{'.'.join(path)} has non-string key"
        assert all(isinstance(val, number) for val in data.values()), f".{'.'.join(path)} has non-number value"

    elif schema is None or isinstance(schema, (number, str)):
        assert data == schema, f".{'.'.join(path)} is not `{schema}`"

    else:
        assert isinstance(data, schema), f".{'.'.join(path)} is not type {schema}"


def check_ab_schema(data):
    schema = {
        "00000000-0000-0000-0000-000000018a89": {
            "is_control": bool,
            "size": number,
            "total": number,
            "avg": number,
            "median": number,
            "ci_50_low": number,
            "ci_50_high": number,
            "ci_95_low": number,
            "ci_95_high": number,
            "improve_avg": None,
            "improve_median": None,
            "improve_ci_95_low": None,
            "improve_ci_95_high": None,
            "improve_ci_50_low": None,
            "improve_ci_50_high": None,
            "win_prob": None,
        },
        "00000000-0000-0000-0000-000000018a8a": {
            "is_control": bool,
            "size": number,
            "total": number,
            "avg": number,
            "median": number,
            "ci_50_low": number,
            "ci_50_high": number,
            "ci_95_low": number,
            "ci_95_high": number,
            "improve_avg": number,
            "improve_median": number,
            "improve_ci_95_low": number,
            "improve_ci_95_high": number,
            "improve_ci_50_low": number,
            "improve_ci_50_high": number,
            "win_prob": number,
        }
    }
    schema_checker(schema, data)


def check_analytic_schema(data):
    search_prod_scheme = [{
        "prod_id": str,
        "value": number,
        "value_diff": number,
        "convert_rate": number,
    }]

    search_schema = [{
        "keyword": str,
        "value": number,
        "rank_diff": int,
        "value_diff": number,
        "conversion_rate": number,
        "products": search_prod_scheme,
    }]

    schema = {
        "timeframe": {
            "start": str,
            "end": str,
            "start_time": int,
            "end_time": int,
            "range": int,
            "interval": str,
        },
        "metrics": {
            "*":{
                "total": [number],
                "miso_assisted": [number],
                "sum": number,
                "previous_sum": number,
            }
        },
        "products": {
            "add_to_cart":   "Dict[str, number]",
            "checkout":      "Dict[str, number]",
            "pv":            "Dict[str, number]",
        },
        "searches": {
            "conversion":      search_schema,
            "conversion_rate": search_schema,
            "search_count":    search_schema,
        },
        "bad_searches": {},
        "short_stats": [{
            "id": str,
            "data": [number],
            "total": number,
            "prev_total": number,
        }],
    }
    schema_checker(schema, data)

    assert data['short_stats'][0]['id'] == 'avg_search_ctr'
    assert data['short_stats'][1]['id'] == 'total_search_volume'
