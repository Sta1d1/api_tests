import requests
import pytest

class Test_jsonplaceholder:
    base_url = "https://jsonplaceholder.typicode.com"
    test_by_country = {"postId": 1, "id": 3}

    @pytest.mark.parametrize("test_id, check_id", [(1, 1), (12, 2), (22, 3), (33, 4), (44, 5), (55, 6), (66, 7), (77, 8), (88, 9), (99, 10)])
    def test_get_by_id(self, test_id, check_id):
        request = requests.get(f"{self.base_url}/posts/{test_id}")
        req = request.json()
        print(req["userId"])
        assert check_id == req["userId"]
    
    def test_get_comments_by_id(self):
        request = requests.get(f"{self.base_url}/posts/2/comments")
        assert request.ok == True

    @pytest.mark.parametrize("test_request", ["/28930785284", "/la", "/test/com", "//f/f//f", "/fsdgsdg"])
    def test_get_not_correction_send(self, test_request):
        request = requests.get(f"{self.base_url}/{test_request}")
        assert request.ok == False

    def test_get_comments_by_id_and_postid(self):
        request = requests.get(f"{self.base_url}/comments/", params=self.test_by_country)
        req = request.json()
        assert "odio adipisci rerum aut animi" in req[0]["name"]

    @pytest.mark.parametrize("id_test", [1,2,3,4,5,6,7,8])
    def test_delete_by_id(self, id_test):
        request = requests.get(f"{self.base_url}/posts/{id_test}")
        assert request.ok == True




