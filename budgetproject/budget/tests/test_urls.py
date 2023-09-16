from django.test import SimpleTestCase
from django.urls import reverse, resolve

from budget.views import project_list, project_detail, ProjectCreateView 
class TestUrls(SimpleTestCase):

    def test_list_urls_resolves(self):

        url = reverse('list')
        print(resolve(url))
        #note below, the object / function itself is checked
        self.assertEquals(resolve(url).func,project_list)
    
    def test_project_create_urls_resolves(self):

        url = reverse('add')
        print(resolve(url))
        #note below, the object / class itself is checked
        self.assertEquals(resolve(url).func.view_class,ProjectCreateView)
    
    def test_details_resolves(self):

        url = reverse('detail',args=['some-slug'])
        print(resolve(url))
        #note below, the object / function itself is checked
        self.assertEquals(resolve(url).func,project_detail)

