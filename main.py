# # import pandas as pd
# # df = pd.read_csv('dummy_interaction.csv')

# # print(df)
# from flask import Flask, jsonify, request

# app = Flask(__name__)

# # Example dataset (replace this with your actual dataset)
# videos_data = {
#     "user1": ["video1", "video2", "video3"],
#     "user2": ["video2", "video4", "video5"],
#     # Add more user recommendations as needed...
# }

# # Route to handle recommendations for a given user ID
# @app.route('/recommendations', methods=['GET'])
# def get_recommendations():
#     user_id = request.args.get('user_id')
#     if user_id is None:
#         return jsonify({"error": "User ID is required"}), 400

#     if user_id not in videos_data:
#         return jsonify({"error": "User ID not found"}), 404

#     recommended_videos = videos_data[user_id]

#     # You can fetch metadata for the recommended videos from your dataset/database
#     # For simplicity, let's just return video IDs
#     return jsonify({"user_id": user_id, "recommended_videos": recommended_videos})

# if __name__ == '__main__':
#     app.run(debug=True)
