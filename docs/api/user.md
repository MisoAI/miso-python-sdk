# `ApiClient.user`

Miso’s User APIs let you upload, read, and delete User records that tell Miso about your site’s unique users and visitors.

----------------------------------------------------------------------

## `ApiClient.user.upload()`

Import multiple user records.

### Example

```python
from miso.sdk import ApiClient

api_client = ApiClient(api_key="{api_key}")

users = [
  # First user
  {
    "user_id": "0000001",
    "name": "Neil Armstrong",
    "description": "The first man on the moon! I am the first!" ,
    "profile_image": "https://example.com/path/to/image.jpg",
    "age": 92,
    "gender": "M",
  },
  # Second user
  {
    "user_id": "denvercoder9",
    "name": "Denver Coder",
    "description": "A programer who needs some help and coffee." ,
    "profile_image": "https://example.com/path/to/image.jpg",
    "age": 19,
    "custom_attributes": {
        "acquisition_channel": "Facebook Campaign 2022",
        "declared_interests": ["Drama", "Romance"],
    },
    "gender": "F",
  },
]

response = api_client.user.upload(data=users)
```

### Parameters

| Name           | Type       | Description |
| -------------- | ---------- | ----------- |
| `data`         | list[dict] | List of user data. |


`data` is a list of dictionaries, each dictionary represents a product or content record.

Often used fields are:

| Name           | Type       | Description |
| -------------- | ---------- | ----------- |
| `user_id`      | str        | Required. Unique ID of the user. |
| `name`         | str        | User name, will be displayed in Dojo. |
| `description`  | str        | Can be user's own bio or internal notes about the user. Will be analyzed to better profile the user if given. |
| `profile_image`| str        | URL to profile image of the user. |
| `age`          | int        | Age of the user. We will internally convert it to year of birth. |
| `gender`       | str        | The user's gender. |
| `custom_attributes` | dict  | A collection of key-value pair that can store arbitrary values. Useful if you want to use fields that are not defined in REST API spec. <br><br>Key must be a string. and value can be a `bool`, a `str`, a `number`, a `list`, or `None` |

Please refer to [REST API document](https://api.askmiso.com/#tag/User-APIs) for complete field list. With more detailed and accurate metadata provided, Miso can yield better search result for your customers.


### Return Value

A dictionary of returned result with following properties:

| Name           | Type       | Description |
| -------------- | ---------- | ----------- |
| `errors`       | bool       | Upload successed or failed. |
| `message`      | str        | Summarized message. |
| `data`         | list[str]  | Detail for each error happend. |

----------------------------------------------------------------------


## `ApiClient.user.read()`

Read a user's data.

### Example

```python
from miso.sdk import ApiClient

api_client = ApiClient(api_key="{api_key}")
response = api_client.user.read(user_id='0000001')

user_data = response['data']
```

### Parameters

| Name           | Type       | Description |
| -------------- | ---------- | ----------- |
| `user_id`      | str        | The user's unique ID |

### Return Value

Returned value is a dict with all fields from user data.

Should cantain all data uploaded with `ApiClient.user.upload()`


## `ApiClient.user.delete()`

Remove a user's data.

This function should be when receiving data removal request from users (right to be forgotten).

### Example

```python
from miso.sdk import ApiClient

api_client = ApiClient(api_key="{api_key}")
api_client.user.delete(user_id='0000001')
```

### Parameters
| Name           | Type       | Description |
| -------------- | ---------- | ----------- |
| `user_id`      | str        | ID of the user to be removed. |

### Return Value
| Name           | Type       | Description |
| -------------- | ---------- | ----------- |
| `message`      | str        | Execution result message. |


## Learn more
For advanced usage and extra parameters, see [REST API](https://api.askmiso.com/#tag/Product-Content-APIs) for detail.
