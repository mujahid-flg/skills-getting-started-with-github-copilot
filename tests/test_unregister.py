def test_unregister_from_activity_success(client):
    # Arrange
    activity_name = "Tennis"
    email = "sarah@mergington.edu"
    endpoint = f"/activities/{activity_name}/participants/{email}"

    # Act
    response = client.delete(endpoint)

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Removed {email} from {activity_name}"}

    activities_response = client.get("/activities")
    participants = activities_response.json()[activity_name]["participants"]
    assert email not in participants


def test_unregister_from_activity_not_found(client):
    # Arrange
    activity_name = "Nonexistent Activity"
    email = "student@mergington.edu"
    endpoint = f"/activities/{activity_name}/participants/{email}"

    # Act
    response = client.delete(endpoint)

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_from_activity_participant_not_found(client):
    # Arrange
    activity_name = "Chess Club"
    email = "not-found@mergington.edu"
    endpoint = f"/activities/{activity_name}/participants/{email}"

    # Act
    response = client.delete(endpoint)

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Participant not found in this activity"}
