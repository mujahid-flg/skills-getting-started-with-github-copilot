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
    assert len(activities) == 10
    assert "Chess Club" in activities
    assert "Manga Maniacs" in activities

    manga_club = activities["Manga Maniacs"]
    assert manga_club["description"] == "Explore the fantastic stories of the most interesting characters from Japanese Manga (graphic novels)."
    assert manga_club["schedule"] == "Wuesdays at 8pm"
    assert manga_club["max_participants"] == 15


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
