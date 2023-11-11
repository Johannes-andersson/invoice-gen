from flask import Blueprint

invoice_blueprint = Blueprint('invoice', __name__)


@invoice_blueprint.route('/invoice/create', methods=['POST'])
def create_invoice():
    # Logic for creating an invoice
    pass

# ... routes for read, update, delete
