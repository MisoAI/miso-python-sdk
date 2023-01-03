# `ApiClient.interaction`

The Interaction APIs let you manage your interaction records stored with Miso.

----------------------------------------------------------------------

## `ApiClient.interaction.upload()`

Insert user Interaction records, and engine will be trained to fit user behavior.

### Example

```python
from miso.sdk import ApiClient

api_client = ApiClient(api_key="{api_key}")

interactions = [
  # First interaction
  {
    "user_id":"f5df9ef",
    "type":"search",
    "search": {
      "keywords": "chips",
    },
    "timestamp": "2023-01-24T14:15:21Z",
  },
  # Second interaction, from another user
  {
    "type": "product_detail_page_view",
    "duration": 61.5,
    "product_ids": [
      "123ABC-BLACK"
    ],
    "product_group_ids": [
      "123ABC"
    ],
    "user_id": "5b09700",
    "anonymous_id": "86D51273AD8BF84217E1567B6CBE7152D7034404",
    "timestamp": "2023-01-24T14:15:22Z",
    "miso_id": "123e4567-e89b-12d3-a456-426614174000",
    "context": {
      "campaign": {
        "name": "spring_sale",
        "source": "Google",
        "medium": "cpc",
        "term": "running+shoes",
        "content": "textlink"
      },
      "truncated_ip": "1.1.1.0",
      "locale": "en-US",
      "region": "US East",
      "page": {
        "url": "https://example.com/miso-tshirt-123ABC",
        "referrer": "https://example.com/",
        "title": "My Product Page"
      },
      "user_agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
      "custom_context": {
        "session_variable_1": [
          "value_1",
          "value_2"
        ]
      }
    }
  },
]

api_client.interaction.upload(data=interactions)
```

### Parameters

| Name           | Type       | Description |
| -------------- | ---------- | ----------- |
| `data`         | dict       | List of user interactions. |


`data` is a list of dictionaries, each dictionary represents a single user interaction.

For different interaction types, different fields can be used:

<div id="interaction-types"></div>
<div class="md-typeset__scrollwrap"><div class="md-typeset__table" id="upload-payload"></div></div>


### Return Value

A dictionary of returned result with following properties:

| Name           | Type       | Description |
| -------------- | ---------- | ----------- |
| `errors`       | bool       | Upload successed or failed. |
| `message`      | str        | Summarized message. |
| `data`         | list[str]  | Detail for each error happend. |

----------------------------------------------------------------------


## `ApiClient.interaction.delete()`

Delete interaction data for specified users.

This function should be when receiving data removal request from users (right to be forgotten).

### Example
Request

```python
from miso.sdk import ApiClient

api_client = ApiClient(api_key="{api_key}")

user_ids = ["5b09700", "f5df9ef", "2bc5d3f"]
response = api_client.interaction.delete(user_ids=user_ids)
```

### Parameters
| Name           | Type       | Description |
| -------------- | ---------- | ----------- |
| `user_ids`     | list[str]  | List of user IDs to be removed. |

### Return Value
| Name           | Type       | Description |
| -------------- | ---------- | ----------- |
| `message`      | str        | Summarized message. |


## Learn more
For advanced usage and extra parameters, see [REST API](https://api.askmiso.com/#tag/Interaction-APIs) for detail.

<!----------------------------------------------------------------->

<style>
  #interaction-types{
    display: flex;
    gap:10px;
    flex-wrap: wrap;
    font-size:.7rem;
  }
  #interaction-types div{
    border:1px solid var(--md-primary-fg-color);
    padding:0 4px;
    border-radius:.1rem;
    color: var(--md-primary-fg-color);
    cursor:pointer;
  }
  #interaction-types div.active{
    background-color:var(--md-primary-fg-color);
    color: var(--md-primary-bg-color);
  }
</style>
<script>
const fields = {
  "type":              ['str', 'Required. Type of the interaction.'],
  "user_id":           ['str', 'The user making the interaction. Either user_id or anonymous_id needs to be specified for personalization to work.'],
  "anonymous_id":      ['str', 'The anonymous visitor making the interaction. Either user_id or anonymous_id needs to be specified for personalization to work.'],
  "timestamp":         ['str', 'The ISO-8601 timestamp specifying when the interaction occurred. Current time will be used if not specified.'],
  "product_ids":       ['list[str]', 'Products or content the user is interacting with.'],
  "product_group_ids": ['list[str]', 'The product groups the user is interacting with.'],
  "miso_id":           ['str', 'Miso-generated unique ID for each recommendation or search result.'],
  "context":           ['dict', 'An object of extra information that provides useful context about an interaction.'],
  "rating":            ['float', 'The rating the user gave in the range of [0, 5]. As a convention in the RecSys community, a rating >= 3.5 is considered positive, a rating <= 2 is negative, and otherwise a rating is neutral. If you use any other rating scale, please normalize it to a [0, 5] scale.'],
  "duration":          ['float', 'How long (in seconds) the user stayed on this page'],
  "search":            ['dict', '`search.keywords` is the search keywords use by the user. `search.filters` is an dictionary of filters users apply to the search results'],
  "quantities":        ['list[int]', 'The quantities of products the user adds to their cart or checks out'],
  "revenue":           ['float', 'Total revenue associated with the checkout'],
  "custom_action_name":['str', 'Name of the custom interaction'],
}

const _items = ['product_ids', 'product_group_ids']

const common_fields = ["type", "user_id", "anonymous_id", "timestamp", "miso_id", "context"];

const interaction_fields = {
  "product_detail_page_view": [..._items, "duration"],
  "search": ['search'],
  "add_to_cart": [..._items, "quantities"],
  "remove_from_cart": [..._items, "quantities"],
  "checkout": ['revenue', ..._items, "quantities"],
  "refund": [..._items],
  "subscribe": [..._items],
  "add_to_collection": [..._items],
  "remove_from_collection": [..._items],
  "read": [..._items, "duration"],
  "watch": [..._items, "duration"],
  "listen": [..._items, "duration"],
  "like": [..._items],
  "dislike": [..._items],
  "share": [..._items],
  "rate": [..._items, "rating"],
  "bookmark": [..._items],
  "complete": [..._items],
  "impression": [..._items],
  "viewable_impression": [..._items],
  "click": [..._items],
  "home_page_view": [..._items, "duration"],
  "category_page_view": [..._items, "duration"],
  "promo_page_view": [..._items, "duration"],
  "product_image_view": [..._items, "duration"],
  "custom": ['custom_action_name', ..._items],
};

const payload_table_wrapper = document.getElementById('upload-payload');

function htmlToElement(html) {
  let template = document.createElement('template');
  template.innerHTML = html.trim();
  return template.content.firstChild;
}

function showUploadPayload(name) {
  const type_specific_fields = interaction_fields[name] || [];
  const tbl = htmlToElement('<table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead></table>');
  const tbody = document.createElement('tbody');
  tbl.append(tbody);

  const all_fields = common_fields.concat(type_specific_fields);
  for (const field of all_fields) {
    const tr = document.createElement('tr');
    for (const val of [field, fields[field][0], fields[field][1]]) {
      const td = document.createElement('td');
      const cd = document.createElement('code');
      if (val == field) {
        cd.textContent = val;
        td.append(cd);
      } else {
        td.textContent = val;
      }
      tr.append(td);
    }
    tbody.append(tr)
  }

  payload_table_wrapper.childNodes.forEach(ele => ele.remove());
  payload_table_wrapper.append(tbl);
}

const interaction_wrapper = document.getElementById('interaction-types')
for (const type in interaction_fields) {
  const interaction_btn = document.createElement('div');
  interaction_btn.textContent = type;
  interaction_btn.id = `interaction_${type}`;
  interaction_btn.addEventListener('click', function(e) {
    document.querySelectorAll('#interaction-types .active').forEach(ele => {
      ele.classList.remove('active');
    })
    this.classList.add('active');
    showUploadPayload(type);
  })
  interaction_wrapper.append(interaction_btn);
}

window.addEventListener('load', ()=> {
  document.getElementById('interaction_search').click();
});

</script>
