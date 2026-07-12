def test_root_redirects_to_static_index(client):
    # Arrange
    endpoint = "/"

    # Act
    response = client.get(endpoint, follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_all_activities(client):
    # Arrange
    endpoint = "/activities"

    # Act
    response = client.get(endpoint)

    # Assert
    assert response.status_code == 200
    activities = response.json()
    assert isinstance(activities, dict)
    assert len(activities) == 9
    assert "Chess Club" in activities


def test_get_activities_returns_expected_activity_shape(client):
    # Arrange
    endpoint = "/activities"
    expected_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get(endpoint)

    # Assert
    assert response.status_code == 200
    activities = response.json()
    for details in activities.values():
        assert expected_keys.issubset(details.keys())
        assert isinstance(details["participants"], list)
