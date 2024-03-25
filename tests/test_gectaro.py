import requests
import pytest

class Test_gectaro:
    base_url = 'https://api.gectaro.com/v1'
    headers = {
        'Authorization': 'Bearer GkCDDdP65R3BfgNC9715BaCGg5rlIznD',
        'Cookie': '_csrf=eVuMsJbpJ--uQUn7Lu8BaHKk-gInhVh7'
        }   
    company_id = 18469

    def test_info_my_user(self):
        request = requests.get(f"{self.base_url}/users/current", headers=self.headers)
        assert request.ok == True

    def test_get_lists_projects(self):
        request = requests.get(f"{self.base_url}/project-statuses", headers=self.headers)
        assert request.ok == True

    def test_get_lists_projects_by_companie_id(self):
        request = requests.get(f"{self.base_url}/companies/{self.company_id}/projects", headers=self.headers)
        assert request.ok == True
    
    @pytest.mark.parametrize("payload_name", ["test","тест","123___321","Тестовое,создание.!","Name)_gdfgda2"])
    def test_post_create_project(self, payload_name):
        payload = {'name': f'{payload_name}'}
        request = requests.post(f"{self.base_url}/companies/{self.company_id}/projects", headers=self.headers, data=payload)
        assert request.ok == True
    

    @pytest.mark.parametrize("project_id", ["80169","80173","l;436","24556","fsdg"])
    def test_get_financial_statistics_for_the_project_bad(self, project_id):
        request = requests.get(f"{self.base_url}/v1/projects/{project_id}/statistics/financial", headers=self.headers)
        assert request.ok == False

