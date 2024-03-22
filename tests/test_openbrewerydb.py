import requests
import pytest

class Test_openbrewerydb:
    base_url = "https://api.openbrewerydb.org/v1"
    test_city = "Norman"
    test_by_country = {"by_country": "south_korea"}

    def test_random_brewery(self):
        request = requests.get(f"{self.base_url}/breweries/random")
        assert request.ok == True
    
    def test_list_breweries_by_city(self):
        request = requests.get(f"{self.base_url}/breweries?by_city=Norman")
        req = request.json()
        assert self.test_city == req[0]["city"]
    
    def test_metadata(self):
        request = requests.get(f"{self.base_url}/breweries/meta")
        req = request.json()
        assert "8251" == req["total"]

    def test_show_south_korean_breweries_meta_data(self):
        request = requests.get(f"{self.base_url}/breweries/meta", params=self.test_by_country)
        req = request.json()
        assert "61" == req["total"]

    @pytest.mark.parametrize("obdb_id", ["b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0", "385a2831-a7d5-4d07-bcff-d9d3312c571c", "7713be83-2ff6-4dc5-a28e-a4f629978402", "28945428-2326-41b3-b2d9-97f6e8154783", "0cbb2117-5968-4d0d-a0fd-9ee7c7f53e31"])
    def test_get_single_brewery(self, obdb_id):
        request = requests.get(f"{self.base_url}/breweries/{obdb_id}")
        req = request.json()
        assert obdb_id == req["id"]

    @pytest.mark.parametrize("test_request", ["/req/", "/test/req", "/fsdf", "пвапва", "  1  ", "///1"])
    def test_get_not_correction_send(self, test_request):
        request = requests.get(f"{self.base_url}/{test_request}")
        assert request.ok == False
