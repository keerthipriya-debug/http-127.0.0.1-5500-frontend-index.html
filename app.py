from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Temporary storage
vehicles = []
documents = []


# Home API
@app.route("/")
def home():
    return jsonify({
        "message": "EV TrustCheck Backend Running Successfully!"
    })


# Backend connection status
@app.route("/api/status", methods=["GET"])
def status():
    return jsonify({
        "status": "success",
        "project": "EV TrustCheck",
        "backend": "Connected"
    })


# Add vehicle details
@app.route("/api/vehicles", methods=["POST"])
def add_vehicle():
    data = request.get_json()

    if not data:
        return jsonify({
            "status": "error",
            "message": "No vehicle data received"
        }), 400

    data["id"] = len(vehicles) + 1
    vehicles.append(data)

    return jsonify({
        "status": "success",
        "message": "Vehicle details saved successfully!",
        "vehicle": data
    }), 201


# View all vehicles
@app.route("/api/vehicles", methods=["GET"])
def get_vehicles():
    return jsonify({
        "status": "success",
        "total_vehicles": len(vehicles),
        "vehicles": vehicles
    })


# Save document information
@app.route("/api/documents", methods=["POST"])
def save_documents():
    data = request.get_json()

    if not data or "documents" not in data:
        return jsonify({
            "status": "error",
            "message": "No document information received"
        }), 400

    record = {
        "id": len(documents) + 1,
        "documents": data["documents"],
        "status": "Pending Review"
    }

    documents.append(record)

    return jsonify({
        "status": "success",
        "message": "Document information saved successfully!",
        "document": record
    }), 201


# View document information
@app.route("/api/documents", methods=["GET"])
def get_documents():
    return jsonify({
        "status": "success",
        "total_documents": len(documents),
        "documents": documents
    })


# Run backend server
if __name__ == "__main__":
    app.run(debug=True, port=5000)