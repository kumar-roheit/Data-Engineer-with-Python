## Snowflake Schema

Updating is typically simpler in a snowflake schema because there are less records to update because redundant values are minimized to their own table (e.g., countries have their own table, dim_country_sf). Snowflake schemas are also better at enforcing naming conventions due to referential integrity.
