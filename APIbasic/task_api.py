from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for demo
data = {'item' : [{'id':1, 'name': 'Item 1'}, {'id':2, 'name':'Item2'}]}

# Route to get a list of items
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(data)

# Route to get a specific item by ID
@app.route('/api/item/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data['items'] if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({'message': 'Item not found'}), 404

# Route to add a new item 
@app.route('/app/items', methods=['POST'])
def add_item():
    new_item = request.get.json()
    if 'name' in new_item:
        new_item['id'] = len(data['items']) + 1
        data['items'].append(new_item)
        return jsonify(new_item), 201
    return jsonify({'messege': 'Name is required'}), 400

# Route to update an existing item
@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    updated_item = request.get_jason()
    item = next((item for item in data['item'] if item['id'] == item_id), None)
    if item:
        item['name'] = updated_item.get('name', item['name'])
        return jsonify(item)
    return jsonify({'message:' 'Item not found'}), 404

# Route to delete an item by ID 
@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = next((item for item in data['item'] if item['id'] == item_id), None)
    if item:
        data['items'].remove(item)
        return jsonify({'message': 'Item deleted'})
    return jsonify({'message': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)