import requests
import pytest

class Test_dog_ceo:
    base_url = "https://dog.ceo/api"
    test_url = "https://images.dog.ceo/breeds/"

    def test_list_all_breeds(self):        
        request = requests.get(f"{self.base_url}/breeds/list/all")
        assert request.ok == True

    def test_random_image(self):
        request = requests.get(f"{self.base_url}/breeds/image/random")
        req = dict(request.json())
        assert self.test_url in req["message"]

    @pytest.mark.parametrize("value", [1,2,3,0,100])
    def test_random_more_one_image(self, value): 
        request = requests.get(f"{self.base_url}/breeds/image/random/{value}")
        assert request.ok == True

    def test_browse_postitive_link(self):
        request = requests.get(f"{self.base_url}/breed/hound/images/random")
        req = dict(request.json())
        assert self.test_url in req["message"]

    @pytest.mark.parametrize("next_link", ["апывапыва", "п5335п", "randomcheg", "randomysik", "testik"])
    def test_browse_negative_link(self, next_link):
        request = requests.get(f"{self.base_url}/breed/Affenpinscher/images/{next_link}")
        assert request.ok == False

