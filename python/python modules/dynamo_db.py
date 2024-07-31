import boto3
from boto3.dynamodb.conditions import Key, Attr

# Initialize the DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Create a DynamoDB table
def create_table():
    table = dynamodb.create_table(
        TableName='my_table',
        KeySchema=[
            {
                'AttributeName': 'partition_key',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'sort_key',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'partition_key',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'sort_key',
                'AttributeType': 'N'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table

# Insert an item into the DynamoDB table
def insert_item(table):
    table.put_item(
        Item={
            'partition_key': 'example',
            'sort_key': 1,
            'attribute1': 'value1',
            'attribute2': 'value2'
        }
    )

# Get an item from the DynamoDB table
def get_item(table):
    response = table.get_item(
        Key={
            'partition_key': 'example',
            'sort_key': 1
        }
    )
    return response.get('Item')

# Query items in the DynamoDB table
def query_items(table):
    response = table.query(
        KeyConditionExpression=Key('partition_key').eq('example') & Key('sort_key').between(1, 5)
    )
    return response.get('Items')

# Scan items in the DynamoDB table
def scan_items(table):
    response = table.scan(
        FilterExpression=Attr('attribute1').contains('value')
    )
    return response.get('Items')

# Query items using a Global Secondary Index
def query_gsi(table):
    response = table.query(
        IndexName='gsi_index',
        KeyConditionExpression=Key('gsi_partition_key').eq('value')
    )
    return response.get('Items')

# Query items using a Local Secondary Index
def query_lsi(table):
    response = table.query(
        IndexName='lsi_index',
        KeyConditionExpression=Key('partition_key').eq('example') & Key('lsi_sort_key').begins_with('prefix')
    )
    return response.get('Items')

# Update an item in the DynamoDB table
def update_item(table):
    table.update_item(
        Key={
            'partition_key': 'example',
            'sort_key': 1
        },
        UpdateExpression='SET attribute1 = :val1',
        ExpressionAttributeValues={
            ':val1': 'new_value'
        }
    )

# Delete an item from the DynamoDB table
def delete_item(table):
    table.delete_item(
        Key={
            'partition_key': 'example',
            'sort_key': 1
        }
    )

# Handle pagination for scanning items
def paginate_scan(table):
    response = table.scan()
    items = response.get('Items')

    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        items.extend(response.get('Items'))

    return items

# Main function to demonstrate the usage of the above functions
def main():
    # Create the table
    table = create_table()
    print("Table status:", table.table_status)

    # Insert an item
    insert_item(table)
    print("Inserted item.")

    # Get the item
    item = get_item(table)
    print("Retrieved item:", item)

    # Query items
    items = query_items(table)
    print("Queried items:", items)

    # Scan items
    scanned_items = scan_items(table)
    print("Scanned items:", scanned_items)

    # Update an item
    update_item(table)
    print("Updated item.")

    # Delete an item
    delete_item(table)
    print("Deleted item.")

    # Paginate scan
    all_items = paginate_scan(table)
    print("All scanned items:", all_items)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("An error occurred:", e)
