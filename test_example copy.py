from playwright.sync_api import Page,expect
import re,pytest

def test_has_title(page:Page):
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page:Page):
    get_started_link=page.get_by_role("link",name="Get started")
    expect(get_started_link).to_have_attribute("href",re.compile("docs/intro"))
    get_started_link.click()
    expect(page.get_by_role("heading",name="Installation")).to_be_visible()

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page:Page):
    page.goto("https://playwright.dev/")
    page.wait_for_timeout(5000)
    yield
    print("After each test case")