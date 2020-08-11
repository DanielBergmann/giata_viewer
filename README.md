# giata_viewer
Helps to get info from GIATA api


## How to use

import adapter.py to your project

get_by_id(ids, params):

    ```
        get_by_id(70785)
        get_by_id(70785, 961142)
        get_by_id(70785, 961142, phones=True, title=True)
    ```
get_by_provider_id(provider, ids, params):
    
    ```
        get_by_provider_id("amadeus", "WYORD998")
        get_by_provider_id("amadeus", "WYORD998","ANYOTHER")
        get_by_provider_id("amadeus", "WYORD998","ANYOTHER",phones=True, emails=True, title=True)
    ```

### Available fields
    * title
    * address
    * city
    * country
    * phones
    * emails
