'''
Created on 29 Apr 2013

@author: Mark.rowlands
'''
import os
import requests
import time
import win32clipboard as WCB
from ..services.selenium_start_service import SeleniumStartService
from ..services.parameters import parameter_singleton
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from xml.etree import ElementTree
from xlrd import open_workbook
from random import randint


class BasePage():

    def __init__(self):
        self.driver = SeleniumStartService().start_driver()
        self.wait = WebDriverWait(self.driver, 15)
    #def __init__(self, driver, wait):
        #self.driver = driver
        #self.wait = wait
        self.baseurl = parameter_singleton["url"]
        self.baseip = self.baseurl.replace("http://", "")

    def get_driver(self):
        return self.driver

    def get_wait(self):
        return self.wait

    def get_baseurl(self):
        return self.baseurl

    def get_page_title(self):
        return self.driver.title

    def open_AIM_homepage_on_base_url(self):
        self.driver.get(self.baseurl)
        self.driver.refresh()

    def open_dashboard_settings_page(self):
        self.driver.get(self.baseurl + "/admin/settings.php")

    def ensure_logged_out(self):
        try:
            self.driver.find_element_by_link_text("Logout").click()
            time.sleep(1)
        except NoSuchElementException:
            pass

    def get_page_logo(self):
        return self.get_element_text_by_css("#admin_logo_right")

    def get_page_name(self):
        return self.get_element_text_by_css("#admin_logo_left")

    def get_footer_text(self):
        return self.get_element_text_by_css("#footer_version")

    def get_text_for_remote_tab(self):
        xpath = "//div[@id='admin_top_nav_bar']/ul/li[3]"
        return self.get_element_text_by_xpath(xpath)

    def get_text_for_local_tab(self):
        xpath = "//div[@id='admin_top_nav_bar']/ul/li[4]"
        return self.get_element_text_by_xpath(xpath)

    def get_receiver_widget_header(self):
        xpath = "//div[@id='widget_receivers']/div"
        return self.get_element_text_by_xpath(xpath)

    def get_transmitter_widget_header(self):
        xpath = "//div[@id='widget_transmitters']/div"
        return self.get_element_text_by_xpath(xpath)

    def get_text_of_remote_subtab_link(self, position):
        xpath = "//div[@id='receivers_links']/ul/li[%s]" % position
        return self.get_element_text_by_xpath(xpath)

    def get_text_of_local_subtab_link(self, position):
        xpath = "//div[@id='transmitters_links']/ul/li[%s]" % position
        return self.get_element_text_by_xpath(xpath)

    def get_element_located_by_id(self, id_):
        locator = (By.ID, id_)
        try:
            el = self.wait.until(EC.presence_of_element_located(locator))
            return el.is_displayed()
        except Exception:
            return False

    def get_element_located_by_link_text(self, link):
        locator = (By.LINK_TEXT, link)
        try:
            el = self.wait.until(EC.presence_of_element_located(locator))
            return el.is_displayed()
        except Exception:
            return False

    def get_element_located_by_xpath(self, xpath):
        locator = (By.XPATH, xpath)
        try:
            el = self.wait.until(EC.presence_of_element_located(locator))
            return el.is_displayed()
        except Exception:
            return False

    def get_element_located_by_css_selector(self, selector):
        locator = (By.CSS_SELECTOR, selector)
        try:
            el = self.wait.until(EC.presence_of_element_located(locator))
            return el.is_displayed()
        except Exception:
            return False

    def get_login_error_text(self):
        locator = (By.XPATH, "//span[contains(@class, 'error_message')]")
        return self.wait.until(EC.presence_of_element_located(locator)).text

    def get_information_to_user_text(self):
        return self.get_login_error_text()

    def get_element_css_property_by_id(self, prop, id_):
        el = self.wait.until(EC.presence_of_element_located((By.ID, id_)))
        return el.value_of_css_property(prop)

    def get_element_css_prop_by_xpath(self, prop, xpath):
        el = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        return el.value_of_css_property(prop)

    def get_element_text_by_xpath(self, xpath):
        el = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        return el.text

    def get_element_text_by_css(self, selector):
        locator = (By.CSS_SELECTOR, selector)
        el = self.wait.until(EC.presence_of_element_located(locator))
        return el.text

    def get_element_comp_text_by_css(self, element, css):
        return element.find_element_by_css_selector(css).text

    def get_attribute_via_xpath(self, xpath, attribute):
        el = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        return el.get_attribute(attribute)

    def get_attribute_via_id(self, id_, attribute):
        self.wait.until(EC.presence_of_element_located((By.ID, id_)))
        return self.driver.find_element_by_id(id_).get_attribute(attribute)

    def get_favicon_href(self):
        xpath = "//link[contains(@rel, 'icon')]"
        el = self.driver.find_element_by_xpath(xpath)
        return el.get_attribute("href")

    def get_list_of_links_on_current_page(self):
        return self.driver.find_elements_by_tag_name("a")

    def get_text_of_page_header(self):
        header = self.get_element_text_by_xpath("//div[@id='admin_body']/h1")
        if header != None:
            return header
        else:
            self.driver.refresh()
            self.get_text_of_page_header()

    def get_colour_property_of_element(self, element):
        return element.value_of_css_property("color")

    def wait_for_select_element(self, selector):
        locator = (By.CSS_SELECTOR, selector)
        self.wait.until(EC.presence_of_element_located(locator))
        return Select(self.driver.find_element_by_css_selector(selector))

    def select_dropdown_item_text(self, selector, text):
        select = self.wait_for_select_element(selector)
        select.select_by_visible_text(text)

    def select_dropdown_item_by_index(self, selector, index):
        select = self.wait_for_select_element(selector)
        select.select_by_index(index)

    def select_dropdown_item_text_for_element(self, element, text):
        self.wait.until(EC.visibility_of(element))
        Select(element).select_by_visible_text(text)

    def get_dropdown_option_texts(self, selector):
        labels = [option.text
                  for option in self.wait_for_select_element(selector).options]
        return labels

    def get_dropdown_options_text_by_element(self, element):
        labels = [option.text
                  for option in Select(element).options]
        return labels

    def get_selected_text_select_element(self, selector):
        select = self.wait_for_select_element(selector)
        return select.first_selected_option.text

    def get_selected_value_select_element(self, selector):
        select = self.wait_for_select_element(selector)
        return select.first_selected_option.get_attribute("value")

    def wait_for_and_click_by_link_text(self, link):
        locator = (By.LINK_TEXT, link)
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def wait_for_and_click_by_css(self, selector):
        locator = (By.CSS_SELECTOR, selector)
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def wait_for_and_click_by_xpath(self, selector):
        locator = (By.XPATH, selector)
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def click_save(self):
        self.wait_for_and_click_by_link_text("Save")
        self.wait_for_save_message_to_be_removed()

    def click_save_ignore_warnings(self):
        self.wait_for_and_click_by_link_text("Save")
        time.sleep(1.5)

    def click_save_settings(self):
        self.wait_for_and_click_by_link_text("Save Settings")
        self.wait_for_save_message_to_be_removed()

    def click_save_usb_settings(self):
        self.wait_for_and_click_by_link_text("Save USB Settings")
        self.wait_for_save_message_to_be_removed()

    def click_save_features(self):
        self.wait_for_and_click_by_link_text("Save Features")
        self.wait_for_save_message_to_be_removed()

    def click_save_features_ignore_warnings(self):
        self.wait_for_and_click_by_link_text("Save Features")

    def click_save_settings_ignore_warnings(self):
        self.wait_for_and_click_by_link_text("Save Settings")
        time.sleep(1)

    def click_save_and_sync(self):
        self.wait_for_and_click_by_link_text("Save & Sync")
        path = "#ldap_import_ajax_message.message_box.mb_green"
        locator = By.CSS_SELECTOR, path
        self.wait.until(EC.visibility_of_element_located(locator))
        self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_save_message_to_be_removed(self):
        messages = ["",
                    "Saving changes...",
                    "Saving settings...",
                    "Settings saved. " +
                    "The change of address will take about 40 seconds."]
        wait = WebDriverWait(self.driver, 60)
        while True:
                try:
                    selector = "span[id*='ajax_message']"
                    message = self.get_element_text_by_css(selector)
                    if message in messages:
                        try:
                            loc = (By.CSS_SELECTOR, selector)
                            wait.until(EC.invisibility_of_element_located(loc))
                            break
                        except TimeoutException:
                            self.wait_for_save_message_to_be_removed()
                    else:
                        raise RuntimeError("Error: %s" % message)
                except NoSuchElementException:
                    break

    def click_cancel(self):
        self.wait_for_and_click_by_link_text("Cancel")

    def show_user_permissions(self):
        if self.get_element_located_by_id("show_user_permissions"):
            self.driver.execute_script("toggle_user_permissions(1)")
            time.sleep(2)

    def show_receiver_permissions(self):
        if self.get_element_located_by_id("show_receiver_permissions"):
            self.driver.execute_script("toggle_receiver_permissions(1)")
            time.sleep(2)

    def form_new_ip_address(self):
        if self.get_element_located_by_id("configure_device"):
            new_ip = self.get_ip_address_from_config_page().split(".")
            if new_ip[3] == "254":
                new_ip[3] = "30"
            elif not new_ip[3] == "254":
                new_ip[3] = str(int(new_ip[3]) + 1)
            return ".".join((new_ip[0], new_ip[1], new_ip[2], new_ip[3]))

    def enter_text_into_input_field(self, id_, text):
        if self.get_element_located_by_id(id_):
            self.driver.find_element_by_id(id_).clear()
            self.driver.find_element_by_id(id_).send_keys(text)

    def get_list(self, _type):
        time.sleep(2)
        url = self.driver.current_url
        if "session" in url or "/login.php?r=%2Fadmin%2Findex.php" in url:
            self.login_as("admin", "password", False)
        if _type is "transmitters":
            if(any(wanted_text in self.get_pagination_text()
                   for wanted_text in ["transmitter", "transmitters"])):
                return self.driver.find_elements_by_xpath("//tbody/tr")
            else:
                self.open_transmitters_tab()
                return self.get_list_of_transmitters()
        elif _type is "receivers":
            if(any(wanted_text in self.get_pagination_text()
                   for wanted_text in ["receiver", "receivers"])):
                return self.driver.find_elements_by_xpath("//tbody/tr")
            else:
                self.open_receivers_tab()
                return self.get_list_of_receivers()
        elif _type is "receiver_groups":
            if(any(wanted_text in self.get_pagination_text()
                   for wanted_text in ["receiver group", "receiver groups"])):
                return self.driver.find_elements_by_xpath("//tbody/tr")
            else:
                self.open_receivers_tab()
                self.open_view_receiver_groups_page()
                return self.get_list_of_receiver_groups()
        elif _type is "channels":
            if(any(wanted_text in self.get_pagination_text()
                   for wanted_text in ["channel", "channels"])):
                return self.driver.find_elements_by_xpath("//tbody/tr")
            else:
                self.open_channels_tab()
                return self.get_list_of_channels()
        elif _type is "channel_groups":
            if(any(wanted_text in self.get_pagination_text()
                   for wanted_text in ["channel group", "channel groups"])):
                return self.driver.find_elements_by_xpath("//tbody/tr")
            else:
                self.open_channels_tab()
                self.click_view_channel_group_button()
                return self.get_list_of_channels()
        elif _type is "servers":
            if self.get_text_of_page_header() == "Servers":
                return self.driver.find_elements_by_xpath("//tbody/tr")
            else:
                self.open_servers_tab()
                return self.get_list_of_servers()
        elif _type is "users":
            if(any(wanted_text in self.get_pagination_text()
                   for wanted_text in ["user", "users"])):
                return self.driver.find_elements_by_xpath("//tbody/tr")
            else:
                self.open_users_tab()
                return self.get_list_of_users()
        elif _type is "user_groups":
            if(any(wanted_text in self.get_pagination_text()
                   for wanted_text in ["user group", "user groups"])):
                return self.driver.find_elements_by_xpath("//tbody/tr")
            else:
                self.open_users_tab()
                self.open_view_user_groups_page()
                return self.get_list_of_user_groups()
        elif _type is "presets":
            if(any(wanted_text in self.get_pagination_text()
                   for wanted_text in ["preset", "presets"])):
                return self.driver.find_elements_by_xpath("//tbody/tr")
            else:
                self.open_presets_tab()
                return self.get_list_of_presets()
        elif _type is "devices":
            if(any(wanted_text in self.get_pagination_text()
                   for wanted_text in ["device", "devices"])):
                return self.driver.find_elements_by_xpath("//tbody/tr")
            else:
                self.open_device_list_directly()
                return self.get_list_of_devices()

    def get_pagination_text(self):
        locator = (By.CSS_SELECTOR, "div.pagination_row")
        el = self.wait.until(EC.presence_of_element_located(locator))
        cols = el.find_elements_by_tag_name("div")
        if len(cols) == 1:
            return cols[0].text.lower()
        else:
            return cols[-1].text.lower()

    def get_pagination_total(self):
        total = self.get_element_text_by_css("div.pagination_row div")
        total = total.split()
        return total[-1]

    def get_attribute_of_cell_by_xpath(self, element, xpath, attribute):
        return element.find_element_by_xpath(xpath).get_attribute(attribute)

    def get_attribute_of_element(self, element, attribute):
        return element.get_attribute(attribute)

    def get_text_of_element(self, element):
        return element.text

    def set_text_of_element(self, element, text):
        self.wait.until(EC.visibility_of(element))
        element.clear()
        element.send_keys(text)

    def get_element_comp_text_by_xpath(self, element, xpath):
        return element.find_element_by_xpath(xpath).text

    def get_element_component_text_by_css(self, element, selector):
        return element.find_element_by_css_selector(selector).text

    def set_css_element_state(self, selector, state):
        locator = (By.CSS_SELECTOR, selector)
        self.wait.until(EC.presence_of_element_located(locator))
        if self.get_state_of_css_element(selector) == state:
            pass
        else:
            self.driver.find_element_by_css_selector(selector).click()

    def get_state_of_css_element(self, selector):
        locator = (By.CSS_SELECTOR, selector)
        el = self.wait.until(EC.presence_of_element_located(locator))
        return el.is_selected()

    def get_visibility_of_link_text(self, link):
        locator = (By.LINK_TEXT, link)
        try:
            el = self.wait.until(EC.visibility_of_element_located(locator))
            return el.is_displayed()
        except TimeoutException:
            return False

    def get_visibility_of_element_by_xpath(self, xpath):
        locator = (By.XPATH, xpath)
        try:
            el = self.wait.until(EC.visibility_of_element_located(locator))
            return el.is_displayed()
        except TimeoutException:
            return False

    def get_visibility_of_element_by_css(self, selector):
        locator = (By.CSS_SELECTOR, selector)
        try:
            el = self.wait.until(EC.visibility_of_element_located(locator))
            return el.is_displayed()
        except TimeoutException:
            return False

    """
    Login Page BasePage
    """
    def wait_for_login(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "username")))

    def login_as(self, username, password, remember):
        self.wait_for_login()
        user_field = self.driver.find_element_by_id("username")
        pass_field = self.driver.find_element_by_id("password")
        self.set_text_of_element(user_field, username)
        self.set_text_of_element(pass_field, password)
        if remember == True:
            self.wait_for_and_click_by_css("#remember_me")
        else:
            pass
        if user_field.get_attribute("value") != "":
            self.wait_for_and_click_by_css("#login")
        else:
            self.login_as(username, password, remember)

    def get_user_validate_tooltip_text(self, state):
        path = ("div.form_row.required.{} " +
                "> div.validation_label.tooltip").format(state)
        el = self.driver.find_element_by_css_selector(path)
        return self.get_attribute_of_element(el, "title")

    def get_located_login_error_message(self):
        locator = (By.XPATH, "//span[contains(@class, 'error_message')]")
        el = self.wait.until(EC.presence_of_element_located(locator))
        return el.is_displayed()

    def get_login_error_message_text(self):
        return self.get_element_text_by_css("span.message_box." +
                                            "mb_red.error_message")

    def get_located_username_input(self):
        return self.get_element_located_by_id("username")

    def get_located_password_input(self):
        return self.get_element_located_by_id("password")

    def get_back_ground_colour(self):
        return self.get_element_css_property_by_id("background-color",
                                                   "login_width_1000")

    def get_back_ground_image(self):
        return self.get_element_css_prop_by_xpath("background-image",
                                                  "//body")

    def get_back_ground_repeat_property(self):
        return self.get_element_css_prop_by_xpath("background-repeat",
                                                  "//body")

    """
    Dashboard Page BasePage
    """
    def open_dashboard_tab(self):
        self.wait_for_and_click_by_link_text("DASHBOARD")

    def get_located_dashboard_link(self):
        return self.get_visibility_of_link_text("DASHBOARD")

    def click_dashboard_home_link(self):
        l = ["DASHBOARD", "Home"]
        action = ActionChains(self.driver)
        (action
         .move_to_element(self.driver.find_element_by_link_text(l[0]))
         .move_to_element(self.driver.find_element_by_link_text(l[1]))
         .click()
         .perform())

    def click_dashboard_settings_link(self):
        l = ["DASHBOARD", "Home", "Settings"]
        action = ActionChains(self.driver)
        (action
        .move_to_element(self.driver.find_element_by_link_text(l[0]))
        .move_to_element(self.driver.find_element_by_link_text(l[1]))
        .move_to_element(self.driver.find_element_by_link_text(l[2]))
        .click()
        .perform())

    def click_dashboard_backups_link(self):
        l = ["DASHBOARD", "Home", "Backups"]
        action = ActionChains(self.driver)
        (action
        .move_to_element(self.driver.find_element_by_link_text(l[0]))
        .move_to_element(self.driver.find_element_by_link_text(l[1]))
        .move_to_element(self.driver.find_element_by_link_text(l[2]))
        .click()
        .perform())

    def click_dashboard_updates_link(self):
        l = ["DASHBOARD", "Home", "Updates"]
        action = ActionChains(self.driver)
        (action
        .move_to_element(self.driver.find_element_by_link_text(l[0]))
        .move_to_element(self.driver.find_element_by_link_text(l[1]))
        .move_to_element(self.driver.find_element_by_link_text(l[2]))
        .click()
        .perform())

    def click_dashboard_active_connections_link(self):
        l = ["DASHBOARD", "Home", "Active Connections"]
        action = ActionChains(self.driver)
        (action
        .move_to_element(self.driver.find_element_by_link_text(l[0]))
        .move_to_element(self.driver.find_element_by_link_text(l[1]))
        .move_to_element(self.driver.find_element_by_link_text(l[2]))
        .click()
        .perform())

    def click_dashboard_connection_log_link(self):
        l = ["DASHBOARD", "Home", "Connection Log"]
        action = ActionChains(self.driver)
        (action
        .move_to_element(self.driver.find_element_by_link_text(l[0]))
        .move_to_element(self.driver.find_element_by_link_text(l[1]))
        .move_to_element(self.driver.find_element_by_link_text(l[2]))
        .click()
        .perform())

    def click_dashboard_event_log_link(self):
        l = ["DASHBOARD", "Home", "Event Log"]
        action = ActionChains(self.driver)
        (action
        .move_to_element(self.driver.find_element_by_link_text(l[0]))
        .move_to_element(self.driver.find_element_by_link_text(l[1]))
        .move_to_element(self.driver.find_element_by_link_text(l[2]))
        .click()
        .perform())

    def click_dashboard_view_all_active_connects_link(self):
        self.wait_for_and_click_by_link_text("View all Active Connections")

    def click_dashboard_view_events_link(self):
        self.wait_for_and_click_by_link_text("View all Events")

    def click_dashboard_view_all_channels_link(self):
        self.wait_for_and_click_by_link_text("View all Channels")

    def click_dashboard_view_all_channel_changes_link(self):
        self.wait_for_and_click_by_link_text("View all Channel Changes")

    def click_dashboard_view_all_OSD_logins_link(self):
        self.wait_for_and_click_by_link_text("View all OSD Logins")

    def click_dashboard_view_all_users_link(self):
        self.wait_for_and_click_by_link_text("View all Users")

    def click_dashboard_view_all_receivers_link(self):
        self.wait_for_and_click_by_link_text("View all Receivers")

    def click_dashboard_view_all_transmitters_link(self):
        self.wait_for_and_click_by_link_text("View all Transmitters")

    def get_located_upload_input_element(self):
        return self.get_element_located_by_id("uploaded_aim_upgrade_file")

    def get_receivers_from_dashboard_widget(self):
        xpath = "//div[@id='widget_receivers']//tbody/tr"
        return self.driver.find_elements_by_xpath(xpath)

    def click_receiver_connect_via_dashboard(self, element):
        element.find_element_by_xpath("./td[2]/a[2]").click()

    def click_receiver_disconnect_via_dashboard(self, element):
        element.find_element_by_xpath("./td[2]/a[3]").click()

    def get_visible_rx_discon_button(self, element):
        try:
            return element.find_element_by_xpath("./td[2]/a[3]").is_displayed()
        except Exception:
            return False

    def get_widget_element_text(self, id_, xpath, text):
        widget = "//div[@id='%s']/div[2]" % id_
        table_rows = "//div[@id='%s']//tbody/tr" % id_
        try:
            if self.get_element_text_by_xpath(widget) != text:
                rows = self.driver.find_elements_by_xpath(table_rows)
                names = [row.find_element_by_xpath(xpath).text
                         for row in rows]
                return names
        except Exception:
            names = []
            return names

    def get_widget_element_link(self, id_, xpath, text):
        widget = "//div[@id='%s']/div[2]" % id_
        table_rows = "//div[@id='%s']//tbody/tr" % id_
        try:
            if self.get_element_text_by_xpath(widget) != text:
                rows = self.driver.find_elements_by_xpath(table_rows)
                links = [row.find_element_by_xpath(xpath).get_attribute("href")
                         for row in rows]
                return links
        except Exception:
            links = []
            return links

    def get_active_connection_user_names(self):
        return self.get_widget_element_text("widget_active_connections",
                                            "./td[3]/a",
                                            "No Active Connections")

    def get_active_connection_user_name_links(self):
        return self.get_widget_element_link("widget_active_connections",
                                            "./td[3]/a",
                                            "No Active Connections")

    def get_active_connection_receiver_names(self):
        return self.get_widget_element_text("widget_active_connections",
                                            "./td[4]/span/a",
                                            "No Active Connections")

    def get_active_connection_receiver_name_links(self):
        return self.get_widget_element_link("widget_active_connections",
                                            "./td[4]/span/a",
                                            "No Active Connections")

    def get_active_connection_channel_names(self):
        return self.get_widget_element_text("widget_active_connections",
                                            "./td[5]/a",
                                            "No Active Connections")

    def get_active_connection_channel_name_links(self):
        return self.get_widget_element_link("widget_active_connections",
                                            "./td[5]/a",
                                            "No Active Connections")

    def get_active_connection_preset_names(self):
        return self.get_widget_element_text("widget_active_connections",
                                            "./td[6]/a",
                                            "No Active Connections")

    def get_active_connection_preset_name_links(self):
        return self.get_widget_element_link("widget_active_connections",
                                            "./td[6]/a",
                                            "No Active Connections")

    def get_event_log_user_names(self):
        return self.get_widget_element_text("widget_events",
                                            "./td[6]/a",
                                            "No Active Connections")

    def get_event_log_user_name_links(self):
        return self.get_widget_element_link("widget_events",
                                            "./td[6]/a",
                                            "No Active Connections")

    def get_event_log_transmitter_names(self):
        return self.get_widget_element_text("widget_events",
                                            "./td[4]/a",
                                            "No Active Connections")

    def get_event_log_transmitter_name_links(self):
        return self.get_widget_element_link("widget_events",
                                            "./td[4]/a",
                                            "No Active Connections")

    def get_event_log_receiver_names(self):
        return self.get_widget_element_text("widget_events",
                                            "./td[5]/a",
                                            "No Active Connections")

    def get_event_log_receiver_name_links(self):
        return self.get_widget_element_link("widget_events",
                                            "./td[5]/a",
                                            "No Active Connections")

    def get_event_log_channel_names(self):
        return self.get_widget_element_text("widget_events",
                                            "./td[7]/a",
                                            "No Active Connections")

    def get_event_log_channel_name_links(self):
        return self.get_widget_element_link("widget_events",
                                            "./td[7]/a",
                                            "No Active Connections")

    def get_channel_names(self):
        return self.get_widget_element_text("widget_channels",
                                            "./td[1]/a",
                                            "No Channels found")

    def get_channel_name_links_from_dashboard_page(self):
        return self.get_widget_element_link("widget_channels",
                                            "./td[1]/a",
                                            "No Channels found")

    def get_channel_configure_links_icon(self):
        return self.get_widget_element_link("widget_channels",
                                            "./td[2]/a[1]",
                                            "No Channels found")

    def get_channel_clone_links_from_icon(self):
        return self.get_widget_element_link("widget_channels",
                                            "./td[2]/a[2]",
                                            "No Channels found")

    def get_user_login_names(self):
        return self.get_widget_element_text("widget_user_logins",
                                            "./td[2]/a",
                                            "No Channels found")

    def get_user_login_name_links(self):
        return self.get_widget_element_link("widget_user_logins",
                                            "./td[1]/a",
                                            "No Channels found")

    def get_user_login_configure_links_from_icon(self):
        return self.get_widget_element_link("widget_user_logins",
                                            "./td[2]/a[1]",
                                            "No Channels found")

    def get_user_login_clone_links_from_icon_on_dashboard_page(self):
        return self.get_widget_element_link("widget_user_logins",
                                            "./td[2]/a[2]",
                                            "No Channels found")

    def get_user_registration_names(self):
        return self.get_widget_element_text("widget_users",
                                            "./td[2]/a",
                                            "No Channels found")

    def get_user_registration_name_links(self):
        return self.get_widget_element_link("widget_users",
                                            "./td[2]/a",
                                            "No Channels found")

    def get_user_reg_config_links_from_icon(self):
        return self.get_widget_element_link("widget_users",
                                            "./td[3]/a[1]",
                                            "No Channels found")

    def get_user_reg_clone_links_from_icon(self):
        return self.get_widget_element_link("widget_users",
                                            "./td[3]/a[2]",
                                            "No Channels found")

    def get_receiver_names(self):
        return self.get_widget_element_text("widget_receivers",
                                            "./td[1]/a",
                                            "No Channels found")

    def get_receiver_name_links(self):
        return self.get_widget_element_link("widget_receivers",
                                            "./td[1]/a",
                                            "No Channels found")

    def get_receiver_configure_links_from_icon(self):
        return self.get_widget_element_link("widget_receivers",
                                            "./td[2]/a[1]",
                                            "No Channels found")

    def get_receiver_connect_links_from_icon(self):
        return self.get_widget_element_link("widget_receivers",
                                            "./td[2]/a[2]",
                                            "No Channels found")

    def get_transmitter_names(self):
        return self.get_widget_element_text("widget_transmitters",
                                            "./td[1]/a",
                                            "No Channels found")

    def get_transmitter_name_links(self):
        return self.get_widget_element_link("widget_transmitters",
                                            "./td[1]/a",
                                            "No Channels found")

    def get_transmitter_confifgure_links_from_icon(self):
        return self.get_widget_element_link("widget_transmitters",
                                            "./td[2]/a[1]",
                                            "No Channels found")

    def get_channel_change_user_name(self):
        return self.get_widget_element_text("widget_channel_changes",
                                            "./td[2]/a",
                                            "No Channels found")

    def get_channel_change_user_name_links(self):
        return self.get_widget_element_link("widget_channel_changes",
                                            "./td[2]/a",
                                            "No Channels found")

    def get_channel_change_receiver_name(self):
        return self.get_widget_element_text("widget_channel_changes",
                                            "./td[3]/a",
                                            "No Channels found")

    def get_channel_change_receiver_links(self):
        return self.get_widget_element_link("widget_channel_changes",
                                            "./td[3]/a",
                                            "No Channels found")

    def get_channel_change_channel_name(self):
        return self.get_widget_element_text("widget_channel_changes",
                                            "./td[4]/a",
                                            "No Channels found")

    def get_channel_change_channel(self):
        return self.get_widget_element_link("widget_channel_changes",
                                            "./td[4]/a",
                                            "No Channels found")

    def get_displayed_time_and_date(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "logout")))
        date_as_string = self.driver.find_element_by_id("logout").text
        date_as_string = date_as_string.rstrip("(admin) Logout")
        date_as_string = date_as_string.split()
        if len(date_as_string[2]) == 1:
            date_as_string[2] = "0" + date_as_string[2]
        sequence = (date_as_string[0],
                    date_as_string[1],
                    date_as_string[2],
                    date_as_string[3],
                    date_as_string[4])
        return " ".join(sequence)

    def get_year_comparison(self, aim_time, system_time):
        aim_time = aim_time.split(" ")
        system_time = system_time.split(" ")
        return aim_time[4] == system_time[4]

    def get_month_comparison(self, aim_time, system_time):
        aim_time = aim_time.split(" ")
        system_time = system_time.split(" ")
        return aim_time[3] == system_time[3]

    def get_date_comparison(self, aim_time, system_time):
        aim_time = aim_time.split(" ")
        system_time = system_time.split(" ")
        return aim_time[2] == system_time[2]

    def get_day_comparison(self, aim_time, system_time):
        aim_time = aim_time.split(" ")
        system_time = system_time.split(" ")
        return aim_time[1] == system_time[1]

    def get_hour_comparison(self, aim_time, system_time):
        aim_time = aim_time.split(" ")
        system_time = system_time.split(" ")
        aim_time = aim_time[0].split(":")
        system_time = system_time[0].split(":")
        hour_match = False
        if aim_time[0] == system_time[0]:
            hour_match = True
        elif (int(aim_time[0]) == int(system_time[0]) - 1
              and aim_time[1] == "59"
              and system_time[1] == "00"):
            hour_match = True
        if hour_match:
            return hour_match
        else:
            raise RuntimeError("Hour Mismatch %s %s" % (aim_time[0],
                                                        system_time[0]))

    def get_min_comparison(self, aim_time, system_time):
        aim_time = aim_time.split(" ")
        system_time = system_time.split(" ")
        aim_time = aim_time[0].split(":")
        system_time = system_time[0].split(":")
        aim_time[1] = aim_time[1].strip(",")
        system_time[1] = system_time[1].strip(",")
        if (aim_time[1] == system_time[1]
            or aim_time[1] == str(int(system_time[1]) + 1)
            or aim_time[1] == str(int(system_time[1]) - 1)):
            return True
        else:
            raise RuntimeError("Minute Mismatch %s %s" % (aim_time[1],
                                                          system_time[1]))

    def get_located_logout_button(self):
        return self.get_element_located_by_link_text("Logout")

    def get_logout_button_colour_property(self):
        xpath = "//div[@id='logout']/a"
        return self.get_element_css_prop_by_xpath("color", xpath)

    def click_restart(self):
        self.wait_for_and_click_by_link_text("Restart")

    def click_shutdown(self):
        self.wait_for_and_click_by_link_text("Shutdown")

    def get_restart_aim_unit_text_from_lightbox(self):
        return self.get_lightbox_title_text()

    def get_shutdown_aim_unit_text_from_lightbox(self):
        return self.get_lightbox_title_text()

    def get_restarting_header(self):
        return self.get_element_text_by_xpath("//div[@id='admin_body']/div/h1")

    def wait_for_reset_to_complete(self):
        wait = WebDriverWait(self.driver, 360)
        locator = By.XPATH, "//div[@id='admin_body']/h1"
        try:
            wait.until(EC.text_to_be_present_in_element(locator, "Dashboard"))
        except Exception:
            self.driver.refresh()
            wait.until(EC.text_to_be_present_in_element(locator, "Dashboard"))

    def get_visibility_of_dashboard_disconnect_all(self):
        path = ("#widget_active_connections " +
                "> div.widget_content.nopadding " +
                "> div:nth-child(1) " +
                "> a")
        return self.get_element_located_by_css_selector(path)

    def click_dashboard_disconnect_all(self):
        path = ("#widget_active_connections " +
                "> div.widget_content.nopadding " +
                "> div:nth-child(1) " +
                "> a")
        self.wait_for_and_click_by_css(path)

    def get_text_of_active_connections_widget(self):
        path = ("#widget_active_connections " +
                "> div.widget_content.nopadding")
        return self.get_element_text_by_css(path)

    """
    Dashboard Settings General
    """

    def click_general_settings_button(self):
        self.wait_for_and_click_by_link_text("General")

    def get_osd_timeout_options(self):
        return self.get_dropdown_option_texts("#osd_cookie_length")

    def get_current_osd_timeout_selection_text(self):
        return self.get_selected_text_select_element("#osd_cookie_length")

    def select_osd_timeout_by_text(self, label):
        self.select_dropdown_item_text("#osd_cookie_length", label)

    def get_admin_timeout_options(self):
        return self.get_dropdown_option_texts("#admin_cookie_length")

    def get_current_admin_timeout_selection_text(self):
        return self.get_selected_text_select_element("#admin_cookie_length")

    def select_admin_timeout_by_text(self, label):
        self.select_dropdown_item_text("#admin_cookie_length", label)

    def set_state_hide_dormant_devices_no(self):
        self.set_css_element_state("#ignore_dormant_devices_0", True)

    def set_state_hide_dormant_devices_yes(self):
        self.set_css_element_state("#ignore_dormant_devices_1", True)

    def get_state_hide_dormant_devices_setting(self, option):
        if option == "no":
            return self.get_state_of_css_element("#ignore_dormant_devices_0")
        elif option == "yes":
            return self.get_state_of_css_element("#ignore_dormant_devices_1")

    def set_state_all_users_exclusive_access_no(self):
        self.set_css_element_state("#allow_users_exclusive_mode_0", True)

    def set_state_all_users_exclusive_access_yes(self):
        self.set_css_element_state("#allow_users_exclusive_mode_1", True)

    def get_state_grant_all_users_exclusive_access(self, option):
        no = "#allow_users_exclusive_mode_0"
        yes = "#allow_users_exclusive_mode_1"
        if option == "no":
            return self.get_state_of_css_element(no)
        elif option == "yes":
            return self.get_state_of_css_element(yes)

    def set_allowed_connection_mode_view(self):
        self.set_css_element_state("#allowed_channel_modes_4", True)

    def set_allowed_connection_mode_view_shared(self):
        self.set_css_element_state("#allowed_channel_modes_1", True)

    def set_allowed_connection_mode_shared(self):
        self.set_css_element_state("#allowed_channel_modes_5", True)

    def set_allowed_connection_mode_exclusive(self):
        self.set_css_element_state("#allowed_channel_modes_2", True)

    def set_allowed_connection_mode_all(self):
        self.set_css_element_state("#allowed_channel_modes_3", True)

    def get_state_allowed_connection_mode(self, option):
        all_ = "#allowed_channel_modes_3"
        view = "#allowed_channel_modes_4"
        view_shared = "#allowed_channel_modes_1"
        shared = "#allowed_channel_modes_5"
        exclusive = "#allowed_channel_modes_2"
        if option == "all":
            return self.get_state_of_css_element(all_)
        elif option == "view":
            return self.get_state_of_css_element(view)
        elif option == "view_shared":
            return self.get_state_of_css_element(view_shared)
        elif option == "shared":
            return self.get_state_of_css_element(shared)
        elif option == "exclusive":
            return self.get_state_of_css_element(exclusive)

    def get_rows_per_page_options(self):
        return self.get_dropdown_option_texts("#rows_per_page")

    def get_current_rows_per_page_selection_text(self):
        return self.get_selected_text_select_element("#rows_per_page")

    def select_rows_per_page_by_text(self, label):
        self.select_dropdown_item_text("#rows_per_page", label)

    def get_current_locale(self):
        return self.get_selected_text_select_element("#locale")

    def get_locales(self):
        return self.get_dropdown_option_texts("#locale")

    def select_locale_by_text(self, text):
        self.select_dropdown_item_text("#locale", text)

    def set_api_login_required_no(self):
        self.set_css_element_state("#api_login_required_0", True)

    def set_api_login_required_yes(self):
        self.set_css_element_state("#api_login_required_1", True)

    def get_api_login_required_setting(self, option):
        no = "#api_login_required_0"
        yes = "#api_login_required_1"
        if option == "no":
            return self.get_state_of_css_element(no)
        elif option == "yes":
            return self.get_state_of_css_element(yes)

    def get_anonymous_user_options(self):
        return self.get_dropdown_option_texts("#anon_user")

    def get_current_anonymous_user_selection_text(self):
        return self.get_selected_text_select_element("#anon_user")

    def select_anonymous_user_by_text(self, label):
        self.select_dropdown_item_text("#anon_user", label)

    def get_api_anonymous_user_options(self):
        return self.get_dropdown_option_texts("#api_anon_user")

    def get_current_api_anonymous_user_selection(self):
        return self.get_selected_text_select_element("#api_anon_user")

    def select_api_anonymous_user_by_text(self, label):
        self.select_dropdown_item_text("#api_anon_user", label)

    """
    Dashboard Setting Transmitters
    """
    def click_transmitters_settings_button(self):
        self.wait_for_and_click_by_link_text("Transmitters")

    def get_global_magic_eye_options(self):
        return self.get_dropdown_option_texts("#magic_eye")

    def get_slected_global_magic_eye(self):
        return self.get_selected_text_select_element("#magic_eye")

    def select_global_magic_eye_by_text(self, label):
        self.select_dropdown_item_text("#magic_eye", label)

    def get_global_ddc_options(self):
        return self.get_dropdown_option_texts("#ddc")

    def get_selected_global_ddc(self):
        return self.get_selected_text_select_element("#ddc")

    def select_global_ddc_by_text(self, label):
        self.select_dropdown_item_text("#ddc", label)

    def get_global_hot_plug_detect_control_options(self):
        return self.get_dropdown_option_texts("#hpd")

    def get_selected_global_hot_plug_detect_control(self):
        return self.get_selected_text_select_element("#hpd")

    def select_global_hot_plug_detect_control_by_text(self, label):
        self.select_dropdown_item_text("#hpd", label)

    def get_global_hot_plug_detect_signal_period_options(self):
        return self.get_dropdown_option_texts("#video_ddc_delay")

    def get_selected_global_hot_plug_detect_period(self):
        return self.get_selected_text_select_element("#video_ddc_delay")

    def select_global_hot_plug_detect_signal_period(self, label):
        self.select_dropdown_item_text("#video_ddc_delay", label)

    def get_global_background_refresh_options(self):
        return self.get_dropdown_option_texts("#video_br")

    def get_selected_global_background_refresh(self):
        return self.get_selected_text_select_element("#video_br")

    def select_global_background_refresh_by_text(self, label):
        self.select_dropdown_item_text("#video_br", label)

    def get_global_compression_level_options(self):
        return self.get_dropdown_option_texts("#video_compression_combo")

    def get_selected_global_compression_level(self):
        path = "#video_compression_combo"
        return self.get_selected_text_select_element(path)

    def select_global_compression_level_by_text(self, label):
        self.select_dropdown_item_text("#video_compression_combo", label)

    def select_global_compression_minimum_by_text(self, label):
        self.select_dropdown_item_text("#video_compression_min", label)

    def select_global_compression_maximum_by_text(self, label):
        self.select_dropdown_item_text("#video_compression_max", label)

    def get_global_usb_speed_setting(self, option):
        if option == "hi_speed":
            return self.get_state_of_css_element("#usb_speed_0")
        elif option == "full_speed":
            return self.get_state_of_css_element("#usb_speed_1")

    def set_state_global_usb_speed_hi_speed(self, state):
        self.set_css_element_state("#usb_speed_0", state)

    def set_state_global_usb_speed_full_speed(self, state):
        self.set_css_element_state("#usb_speed_1", state)

    def get_global_usb_hub_size_setting(self, option):
        if option == "13":
            return self.get_state_of_css_element("#usb_hub_size_13")
        elif option == "7":
            return self.get_state_of_css_element("#usb_hub_size_7")

    def set_state_global_usb_hub_size_13(self, state):
        self.set_css_element_state("#usb_hub_size_13", state)

    def set_state_global_usb_hub_size_7(self, state):
        self.set_css_element_state("#usb_hub_size_7", state)

    def get_global_enable_dummy_boot_keyboard_setting(self, option):
        if option == "yes":
            return self.get_state_of_css_element("#fk_enable_1")
        elif option == "no":
            return self.get_state_of_css_element("#fk_enable_0")

    def set_state_global_dummy_keyboard_yes(self, state):
        self.set_css_element_state("#fk_enable_1", state)

    def set_state_global_dummy_keyboard_no(self, state):
        self.set_css_element_state("#fk_enable_0", state)

    def get_global_reserved_usb_port_setting(self):
        return self.get_selected_text_select_element("#usb_fixed_ports")

    def get_global_reserved_usb_port_options(self):
        return self.get_dropdown_option_texts("#usb_fixed_ports")

    def select_global_reserved_usb_port_by_text(self, label):
        self.select_dropdown_item_text("#usb_fixed_ports", label)

    def get_global_serial_parity_options(self):
        return self.get_dropdown_option_texts("#serial_parity")

    def get_selected_global_serial_parity(self):
        return self.get_selected_text_select_element("#serial_parity")

    def select_global_serial_parity_by_text(self, label):
        self.select_dropdown_item_text("#serial_parity", label)

    def get_global_serial_data_bits_options(self):
        return self.get_dropdown_option_texts("#serial_data_bits")

    def get_selected_global_serial_data_bits(self):
        return self.get_selected_text_select_element("#serial_data_bits")

    def select_global_serial_data_bits_by_text(self, label):
        self.select_dropdown_item_text("#serial_data_bits", label)

    def get_global_serial_stop_bits_options(self):
        return self.get_dropdown_option_texts("#serial_stop_bits")

    def get_selected_global_serial_stop_bits(self):
        return self.get_selected_text_select_element("#serial_stop_bits")

    def select_global_serial_stop_bits_by_text(self, label):
        self.select_dropdown_item_text("#serial_stop_bits", label)

    def get_global_serial_speed_options(self):
        return self.get_dropdown_option_texts("#serial_speed")

    def get_selected_global_serial_speed(self):
        return self.get_selected_text_select_element("#serial_speed")

    def select_global_serial_speed_by_text(self, label):
        self.select_dropdown_item_text("#serial_speed", label)

    """
    Dashboard Setting Receivers
    """
    def click_receivers_settings_button(self):
        self.wait_for_and_click_by_link_text("Receivers")

    def get_global_login_required_setting(self, option):
        if option == "yes":
            return self.get_state_of_css_element("#login_required_1")
        elif option == "no":
            return self.get_state_of_css_element("#login_required_0")

    def set_state_global_login_required_yes(self, state):
        self.set_css_element_state("#login_required_1", state)

    def set_state_global_login_required_no(self, state):
        self.set_css_element_state("#login_required_0", state)

    def get_enable_receiver_osd_alerts_setting(self, option):
        if option == "yes":
            return self.get_state_of_css_element("#osd_alerts_1")
        elif option == "no":
            return self.get_state_of_css_element("#osd_alerts_0")

    def set_state_global_osd_alerts_yes(self, state):
        self.set_css_element_state("#osd_alerts_1", state)

    def set_state_global_osd_alerts_no(self, state):
        self.set_css_element_state("#osd_alerts_0", state)

    def get_audio_input_type_mode_options(self, option):
        if option == "line":
            return self.get_state_of_css_element("#audio_is_0")
        elif option == "mic":
            return self.get_state_of_css_element("#audio_is_1")
        elif option == "mic_boost":
            return self.get_state_of_css_element("#audio_is_2")

    def set_state_global_audio_input_line(self, state):
        self.set_css_element_state("#audio_is_0", state)

    def set_state_global_audio_input_mic(self, state):
        self.set_css_element_state("#audio_is_1", state)

    def set_state_global_audio_input_mic_boost(self, state):
        self.set_css_element_state("#audio_is_2", state)

    def get_global_video_compatibility_check_options(self):
        return self.get_dropdown_option_texts("#video_compatibility_check")

    def get_selected_global_video_compatibility(self):
        path = "#video_compatibility_check"
        return self.get_selected_text_select_element(path)

    def select_global_video_compatibility_check_by_text(self, text):
        self.select_dropdown_item_text("#video_compatibility_check", text)

    def get_receiver_keyboard_country_code_options(self):
        return self.get_dropdown_option_texts("#keyboard_country")

    def get_selected_receiver_keyboard_country_code(self):
        return self.get_selected_text_select_element("#keyboard_country")

    def select_receiver_keyboard_country_code_by_text(self, text):
        self.select_dropdown_item_text("#keyboard_country", text)

    def get_selected_first_osd_hotkey(self):
        return self.get_selected_text_select_element("#osd_hotkey_1")

    def get_selected_second_osd_hotkey(self):
        return self.get_selected_text_select_element("#osd_hotkey_2")

    def get_osd_hotkey_icon_img(self):
        xpath = ("//div[contains(text(), 'OSD Hotkeys')]" +
                 "/following-sibling::div[2]")
        return self.get_element_css_prop_by_xpath("background-image", xpath)

    def select_second_osd_hotkey(self, label):
        self.select_dropdown_item_text("#osd_hotkey_2", label)

    def get_selected_first_shortcut_hotkey(self):
        return self.get_selected_text_select_element("#shortcut_hotkey_1")

    def get_selected_second_shortcut_hotkey(self):
        return self.get_selected_text_select_element("#shortcut_hotkey_2")

    def get_shortcut_hotkey_icon_img(self):
        xpath = ("//div[contains(text(), 'Shortcut Hotkeys')]" +
                 "/following-sibling::div[2]")
        return self.get_element_css_prop_by_xpath("background-image", xpath)

    def select_second_shortcut_hotkey(self, label):
        self.select_dropdown_item_text("#shortcut_hotkey_2", label)

    def get_selected_first_last_channel_hotkey(self):
        return self.get_selected_text_select_element("#last_channel_hotkey_1")

    def get_selected_second_last_channel_hotkey(self):
        return self.get_selected_text_select_element("#last_channel_hotkey_2")

    def get_last_channel_hotkey_icon_img(self):
        xpath = ("//div[contains(text(), 'Last-Channel Hotkey')]" +
                 "/following-sibling::div[2]")
        return self.get_element_css_prop_by_xpath("background-image", xpath)

    def select_second_last_channel_hotkey(self, label):
        self.select_dropdown_item_text("#last_channel_hotkey_2", label)

    def get_selected_first_view_only_mode_hotkey(self):
        return self.get_selected_text_select_element("#view_only_hotkey_1")

    def get_selected_second_view_only_mode_hotkey(self):
        return self.get_selected_text_select_element("#view_only_hotkey_2")

    def get_view_only_mode_hotkey_icon_img(self):
        xpath = ("//div[contains(text(), 'View-Only Mode Hotkeys')]" +
                 "/following-sibling::div[2]")
        return self.get_element_css_prop_by_xpath("background-image", xpath)

    def select_second_view_only_mode_hotkey(self, label):
        self.select_dropdown_item_text("#view_only_hotkey_2", label)

    def get_selected_first_shared_mode_hotkey(self):
        return self.get_selected_text_select_element("#shared_hotkey_1")

    def get_selected_second_shared_mode_hotkey(self):
        return self.get_selected_text_select_element("#shared_hotkey_2")

    def get_shared_mode_hotkey_validation_icon(self):
        xpath = ("//div[contains(text(), 'Shared Mode Hotkeys')]" +
                 "/following-sibling::div[2]")
        return self.get_element_css_prop_by_xpath("background-image", xpath)

    def select_second_shared_mode_hotkey(self, label):
        self.select_dropdown_item_text("#shared_hotkey_2", label)

    def get_selected_first_exclusive_mode_hotkey(self):
        return self.get_selected_text_select_element("#exclusive_hotkey_1")

    def get_selected_second_exclusive_mode_hotkey(self):
        return self.get_selected_text_select_element("#exclusive_hotkey_2")

    def get_exclusive_hotkey_icon_img(self):
        xpath = ("//div[contains(text(), 'Exclusive Mode Hotkeys')]" +
                 "/following-sibling::div[2]")
        return self.get_element_css_prop_by_xpath("background-image", xpath)

    def select_second_exclusive_mode_hotkey(self, label):
        self.select_dropdown_item_text("#exclusive_hotkey_2", label)

    def get_selected_first_disconnect_hotkey(self):
        return self.get_selected_text_select_element("#disconnect_hotkey_1")

    def get_selected_second_disconnect_hotkey(self):
        return self.get_selected_text_select_element("#disconnect_hotkey_2")

    def get_disconnect_icon_img(self):
        xpath = ("//div[contains(text(), 'Disconnect Hotkeys')]" +
                 "/following-sibling::div[2]")
        return self.get_element_css_prop_by_xpath("background-image", xpath)

    def select_second_disconnect_hotkey(self, label):
        self.select_dropdown_item_text("#disconnect_hotkey_2", label)

    def get_global_hid_only_setting(self, option):
        no = "#hid_only_0"
        yes = "#hid_only_1"
        if option == "no":
            return self.get_state_of_css_element(no)
        elif option == "yes":
            return self.get_state_of_css_element(yes)

    def set_state_global_hid_only_no(self, state):
        self.set_css_element_state("#hid_only_0", state)

    def set_state_global_hid_only_yes(self, state):
        self.set_css_element_state("#hid_only_1", state)

    def get_disable_iso_endpoint_osd_alert_setting(self, option):
        no = "#isochronous_user_warning_0"
        yes = "#isochronous_user_warning_1"
        if option == "no":
            return self.get_state_of_css_element(no)
        elif option == "yes":
            return self.get_state_of_css_element(yes)

    def set_state_global_disable_isochronous_endpoint_alerts_no(self):
        self.set_css_element_state("#isochronous_user_warning_0", True)

    def set_state_global_disable_isochronous_endpoint_alerts_yes(self):
        self.set_css_element_state("#isochronous_user_warning_1", True)

    def get_enable_iso_endpoint_attach_setting(self, option):
        no = "#isochronous_enabled_0"
        yes = "#isochronous_enabled_1"
        if option == "no":
            return self.get_state_of_css_element(no)
        elif option == "yes":
            return self.get_state_of_css_element(yes)

    def set_state_global_enable_iso_endpoint_attach_no(self):
        self.set_css_element_state("#isochronous_enabled_0", True)

    def set_state_global_enable_iso_endpoint_attach_yes(self):
        self.set_css_element_state("#isochronous_enabled_1", True)

    """
    Dashboard Setting Network
    """
    def get_visibility_of_settings_warning(self):
        el = self.driver.find_element_by_css_selector("#settings_ajax_message")
        return el.is_displayed()

    def click_network_settings_button(self):
        self.wait_for_and_click_by_link_text("Network")

    def select_syslog_enabled(self, state):
        if state:
            self.wait_for_and_click_by_css("#syslog_enabled_1")
        else:
            self.wait_for_and_click_by_css("#syslog_enabled_0")

    def get_visible_aim_mac_address_2(self, connection_type):
        xpath = ("//div[@id='eth1_" + connection_type + "_div']" +
                 "/div" +
                 "/div[contains(text(), 'AIM MAC Address 2')]")
        return self.get_visibility_of_element_by_xpath(xpath)

    def get_visible_aim_ip_address_2(self, connection_type):
        xpath = ("//div[@id='eth1_" + connection_type + "_div']" +
                 "/div" +
                 "/div[contains(text(), 'AIM IP Address 2')]")
        return self.get_visibility_of_element_by_xpath(xpath)

    def get_visible_of_gateway_ip_address(self, connection_type):
        xpath = ("//div[@id='eth1_" + connection_type + "_div']" +
                 "/div" +
                 "/div[contains(text(), 'Gateway IP Address')]")
        return self.get_visibility_of_element_by_xpath(xpath)

    def get_visibility_of_netmask_label(self, connection_type):
        xpath = ("//div[@id='eth1_" + connection_type + "_div']" +
                 "/div" +
                 "/div[contains(text(), 'Netmask')]")
        return self.get_visibility_of_element_by_xpath(xpath)

    def get_visible_dns_ip_address(self, connection_type):
        xpath = ("//div[@id='eth1_" + connection_type + "_div']" +
                 "/div" +
                 "/div[contains(text(), 'DNS Server IP Address')]")
        return self.get_visibility_of_element_by_xpath(xpath)

    def get_visible_aim_mac_address_2_value(self, connection_type):
        xpath = ("//div[@id='eth1_" + connection_type + "_div']" +
                 "/div" +
                 "/div[contains(text(), 'AIM MAC Address 2')]" +
                 "/following-sibling::div")
        return self.get_visibility_of_element_by_xpath(xpath)

    def get_visible_aim_ip_address_2_value(self, connection_type):
        xpath = ("//div[@id='eth1_" + connection_type + "_div']" +
                 "/div" +
                 "/div[contains(text(), 'AIM IP Address 2')]" +
                 "/following-sibling::div")
        return self.get_visibility_of_element_by_xpath(xpath)

    def get_visible_gateway_ip_address_value(self, connection_type):
        xpath = ("//div[@id='eth1_" + connection_type + "_div']" +
                 "/div" +
                 "/div[contains(text(), 'Gateway IP Address')]" +
                 "/following-sibling::div")
        return self.get_visibility_of_element_by_xpath(xpath)

    def get_visibility_of_netmask_value(self, connection_type):
        xpath = ("//div[@id='eth1_" + connection_type + "_div']" +
                 "/div" +
                 "/div[contains(text(), 'Netmask')]" +
                 "/following-sibling::div")
        return self.get_visibility_of_element_by_xpath(xpath)

    def get_visible_dns_ip_address_value(self, connection_type):
        xpath = ("//div[@id='eth1_" + connection_type + "_div']" +
                 "/div" +
                 "/div[contains(text(), 'DNS Server IP Address')]" +
                 "/following-sibling::div")
        return self.get_visibility_of_element_by_xpath(xpath)

#     def get_visible_aim_mac_address_2_value(self, connection_type):
#         if self.get_visible_aim_mac_address_2(connection_type):
#             xpath = ("//div[@id='eth1_%s_div']" +
#                      "/div" +
#                      "/div[contains(text(), 'AIM MAC Address 2')]" +
#                      "/following-sibling::div"
#                      % connection_type)
#             return self.get_element_text_by_xpath(xpath)

    def get_aim_ip_address_2_value(self, connection_type):
        if self.get_visible_aim_ip_address_2_value(connection_type):
            xpath = ("//div[@id='eth1_" + connection_type + "_div']" +
                     "/div" +
                     "/div[contains(text(), 'AIM IP Address 2')]" +
                     "/following-sibling::div")
            return self.get_element_text_by_xpath(xpath)

    def set_network_setting_ip(self, id_, address):
        self.set_text_of_element(self.driver.find_element_by_id(id_), address)

    def get_network_setting_ip_validate(self, form_label):
        xpath = ("//div[contains(text(), '" + form_label + "')]" +
                 "/following-sibling::div[2]")
        return self.get_element_css_prop_by_xpath("background-image", xpath)

    def get_network_setting_ip_2_validate_appearance(self, form_label):
        xpath = ("//div[@id='eth1_static_div']" +
                 "//div[contains(text(), '" + form_label + "')]" +
                 "/following-sibling::div[2]")
        return self.get_element_css_prop_by_xpath("background-image", xpath)

    def set_syslog_ip(self, address):
        self.set_network_setting_ip("ip_syslog", address)

    def get_syslog_ip(self):
        el = self.driver.find_element_by_id("ip_syslog")
        return el.get_attribute("value")

    def get_syslog_ip_validation_icon(self):
        return self.get_network_setting_ip_validate("Syslog IP Address")

    def set_multicast_ip_base(self, address):
        self.set_network_setting_ip("multicast_ip_address_base", address)

    def get_multicast_ip_base(self):
        el = self.driver.find_element_by_id("multicast_ip_address_base")
        return el.get_attribute("value")

    def get_multicast_ip_base_validation_icon(self):
        return self.get_network_setting_ip_validate("Multicast IP Base")

    def set_aim_ip(self, address):
        self.set_network_setting_ip("ip_aim_server", address)

    def get_aim_ip(self):
        el = self.driver.find_element_by_id("ip_aim_server")
        return el.get_attribute("value")

    def get_aim_ip_validation_icon_appearance(self):
        return self.get_network_setting_ip_validate("AIM IP Address")

    def set_gateway_ip(self, address):
        self.set_network_setting_ip("ip_gateway", address)

    def get_gateway_ip_validation_icon(self):
        return self.get_network_setting_ip_validate("Gateway IP Address")

    def set_netmask(self, address):
        self.set_network_setting_ip("ip_netmask", address)

    def get_netmask_validation_icon_appearance(self):
        return self.get_network_setting_ip_validate("Netmask")

    def set_dns_server_ip(self, address):
        self.set_network_setting_ip("ip_name_server", address)

    def get_dns_server_ip_validation_icon_appearance(self):
        form_label = "DNS Server IP Address"
        return self.get_network_setting_ip_validate(form_label)

    def set_aim_ip_2(self, address):
        self.set_network_setting_ip("ip_aim_server1", address)

    def get_aim_ip_2_validation_icon(self):
        form_label = "AIM IP Address 2"
        return self.get_network_setting_ip_2_validate_appearance(form_label)

    def set_gateway_ip_2(self, address):
        self.set_network_setting_ip("ip_gateway1", address)

    def get_gateway_ip_2_validation_icon(self):
        form_label = "Gateway IP Address"
        return self.get_network_setting_ip_2_validate_appearance(form_label)

    def set_netmask_2(self, address):
        self.set_network_setting_ip("ip_netmask1", address)

    def get_netmask_2_validation_icon(self):
        form_label = "Netmask"
        return self.get_network_setting_ip_2_validate_appearance(form_label)

    def set_dns_server_ip_2(self, address):
        self.set_network_setting_ip("ip_name_server1", address)

    def get_dns_server_ip_2_validation_icon(self):
        form_label = "DNS Server IP Address"
        return self.get_network_setting_ip_2_validate_appearance(form_label)

    def select_no_ethernet_2(self):
        self.set_css_element_state("#eth1_enabled_0", True)

    def select_dhcp_ethernet_2(self):
        self.set_css_element_state("#eth1_enabled_1", True)

    def select_static_ethernet_2(self):
        self.set_css_element_state("#eth1_enabled_2", True)

    def set_snmp_enabled(self, state):
        if state == "yes":
            self.set_css_element_state("#snmp_enabled_1", True)
        else:
            self.set_css_element_state("#snmp_enabled_0", True)

    def get_display_state_snmp_username(self):
        return self.get_element_located_by_id("snmp_username")

    """
    Dashboard Settings Time
    """
    def click_time_settings_button(self):
        self.wait_for_and_click_by_link_text("Time")

    def select_time_zone(self, zone):
        self.select_dropdown_item_text("#timezone_area", zone)

    def select_time_zone_location(self, zone, location):
        self.select_dropdown_item_text("#timezone_location_" + zone, location)

    def get_all_time_zone_locations(self, zone):
        if self.driver.name == "chrome":
            time.sleep(4)
        return self.get_dropdown_option_texts("#timezone_location_" + zone)

    def change_hour_for_ntp_test(self):
        time = self.get_displayed_time_and_date()
        hour = time.split(" ")
        hour = int(hour[0].split(":"))
        if randint(1, 2) % 2:
            hour = hour + randint(1, 9)
        else:
            hour = hour - randint(1, 9)
        if hour < 10:
            hour = str("0" + hour)
        else:
            hour = str(hour)
        self.select_dropdown_item_text("#date_hour", hour)

    def get_time_date(self):
        return self.get_selected_text_select_element("#date_day")

    def select_time_day(self, day):
        self.select_dropdown_item_text("#date_day", day)

    def get_all_time_month_day_texts(self):
        return self.get_dropdown_option_texts("#date_month")

    def get_time_month(self):
        return self.get_selected_text_select_element("#date_month")

    def select_time_month(self, month):
        self.select_dropdown_item_text("date_month", month)

    def get_time_year(self):
        return self.get_attribute_via_id("date_year", "value")

    def select_time_year(self, year):
        self.set_text_of_element(self.driver.find_element_by_id("date_year"),
                                 year)

    def set_ntp_enabled(self, state):
        if state == "yes":
            self.set_css_element_state("#ntp_enabled_1", True)
        else:
            self.set_css_element_state("#ntp_enabled_0", True)

    def get_ntp_enabled(self, option):
        if option == "no":
            return self.get_state_of_css_element("#ntp_enabled_0")
        elif option == "yes":
            return self.get_state_of_css_element("#ntp_enabled_1")

    def get_display_state_ntp_servername(self):
        return self.get_element_located_by_id("ntp_on_div")

    def get_appearance_of_ntp_1(self):
        locator = (By.CSS_SELECTOR, "#ntp_hide_row_1 > div.form_label")
        link_path = "#ntp_hide_row_1 > div:nth-child(2) > a"
        label = self.wait.until(EC.presence_of_element_located(locator))
        set_link = self.driver.find_element_by_css_selector(link_path)
        if label.is_displayed() == True and set_link.is_displayed() == True:
            return True
        else:
            return False

    def get_appearance_of_ntp_2(self):
        locator = (By.CSS_SELECTOR, "#ntp_hide_row_2 > div.form_label")
        link_path = "#ntp_hide_row_2 > div:nth-child(2) > a"
        label = self.wait.until(EC.presence_of_element_located(locator))
        link = self.driver.find_element_by_css_selector(link_path)
        if label.is_displayed() == True and link.is_displayed() == True:
            return True
        else:
            return False

    def get_appearance_of_ntp_3(self):
        locator = (By.CSS_SELECTOR, "#ntp_hide_row_3 > div.form_label")
        link_path = "#ntp_hide_row_3 > div:nth-child(2) > a"
        label = self.wait.until(EC.presence_of_element_located(locator))
        link = self.driver.find_element_by_css_selector(link_path)
        if label.is_displayed() == True and link.is_displayed() == True:
            return True
        else:
            return False

    def click_ntp1_set(self):
        path = "#ntp_hide_row_1 > div:nth-child(2) > a"
        self.wait_for_and_click_by_css(path)

    def click_ntp1_unset(self):
        path = "#ntp_show_row_1 > div.form_row > div:nth-child(4) > a"
        self.wait_for_and_click_by_css(path)

    def click_ntp2_set(self):
        path = "#ntp_hide_row_2 > div:nth-child(2) > a"
        self.wait_for_and_click_by_css(path)

    def click_ntp2_unset(self):
        path = "#ntp_show_row_2 > div.form_row > div:nth-child(4) > a"
        self.wait_for_and_click_by_css(path)

    def click_ntp3_set(self):
        path = "#ntp_hide_row_3 > div:nth-child(2) > a"
        self.wait_for_and_click_by_css(path)

    def click_ntp3_unset(self):
        path = "#ntp_show_row_3 > div.form_row > div:nth-child(4) > a"
        self.wait_for_and_click_by_css(path)

    def get_appearance_of_ntp_1_full_settings(self):
        locator = (By.CSS_SELECTOR, "#ntp_server_1")
        server = self.wait.until(EC.presence_of_element_located(locator))
        number = self.driver.find_element_by_css_selector("#ntp_ext_key_id_1")
        key = self.driver.find_element_by_css_selector("#ntp_ext_key_val_1")
        return (server.is_displayed()
                and number.is_displayed()
                and key.is_displayed())

    def get_appearance_of_ntp_2_full_settings(self):
        locator = (By.CSS_SELECTOR, "#ntp_server_2")
        server = self.wait.until(EC.presence_of_element_located(locator))
        number = self.driver.find_element_by_css_selector("#ntp_ext_key_id_2")
        key = self.driver.find_element_by_css_selector("#ntp_ext_key_val_2")
        return (server.is_displayed()
                and number.is_displayed()
                and key.is_displayed())

    def get_appearance_of_ntp_3_full_settings(self):
        locator = (By.CSS_SELECTOR, "#ntp_server_3")
        server = self.wait.until(EC.presence_of_element_located(locator))
        number = self.driver.find_element_by_css_selector("#ntp_ext_key_id_3")
        key = self.driver.find_element_by_css_selector("#ntp_ext_key_val_3")
        return (server.is_displayed()
                and number.is_displayed()
                and key.is_displayed())

    """
    Dashboard Settings Mail
    """
    def click_mail_settings_button(self):
        self.wait_for_and_click_by_link_text("Mail")

    def click_mail_enable_yes(self):
        self.set_css_element_state("#mail_enabled_1", True)

    def click_mail_enable_no(self):
        self.set_css_element_state("#mail_enabled_0", True)

    def is_server_setting_active(self, selector):
        locator = (By.CSS_SELECTOR, selector)
        el = self.wait.until(EC.presence_of_element_located(locator))
        return el.is_enabled()

    def is_mail_smpt_domain_name_ip_active(self):
        return self.is_server_setting_active("#smtp_host")

    def is_mail_smpt_port_active(self):
        return self.is_server_setting_active("#smtp_port")

    def is_mail_username_active(self):
        return self.is_server_setting_active("#smtp_user")

    def is_mail_password_active(self):
        return self.is_server_setting_active("#smtp_pass")

    def is_mail_alert_email_address_active(self):
        return self.is_server_setting_active("#alert_email_address")

    """
    Dashboard Settings Active Directory
    """
    def click_active_directory_settings_button(self):
        self.wait_for_and_click_by_link_text("Active Directory")

    def get_active_directory_enable_state(self):
        return self.get_state_of_css_element("#ad_enabled_1")

    def click_active_directory_enable_yes(self):
        self.set_css_element_state("#ad_enabled_1", True)

    def click_active_directory_enable_no(self):
        self.set_css_element_state("#ad_enabled_0", True)

    def is_active_directory_account_suffix_active(self):
        return self.is_server_setting_active("#ad_account_suffix")

    def is_active_directory_base_dn_active(self):
        return self.is_server_setting_active("#ad_base_dn")

    def is_active_directory_domain_controller_active(self):
        return self.is_server_setting_active("#ad_domain_controllers")

    def is_active_directory_username_active(self):
        return self.is_server_setting_active("#ad_username")

    def is_active_directory_password_active(self):
        return self.is_server_setting_active("#ad_password")

    def is_active_directory_sync_schedule_never_active(self):
        return self.is_server_setting_active("#ad_schedule_0")

    def is_active_directory_sync_schedule_hourly_active(self):
        return self.is_server_setting_active("#ad_schedule_1")

    def is_active_directory_sync_schedule_daily_active(self):
        return self.is_server_setting_active("#ad_schedule_2")

    def is_active_directory_sync_schedule_weekly_active(self):
        return self.is_server_setting_active("#ad_schedule_3")

    def get_text_of_mail_settings(self):
        xpath = "//div[@id='tab_content_mail']/div/div"
        return self.get_element_text_by_xpath(xpath)

    def enter_active_directory_suffix(self):
        el = self.driver.find_element_by_css_selector("#ad_account_suffix")
        self.set_text_of_element(el, "@addertest0.local")

    def enter_active_directory_base_dn(self):
        el = self.driver.find_element_by_css_selector("#ad_base_dn")
        self.set_text_of_element(el, "dc=addertest0,dc=local")

    def enter_active_directory_domain(self):
        el = self.driver.find_element_by_css_selector("#ad_domain_controllers")
        self.set_text_of_element(el, "10.10.10.242")

    def enter_active_directory_username(self):
        el = self.driver.find_element_by_css_selector("#ad_username")
        self.set_text_of_element(el, "admin")

    def enter_active_directory_password(self):
        el = self.driver.find_element_by_css_selector("#ad_password")
        self.set_text_of_element(el, "4xytv9")
    """
    Dashboard Backups BasePage
    """
    def get_download_to_computer_current_setting(self):
        return self.get_state_of_css_element("#download_backup")

    def click_download_to_computer(self, set_to):
        locator = (By.ID, "download_backup")
        self.wait.until(EC.presence_of_element_located(locator))
        current = self.get_download_to_computer_current_setting()
        if set_to == True:
            if current != True:
                self.wait_for_and_click_by_css("#download_backup")
        elif set_to == False:
            if current == True:
                self.wait_for_and_click_by_css("#download_backup")

    def click_mail_settings_link(self):
        xpath = "//form[@id='backup']//a[contains(text(), 'Settings')]"
        self.wait_for_and_click_by_xpath(xpath)

    def select_backup_never(self):
        self.set_css_element_state("#backup_schedule_0", True)

    def select_backup_hourly(self):
        self.set_css_element_state("#backup_schedule_1", True)

    def select_backup_daily(self):
        self.set_css_element_state("#backup_schedule_2", True)

    def select_backup_weekly(self):
        self.set_css_element_state("#backup_schedule_3", True)

    def get_schedule_setting_state(self, option):
        if option == "never":
            return self.get_state_of_css_element("#backup_schedule_0")
        elif option == "hourly":
            return self.get_state_of_css_element("#backup_schedule_1")
        elif option == "daily":
            return self.get_state_of_css_element("#backup_schedule_2")
        elif option == "weekly":
            return self.get_state_of_css_element("#backup_schedule_3")

    def click_backup_now_button(self):
        self.wait_for_and_click_by_link_text("Backup now")

    def get_list_of_backups(self):
        return self.get_dropdown_option_texts("#selected_backup")

    def wait_for_backing_up_database_message_to_be_removed(self):
        locator = (By.ID, "backup_ajax_message")
        self.wait.until(EC.invisibility_of_element_located(locator))

    def select_backup_via_visible_text(self, text):
        self.select_dropdown_item_text("#selected_backup", text)

    def click_restore_backup(self):
        self.wait_for_and_click_by_link_text("Restore")

    def wait_for_restoring_backup_message_to_be_removed(self):
        wait = WebDriverWait(self.driver, 60)
        locator = By.ID, "restore_server_ajax_message"
        wait.until(EC.invisibility_of_element_located(locator))

    def delete_backup(self, file_name):
        self.driver.execute_script("confirm_delete_backup('%s')"
                                   % file_name)

    def wait_for_backup_deleted_message_to_be_removed(self):
        locator = (By.ID, "restore_server_ajax_message")
        self.wait.until(EC.invisibility_of_element_located(locator))

    def get_filename_from_element(self, selected):
        select = self.wait_for_select_element("#selected_backup")
        return select.first_selected_option.get_attribute("value")

    def get_list_of_archives(self):
        return self.get_dropdown_option_texts("#selected_archive")

    def select_archive_type_via_visible_text(self, text):
        self.select_dropdown_item_text("#log_type", text)

    def create_archive(self):
        self.driver.execute_script("archive_log()")

    def wait_for_archiving_message_to_be_removed(self):
        locator = By.ID, "archive_event_log_ajax_message"
        self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_archiving_message_to_confirm_data_saved(self):
        msgs = ["Archiving log data...", "Log data archived"]
        try:
            locator = (By.ID, "archive_event_log_ajax_message")
            self.wait.until(EC.text_to_be_present_in_element(locator, msgs[0]))
            self.wait.until(EC.text_to_be_present_in_element(locator, msgs[1]))
            return True
        except Exception:
            return False

    """
    Dashboard Updates Page
    """
    def select_aim_upgrade_file(self):
        f_path = os.path.abspath("../resources/upgrade_4.0.32179.tar.gz.asc")
        locator = By.CSS_SELECTOR, "#uploaded_aim_upgrade_file"
        el = self.wait.until(EC.presence_of_element_located(locator))
        el.send_keys(f_path)

    def select_aim_downgrade_file(self):
        f_path = os.path.abspath("../resources/upgrade_4.0.32179.tar.gz.asc")
        locator = By.CSS_SELECTOR, "#uploaded_aim_upgrade_file"
        el = self.wait.until(EC.presence_of_element_located(locator))
        el.send_keys(f_path)

    def wait_for_upload_process_to_finish(self):
        path = By.CSS_SELECTOR, "#upload_aim_upgrade_ajax_message"
        self.wait.until(EC.invisibility_of_element_located(path))
        while True:
            url = self.driver.current_url.replace("http://", "")
            if url.startswith("10.10.10.10"):
                break
            else:
                time.sleep(2)

    def click_upload(self):
        self.driver.execute_script("upload_aim_upgrade()")

    """
    Import Configuration
    """
    def click_import_configuration(self):
        self.wait_for_and_click_by_link_text("Import Configuration")

    def enter_tx_import_details(self):
        data = self.get_import_config_xls_data("txs")
        self.set_clipboard_contents(data)
        path = "form#import_config > textarea:nth-of-type(1)"
        locator = By.CSS_SELECTOR, path
        tx_entry = self.wait.until(EC.presence_of_element_located(locator))
        tx_entry.send_keys(Keys.CONTROL, "v")

    def enter_rx_import_details(self):
        data = self.get_import_config_xls_data("rxs")
        self.set_clipboard_contents(data)
        path = "form#import_config > textarea:nth-of-type(2)"
        locator = By.CSS_SELECTOR, path
        rx_entry = self.wait.until(EC.presence_of_element_located(locator))
        rx_entry.send_keys(Keys.CONTROL, "v")

    def enter_channel_import_details(self):
        data = self.get_import_config_xls_data("channels")
        self.set_clipboard_contents(data)
        path = "form#import_config > textarea:nth-of-type(3)"
        locator = By.CSS_SELECTOR, path
        c_entry = self.wait.until(EC.presence_of_element_located(locator))
        c_entry.send_keys(Keys.CONTROL, "v")

    def enter_user_import_details(self):
        data = self.get_import_config_xls_data("users")
        self.set_clipboard_contents(data)
        path = "form#import_config > textarea:nth-of-type(4)"
        locator = By.CSS_SELECTOR, path
        u_entry = self.wait.until(EC.presence_of_element_located(locator))
        u_entry.send_keys(Keys.CONTROL, "v")

    def get_import_config_xls_data(self, target_sheet):
        if parameter_singleton["local_only"]:
            f_path = os.path.abspath("../resources/import_configuration.xlsx")
        else:
            f_path = os.path.abspath("./resources/import_configuration.xlsx")
        if target_sheet == "users":
            target_index = 4
            end_point = 7
        elif target_sheet == "rxs":
            target_index = 2
            end_point = 11
        elif target_sheet == "txs":
            target_index = 1
            end_point = 12
        elif target_sheet == "channels":
            target_index = 3
            end_point = 13
        book = open_workbook(f_path)
        sheet = book.sheet_by_index(target_index)
        output = ""
        for counter in range(5, sheet.nrows):
            output += ("\t".join(sheet.row_values(counter, 2, end_point)) +
                       "\r\n")
        return output

    def set_clipboard_contents(self, data):
        WCB.OpenClipboard()
        WCB.EmptyClipboard()
        WCB.SetClipboardText(data)

    def click_submit(self):
        self.wait_for_and_click_by_css("form#import_config > input")

    """
    Transmitter Page BasePage
    """
    def get_transmitters_link_element(self):
        if self.get_element_located_by_link_text("TRANSMITTERS"):
            return self.driver.find_element_by_link_text("TRANSMITTERS")

    def open_transmitters_tab(self):
        self.wait_for_and_click_by_link_text("TRANSMITTERS")

    def get_locals_link_element(self):
        if self.get_element_located_by_link_text("LOCALS"):
            return self.driver.find_element_by_link_text("LOCALS")

    def open_locals_tab(self):
        self.wait_for_and_click_by_link_text("LOCALS")

    def get_text_of_view_transmitters_link(self):
        xpath = "//div[@id='transmitters_links']/ul/li[1]/a"
        return self.get_element_text_by_xpath(xpath)

    def get_text_of_update_firmware_link(self):
        xpath = "//div[@id='transmitters_links']/ul/li[2]/a"
        return self.get_element_text_by_xpath(xpath)

    def get_list_of_transmitters(self):
        return self.get_list("transmitters")

    def get_cell_elements(self, element):
        return element.find_elements_by_tag_name("td")

    def get_row_id_of_transmitter(self, element):
        return self.get_attribute_of_element(element, "id")

    def get_transmitter_name(self, element):
        return self.get_element_comp_text_by_xpath(element, "./td[2]")

    def get_transmitter_ip(self, element):
        ip = self.get_element_comp_text_by_xpath(element, "./td[3]")
        if len(ip) > 11:
            ip = ip[0:11]
        return ip

    def get_transmitter_description(self, element):
        return self.get_element_comp_text_by_xpath(element, "./td[8]")

    def get_transmitter_location(self, element):
        return self.get_element_comp_text_by_xpath(element, "./td[9]")

    def get_transmitter_linktext(self, element):
        tx_cell = element.find_element_by_xpath("./td[10]/span[1]/a")
        return self.get_attribute_of_element(tx_cell, "href")

    def get_tx_status_img_src(self, element):
        tx_cell = element.find_element_by_xpath("./td[1]")
        return self.check_online_status_image_src(tx_cell)

    def click_transmitter_configure(self, element):
        element.find_element_by_xpath("./td[10]/span[1]/a").click()

    def click_transmitter_delete(self, element):
        element.find_element_by_xpath("./td[10]/a").click()

    def click_transmitter_reboot(self, element):
        element.find_element_by_xpath("./td[10]/span[2]/a").click()

    def click_transmitter_identify(self, element):
        element.find_element_by_xpath("./td[10]/span[3]/a[1]").click()

    def get_device_type(self, element):
        return self.get_text_of_element(element)

    def check_for_span_type_tooltip(self, element):
        return self.get_attribute_of_cell_by_xpath(element, "./span", "class")

    def get_element_class_attribute(self, element):
        return self.get_attribute_of_element(element, "class")

    def get_class_attribute_of_link(self, element):
        return self.get_attribute_of_cell_by_xpath(element, "./a", "class")

    def get_device_type_image_src(self, element):
        return self.get_attribute_of_cell_by_xpath(element,
                                                   "./span[1]/img",
                                                   "src")

    def check_online_status_image_src(self, element):
        time.sleep(5)
        return self.get_attribute_of_cell_by_xpath(element,
                                                   "./span[2]/img",
                                                   "src")

    def get_form_edit_image_src(self, element):
        return self.get_attribute_of_cell_by_xpath(element,
                                                   "./img",
                                                   "src")

    def get_config_device_img_src(self, element):
        return self.get_attribute_of_cell_by_xpath(element,
                                                   "./span[1]/a/img",
                                                   "src")

    def get_refresh_arrow_image_src(self, element):
        return self.get_attribute_of_cell_by_xpath(element,
                                                   "./span[2]/a/img",
                                                   "src")

    def get_identify_image_src(self, element):
        return self.get_attribute_of_cell_by_xpath(element,
                                                   "./span[3]/a/img",
                                                   "src")

    def get_delete_image_src(self, element):
        return self.get_attribute_of_cell_by_xpath(element,
                                                   "./a/img",
                                                   "src")

    def get_connect_device_src(self, element):
        return self.get_attribute_of_cell_by_xpath(element,
                                                   "./span[4]/a/img",
                                                   "src")

    def get_device_version_via_api(self):
        device_info = {}
        for device in self.get_devices_from_api(self.get_api_token()):
            d_id = device.find("d_id").text
            d_version = device.find("d_version").text
            device_info[d_id] = d_version
        return device_info

    def get_api_token(self):
        r = self.get_api_response({"v": "2",
                                   "method": "login",
                                   "username": "admin",
                                   "password": "password"})
        data = self.get_parsed_api_response(r.content)
        return data.find("token").text

    def get_devices_from_api(self, token):
        r = self.get_api_response({"v": "2",
                                   "token": token,
                                   "method": "get_devices",
                                   "show_all": "1"})
        data = self.get_parsed_api_response(r.content)
        return data.findall(".//device")

    def get_api_response(self, payload):
        r = requests.get("http://%s/api" % self.baseip, params=payload)
        return r

    def get_parsed_api_response(self, content):
        return ElementTree.fromstring(content)

    def get_device_id_from_row_id(self, row_id):
        row_id = row_id.replace("row_id_", "")
        return row_id

    def open_update_transmitter_firmware_page(self):
        steps = ["Update Firmware"]
        action = ActionChains(self.driver)
        (action.move_to_element(self.get_transmitters_link_element())
        .move_to_element(self.driver.find_element_by_link_text(steps[0]))
        .click()
        .perform())

    def open_update_local_firmware_page(self):
        steps = ["#transmitters_links > ul > li:nth-child(1) > a"]
        action = ActionChains(self.driver)
        (action.move_to_element(self.get_locals_link_element())
        .move_by_offset(0, 19)
        .move_to_element(self.driver.find_element_by_css_selector(steps[0]))
        .click()
        .perform())

    def open_view_transmitters_page(self):
        steps = ["#transmitters_links > ul > li:nth-child(2) > a",
                 "#transmitters_links > ul > li:nth-child(1) > a"]
        action = ActionChains(self.driver)
        (action.move_to_element(self.get_transmitters_link_element())
         .move_to_element(self.driver.find_element_by_css_selector(steps[0]))
         .move_to_element(self.driver.find_element_by_css_selector(steps[1]))
         .click()
         .perform())

    def open_view_locals_page(self):
        steps = ["#transmitters_links > ul > li:nth-child(2) > a",
                 "#transmitters_links > ul > li:nth-child(1) > a"]
        action = ActionChains(self.driver)
        (action.move_to_element(self.get_transmitters_link_element())
         .move_by_offset(0, 19)
         .move_to_element(self.driver.find_element_by_css_selector(steps[0]))
         .move_to_element(self.driver.find_element_by_css_selector(steps[1]))
         .click()
         .perform())

    def get_located_name_search_field(self):
        return self.get_element_located_by_id("filter_d_name")

    def send_filter_term_to_element(self, id_, term):
        self.enter_text_into_input_field(id_, term)

    def send_search_term_tx_name_field(self, term):
        self.send_filter_term_to_element("filter_d_name", term)

    def send_search_term_tx_description_field(self, term):
        self.send_filter_term_to_element("filter_d_description", term)

    def send_search_term_tx_location_field(self, term):
        self.send_filter_term_to_element("filter_d_location", term)

    def clear_filter_of_element(self, id_):
        if self.get_element_located_by_id(id_):
            self.driver.find_element_by_id(id_).clear()

    def clear_transmitter_names_filter(self):
        self.clear_filter_of_element("filter_d_name")

    def clear_transmitter_descriptions_filter(self):
        self.clear_filter_of_element("filter_d_description")

    def clear_transmitter_locations_filter(self):
        self.clear_filter_of_element("filter_d_location")

    def click_on_filter(self, id_):
        if self.get_element_located_by_id(id_):
            self.driver.find_element_by_id(id_).click()

    def click_on_filter_transmitters_by_name(self):
        self.click_on_filter("filter_d_name_icon")

    def click_on_filter_transmitters_by_description(self):
        self.click_on_filter("filter_d_description_icon")

    def click_on_filter_transmitters_by_location(self):
        self.click_on_filter("filter_d_location_icon")

    def click_on_remove_transmitters_name_filter(self):
        self.click_on_filter("remove_filter_d_name_icon")

    def click_on_remove_transmitters_description_filter(self):
        self.click_on_filter("remove_filter_d_description_icon")

    def click_on_remove_transmitters_location_filter(self):
        self.click_on_filter("remove_filter_d_location_icon")

    def click_on_remove_filters(self):
        self.wait_for_and_click_by_link_text("Remove Filters")

    def click_on_ascend_transmitter_names(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[2]/a[1]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_on_decend_transmitter_names(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[2]/a[2]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_on_ascend_transmitter_descriptions(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[8]/a[1]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_on_decend_transmitter_descriptions(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[8]/a[2]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_on_ascend_transmitter_locations(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[9]/a[1]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_on_decend_transmitter_locations(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[9]/a[2]"
        self.wait_for_and_click_by_xpath(xpath)

    def wait_for_and_click_reboot_confirm(self):
        wait = WebDriverWait(self.driver, 120)
        locator = By.LINK_TEXT, "Reboot"
        wait.until(EC.visibility_of_element_located(locator)).click()

    def wait_for_and_click_reset_confirm(self):
        wait = WebDriverWait(self.driver, 120)
        locator = By.LINK_TEXT, "Factory Reset"
        wait.until(EC.visibility_of_element_located(locator)).click()

    def wait_for_and_click_reboot_cancel(self):
        wait = WebDriverWait(self.driver, 120)
        locator = By.LINK_TEXT, "Cancel"
        wait.until(EC.visibility_of_element_located(locator)).click()

    def wait_for_rebooting_message_to_be_removed(self):
        wait = WebDriverWait(self.driver, 120)
        locator = By.XPATH, "//span[@id='warnings']/span/a"
        wait.until(EC.invisibility_of_element_located(locator))

    def get_located_search_by_name(self):
        return self.get_element_located_by_id("filter_d_name")

    def get_located_search_by_description(self):
        return self.get_element_located_by_id("filter_d_description")

    def get_located_search_by_location(self):
        return self.get_element_located_by_id("filter_d_location")

    """
    Transmitter Configure BasePage
    """
    def get_device_id_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            xpath = ("//div[contains(text(), 'Device ID')]" +
                     "/following-sibling::div")
            return self.get_element_text_by_xpath(xpath)

    def get_online_img_src_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            xpath = ("//div[contains(text(), 'Online?')]" +
                     "/following-sibling::div/span/img")
            return self.get_attribute_via_xpath(xpath, "src")

    def get_date_added_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            xpath = ("//div[contains(text(), 'Date Added')]" +
                     "/following-sibling::div")
            return self.get_element_text_by_xpath(xpath)

    def get_mac_address_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            xpath = ("//div[contains(text(), 'MAC Address')]" +
                     "/following-sibling::div")
            return self.get_element_text_by_xpath(xpath)

    def get_main_firmware_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            xpath = ("//div[contains(text(), 'Main Firmware')]" +
                     "/following-sibling::div")
            return self.get_element_text_by_xpath(xpath)

    def get_backup_firmware_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            xpath = ("//div[contains(text(), 'Backup Firmware')]" +
                     "/following-sibling::div")
            return self.get_element_text_by_xpath(xpath)

    def get_ip_address_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            xpath = ("//div[contains(text(), 'IP Address')]" +
                     "/following-sibling::div/input")
            return self.get_attribute_via_xpath(xpath, "value")

    def get_ip_help_text_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            xpath = ("//div[contains(text(), 'IP Address')]" +
                     "/following-sibling::div[3]")
            return self.get_element_text_by_xpath(xpath)

    def set_state_dummy_keyboard_no(self, state):
        self.set_css_element_state("#tp_fk_enable_0", state)

    def set_state_dummy_keyboard_yes(self, state):
        self.set_css_element_state("#tp_fk_enable_1", state)

    def set_state_dummy_keyboard_global(self, state):
        self.set_css_element_state("#tp_fk_enable_-1", state)

    def get_state_dummy_keyboard(self, option):
        global_ = "#tp_fk_enable_-1"
        no = "#tp_fk_enable_0"
        yes = "#tp_fk_enable_1"
        if option == "global":
            return self.get_state_of_css_element(global_)
        elif option == "no":
            return self.get_state_of_css_element(no)
        elif option == "yes":
            return self.get_state_of_css_element(yes)

    def get_dummy_keyboard_help_text_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            xpath = ("//div[contains(text(), 'Enable Dummy Boot Keyboard')]" +
                     "/following-sibling::div[3]")
            return self.get_element_text_by_xpath(xpath)

    def set_state_usb_speed_global(self, state):
        self.set_css_element_state("#tp_usb_speed_-1", state)

    def set_state_usb_speed_hi_speed(self, state):
        self.set_css_element_state("#tp_usb_speed_0", state)

    def set_state_usb_speed_full_speed(self, state):
        self.set_css_element_state("#tp_usb_speed_1", state)

    def get_state_usb_speed(self, option):
        global_ = "#tp_usb_speed_-1"
        hi_speed = "#tp_usb_speed_0"
        full_speed = "#tp_usb_speed_1"
        if option == "global":
            return self.get_state_of_css_element(global_)
        elif option == "hi_speed":
            return self.get_state_of_css_element(hi_speed)
        elif option == "full_speed":
            return self.get_state_of_css_element(full_speed)

    def get_usb_speed_help_text_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            xpath = ("//div[contains(text(), 'USB Speed')]" +
                     "/following-sibling::div[3]")
            return self.get_element_text_by_xpath(xpath)

    def set_state_usb_hub_size_global(self, state):
        self.set_css_element_state("#tp_usb_hub_size_-1", state)

    def set_state_usb_hub_size_13(self, state):
        self.set_css_element_state("#tp_usb_hub_size_13", state)

    def set_state_usb_hub_size_7(self, state):
        self.set_css_element_state("#tp_usb_hub_size_7", state)

    def get_state_hub_size(self, option):
        global_ = "#tp_usb_hub_size_-1"
        size_13 = "#tp_usb_hub_size_13"
        size_7 = "#tp_usb_hub_size_7"
        if option == "global":
            return self.get_state_of_css_element(global_)
        elif option == "13":
            return self.get_state_of_css_element(size_13)
        elif option == "7":
            return self.get_state_of_css_element(size_7)

    def get_usb_hub_help_text_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            xpath = ("//div[contains(text(), 'USB Hub Size')]" +
                     "/following-sibling::div[3]")
            return self.get_element_text_by_xpath(xpath)

    def get_bandwidth_limit_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            xpath = ("//div[contains(text(), 'Peak Bandwidth Limiter')]" +
                     "/following-sibling::div/div[2]")
            return self.get_element_text_by_xpath(xpath)

    def get_selected_magic_eye_setting(self):
        return self.get_selected_text_select_element("#tp_magic_eye")

    def get_selected_magic_eye_value_setting(self):
        return self.get_selected_value_select_element("#tp_magic_eye")

    def get_magic_eye_options(self):
        return self.get_dropdown_option_texts("#tp_magic_eye")

    def set_magic_eye_option(self, option):
        self.select_dropdown_item_text("#tp_magic_eye", option)

    def get_selected_ddc_setting(self):
        return self.get_selected_text_select_element("#tp_ddc")

    def get_selected_ddc_value_setting(self):
        return self.get_selected_value_select_element("#tp_ddc")

    def get_ddc_options(self):
        return self.get_dropdown_option_texts("#tp_ddc")

    def set_ddc_option(self, ddc):
        self.select_dropdown_item_text("#tp_ddc", ddc)

    def get_ddc_help_text_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            xpath = ("//div[contains(text(), 'DDC')]" +
                     "/following-sibling::div[3]")
            return self.get_element_text_by_xpath(xpath)

    def set_state_edid_optimisation_global(self, state):
        self.set_css_element_state("#tp_video_ddc_optimisation_-1", state)

    def set_state_edid_optimisation_no(self, state):
        self.set_css_element_state("#tp_video_ddc_optimisation_1", state)

    def set_state_edid_optimisation_yes(self, state):
        self.set_css_element_state("#tp_video_ddc_optimisation_0", state)

    def get_state_edid_optimisation(self, option):
        global_ = "#tp_video_ddc_optimisation_-1"
        no = "#tp_video_ddc_optimisation_1"
        yes = "#tp_video_ddc_optimisation_0"
        if option == "global":
            return self.get_state_of_css_element(global_)
        elif option == "no":
            return self.get_state_of_css_element(no)
        elif option == "yes":
            return self.get_state_of_css_element(yes)

    def get_selected_hot_plug_detect_setting(self):
        return self.get_selected_text_select_element("#tp_hpd")

    def get_selected_hot_plug_detect_value(self):
        return self.get_selected_value_select_element("#tp_hpd")

    def get_hot_plug_detect_options(self):
        return self.get_dropdown_option_texts("#tp_hpd")

    def set_hot_plug_detect_option(self, plug):
        self.select_dropdown_item_text("#tp_hpd", plug)

    def get_hot_plug_dectect_help_text_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            xpath = ("//div[contains(text(), 'Hot Plug Detect Control')]" +
                     "/following-sibling::div[3]")
            return self.get_element_text_by_xpath(xpath)

    def get_selected_hot_plug_period(self):
        return self.get_selected_text_select_element("#tp_video_ddc_delay")

    def get_selected_hot_plug_period_value(self):
        return self.get_selected_value_select_element("#tp_video_ddc_delay")

    def get_hot_plug_period_options(self):
        return self.get_dropdown_option_texts("#tp_video_ddc_delay")

    def set_hot_plug_period_option(self, period):
        self.select_dropdown_item_text("#tp_video_ddc_delay", period)

    def get_hot_plug_signal_help_text_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            xpath = ("//div[contains(text(), " +
                     "'Hot Plug Detect Signal Period')]" +
                     "/following-sibling::div[3]")
            return self.get_element_text_by_xpath(xpath)

    def get_selected_bkground_refresh_period(self):
        return self.get_selected_text_select_element("#tp_video_br")

    def get_selected_bkground_refresh_period_value(self):
        return self.get_selected_value_select_element("#tp_video_br")

    def get_background_refresh_period_options(self):
        return self.get_dropdown_option_texts("#tp_video_br")

    def set_background_refresh_period_option(self, period):
        self.select_dropdown_item_text("#tp_video_br", period)

    def get_frame_skipping_label_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            xpath = ("//div[contains(text(), 'Frame Skipping')]" +
                     "/following-sibling::div/div[2]")
            return self.get_element_text_by_xpath(xpath)

    def get_selected_compression_setting(self):
        path = "#tp_video_compression_combo"
        return self.get_selected_text_select_element(path)

    def get_compression_options(self):
        return self.get_dropdown_option_texts("#tp_video_compression_combo")

    def set_compression_option(self, option):
        self.select_dropdown_item_text("#tp_video_compression_combo", option)

    def set_compression_minimum(self, option):
        self.select_dropdown_item_text("#tp_video_compression_min", option)

    def set_compression_maxiumum(self, option):
        self.select_dropdown_item_text("#tp_video_compression_min", option)

    def get_selected_serial_parity(self):
        return self.get_selected_text_select_element("#tp_serial_parity")

    def get_selected_serial_parity_value(self):
        return self.get_selected_value_select_element("#tp_serial_parity")

    def get_serial_parity_options(self):
        return self.get_dropdown_option_texts("#tp_serial_parity")

    def set_serial_parity_option(self, option):
        self.select_dropdown_item_text("#tp_serial_parity", option)

    def get_selected_serial_data_bit(self):
        return self.get_selected_text_select_element("#tp_serial_data_bits")

    def get_selected_serial_data_bit_value(self):
        return self.get_selected_value_select_element("#tp_serial_data_bits")

    def get_serial_data_bit_options(self):
        return self.get_dropdown_option_texts("#tp_serial_data_bits")

    def set_serial_data_bit_option(self, option):
        self.select_dropdown_item_text("#tp_serial_data_bits", option)

    def get_selected_serial_data_stop(self):
        return self.get_selected_text_select_element("#tp_serial_stop_bits")

    def get_selected_serial_data_stop_value(self):
        return self.get_selected_value_select_element("#tp_serial_stop_bits")

    def get_serial_data_stop_options(self):
        return self.get_dropdown_option_texts("#tp_serial_stop_bits")

    def set_serial_data_stop_option(self, option):
        self.select_dropdown_item_text("#tp_serial_stop_bits", option)

    def get_selected_serial_speed(self):
        return self.get_selected_text_select_element("#tp_serial_speed")

    def get_selected_serial_speed_value(self):
        return self.get_selected_value_select_element("#tp_serial_speed")

    def get_serial_speed_options(self):
        return self.get_dropdown_option_texts("#tp_serial_speed")

    def set_serial_speed_option(self, option):
        self.select_dropdown_item_text("#tp_serial_speed", option)

    def set_transmitter_ip_via_config_page(self, new_ip):
        if self.get_element_located_by_id("configure_device"):
            self.enter_text_into_input_field("d_ip_address", new_ip)

    def get_transmitter_name_from_config_page(self):
        if self.get_element_located_by_id("d_name"):
            tx_name = self.driver.find_element_by_id("d_name")
            return self.get_attribute_of_element(tx_name, "value")

    def set_transmitter_name_via_config_page(self, text):
        if self.get_element_located_by_id("d_name"):
            self.enter_text_into_input_field("d_name", text)

    def get_transmitter_desc_from_config_page(self):
        if self.get_element_located_by_id("d_description"):
            tx_desc = self.driver.find_element_by_id("d_description")
            return self.get_attribute_of_element(tx_desc, "value")

    def set_transmitter_desc_via_config_page(self, text):
        if self.get_element_located_by_id("d_description"):
            self.enter_text_into_input_field("d_description", text)

    def get_transmitter_loc_from_config_page(self):
        if self.get_element_located_by_id("d_location"):
            tx_loc = self.driver.find_element_by_id("d_location")
            return self.get_attribute_of_element(tx_loc, "value")

    def set_transmitter_location_via_config_page(self, text):
        if self.get_element_located_by_id("d_location"):
            self.enter_text_into_input_field("d_location", text)

    def get_lightbox_title_text(self):
        xpath = ("//div[@id='ibox']" +
                 "//div[@id='ibox_wrapper']" +
                 "//div[@class='lightbox_title']")
        return self.get_element_text_by_xpath(xpath)

    def click_lightbox_ok_button(self):
        if self.get_element_located_by_id("ibox"):
            self.wait_for_and_click_by_link_text("OK")

    """
    Channels Page BasePage
    """
    def get_channels_link_element(self):
        if self.get_element_located_by_link_text("CHANNELS"):
            return self.driver.find_element_by_link_text("CHANNELS")

    def open_channels_tab(self):
        self.wait_for_and_click_by_link_text("CHANNELS")

    def get_text_of_view_channel_link(self):
        xpath = "//div[@id='channels_links']/ul/li[1]/a"
        return self.get_element_text_by_xpath(xpath)

    def get_text_of_add_channel_link_link(self):
        xpath = "//div[@id='channels_links']/ul/li[2]/a"
        return self.get_element_text_by_xpath(xpath)

    def get_text_of_view_channel_group_link(self):
        xpath = "//div[@id='channels_links']/ul/li[3]/a"
        return self.get_element_text_by_xpath(xpath)

    def get_text_of_add_channel_group_link(self):
        xpath = "//div[@id='channels_links']/ul/li[4]/a"
        return self.get_element_text_by_xpath(xpath)

    def click_view_channels_subtab_link(self):
        steps = ["#channels_links > ul > li:nth-child(2) > a",
                 "#channels_links > ul > li:nth-child(1) > a"]
        action = ActionChains(self.driver)
        (action.move_to_element(self.get_channels_link_element())
        .move_to_element(self.driver.find_element_by_css_selector(steps[0]))
        .move_to_element(self.driver.find_element_by_css_selector(steps[1]))
        .click()
        .perform())

    def click_add_channel_subtab_link(self):
        steps = ["#channels_links > ul > li:nth-child(2) > a"]
        action = ActionChains(self.driver)
        (action.move_to_element(self.get_channels_link_element())
        .move_to_element(self.driver.find_element_by_css_selector(steps[0]))
        .click()
        .perform())

    def click_view_channel_groups_subtab_link(self):
        steps = ["#channels_links > ul > li:nth-child(2) > a",
                 "#channels_links > ul > li:nth-child(3) > a"]
        action = ActionChains(self.driver)
        (action.move_to_element(self.get_channels_link_element())
        .move_to_element(self.driver.find_element_by_css_selector(steps[0]))
        .move_to_element(self.driver.find_element_by_css_selector(steps[1]))
        .click()
        .perform())

    def click_add_channel_group_subtab_link(self):
        steps = ["#channels_links > ul > li:nth-child(2) > a",
                 "#channels_links > ul > li:nth-child(4) > a"]
        action = ActionChains(self.driver)
        (action.move_to_element(self.get_channels_link_element())
        .move_to_element(self.driver.find_element_by_css_selector(steps[0]))
        .move_to_element(self.driver.find_element_by_css_selector(steps[1]))
        .click()
        .perform())

    def click_batch_delete_mode(self):
        self.wait_for_and_click_by_css("#toggle_batch_delete_button")

    def verify_batch_delete_checkbox(self):
        return self.get_element_located_by_id("toggle_delete_checkbox")

    def verify_batch_delete_channel(self, element):
        return element.find_element_by_xpath("./td[8]/input").is_displayed()

    def click_batch_delete_channel(self, element):
        element.find_element_by_xpath("./td[8]/input").click()

    def verify_batch_delete_channel_group(self, element):
        return element.find_element_by_xpath("./td[5]/input").is_displayed()

    def click_batch_delete_for_channel_group(self, element):
        element.find_element_by_xpath("./td[5]/input").click()

    def click_batch_delete_channels(self):
        self.wait_for_and_click_by_link_text("Delete selected channels")

    def click_batch_delete_channel_groups(self):
        self.wait_for_and_click_by_link_text("Delete selected channel groups")

    def click_add_channel_button(self):
        self.wait_for_and_click_by_link_text("Add Channel")

    def click_view_channel_group_button(self):
        self.wait_for_and_click_by_link_text("View Channel Groups")

    def click_add_channel_group_button(self):
        self.wait_for_and_click_by_link_text("Add Channel Group")

    def get_list_of_channels(self):
        return self.get_list("channels")

    def get_list_of_channel_groups(self):
        return self.get_list("channel_groups")

    def get_channel_name(self, element):
        return self.get_element_comp_text_by_xpath(element, "./td[1]")

    def get_channel_group_name(self, element):
        return self.get_element_comp_text_by_xpath(element, "./td[1]")

    def get_channel_desc(self, element):
        return self.get_element_comp_text_by_xpath(element, "./td[6]")

    def get_channel_group_desc(self, element):
        return self.get_element_comp_text_by_xpath(element, "./td[2]")

    def get_channel_loc(self, element):
        return self.get_element_comp_text_by_xpath(element, "./td[7]")

    def get_channel_connection_img_src(self, element):
        sources = [self.get_attribute_of_element(image, "src")
                   for image in element.find_elements_by_xpath("./td[2]/img")]
        return sources

    def get_channel_conx_default_img_src(self, element):
        return self.get_attribute_of_cell_by_xpath(element,
                                                   "./img",
                                                   "src")

    def get_configure_channel_img_src(self, element):
        return self.get_attribute_of_cell_by_xpath(element,
                                                   "./a[1]/img",
                                                   "src")

    def get_clone_channel_img_src(self, element):
        return self.get_attribute_of_cell_by_xpath(element,
                                                   "./a[2]/img",
                                                   "src")

    def get_delete_channel_img_src(self, element):
        return self.get_attribute_of_cell_by_xpath(element,
                                                   "./a[3]/img",
                                                   "src")

    def get_located_search_by_channel_name(self):
        return self.get_element_located_by_id("filter_c_name")

    def get_located_search_by_channel_description(self):
        return self.get_element_located_by_id("filter_c_description")

    def get_located_search_by_channel_location(self):
        return self.get_element_located_by_id("filter_c_location")

    def get_located_search_by_username(self):
        return self.get_element_located_by_id("filter_username")

    def get_located_search_by_firstname(self):
        return self.get_element_located_by_id("filter_firstname")

    def get_located_search_by_lastname(self):
        return self.get_element_located_by_id("filter_lastname")

    def send_search_term_to_channel_name(self, term):
        self.send_filter_term_to_element("filter_c_name", term)

    def send_search_to_c_group_name_field(self, term):
        self.send_filter_term_to_element("filter_cg_name", term)

    def send_search_term_to_channel_desc(self, term):
        self.send_filter_term_to_element("filter_c_description", term)

    def send_search_to_c_group_desc_field(self, term):
        self.send_filter_term_to_element("filter_cg_description", term)

    def send_search_term_to_channel_loc(self, term):
        self.send_filter_term_to_element("filter_c_location", term)

    def click_on_filter_channels_by_name(self):
        self.click_on_filter("filter_c_name_icon")

    def click_on_filter_channel_groups_by_name(self):
        self.click_on_filter("filter_cg_name_icon")

    def click_on_filter_channels_by_description(self):
        self.click_on_filter("filter_c_description_icon")

    def click_on_filter_channel_groups_by_description(self):
        self.click_on_filter("filter_cg_description_icon")

    def click_on_filter_channels_by_location(self):
        self.click_on_filter("filter_c_location_icon")

    def click_on_remove_channels_name_filter(self):
        self.click_on_filter("remove_filter_c_name_icon")

    def click_on_remove_channel_groups_name_filter(self):
        self.click_on_filter("remove_filter_cg_name_icon")

    def click_on_remove_channels_description_filter(self):
        self.click_on_filter("remove_filter_c_description_icon")

    def click_on_remove_channel_groups_description_filter(self):
        self.click_on_filter("remove_filter_cg_description_icon")

    def click_on_remove_channels_location_filter(self):
        self.click_on_filter("remove_filter_c_location_icon")

    def clear_channel_names_filter(self):
        self.clear_filter_of_element("filter_c_name")

    def clear_channel_group_names_filter(self):
        self.clear_filter_of_element("filter_cg_name")

    def clear_channel_descriptions_filter(self):
        self.clear_filter_of_element("filter_c_description")

    def clear_channel_group_descriptions_filter(self):
        self.clear_filter_of_element("filter_cg_description")

    def clear_channel_locations_filter(self):
        self.clear_filter_of_element("filter_c_location")

    def click_on_ascend_channel_names(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[1]/a[1]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_on_decend_channel_names(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[1]/a[2]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_on_ascend_channel_group_names(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[1]/a[1]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_on_decend_channel_group_names(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[1]/a[2]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_on_ascend_channel_descriptions(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[6]/a[1]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_on_decend_channel_descriptions(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[6]/a[2]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_on_ascend_channel_group_descriptions(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[2]/a[1]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_on_decend_channel_group_descriptions(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[2]/a[2]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_on_ascend_channel_locations(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[7]/a[1]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_on_decend_channel_locations(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[7]/a[2]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_configure_channel(self, element):
        element.find_element_by_xpath("./td[8]/a[1]").click()

    def click_configure_channel_group(self, element):
        element.find_element_by_xpath("./td[5]/a[1]").click()

    def get_channel_config_linktext(self, element):
        channel_cell = element.find_element_by_xpath("./td[8]/a[1]")
        return self.get_attribute_of_element(channel_cell, "href")

    def get_channel_group_config_linktext(self, element):
        channel_cell = element.find_element_by_xpath("./td[5]/a[1]")
        return self.get_attribute_of_element(channel_cell, "href")

    def get_channel_clone_linktext(self, element):
        channel_cell = element.find_element_by_xpath("./td[8]/a[2]")
        return self.get_attribute_of_element(channel_cell, "href")

    def get_channel_group_clone_linktext(self, element):
        channel_cell = element.find_element_by_xpath("./td[5]/a[2]")
        return self.get_attribute_of_element(channel_cell, "href")

    def click_channel_delete(self, element):
        element.find_element_by_xpath("./td[8]/a[3]").click()

    def click_channel_group_delete(self, element):
        element.find_element_by_xpath("./td[5]/a[3]").click()

    def click_channel_clone(self, element):
        element.find_element_by_xpath("./td[8]/a[2]").click()

    def click_channel_group_clone(self, element):
        element.find_element_by_xpath("./td[5]/a[2]").click()

    def click_connect_receiver_to_channel_view_only(self, element):
        element.find_element_by_xpath("./td[4]/a[1]").click()

    def click_on_connect_receiver_to_channel_shared_access(self, element):
        element.find_element_by_xpath("./td[4]/a[2]").click()

    def click_on_connect_receiver_to_channel_exclusive_only(self, element):
        element.find_element_by_xpath("./td[4]/a[3]").click()

    def get_delete_chnl_txt_from_lightbox(self):
        return self.get_lightbox_title_text()

    def get_delete_chnl_grp_txt_from_lightbox(self):
        return self.get_lightbox_title_text()

    def click_lightbox_reboot_button(self):
        if self.get_element_located_by_id("ibox"):
            self.wait_for_and_click_by_link_text("Reboot")

    def click_lightbox_cancel_button(self):
        if self.get_element_located_by_id("ibox"):
            self.wait_for_and_click_by_link_text("Cancel")

    def click_lightbox_delete_button(self):
        if self.get_element_located_by_id("ibox"):
            self.wait_for_and_click_by_link_text("Delete")
            found = True
            while(found == True):
                if self.check_lightbox_visibility() == False:
                    found = False

    def click_lightbox_disconnect_button(self):
#         Had to use direct URL as clicking button via
#         webdriver would not disconnect
        disconnect = ("/admin/process_disconnect_all.php?" +
                      "r=%2Fadmin%2Fdevices.php%3Ft%3Drx")
        if self.get_element_located_by_id("ibox"):
            self.driver.get(self.baseurl + disconnect)

    def open_restart_url(self):
#         Had to use direct URL as clicking button via
#         webdriver would not start restart procedure
        restart = "/admin/process_power.php?mode=restart"
        if self.get_element_located_by_id("ibox"):
            self.driver.get(self.baseurl + restart)

    def check_lightbox_visibility(self):
        time.sleep(1)
        return self.get_element_located_by_id("ibox_overlay")

    """
    Configure Channel BasePage
    """
    def get_channel_name_from_config_page(self):
        if self.get_element_located_by_id("c_name"):
            channel_name = self.driver.find_element_by_id("c_name")
            return self.get_attribute_of_element(channel_name, "value")

    def set_channel_name_via_config_page(self, text):
        if self.get_element_located_by_id("c_name"):
            self.enter_text_into_input_field("c_name", text)

    def get_channel_group_name_from_config_page(self):
        if self.get_element_located_by_id("cg_name"):
            channel_grp_name = self.driver.find_element_by_id("cg_name")
            return self.get_attribute_of_element(channel_grp_name, "value")

    def set_channel_group_name_via_config_page(self, text):
        if self.get_element_located_by_id("cg_name"):
            self.enter_text_into_input_field("cg_name", text)

    def get_channel_description_from_config_page(self):
        if self.get_element_located_by_id("c_description"):
            channel_desc = self.driver.find_element_by_id("c_description")
            return self.get_attribute_of_element(channel_desc, "value")

    def set_channel_description_via_config_page(self, text):
        if self.get_element_located_by_id("c_description"):
            self.enter_text_into_input_field("c_description", text)

    def get_channel_group_description_from_config_page(self):
        if self.get_element_located_by_id("cg_description"):
            channel_grp_desc = self.driver.find_element_by_id("cg_description")
            return self.get_attribute_of_element(channel_grp_desc, "value")

    def set_channel_group_desc_via_config_page(self, text):
        if self.get_element_located_by_id("cg_description"):
            self.enter_text_into_input_field("cg_description", text)

    def get_channel_location_from_config_page(self):
        if self.get_element_located_by_id("c_location"):
            channel_loc = self.driver.find_element_by_id("c_location")
            return self.get_attribute_of_element(channel_loc, "value")

    def set_channel_location_via_config_page(self, text):
        if self.get_element_located_by_id("c_location"):
            self.enter_text_into_input_field("c_location", text)

    def get_different_video_source(self, current):
        sources = self.get_dropdown_option_texts("#video_e_id")
        sources.remove("- OFF -")
        for source in sources:
            if source != current:
                return source

    def get_selected_video_source(self):
        return self.get_selected_text_select_element("#video_e_id")

    def set_channel_video_source(self, text):
        self.select_dropdown_item_text("#video_e_id", text)

    def reset_channel_video_source(self, text):
        self.set_channel_video_source(text)

    def get_different_video2_source(self, current):
        sources = self.get_video2_source_options()
        sources.remove("- OFF -")
        for source in sources:
            if source != current:
                return source

    def get_selected_video2_source(self):
        return self.get_selected_text_select_element("#video1_e_id")

    def get_video2_source_options(self):
        return self.get_dropdown_option_texts("#video1_e_id")

    def set_channel_video2_source(self, text):
        self.select_dropdown_item_text("#video1_e_id", text)

    def reset_channel_video2_source(self, text):
        self.set_channel_video2_source(text)

    def get_selected_audio_source(self):
        return self.get_selected_text_select_element("#audio_e_id")

    def set_channel_audio_source(self, text):
        self.select_dropdown_item_text("#audio_e_id", text)

    def reset_channel_audio_source(self, text):
        self.set_channel_audio_source(text)

    def get_selected_usb_source(self):
        return self.get_selected_text_select_element("#usb_e_id")

    def set_channel_usb_source(self, text):
        self.select_dropdown_item_text("#usb_e_id", text)

    def reset_channel_usb_source(self, text):
        self.set_channel_usb_source(text)

    def get_different_usb_source(self, current):
        sources = self.get_dropdown_option_texts("#usb_e_id")
        sources.remove("- OFF -")
        for source in sources:
            if source != current:
                return source

    def get_selected_serial_source(self):
        return self.get_selected_text_select_element("#serial_e_id")

    def set_channel_serial_source(self, text):
        self.select_dropdown_item_text("#serial_e_id", text)

    def reset_channel_serial_source(self, text):
        self.set_channel_serial_source(text)

    def get_different_serial_source(self, current):
        sources = self.get_dropdown_option_texts("#serial_e_id")
        sources.remove("- OFF -")
        for source in sources:
            if source != current:
                return source

    def set_channel_connections_to_global_settings(self):
        self.set_css_element_state("#c_allowed_modes_0", True)

    def set_channel_connections_to_view_only(self):
        self.set_css_element_state("#c_allowed_modes_4", True)

    def set_channel_connections_to_view_shared_only(self):
        self.set_css_element_state("#c_allowed_modes_1", True)

    def set_channel_connections_to_shared_only(self):
        self.set_css_element_state("#c_allowed_modes_5", True)

    def set_channel_connections_to_exclusive_only(self):
        self.set_css_element_state("#c_allowed_modes_2", True)

    def set_channel_connections_to_view_shared_and_exclusive(self):
        self.set_css_element_state("#c_allowed_modes_3", True)

    def get_channel_connection_state(self, connection):
        if connection == "inherit":
            return self.get_state_of_css_element("#c_allowed_modes_0")
        elif connection == "view_only":
            return self.get_state_of_css_element("#c_allowed_modes_4")
        elif connection == "view_shared":
            return self.get_state_of_css_element("#c_allowed_modes_1")
        elif connection == "shared":
            return self.get_state_of_css_element("#c_allowed_modes_5")
        elif connection == "exclusive":
            return self.get_state_of_css_element("#c_allowed_modes_2")
        elif connection == "all":
            return self.get_state_of_css_element("#c_allowed_modes_3")

    def add_user_to_channel_permission(self, user):
        self.select_dropdown_item_text("#all_users", user)
        self.wait_for_and_click_by_css("#add_one_user")

    def add_user_to_channel_group_permission(self, user):
        self.select_dropdown_item_text("#all_users", user)
        self.wait_for_and_click_by_css("#add_one_user")

    def remove_user_from_channel_permission(self, user):
        self.select_dropdown_item_text("#selected_users", user)
        self.wait_for_and_click_by_css("#remove_one_user")

    def remove_user_from_channel_group_permission(self, user):
        self.select_dropdown_item_text("#selected_users", user)
        self.wait_for_and_click_by_css("#remove_one_user")

    def get_all_users_for_channel(self):
        return self.get_dropdown_option_texts("#selected_users")

    def get_all_users_for_channel_group(self):
        return self.get_dropdown_option_texts("#selected_users")

    def add_channel_to_group(self, text):
        self.select_dropdown_item_text("#all_channel_groups", text)
        self.wait_for_and_click_by_css("#add_one_channel_group")

    def remove_channel_from_group(self, text):
        self.select_dropdown_item_text("#selected_channel_groups", text)
        self.wait_for_and_click_by_css("#remove_one_channel_group")

    def add_channel_to_user_group(self, text):
        self.select_dropdown_item_text("#all_user_groups", text)
        self.wait_for_and_click_by_css("#add_one_user_group")

    def add_channel_group_to_user_group(self, text):
        self.select_dropdown_item_text("#all_user_groups", text)
        self.wait_for_and_click_by_css("#add_one_user_group")

    def remove_channel_from_user_group(self, text):
        self.select_dropdown_item_text("#selected_user_groups", text)
        self.wait_for_and_click_by_css("#remove_one_user_group")

    def remove_channel_group_from_user_group(self, text):
        self.select_dropdown_item_text("#selected_user_groups", text)
        self.wait_for_and_click_by_css("#remove_one_user_group")

    def get_all_user_groups_for_channel(self):
        return self.get_dropdown_option_texts("#selected_user_groups")

    def get_all_user_groups_for_channel_group(self):
        return self.get_dropdown_option_texts("#selected_user_groups")

    def get_channel_linktext(self, element):
        channel_link = element.find_element_by_xpath("./td[8]/a[1]")
        return self.get_attribute_of_element(channel_link, "href")

    def get_channel_group_linktext(self, element):
        channel_grp_link = element.find_element_by_xpath("./td[5]/a[1]")
        return self.get_attribute_of_element(channel_grp_link, "href")

    def is_ajax_error_message_displayed_for_channel(self):
        return self.get_element_located_by_id("configure_channel_ajax_message")

    def is_error_message_displayed_for_channel_group(self):
        id_ = "configure_channel_group_ajax_message"
        return self.get_element_located_by_id(id_)

    def get_all_channels_for_channel_group(self):
        return self.get_dropdown_option_texts("#selected_channels")

    def add_channel_to_channel_group(self, text):
        self.select_dropdown_item_text("#all_channels", text)
        self.wait_for_and_click_by_css("#add_one_channel")

    def add_all_channels_to_channel_group(self):
        self.wait_for_and_click_by_css("#add_all_channels")

    def get_all_not_permitted_channels_for_group(self):
        return self.get_dropdown_option_texts("#all_channels")

    def get_all_permitted_channels_in_group(self):
        return self.get_dropdown_option_texts("#selected_channels")

    def remove_all_channels_from_group(self):
        self.wait_for_and_click_by_css("#remove_all_channels")

    """
    Receiver Page
    """
    def get_receivers_link_element(self):
        if self.get_element_located_by_link_text("RECEIVERS"):
            return self.driver.find_element_by_link_text("RECEIVERS")

    def open_receivers_tab(self):
        self.wait_for_and_click_by_link_text("RECEIVERS")

    def get_remotes_link_element(self):
        if self.get_element_located_by_link_text("REMOTES"):
            return self.driver.find_element_by_link_text("REMOTES")

    def open_remotes_tab(self):
        self.wait_for_and_click_by_link_text("REMOTES")

    def open_view_receivers_page(self):
        steps = ["#receivers_links > ul > li:nth-child(2) > a",
                 "#receivers_links > ul > li:nth-child(1) > a"]
        action = ActionChains(self.driver)
        (action.move_to_element(self.get_receivers_link_element())
        .move_to_element(self.driver.find_element_by_css_selector(steps[0]))
        .move_to_element(self.driver.find_element_by_css_selector(steps[1]))
        .click()
        .perform())

    def open_view_remotes_page(self):
        self.open_view_receivers_page()

    def open_view_receiver_groups_page(self):
        steps = ["#receivers_links > ul > li:nth-child(2) > a"]
        action = ActionChains(self.driver)
        (action.move_to_element(self.get_receivers_link_element())
        .move_to_element(self.driver.find_element_by_css_selector(steps[0]))
        .click()
        .perform())

    def open_view_remote_groups_page(self):
        self.open_view_receiver_groups_page()

    def open_add_receiver_groups_page(self):
        steps = ["#receivers_links > ul > li:nth-child(2) > a",
                 "#receivers_links > ul > li:nth-child(3) > a"]
        action = ActionChains(self.driver)
        (action.move_to_element(self.get_receivers_link_element())
        .move_to_element(self.driver.find_element_by_css_selector(steps[0]))
        .move_to_element(self.driver.find_element_by_css_selector(steps[1]))
        .click()
        .perform())

    def open_add_remote_groups_page(self):
        self.open_add_receiver_groups_page()

    def open_update_receiver_firmware_page(self):
        steps = ["#receivers_links > ul > li:nth-child(2) > a",
                 "#receivers_links > ul > li:nth-child(4) > a"]
        action = ActionChains(self.driver)
        (action.move_to_element(self.get_receivers_link_element())
        .move_to_element(self.driver.find_element_by_css_selector(steps[0]))
        .move_to_element(self.driver.find_element_by_css_selector(steps[1]))
        .click()
        .perform())

    def open_update_remote_firmware_page(self):
        self.open_update_receiver_firmware_page()

    def get_text_of_view_receivers_link(self):
        xpath = "//div[@id='receivers_links']/ul/li[1]/a"
        return self.get_element_text_by_xpath(xpath)

    def get_text_of_view_receiver_groups_link(self):
        xpath = "//div[@id='receivers_links']/ul/li[2]/a"
        return self.get_element_text_by_xpath(xpath)

    def get_text_of_add_receiver_groups_link(self):
        xpath = "//div[@id='receivers_links']/ul/li[3]/a"
        return self.get_element_text_by_xpath(xpath)

    def get_text_of_update_rx_firmware_link(self):
        xpath = "//div[@id='receivers_links']/ul/li[4]/a"
        return self.get_element_text_by_xpath(xpath)

    def get_list_of_receivers(self):
        return self.get_list("receivers")

    def get_row_id_of_receiver(self, element):
        return self.get_attribute_of_element(element, "id")

    def get_receiver_name(self, element):
        return self.get_element_comp_text_by_xpath(element, "./td[2]")

    def get_receiver_ip(self, element):
        ip = self.get_element_comp_text_by_xpath(element, "./td[3]")
        if "\n" in ip:
            ip = ip.split("\n")
            ip = ip[0]
        return ip

    def get_receiver_desc(self, element):
        return self.get_element_comp_text_by_xpath(element, "./td[9]")

    def get_receiver_loc(self, element):
        return self.get_element_comp_text_by_xpath(element, "./td[10]")

    def get_receiver_linktext(self, element):
        rx_link = element.find_element_by_xpath("./td[11]/span[1]/a")
        return self.get_attribute_of_element(rx_link, "href")

    def get_receiver_status_image_src(self, element):
        rx_img = element.find_element_by_xpath("./td[1]")
        return self.check_online_status_image_src(rx_img)

    def send_search_term_to_receiver_name(self, term):
        self.send_filter_term_to_element("filter_d_name", term)

    def send_search_term_to_receiver_desc(self, term):
        self.send_filter_term_to_element("filter_d_description", term)

    def send_search_term_to_receiver_loc(self, term):
        self.send_filter_term_to_element("filter_d_location", term)

    def click_on_filter_receivers_by_name(self):
        self.click_on_filter("filter_d_name_icon")

    def click_on_filter_receivers_by_description(self):
        self.click_on_filter("filter_d_description_icon")

    def click_on_filter_receivers_by_location(self):
        self.click_on_filter("filter_d_location_icon")

    def click_on_remove_receivers_name_filter(self):
        self.click_on_filter("remove_filter_d_name_icon")

    def click_on_remove_receivers_description_filter(self):
        self.click_on_filter("remove_filter_d_description_icon")

    def click_on_remove_receivers_location_filter(self):
        self.click_on_filter("remove_filter_d_location_icon")

    def clear_receiver_names_filter(self):
        self.clear_filter_of_element("filter_d_name")

    def clear_receiver_descriptions_filter(self):
        self.clear_filter_of_element("filter_d_description")

    def clear_receiver_locations_filter(self):
        self.clear_filter_of_element("filter_d_location")

    def click_on_ascend_receiver_names(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[2]/a[1]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_on_decend_receiver_names(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[2]/a[2]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_on_ascend_receiver_descriptions(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[9]/a[1]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_on_decend_receiver_descriptions(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[9]/a[2]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_on_ascend_receiver_locations(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[10]/a[1]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_on_decend_receiver_locations(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[10]/a[2]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_receiver_configure(self, element):
        element.find_element_by_xpath("./td[11]/span[1]/a").click()

    def click_receiver_statistics(self, element):
        element.find_element_by_xpath("./td[11]/a[2]").click()

    def click_receiver_reboot(self, element):
        element.find_element_by_xpath("./td[11]/span[2]/a").click()

    def click_receiver_identify(self, element):
        element.find_element_by_xpath("./td[11]/span[3]/a[1]").click()

    def click_receiver_delete(self, element):
        element.find_element_by_xpath("./td[11]/a[1]").click()

    def click_receiver_connect_to_channel(self, element):
        element.find_element_by_xpath("./td[11]/span[4]/a").click()

    def get_receiver_channel_connect_linktext(self, element):
        rx_connect = element.find_element_by_xpath("./td[11]/span[4]/a")
        return self.get_attribute_of_element(rx_connect, "href")

    def get_visibility_of_receiver_disconnect(self, element):
        try:
            time.sleep(1)
            path = "td.admin_icons span[id^='disconnect_link'] a"
            return element.find_element_by_css_selector(path).is_displayed()
        except Exception:
            return False

    def click_receiver_disconnect_from_channel(self, element):
        path = "td.admin_icons span[id^='disconnect_link'] a"
        element.find_element_by_css_selector(path).click()

    def click_disconnect_all_receivers(self):
        self.wait_for_and_click_by_xpath("//table/thead/tr/th[11]/a")

    def wait_for_receiver_added_message(self):
        expected = "1 new Receiver added. Configure"
        wait = WebDriverWait(self.driver, 120)
        locator = By.XPATH, "//span[@id='warnings']/span"
        wait.until(EC.text_to_be_present_in_element(locator, expected))

    def wait_for_receiver_rebooting_message(self):
        expected = "1 Receiver currently rebooting"
        wait = WebDriverWait(self.driver, 120)
        locator = By.XPATH, "//span[@id='warnings']/span"
        wait.until(EC.text_to_be_present_in_element(locator, expected))

    """
    Receiver Config BasePage
    """
    def set_receiver_ip_via_config_page(self, new_ip):
        if self.get_element_located_by_id("configure_device"):
            self.enter_text_into_input_field("d_ip_address", new_ip)

    def get_receiver_name_from_config_page(self):
        return self.get_attribute_via_id("d_name", "value")

    def set_receiver_name(self, text):
        if self.get_element_located_by_id("d_name"):
            self.enter_text_into_input_field("d_name", text)

    def get_receiver_desc_from_config_page(self):
        return self.get_attribute_via_id("d_description", "value")

    def set_receiver_desc(self, text):
        if self.get_element_located_by_id("d_description"):
            self.enter_text_into_input_field("d_description", text)

    def get_receiver_location_from_config_page(self):
        return self.get_attribute_via_id("d_location", "value")

    def set_receiver_loc(self, text):
        if self.get_element_located_by_id("d_location"):
            self.enter_text_into_input_field("d_location", text)

    def select_login_required_global(self):
        self.set_css_element_state("#rp_login_required_-1", True)

    def select_login_required_no(self):
        self.set_css_element_state("#rp_login_required_0", True)

    def select_login_required_yes(self):
        self.set_css_element_state("#rp_login_required_1", True)

    def get_login_required_option_state(self, option):
        if option == "inherit":
            return self.get_state_of_css_element("#rp_login_required_-1")
        elif option == "no":
            return self.get_state_of_css_element("#rp_login_required_0")
        elif option == "yes":
            return self.get_state_of_css_element("#rp_login_required_1")

    def select_osd_alerts_global(self):
        self.set_css_element_state("#rp_osd_alerts_-1", True)

    def select_osd_alerts_no(self):
        self.set_css_element_state("#rp_osd_alerts_0", True)

    def select_osd_alerts_yes(self):
        self.set_css_element_state("#rp_osd_alerts_1", True)

    def get_osd_alerts_option_state(self, option):
        if option == "inherit":
            return self.get_state_of_css_element("#rp_osd_alerts_-1")
        elif option == "no":
            return self.get_state_of_css_element("#rp_osd_alerts_0")
        elif option == "yes":
            return self.get_state_of_css_element("#rp_osd_alerts_1")

    def get_all_keyboard_country_options(self):
        return self.get_dropdown_option_texts("#rp_keyboard_country")

    def set_keyboard_country_to_visible_text(self, text):
        self.select_dropdown_item_text("#rp_keyboard_country", text)

    def get_selected_keyboard_country(self):
        return self.get_selected_text_select_element("#rp_keyboard_country")

    def select_audio_input_global(self):
        self.set_css_element_state("#rp_audio_is_-1", True)

    def select_audio_input_line(self):
        self.set_css_element_state("#rp_audio_is_0", True)

    def select_audio_input_mic(self):
        self.set_css_element_state("#rp_audio_is_1", True)

    def select_audio_input_mic_boost(self):
        self.set_css_element_state("#rp_audio_is_2", True)

    def get_audio_input_option_state(self, option):
        if option == "global":
            return self.get_state_of_css_element("#rp_audio_is_-1")
        elif option == "line":
            return self.get_state_of_css_element("#rp_audio_is_0")
        elif option == "mic":
            return self.get_state_of_css_element("#rp_audio_is_1")
        elif option == "mic_boost":
            return self.get_state_of_css_element("#rp_audio_is_2")

    def select_video_one_compatibility_global(self):
        self.set_css_element_state("#rp_video_compatibility_check_-1", True)

    def select_video_one_compatibility_no(self):
        self.set_css_element_state("#rp_video_compatibility_check_0", True)

    def select_video_one_compatibility_yes(self):
        self.set_css_element_state("#rp_video_compatibility_check_1", True)

    def get_video_one_compatibility_state(self, option):
        inherit = "#rp_video_compatibility_check_-1"
        no = "#rp_video_compatibility_check_0"
        yes = "#rp_video_compatibility_check_1"
        if option == "inherit":
            return self.get_state_of_css_element(inherit)
        elif option == "no":
            return self.get_state_of_css_element(no)
        elif option == "yes":
            return self.get_state_of_css_element(yes)

    def select_video_two_compatibility_global(self):
        self.set_css_element_state("#rp_video_compatibility_check1_-1", True)

    def select_video_two_compatibility_no(self):
        self.set_css_element_state("#rp_video_compatibility_check1_0", True)

    def select_video_two_compatibility_yes(self):
        self.set_css_element_state("#rp_video_compatibility_check1_1", True)

    def get_video_two_compatibility_state(self, option):
        inherit = "#rp_video_compatibility_check1_-1"
        no = "#rp_video_compatibility_check1_0"
        yes = "#rp_video_compatibility_check1_1"
        if option == "inherit":
            return self.get_state_of_css_element(inherit)
        elif option == "no":
            return self.get_state_of_css_element(no)
        elif option == "yes":
            return self.get_state_of_css_element(yes)

    def add_receiver_to_receiver_group(self, group_name):
        self.select_dropdown_item_text("#all_receiver_groups", group_name)
        self.wait_for_and_click_by_css("#add_one_receiver_group")

    def get_all_current_rx_groups_for_rx(self):
        return self.get_dropdown_option_texts("#selected_receiver_groups")

    def remove_all_receivers_from_receiver_group(self):
        self.wait_for_and_click_by_css("#remove_all_receiver_groups")

    def add_user_to_receiver(self, user):
        self.select_dropdown_item_text("#all_users", user)
        self.wait_for_and_click_by_css("#add_one_user")

    def add_all_users_to_receiver(self):
        self.wait_for_and_click_by_css("#add_all_users")

    def get_all_current_users_for_rx(self):
        return self.get_dropdown_option_texts("#selected_users")

    def remove_all_users_from_receiver(self):
        self.wait_for_and_click_by_css("#remove_all_users")

    def add_receiver_to_user_group(self, text):
        self.select_dropdown_item_text("#all_user_groups", text)
        self.wait_for_and_click_by_css("#add_one_user_group")

    def remove_receiver_from_user_group(self, text):
        self.select_dropdown_item_text("#selected_user_groups", text)
        self.wait_for_and_click_by_css("#remove_one_user_group")

    def get_all_current_user_groups_for_rx(self):
        return self.get_dropdown_option_texts("#selected_user_groups")

    """
    Receiver USB BasePage
    """
    def open_receiver_usb_settings(self):
        self.wait_for_and_click_by_link_text("Configure")

    def open_receiver_usb_settings_2(self):
        self.wait_for_and_click_by_link_text("USB settings")

    def select_HID_connection_global(self):
        self.set_css_element_state("#hid_only_-1", True)

    def select_HID_connection_no(self):
        self.set_css_element_state("#hid_only_0", True)

    def select_HID_connection_yes(self):
        self.set_css_element_state("#hid_only_1", True)

    def get_HID_connection_option_state(self, option):
        if option == "inherit":
            return self.get_state_of_css_element("#hid_only_-1")
        elif option == "no":
            return self.get_state_of_css_element("#hid_only_0")
        elif option == "yes":
            return self.get_state_of_css_element("#hid_only_1")

    def select_disable_isochronous_endpoint_osd_alerts_global(self):
        self.set_css_element_state("#isochronous_user_warning_-1", True)

    def select_disable_isochronous_endpoint_osd_alerts_no(self):
        self.set_css_element_state("#isochronous_user_warning_0", True)

    def select_disable_isochronous_endpoint_osd_alerts_yes(self):
        self.set_css_element_state("#isochronous_user_warning_1", True)

    def get_disable_iso_endpoint_alert_state(self, option):
        inherit = "#isochronous_user_warning_-1"
        no = "#isochronous_user_warning_0"
        yes = "#isochronous_user_warning_1"
        if option == "inherit":
            return self.get_state_of_css_element(inherit)
        elif option == "no":
            return self.get_state_of_css_element(no)
        elif option == "yes":
            return self.get_state_of_css_element(yes)

    def select_enable_isochronous_endpoint_attach_global(self):
        self.set_css_element_state("#isochronous_enabled_-1", True)

    def select_enable_isochronous_endpoint_attach_no(self):
        self.set_css_element_state("#isochronous_enabled_0", True)

    def select_enable_isochronous_endpoint_attach_yes(self):
        self.set_css_element_state("#isochronous_enabled_1", True)

    def get_enable_iso_endpoint_attach_state(self, option):
        if option == "inherit":
            return self.get_state_of_css_element("#isochronous_enabled_-1")
        elif option == "no":
            return self.get_state_of_css_element("#isochronous_enabled_0")
        elif option == "yes":
            return self.get_state_of_css_element("#isochronous_enabled_1")

    """
    Receiver Group BasePage
    """
    def get_list_of_receiver_groups(self):
        return self.get_list("receiver_groups")

    def get_receiver_group_name(self, element):
        return self.get_element_comp_text_by_xpath(element, "./td[1]")

    def get_receiver_group_description(self, element):
        return self.get_element_comp_text_by_xpath(element, "./td[2]")

    def get_receiver_group_config_linktext(self, element):
        rx_grp_config_link = element.find_element_by_xpath("./td[6]/a[1]")
        return self.get_attribute_of_element(rx_grp_config_link, "href")

    def get_receiver_group_clone_linktext(self, element):
        rx_grp_clone_link = element.find_element_by_xpath("./td[6]/a[2]")
        return self.get_attribute_of_element(rx_grp_clone_link, "href")

    def click_add_receiver_group_button(self):
        xpath = "//span/img[@alt='Add Receiver Group']"
        self.wait_for_and_click_by_xpath(xpath)

    def send_search_term_to_receiver_group_name_field(self, term):
        self.send_filter_term_to_element("filter_rg_name", term)

    def click_on_filter_receiver_groups_by_name(self):
        self.click_on_filter("filter_rg_name_icon")

    def click_on_remove_receiver_groups_name_filter(self):
        self.click_on_filter("remove_filter_rg_name_icon")

    def clear_receiver_groups_names_filter(self):
        self.clear_filter_of_element("filter_rg_name")

    def send_search_to_receiver_group_desc_field(self, term):
        self.send_filter_term_to_element("filter_rg_description", term)

    def click_on_filter_receiver_groups_by_description(self):
        self.click_on_filter("filter_rg_description_icon")

    def click_on_remove_receiver_groups_description_filter(self):
        self.click_on_filter("remove_filter_rg_description_icon")

    def clear_remove_receiver_group_descriptions_filter(self):
        self.clear_filter_of_element("filter_rg_description")

    def click_on_ascend_receiver_group_names(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[1]/a[1]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_on_decend_receiver_group_names(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[1]/a[2]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_on_ascend_receiver_group_descriptions(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[2]/a[1]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_on_decend_receiver_group_descriptions(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[2]/a[2]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_receiver_group_delete(self, element):
        element.find_element_by_xpath("./td[6]/a[3]").click()

    def click_batch_delete_receiver_group(self, element):
        element.find_element_by_xpath("./td[6]/input").click()

    def click_receiver_group_config(self, element):
        element.find_element_by_xpath("./td[6]/a[1]").click()

    def click_receiver_group_clone(self, element):
        element.find_element_by_xpath("./td[6]/a[2]").click()

    def click_batch_delete_receiver_groups(self):
        self.wait_for_and_click_by_link_text("Delete selected Receiver Groups")

    def verify_batch_delete_for_receiver_group(self, element):
        return element.find_element_by_xpath("./td[6]/input").is_displayed()

    def get_delete_receiver_text_from_lightbox(self):
        return self.get_lightbox_title_text()

    """
    Receiver Group Config
    """
    def get_receiver_group_name_from_config_page(self):
        return self.get_attribute_via_id("rg_name", "value")

    def set_receiver_group_name(self, text):
        if self.get_element_located_by_id("rg_name"):
            self.enter_text_into_input_field("rg_name", text)

    def get_receiver_group_desc_from_config_page(self):
        return self.get_attribute_via_id("rg_description", "value")

    def set_receiver_group_description(self, text):
        if self.get_element_located_by_id("rg_description"):
            self.enter_text_into_input_field("rg_description", text)

    def select_receiver_group_login_required(self):
        self.set_css_element_state("#rg_login_required_-1", True)

    def select_receiver_group_login_required_no(self):
        self.set_css_element_state("#rg_login_required_0", True)

    def select_receiver_group_login_required_yes(self):
        self.set_css_element_state("#rg_login_required_1", True)

    def get_state_of_rx_group_login_required(self, option):
        if option == "inherit":
            return self.get_state_of_css_element("#rg_login_required_-1")
        elif option == "no":
            return self.get_state_of_css_element("#rg_login_required_0")
        elif option == "yes":
            return self.get_state_of_css_element("#rg_login_required_1")

    def select_receiver_group_osd_alerts_global(self):
        self.set_css_element_state("#rg_osd_alerts_-1", True)

    def select_receiver_group_osd_alerts_no(self):
        self.set_css_element_state("#rg_osd_alerts_0", True)

    def select_receiver_group_osd_alerts_yes(self):
        self.set_css_element_state("#rg_osd_alerts_1", True)

    def get_state_receiver_group_osd_alerts(self, option):
        if option == "inherit":
            return self.get_state_of_css_element("#rg_osd_alerts_-1")
        elif option == "no":
            return self.get_state_of_css_element("#rg_osd_alerts_0")
        elif option == "yes":
            return self.get_state_of_css_element("#rg_osd_alerts_1")

    def select_receiver_group_HID_connection_global(self):
        self.set_css_element_state("#hid_only_-1", True)

    def select_receiver_group_HID_connection_no(self):
        self.set_css_element_state("#hid_only_0", True)

    def select_receiver_group_HID_connection_yes(self):
        self.set_css_element_state("#hid_only_1", True)

    def get_state_receiver_group_hid_only(self, option):
        if option == "inherit":
            return self.get_state_of_css_element("#hid_only_-1")
        elif option == "no":
            return self.get_state_of_css_element("#hid_only_0")
        elif option == "yes":
            return self.get_state_of_css_element("#hid_only_1")

    def select_receiver_grp_disable_iso_endpoint_alerts_global(self):
        self.set_css_element_state("#isochronous_user_warning_-1", True)

    def select_receiver_grp_disable_iso_endpoint_alerts_no(self):
        self.set_css_element_state("#isochronous_user_warning_0", True)

    def select_receiver_grp_disable_iso_endpoint_alerts_yes(self):
        self.set_css_element_state("#isochronous_user_warning_1", True)

    def get_state_rx_grp_disable_iso_endpoint_alert(self, option):
        inherit = "#isochronous_user_warning_-1"
        no = "#isochronous_user_warning_0"
        yes = "#isochronous_user_warning_1"
        if option == "inherit":
            return self.get_state_of_css_element(inherit)
        elif option == "no":
            return self.get_state_of_css_element(no)
        elif option == "yes":
            return self.get_state_of_css_element(yes)

    def select_rx_grp_enable_iso_endpoint_attach_global(self):
        self.set_css_element_state("#isochronous_enabled_-1", True)

    def select_rx_grp_enable_iso_endpoint_attach_no(self):
        self.set_css_element_state("#isochronous_enabled_0", True)

    def select_rx_grp_enable_iso_endpoint_attach_yes(self):
        self.set_css_element_state("#isochronous_enabled_1", True)

    def get_state_rx_grp_enable_iso_endpoint_attach(self, option):
        if option == "inherit":
            return self.get_state_of_css_element("#isochronous_enabled_-1")
        elif option == "no":
            return self.get_state_of_css_element("#isochronous_enabled_0")
        elif option == "yes":
            return self.get_state_of_css_element("#isochronous_enabled_1")

    def select_receiver_group_video_compatibility(self):
        self.set_css_element_state("#rg_video_compatibility_check_-1", True)

    def select_receiver_group_video_compatibility_no(self):
        self.set_css_element_state("#rg_video_compatibility_check_0", True)

    def select_receiver_group_video_compatibility_yes(self):
        self.set_css_element_state("#rg_video_compatibility_check_1", True)

    def get_state_rx_group_video_compatibility(self, option):
        inherit = "#rg_video_compatibility_check_-1"
        no = "#rg_video_compatibility_check_0"
        yes = "#rg_video_compatibility_check_1"
        if option == "inherit":
            return self.get_state_of_css_element(inherit)
        elif option == "no":
            return self.get_state_of_css_element(no)
        elif option == "yes":
            return self.get_state_of_css_element(yes)

    def get_all_rxs_not_in_receiver_group(self):
        return self.get_dropdown_option_texts("#all_rxs")

    def add_member_receiver_to_receiver_group(self, text):
        self.select_dropdown_item_text("#all_rxs", text)
        self.wait_for_and_click_by_css("#add_one_rx")

    def add_all_receivers_to_receiver_group(self):
        self.driver.find_element_by_id("add_all_rxs").click()

    def get_all_rxs_in_receiver_group(self):
        return self.get_dropdown_option_texts("#selected_rxs")

    def remove_all_member_receivers_from_receiver_group(self):
        self.wait_for_and_click_by_css("#remove_all_rxs")

    def get_all_not_permitted_users_of_receiver_group(self):
        return self.get_dropdown_option_texts("#all_users")

    def get_all_users_of_receiver_group(self):
        return self.get_dropdown_option_texts("#selected_users")

    def add_user_to_receiver_group(self, user):
        self.select_dropdown_item_text("#all_users", user)
        self.wait_for_and_click_by_css("#add_one_user")

    def get_all_users_for_receiver_group(self):
        return self.get_dropdown_option_texts("#selected_users")

    def remove_all_users_from_receiver_group(self):
        self.wait_for_and_click_by_css("#remove_all_users")

    def get_all_not_permitted_user_groups_for_rx_group(self):
        return self.get_dropdown_option_texts("#all_user_groups")

    def add_user_group_to_receiver_group(self, user):
        self.select_dropdown_item_text("#all_user_groups", user)
        self.wait_for_and_click_by_css("#add_one_user_group")

    def add_all_user_groups_to_receiver_group(self):
        self.wait_for_and_click_by_css("#add_all_user_groups")

    def get_selected_user_groups_of_rx_group(self):
        return self.get_dropdown_option_texts("#selected_user_groups")

    def remove_all_user_groups_from_receiver_group(self):
        self.wait_for_and_click_by_css("#remove_all_user_groups")

    """
    Receiver Group Add
    """
    def is_error_message_displayed_for_rx_group(self):
        id_ = "configure_receiver_group_ajax_message"
        return self.get_element_located_by_id(id_)

    def get_list_of_non_member_receivers_for_group(self):
        return self.get_dropdown_option_texts("#all_rxs")

    def get_list_of_member_receivers_in_group(self):
        return self.get_dropdown_option_texts("#selected_rxs")

    def select_login_required_for_receiver_group_global(self):
        self.set_css_element_state("#rg_login_required_-1", True)

    def select_login_required_for_receiver_group_no(self):
        self.set_css_element_state("#rg_login_required_0", True)

    def select_login_required_for_receiver_group_yes(self):
        self.set_css_element_state("#rg_login_required_1", True)

    def get_login_required_for_receiver_group(self, option):
        if option == "global":
            return self.get_state_of_css_element("#rg_login_required_-1")
        elif option == "no":
            return self.get_state_of_css_element("#rg_login_required_0")
        elif option == "yes":
            return self.get_state_of_css_element("#rg_login_required_1")

    def select_enable_osd_alerts_for_receiver_group_global(self):
        self.set_css_element_state("#rg_osd_alerts_-1", True)

    def select_enable_osd_alerts_for_receiver_group_no(self):
        self.set_css_element_state("#rg_osd_alerts_0", True)

    def select_enable_osd_alerts_for_receiver_group_yes(self):
        self.set_css_element_state("#rg_osd_alerts_1", True)

    def get_enabled_osd_alerts_for_receiver_group(self, option):
        if option == "global":
            return self.get_state_of_css_element("#rg_osd_alerts_-1")
        elif option == "no":
            return self.get_state_of_css_element("#rg_osd_alerts_0")
        elif option == "yes":
            return self.get_state_of_css_element("#rg_osd_alerts_1")

    def select_enable_video_compatibility_for_receiver_group(self):
        self.set_css_element_state("#rg_video_compatibility_check_-1", True)

    def select_enable_video_compatibility_for_receiver_group_no(self):
        self.set_css_element_state("#rg_video_compatibility_check_0", True)

    def select_enable_video_compatibility_for_receiver_group_yes(self):
        self.set_css_element_state("#rg_video_compatibility_check_1", True)

    def get_enable_video_compatibility_for_rx_group(self, option):
        global_ = "#rg_video_compatibility_check_-1"
        no = "#rg_video_compatibility_check_0"
        yes = "#rg_video_compatibility_check_1"
        if option == "global":
            return self.get_state_of_css_element(global_)
        elif option == "no":
            return self.get_state_of_css_element(no)
        elif option == "yes":
            return self.get_state_of_css_element(yes)

    """
    Presets Page BasePage
    """
    def get_presets_link_element(self):
        if self.get_element_located_by_link_text("PRESETS"):
            return self.driver.find_element_by_link_text("PRESETS")

    def open_presets_tab(self):
        self.wait_for_and_click_by_link_text("PRESETS")

    def get_text_of_view_presets_link(self):
        xpath = "//div[@id='presets_links']/ul/li[1]/a"
        return self.get_element_text_by_xpath(xpath)

    def get_text_of_add_preset_link(self):
        xpath = "//div[@id='presets_links']/ul/li[2]/a"
        return self.get_element_text_by_xpath(xpath)

    def open_view_presets_page(self):
        steps = ["#presets_links > ul > li:nth-child(1) > a"]
        action = ActionChains(self.driver)
        (action.move_to_element(self.get_presets_link_element())
        .move_by_offset(0, 19)
        .move_to_element(self.driver.find_element_by_css_selector(steps[0]))
        .click()
        .perform())

    def open_add_presets_page(self):
        steps = ["#presets_links > ul > li:nth-child(2) > a"]
        action = ActionChains(self.driver)
        (action.move_to_element(self.get_presets_link_element())
        .move_by_offset(0, 19)
        .move_to_element(self.driver.find_element_by_css_selector(steps[0]))
        .click()
        .perform())

    def click_add_preset_button(self):
        xpath = ("//div[@class='button_wrapper']" +
                 "/a" +
                 "/span[contains(text(), 'Add Preset')]")
        self.wait_for_and_click_by_xpath(xpath)

    def get_preset_configure_img_src(self, element):
        return self.get_attribute_of_cell_by_xpath(element,
                                                   "./a[1]/img",
                                                   "src")

    def get_preset_clone_image_src(self, element):
        return self.get_attribute_of_cell_by_xpath(element,
                                                   "./a[2]/img",
                                                   "src")

    def get_preset_delete_image_src(self, element):
        return self.get_attribute_of_cell_by_xpath(element,
                                                   "./a[3]/img",
                                                   "src")

    def get_preset_view_only_img_src(self, element):
        return self.get_attribute_of_cell_by_xpath(element,
                                                   "./a[1]/img",
                                                   "src")

    def get_preset_shared_img_src(self, element):
        return self.get_attribute_of_cell_by_xpath(element,
                                                   "./a[2]/img",
                                                   "src")

    def get_preset_exclusive_img_src(self, element):
        return self.get_attribute_of_cell_by_xpath(element,
                                                   "./a[3]/img",
                                                   "src")

    def get_list_of_presets(self):
        return self.get_list("presets")

    def get_preset_name(self, element):
        return element.find_element_by_xpath("./td[1]").text

    def get_preset_description(self, element):
        return element.find_element_by_xpath("./td[2]").text

    def get_preset_allowed_connection_image_src(self, element):
        preset_img = element.find_element_by_xpath("./td[4]/img")
        return preset_img.get_attribute("src")

    def verify_batch_delete_preset(self, element):
        return element.find_element_by_xpath("./td[6]/input").is_displayed()

    def click_preset_disconnect(self, element):
        time.sleep(1)
        xpath = "./td[5]/a/img[@src='/admin/images/silk_icons/disconnect.png']"
        element.find_element_by_xpath(xpath).click()

    def click_preset_connect_view_only(self, element):
        time.sleep(1)
        xpath = "./td[5]/a/img[@src='/admin/images/silk_icons/eye.png']"
        element.find_element_by_xpath(xpath).click()

    def click_preset_connect_shared(self, element):
        time.sleep(1)
        xpath = "./td[5]/a/img[@src='/admin/images/silk_icons/multicast.png']"
        element.find_element_by_xpath(xpath).click()

    def click_preset_connect_exclusive(self, element):
        time.sleep(1)
        xpath = "./td[5]/a/img[@src='/admin/images/silk_icons/lock.png']"
        element.find_element_by_xpath(xpath).click()

    def check_for_preset_disconnect_button(self, element):
        try:
            xpath = ("./td[5]" +
                     "/a" +
                     "/img[@src='/admin/images/silk_icons/disconnect.png']")
            return element.find_element_by_xpath(xpath).is_displayed()
        except Exception:
            return False

    def check_connect_view_only_button(self, element):
        xpath = ("./td[5]" +
                 "/a" +
                 "/img[@src='/admin/images/silk_icons/eye.png']" +
                 "/parent::a")
        return element.find_element_by_xpath(xpath).get_attribute("class")

    def check_connect_shared_button(self, element):
        xpath = ("./td[5]" +
                 "/a" +
                 "/img[@src='/admin/images/silk_icons/multicast.png']" +
                 "/parent::a")
        return element.find_element_by_xpath(xpath).get_attribute("class")

    def check_connect_exclusive_button(self, element):
        xpath = ("./td[5]" +
                 "/a" +
                 "/img[@src='/admin/images/silk_icons/lock.png']" +
                 "/parent::a")
        return element.find_element_by_xpath(xpath).get_attribute("class")

    def get_preset_config_linktext(self, element):
        preset_config_link = element.find_element_by_xpath("./td[6]/a[1]")
        return self.get_attribute_of_element(preset_config_link, "href")

    def get_preset_clone_linktext(self, element):
        preset_clone_link = element.find_element_by_xpath("./td[6]/a[2]")
        return self.get_attribute_of_element(preset_clone_link, "href")

    def click_preset_configure(self, element):
        element.find_element_by_xpath("./td[6]/a[1]").click()

    def click_preset_clone(self, element):
        element.find_element_by_xpath("./td[6]/a[2]").click()

    def click_preset_delete(self, element):
        element.find_element_by_xpath("./td[6]/a[3]").click()

    def get_preset_search_by_name(self):
        return self.get_element_located_by_id("filter_cp_name")

    def get_preset_search_by_description(self):
        return self.get_element_located_by_id("filter_cp_description")

    def get_preset_name_from_config_page(self):
        return self.get_attribute_via_id("cp_name", "value")

    def set_preset_name_via_config_page(self, text):
        if self.get_element_located_by_id("cp_name"):
            self.enter_text_into_input_field("cp_name", text)

    def get_preset_desc_from_config_page(self):
        return self.get_attribute_via_id("cp_description", "value")

    def set_preset_description_via_config_page(self, text):
        if self.get_element_located_by_id("cp_description"):
            self.enter_text_into_input_field("cp_description", text)

    def get_list_of_preset_pairs(self):
        xpath = "//div[starts-with(@id, 'cp_pair_')]"
        self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        return self.driver.find_elements_by_xpath(xpath)

    def get_list_of_preset_pair_receiver_selects(self):
        xpath = "//select[starts-with(@id, 'receiver_id_')]"
        return self.driver.find_elements_by_xpath(xpath)

    def get_list_of_preset_pair_channel_selects(self):
        xpath = "//select[starts-with(@id, 'channel_id_')]"
        return self.driver.find_elements_by_xpath(xpath)

    def reset_preset_pairs(self):
        xpath = "//div[@class='cp_remove_pair']/a"
        pair_delete_buttons = self.driver.find_elements_by_xpath(xpath)
        for button_ in pair_delete_buttons:
            button_.click()

    def add_new_preset_pair(self):
        self.wait_for_and_click_by_xpath("//div[@class='form_row']/a")
        current_rx = self.get_selected_text_select_element("#receiver_id_1")
        current_chnl = self.get_selected_text_select_element("#channel_id_1")
        receivers = self.get_dropdown_option_texts("#receiver_id_2")
        channels = self.get_dropdown_option_texts("#channel_id_2")
        receivers.remove(current_rx)
        receivers.remove("- Select a Receiver -")
        channels.remove(current_chnl)
        channels.remove("- Select a Channel -")
        self.select_dropdown_item_text("#receiver_id_2", receivers[0])
        self.select_dropdown_item_text("#channel_id_2", channels[0])

    def add_all_available_pairs(self):
        locator = By.XPATH, "//div[@class='form_row']/a"
        self.wait.until(EC.presence_of_element_located(locator))

        all_receivers = self.get_dropdown_option_texts("#receiver_id_1")

        pairs = self.get_list_of_preset_pair_receiver_selects()
        all_selected = [Select(pair).first_selected_option.text
                        for pair in pairs]

        rxs_to_select = list(set(all_receivers) - set(all_selected))
        rxs_to_select.remove("- Select a Receiver -")

        active_channel = self.driver.find_element_by_id("channel_id_1")
        all_channels = [channel.text
                        for channel in Select(active_channel).options]

        chnl_select_elements = self.get_list_of_preset_pair_channel_selects()
        all_selected = [Select(pair).first_selected_option.text
                        for pair in chnl_select_elements]

        chnls_to_select = list(set(all_channels) - set(all_selected))
        chnls_to_select.remove("- Select a Channel -")

        if len(rxs_to_select) > len(chnls_to_select):
            stop = False
            while stop == False:
                rxs_to_select.pop()
                if len(rxs_to_select) == len(chnls_to_select):
                    stop = True

        if len(chnls_to_select) > len(rxs_to_select):
            stop = False
            while stop == False:
                chnls_to_select.pop()
                if len(rxs_to_select) == len(chnls_to_select):
                    stop = True

        for receiver in rxs_to_select:
            idx = rxs_to_select.index(receiver)
            self.wait_for_and_click_by_xpath("//div[@class='form_row']/a")
            pairs = self.get_list_of_preset_pair_receiver_selects()
            self.select_dropdown_item_text_for_element(pairs[-1], receiver)
            xpath = ("./parent::div" +
                     "/following-sibling::div" +
                     "/select[starts-with(@id, 'channel_id_')]")
            matchpair = pairs[-1].find_element_by_xpath(xpath)
            self.select_dropdown_item_text_for_element(matchpair,
                                                       chnls_to_select[idx])

    def add_multicast_pair(self):
        locator = By.XPATH, "//div[@class='form_row']/a"
        self.wait.until(EC.presence_of_element_located(locator))
        self.driver.find_element_by_xpath("//div[@class='form_row']/a").click()
        current_rx = self.get_selected_text_select_element("#receiver_id_1")
        current_chnl = self.get_selected_text_select_element("#channel_id_1")
        receivers = self.get_dropdown_option_texts("#receiver_id_2")
        receivers.remove(current_rx)
        receivers.remove("- Select a Receiver -")
        self.select_dropdown_item_text("#receiver_id_2", receivers[0])
        self.select_dropdown_item_text("#channel_id_2", current_chnl)
        self.click_save_ignore_warnings()
        path = "#configure_connection_preset_ajax_message > a"
        #configure_connection_preset_ajax_message > a
        self.wait_for_and_click_by_css(path)

    def add_same_receiver_pair(self):
        self.wait_for_and_click_by_xpath("//div[@class='form_row']/a")
        current_rx = self.get_selected_text_select_element("#receiver_id_1")
        current_chnl = self.get_selected_text_select_element("#channel_id_1")
        self.select_dropdown_item_text("#receiver_id_2", current_rx)
        self.select_dropdown_item_text("#channel_id_2", current_chnl)
        self.click_save_ignore_warnings()
        if self.driver.name == "chrome":
            time.sleep(2)

    def get_receiver_single_connnection_error_message(self):
        path = "#configure_connection_preset_ajax_message"
        return self.get_element_text_by_css(path)

    def select_preset_connection_global(self):
        self.wait_for_and_click_by_css("#cp_allowed_modes_0")

    def select_preset_connection_view_only(self):
        self.wait_for_and_click_by_css("#cp_allowed_modes_4")

    def select_preset_connection_shared(self):
        self.wait_for_and_click_by_css("#cp_allowed_modes_1")

    def select_preset_connection_exclusive(self):
        self.wait_for_and_click_by_css("#cp_allowed_modes_2")

    def select_preset_connection_all(self):
        self.wait_for_and_click_by_css("#cp_allowed_modes_3")

    def get_preset_connection_image_srcs(self, element):
        srcs = [self.get_attribute_of_element(img, "src")
                for img in element.find_elements_by_xpath("./td[3]/img")]
        return srcs

    def get_preset_conx_view_only_visibility(self, element):
        path = "img[src*='eye.png']"
        return element.find_element_by_css_selector(path).is_displayed()

    def get_preset_conx_shared_visibility(self, element):
        path = "img[src*='multicast.png']"
        return element.find_element_by_css_selector(path).is_displayed()

    def get_preset_conx_exclusive_visibility(self, element):
        path = "img[src*='lock.png']"
        return element.find_element_by_css_selector(path).is_displayed()

    """
    Users BasePage
    """

    def get_users_link_element(self):
        if self.get_element_located_by_link_text("USERS"):
            return self.driver.find_element_by_link_text("USERS")

    def open_users_tab(self):
        self.wait_for_and_click_by_link_text("USERS")

    def get_text_of_view_users_link(self):
        xpath = "//div[@id='users_links']/ul/li[1]/a"
        return self.get_element_text_by_xpath(xpath)

    def get_text_of_add_user_link(self):
        xpath = "//div[@id='users_links']/ul/li[2]/a"
        return self.get_element_text_by_xpath(xpath)

    def get_text_of_view_user_groups_link(self):
        xpath = "//div[@id='users_links']/ul/li[3]/a"
        return self.get_element_text_by_xpath(xpath)

    def get_text_of_add_user_group_link(self):
        xpath = "//div[@id='users_links']/ul/li[4]/a"
        return self.get_element_text_by_xpath(xpath)

    def get_text_of_active_directory_link(self):
        xpath = "//div[@id='users_links']/ul/li[5]/a"
        return self.get_element_text_by_xpath(xpath)

    def open_view_users_page(self):
        steps = ["#users_links > ul > li:nth-child(4) > a",
                 "#users_links > ul > li:nth-child(1) > a"]
        action = ActionChains(self.driver)
        (action.move_to_element(self.get_users_link_element())
        .move_to_element(self.driver.find_element_by_css_selector(steps[0]))
        .move_to_element(self.driver.find_element_by_css_selector(steps[1]))
        .click()
        .perform())

    def open_add_user_page(self):
        steps = ["#users_links > ul > li:nth-child(4) > a",
                 "#users_links > ul > li:nth-child(2) > a"]
        action = ActionChains(self.driver)
        (action.move_to_element(self.get_users_link_element())
        .move_to_element(self.driver.find_element_by_css_selector(steps[0]))
        .move_to_element(self.driver.find_element_by_css_selector(steps[1]))
        .click()
        .perform())

    def open_view_user_groups_page(self):
        steps = ["#users_links > ul > li:nth-child(4) > a",
                 "#users_links > ul > li:nth-child(3) > a"]
        action = ActionChains(self.driver)
        (action.move_to_element(self.get_users_link_element())
        .move_to_element(self.driver.find_element_by_css_selector(steps[0]))
        .move_to_element(self.driver.find_element_by_css_selector(steps[1]))
        .click()
        .perform())

    def open_add_user_group_page(self):
        steps = ["#users_links > ul > li:nth-child(4) > a"]
        action = ActionChains(self.driver)
        (action.move_to_element(self.get_users_link_element())
        .move_to_element(self.driver.find_element_by_css_selector(steps[0]))
        .click()
        .perform())

    def open_active_directory_page(self):
        steps = ["#users_links > ul > li:nth-child(4) > a",
                 "#users_links > ul > li:nth-child(5) > a"]
        action = ActionChains(self.driver)
        (action.move_to_element(self.get_users_link_element())
        .move_to_element(self.driver.find_element_by_css_selector(steps[0]))
        .move_to_element(self.driver.find_element_by_css_selector(steps[1]))
        .click()
        .perform())

    def get_list_of_users(self):
        return self.get_list("users")

    def get_user_username(self, element):
        return self.get_element_comp_text_by_xpath(element, "./td[2]")

    def get_user_firstname(self, element):
        return self.get_element_comp_text_by_xpath(element, "./td[3]")

    def get_user_lastname(self, element):
        return self.get_element_comp_text_by_xpath(element, "./td[4]")

    def get_user_connection_image_src(self, element):
        user_con_img = element.find_element_by_xpath("./td[8]/img")
        return self.get_attribute_of_element(user_con_img, "src")

    def get_user_config_linktext(self, element):
        user_config_link = element.find_element_by_xpath("./td[12]/a[1]")
        return self.get_attribute_of_element(user_config_link, "href")

    def get_user_clone_linktext(self, element):
        user_clone_link = element.find_element_by_xpath("./td[12]/a[2]")
        return self.get_attribute_of_element(user_clone_link, "href")

    def click_batch_delete_selector_for_user_element(self, element):
        element.find_element_by_xpath("./td[12]/input").click()

    def get_user_allowed_connections_img_src(self, element):
        return self.get_attribute_of_cell_by_xpath(element, "./img", "src")

    def get_user_remote_osd_image_src(self, element):
        return self.get_attribute_of_cell_by_xpath(element, "./img", "src")

    def get_user_suspended_image_src(self, element):
        return self.get_attribute_of_cell_by_xpath(element, "./img", "src")

    def get_user_aim_admin_image_src(self, element):
        return self.get_attribute_of_cell_by_xpath(element, "./img", "src")

    def get_clone_user_image_src(self, element):
        return self.get_attribute_of_cell_by_xpath(element,
                                                   "./a[2]/img",
                                                   "src")

    def get_delete_user_image_src(self, element):
        return self.get_attribute_of_cell_by_xpath(element,
                                                   "./a[3]/img",
                                                   "src")

    def send_search_term_to_user_username_field(self, term):
        self.send_filter_term_to_element("filter_username", term)

    def send_search_term_to_user_firstname_field(self, term):
        self.send_filter_term_to_element("filter_firstname", term)

    def send_search_term_to_user_lastname_field(self, term):
        self.send_filter_term_to_element("filter_lastname", term)

    def click_on_filter_users_by_username(self):
        self.click_on_filter("filter_username_icon")

    def click_on_filter_users_by_firstname(self):
        self.click_on_filter("filter_firstname_icon")

    def click_on_filter_users_by_lastname(self):
        self.click_on_filter("filter_lastname_icon")

    def click_on_remove_user_username_filter(self):
        self.click_on_filter("remove_filter_username_icon")

    def click_on_remove_user_firstname_filter(self):
        self.click_on_filter("remove_filter_firstname_icon")

    def click_on_remove_user_lastname_filter(self):
        self.click_on_filter("remove_filter_lastname_icon")

    def clear_user_usernames_filter(self):
        self.clear_filter_of_element("filter_username")

    def clear_user_firstnames_filter(self):
        self.clear_filter_of_element("filter_firstname")

    def clear_user_lastnames_filter(self):
        self.clear_filter_of_element("filter_lastname")

    def click_on_ascend_user_usernames(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[2]/a[1]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_on_decend_user_usernames(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[2]/a[2]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_on_ascend_user_firstnames(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[3]/a[1]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_on_decend_user_firstnames(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[3]/a[2]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_on_ascend_user_lastnames(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[4]/a[1]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_on_decend_user_lastnames(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[4]/a[2]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_user_config(self, element):
        element.find_element_by_xpath("./td[12]/a[1]").click()

    def click_user_clone(self, element):
        element.find_element_by_xpath("./td[12]/a[2]").click()

    def click_user_delete(self, element):
        element.find_element_by_xpath("./td[12]/a[3]").click()

    def click_batch_delete_users(self):
        self.wait_for_and_click_by_link_text("Delete selected Users")

    def get_user_email_from_config_page(self):
        if self.get_element_located_by_id("configure_user"):
                user_email = self.driver.find_element_by_id("u_email")
                email = self.get_attribute_of_element(user_email, "value")
                if email != "":
                    return email
                elif email == "":
                    return "not@here.com"

    def get_user_username_from_config_page(self):
        if self.get_element_located_by_id("configure_user"):
            user_name = self.driver.find_element_by_id("u_username")
            return self.get_attribute_of_element(user_name, "value")

    def set_user_username_via_config_page(self, name):
        if self.get_element_located_by_id("configure_user"):
            self.enter_text_into_input_field("u_username", name)

    def set_user_firstname_via_config_page(self, name):
        if self.get_element_located_by_id("configure_user"):
            self.enter_text_into_input_field("u_firstname", name)

    def set_user_lastname_via_config_page(self, name):
        if self.get_element_located_by_id("configure_user"):
            self.enter_text_into_input_field("u_lastname", name)

    def set_user_email_via_config_page(self, email):
        if self.get_element_located_by_id("configure_user"):
            self.enter_text_into_input_field("u_email", email)

    def set_user_password_via_config_page(self, password):
        if self.get_element_located_by_id("configure_user"):
            self.enter_text_into_input_field("password", password)

    def set_user_password2_via_config_page(self, password):
        if self.get_element_located_by_id("configure_user"):
            self.enter_text_into_input_field("password2", password)

    def select_user_change_password(self):
        self.set_css_element_state("#password_mode_set", True)

    def select_user_no_password(self):
        self.set_css_element_state("#password_mode_none", True)

    def get_require_password_for_user_state(self, option):
        if option == "keep":
            return self.get_state_of_css_element("#password_mode_keep")
        elif option == "change":
            return self.get_state_of_css_element("#password_mode_set")
        elif option == "no":
            return self.get_state_of_css_element("#password_mode_none")

    def select_aim_admin_no(self):
        self.set_css_element_state("#u_admin_0", True)

    def select_aim_admin_yes(self):
        self.set_css_element_state("#u_admin_1", True)

    def get_aim_admin_for_user_state(self, option):
        if option == "no":
            return self.get_state_of_css_element("#u_admin_0")
        elif option == "yes":
            return self.get_state_of_css_element("#u_admin_1")

    def select_user_suspended_no(self):
        self.set_css_element_state("#u_suspended_0", True)

    def select_user_suspended_yes(self):
        self.set_css_element_state("#u_suspended_1", True)

    def get_user_suspended_for_user_state(self, option):
        if option == "no":
            return self.get_state_of_css_element("#u_suspended_0")
        elif option == "yes":
            return self.get_state_of_css_element("#u_suspended_1")

    def select_user_exclusive_no(self):
        self.set_css_element_state("#u_allow_exclusive_mode_0", True)

    def select_user_exclusive_global(self):
        self.set_css_element_state("#u_allow_exclusive_mode_-1", True)

    def select_user_exclusive_yes(self):
        self.set_css_element_state("#u_allow_exclusive_mode_1", True)

    def get_user_exclusive_for_user_state(self, option):
        if option == "no":
            return self.get_state_of_css_element("#u_allow_exclusive_mode_0")
        elif option == "yes":
            return self.get_state_of_css_element("#u_allow_exclusive_mode_1")
        elif option == "inherit":
            return self.get_state_of_css_element("#u_allow_exclusive_mode_-1")

    def add_user_to_usergroup_via_user_config_page(self, text):
        self.select_dropdown_item_text("#all_user_groups", text)
        self.wait_for_and_click_by_css("#add_one_user_group")

    def remove_all_user_groups_from_user_via_user_config_page(self):
        self.wait_for_and_click_by_css("#remove_all_user_groups")

    def get_all_user_groups_for_user(self):
        return self.get_dropdown_option_texts("#selected_user_groups")

    def add_channel_permission_to_user(self, text):
        self.select_dropdown_item_text("#all_channels", text)
        self.wait_for_and_click_by_css("#add_one_channel")

    def add_all_channel_permissions_to_user_via_user_config_page(self):
        self.wait_for_and_click_by_css("#add_all_channels")

    def get_all_channel_permissions_for_user(self):
        return self.get_dropdown_option_texts("#selected_channels")

    def remove_all_channels_from_user(self):
        self.wait_for_and_click_by_css("#remove_all_channels")

    def add_channel_group_permission_to_user(self, text):
        self.select_dropdown_item_text("#all_channel_groups", text)
        self.wait_for_and_click_by_css("#add_one_channel_group")

    def get_selected_c_groups_for_user(self):
        return self.get_dropdown_option_texts("#selected_channel_groups")

    def remove_all_channel_group_permissions_via_user_config_page(self):
        self.wait_for_and_click_by_css("#remove_all_channel_groups")

    def add_receiver_permission_to_user_via_user_config_page(self, text):
        self.select_dropdown_item_text("#all_rxs", text)
        self.wait_for_and_click_by_css("#add_one_rx")

    def get_all_receivers_for_user(self):
        return self.get_dropdown_option_texts("#selected_rxs")

    def add_all_receiver_permissions_via_user_config_page(self):
        self.wait_for_and_click_by_css("#add_all_rxs")

    def remove_all_receiver_permissions_from_user(self):
        self.wait_for_and_click_by_css("#remove_all_rxs")

    def add_receiver_group_permission_to_user(self, text):
        self.select_dropdown_item_text("#all_receiver_groups", text)
        self.wait_for_and_click_by_css("#add_one_receiver_group")

    def get_all_rx_groups_for_user(self):
        return self.get_dropdown_option_texts("#selected_receiver_groups")

    def remove_all_receiver_group_permissions_via_user_config_page(self):
        self.wait_for_and_click_by_css("#remove_all_receiver_groups")

    def is_ajax_error_message_displayed_for_user(self):
        return self.get_element_located_by_id("configure_user_ajax_message")

    """
    User Group BasePage
    """
    def get_list_of_user_groups(self):
        return self.get_list("user_groups")

    def get_user_group_name(self, element):
        return self.get_element_comp_text_by_xpath(element, "./td[2]")

    def get_user_group_connection_image_src(self, element):
        user_grp_con_img = element.find_element_by_xpath("./td[6]/img")
        return self.get_attribute_of_element(user_grp_con_img, "src")

    def get_user_group_config_linktext(self, element):
        user_grp_config_link = element.find_element_by_xpath("./td[8]/a[1]")
        return self.get_attribute_of_element(user_grp_config_link, "href")

    def get_user_group_clone_linktext(self, element):
        user_grp_clone_link = element.find_element_by_xpath("./td[8]/a[2]")
        return self.get_attribute_of_element(user_grp_clone_link, "href")

    def click_add_user_group_button(self):
        self.wait_for_and_click_by_xpath("//span/img[@alt='Add User Group']")

    def get_user_group_search_by_name(self):
        return self.get_element_located_by_id("filter_ug_name")

    def send_search_term_to_user_group_name_field(self, term):
        self.send_filter_term_to_element("filter_ug_name", term)

    def click_on_filter_user_groups_by_name(self):
        self.click_on_filter("filter_ug_name_icon")

    def click_on_remove_user_groups_name_filter(self):
        self.click_on_filter("remove_filter_ug_name_icon")

    def clear_user_groups_names_filter(self):
        self.clear_filter_of_element("filter_ug_name")

    def click_on_ascend_user_group_names(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[2]/a[1]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_on_decend_user_group_names(self):
        xpath = "//div[@id='admin_body']/table/thead/tr/th[2]/a[2]"
        self.wait_for_and_click_by_xpath(xpath)

    def click_user_group_config(self, element):
        element.find_element_by_xpath("./td[8]/a[1]").click()

    def click_user_group_clone(self, element):
        element.find_element_by_xpath("./td[8]/a[2]").click()

    def click_user_group_delete(self, element):
        element.find_element_by_xpath("./td[8]/a[3]").click()

    def click_batch_delete_user_group(self, element):
        element.find_element_by_xpath("./td[8]/input").click()

    def click_batch_delete_user_groups(self):
        self.wait_for_and_click_by_link_text("Delete selected User Groups")

    def get_user_group_users_class(self, element):
        return self.get_attribute_of_cell_by_xpath(element, "./a", "class")

    def get_u_group_channels_class(self, element):
        return self.get_attribute_of_cell_by_xpath(element, "./a", "class")

    def get_u_group_receivers_class(self, element):
        return self.get_attribute_of_cell_by_xpath(element, "./a", "class")

    def get_u_group_config_img_src(self, element):
        return self.get_attribute_of_cell_by_xpath(element,
                                                   "./a[1]/img", "src")

    def get_user_group_clone_img_src(self, element):
        return self.get_attribute_of_cell_by_xpath(element,
                                                   "./a[2]/img", "src")

    def get_u_group_delete_img_src(self, element):
        return self.get_attribute_of_cell_by_xpath(element,
                                                   "./a[3]/img", "src")

    def set_user_group_name_via_config_page(self, name):
        if self.get_element_located_by_id("configure_user_group"):
            self.enter_text_into_input_field("ug_name", name)

    def select_user_group_exclusive_no(self):
        self.set_css_element_state("#ug_allow_exclusive_mode_0", True)

    def select_user_group_exclusive_global(self):
        self.set_css_element_state("#ug_allow_exclusive_mode_-1", True)

    def select_user_group_exclusive_yes(self):
        self.set_css_element_state("#ug_allow_exclusive_mode_1", True)

    def get_state_of_user_group_exclusive(self, option):
        if option == "inherit":
            return self.get_state_of_css_element("#ug_allow_exclusive_mode_-1")
        elif option == "no":
            return self.get_state_of_css_element("#ug_allow_exclusive_mode_0")
        elif option == "yes":
            return self.get_state_of_css_element("#ug_allow_exclusive_mode_1")

    def select_user_group_remote_osd_no(self):
        self.set_css_element_state("#ug_allow_remote_osd_0", True)

    def select_user_group_remote_osd_global(self):
        self.set_css_element_state("#ug_allow_remote_osd_-1", True)

    def select_user_group_remote_osd_yes(self):
        self.set_css_element_state("#ug_allow_remote_osd_1", True)

    def get_state_of_user_group_remote_osd(self, option):
        if option == "inherit":
            return self.get_state_of_css_element("#ug_allow_remote_osd_-1")
        elif option == "no":
            return self.get_state_of_css_element("#ug_allow_remote_osd_0")
        elif option == "yes":
            return self.get_state_of_css_element("#ug_allow_remote_osd_1")

    def get_all_members_of_user_group(self):
        return self.get_dropdown_option_texts("#selected_users")

    def add_member_to_user_group(self, user):
        self.select_dropdown_item_text("#all_users", user)
        self.wait_for_and_click_by_css("#add_one_user")

    def remove_member_from_user_group_permission(self, user):
        self.select_dropdown_item_text("#selected_users", user)
        self.wait_for_and_click_by_css("#remove_one_user")

    def remove_all_members_from_user_group(self):
        self.wait_for_and_click_by_css("#remove_all_users")

    def add_channel_permission_to_user_group(self, channel):
        self.select_dropdown_item_text("#all_channels", channel)
        self.wait_for_and_click_by_css("#add_one_channel")

    def get_all_channel_permissions_for_user_group(self):
        return self.get_dropdown_option_texts("#selected_channels")

    def add_all_channel_permissions_to_user_group(self):
        self.wait_for_and_click_by_css("#add_all_channels")

    def remove_all_channels_from_user_group(self):
        self.wait_for_and_click_by_css("#remove_all_channels")

    def add_channel_group_permission_to_user_group(self, group):
        self.select_dropdown_item_text("#all_channel_groups", group)
        self.wait_for_and_click_by_css("#add_one_channel_group")

    def get_all_channel_groups_for_user_group(self):
        return self.get_dropdown_option_texts("#selected_channel_groups")

    def add_all_channel_group_permissions_to_user_group(self):
        self.wait_for_and_click_by_css("#add_all_channel_groups")

    def remove_all_channel_groups_from_user_group(self):
        self.wait_for_and_click_by_css("#remove_all_channel_groups")

    def add_receiver_permission_to_user_group(self, rx):
        self.select_dropdown_item_text("#all_rxs", rx)
        self.wait_for_and_click_by_css("#add_one_rx")

    def get_all_rxs_for_user_group(self):
        return self.get_dropdown_option_texts("#selected_rxs")

    def add_all_receiver_permissions_to_user_group(self):
        self.wait_for_and_click_by_css("#add_all_rxs")

    def remove_all_receivers_from_user_group(self):
        self.wait_for_and_click_by_css("#remove_all_rxs")

    def add_receiver_group_permission_to_user_group(self, group):
        self.select_dropdown_item_text("#all_receiver_groups", group)
        self.wait_for_and_click_by_css("#add_one_receiver_group")

    def get_all_rx_groups_for_user_group(self):
        return self.get_dropdown_option_texts("#selected_receiver_groups")

    def remove_all_receiver_group_permissions(self):
        self.wait_for_and_click_by_css("#remove_all_receiver_groups")

    """
    Add User Group BasePage
    """
    def is_ajax_error_message_displayed_for_user_group(self):
        id_ = "configure_user_group_ajax_message"
        return self.get_element_located_by_id(id_)

    """
    User Active Directory
    """
    def click_rescan_active_directory(self):
        self.wait_for_and_click_by_css("#rescan_ldap_button")

    def get_active_directory_content(self):
        msg = "#ldap_import_ajax_message.message_box.mb_green"
        button = "#rescan_ldap_button"
        locator = By.CSS_SELECTOR, msg
        self.wait.until(EC.invisibility_of_element_located(locator))
        locator = By.CSS_SELECTOR, button
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_elements_by_xpath("//tbody/tr")

    def get_active_directory_table_cells(self, row):
        return row.find_elements_by_tag_name("td")

    def select_ad_import(self, cell):
        cell.click()

    """
    USB Port Reservation BasePage
    """
    def get_port_reservation_labels(self, suffix):
        return self.get_dropdown_option_texts("#port_reservation_" + suffix)

    def select_port_reservation(self, element, label):
        select = Select(element)
        select.select_by_visible_text(label)

    def get_selected_rx_reserved_usb_port(self, element):
        select = Select(element)
        return select.first_selected_option.text

    def get_list_of_port_reservation_dropdowns(self):
        path = "select[id^='port_reservation_']"
        locator = By.CSS_SELECTOR, path
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements_by_css_selector(path)

    def get_port_reservation_merge_checkboxes(self):
        path = "input[id^='merge_']"
        locator = By.CSS_SELECTOR, path
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements_by_css_selector(path)

    def get_port_reservation_device_dropdowns(self):
        path = "select[id^='port_quirk_']"
        locator = By.CSS_SELECTOR, path
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements_by_css_selector(path)

    def get_list_of_reserved_devices(self, element):
        return self.get_dropdown_options_text_by_element(element)

    def select_port_reservation_device(self, element, label):
        select = Select(element)
        select.select_by_visible_text(label)

    def get_selected_rx_reserved_usb_port_device(self, element):
        select = Select(element)
        return select.first_selected_option.text

    def show_advanced_usb_features(self):
        if self.get_element_located_by_id("show_quirks_table"):
            self.driver.execute_script("toggle_quirks_table(1)")
            time.sleep(2)

    def get_list_usb_devices(self):
        path = ("div#quirks_table_container " +
                "> form#usb_quirks " +
                "> table.zebra tbody " +
                "> tr")
        return self.driver.find_elements_by_css_selector(path)

    def get_name(self, element):
        return element.find_element_by_css_selector("td:nth-child(1)").text

    def toggle_hide_usb_device(self, element):
        path = "input[id^='show_quirk_']"
        locator = By.CSS_SELECTOR, path
        self.wait.until(EC.presence_of_element_located(locator))
        try:
            element.find_element_by_css_selector(path).click()
        except NoSuchElementException:
            img_path = "td:nth-child(6) > img"
            quirk_tick = element.find_element_by_css_selector(img_path)
            if "tick.png" in quirk_tick.get_attribute("src"):
                pass
            else:
                raise RuntimeError("Couldn't find show_quirk checkbox" +
                                   "nor green tick icon.")

    def set_status_hide_usb_device_global(self):
        self.wait_for_and_click_by_css("#toggle_show_checkbox")

    def get_show_status_of_usb_device(self, element):
        self.get_state_of_css_element("input[id^='show_quirk_']")

    def add_test_usb_device(self, name, desc, kernel, user):
        n_path = "#new_quirk_name"
        d_path = "#new_quirk_descrip"
        k_path = "#new_quirk_kernel"
        u_path = "#new_quirk_user"
        self.driver.find_element_by_css_selector(n_path).clear()
        self.driver.find_element_by_css_selector(d_path).clear()
        self.driver.find_element_by_css_selector(d_path).clear()
        self.driver.find_element_by_css_selector(u_path).clear()
        self.driver.find_element_by_css_selector(n_path).send_keys(name)
        self.driver.find_element_by_css_selector(d_path).send_keys(desc)
        self.driver.find_element_by_css_selector(k_path).send_keys(kernel)
        self.driver.find_element_by_css_selector(u_path).send_keys(user)

    def delete_test_usb_device(self):
        path = "div#quirks_table_container form#usb_quirks table.zebra tbody"
        table = self.driver.find_element_by_css_selector(path)
        input_path = "input[id^='delete_quirk_']"
        table.find_element_by_css_selector(input_path).click()

    def get_port_merge_selector_state(self, element):
        return element.is_selected()

    def toggle_port_merge_state(self, element):
        element.click()

    def get_quirk_ajax_message_text(self):
        path = "span#usb_quirks_ajax_message.message_box.mb_red"
        return self.get_element_text_by_css(path)

    """
    Statistics Page BasePage
    """
    def open_statistics_tab(self):
        self.wait_for_and_click_by_link_text("STATISTICS")

    def get_no_enabled_devices_text_from_lightbox(self):
        return self.get_lightbox_title_text()

    def click_open_device_list_within_lightbox(self):
        if self.get_element_located_by_id("ibox"):
            self.wait_for_and_click_by_link_text("the devices page")

    def open_device_list_directly(self):
        self.driver.get(self.baseurl + "/admin/devices.php")

    def get_list_of_devices(self):
        return self.get_list("devices")

    def get_device_name(self, element):
        return self.get_element_comp_text_by_xpath(element, "./td[2]")

    def click_device_statistics_icon(self, element):
        element.find_element_by_xpath("./td[8]/a[2]").click()
        time.sleep(0.5)

    def select_rx_bandwidth(self, state):
        self.set_css_element_state("input[name='rxBandwidth']", state)

    def select_rx_throughput(self, state):
        self.set_css_element_state("input[name='rxData']", state)

    def select_tx_bandwidth(self, state):
        self.set_css_element_state("input[name='txBandwidth']", state)

    def select_tx_throughput(self, state):
        self.set_css_element_state("input[name='txData']", state)

    def select_framecount(self, state):
        self.set_css_element_state("input[name='frameCount']", state)

    def select_head0_frame_rate(self, state):
        self.set_css_element_state("input[name='fcnt0']", state)

    def select_head1_frame_rate(self, state):
        self.set_css_element_state("input[name='fcnt1']", state)

    def click_lightbox_submit_button(self):
        if self.get_element_located_by_id("ibox"):
            self.wait_for_and_click_by_link_text("Submit")

    def get_device_name_from_statistics_graph(self):
        path = "#container > div > h2"
        titles = self.driver.find_elements_by_css_selector(path)
        names = [title.text
                 for title in titles]
        return names

    def get_graph_type_from_statistics_graph_left_axis(self):
        path = ("#container " +
                "> div " +
                "> div " +
                "> div[style*='rotate(-90deg)']:first-of-type")
        graphs = self.driver.find_elements_by_css_selector(path)
        names = [each.text
                 for each in graphs]
        return names

    def get_graph_type_from_statistics_graph_right_axis(self):
        path = ("#container " +
                "> div" +
                "> div" +
                "> div[style*='rotate(-90deg)']:last-of-type")
        graphs = self.driver.find_elements_by_css_selector(path)
        names = [each.text
                 for each in graphs]
        return names

    """
    New Statistics Page BasePage
    """
    def click_show_receivers(self):
        self.wait_for_and_click_by_css("#filterRxs")
        time.sleep(1)

    def click_show_transmitters(self):
        self.wait_for_and_click_by_css("#filterTxs")
        time.sleep(1)

    def get_device_type_img(self, device):
        path = "td > span.tooltip > img.icon"
        device_img = device.find_element_by_css_selector(path)
        return device_img.get_attribute("src")

    def click_activate_statistics(self, device):
        device.find_element_by_css_selector("td.admin_icons > a").click()

    def click_device_name(self, device):
        time.sleep(1)
        device.find_element_by_css_selector("td.left.device_name > a").click()

    def get_number_device_name_links(self, device):
        time.sleep(1)
        path = "td.left.device_name > a"
        return len(device.find_elements_by_css_selector(path))

    def get_graph_title(self):
        return self.driver.find_element_by_css_selector("div#right > h1").text

    def click_disable_all_device_statistics(self):
        self.wait_for_and_click_by_link_text("Disable All")

    def send_search_term_to_name(self, search_term):
        name = self.driver.find_element_by_css_selector("#filter_d_name")
        self.set_text_of_element(name, search_term)

    def click_filter_by_name(self):
        self.wait_for_and_click_by_css("#filter_d_name_icon")

    def send_search_term_to_description(self, search_term):
        path = "#filter_d_description"
        desc = self.driver.find_element_by_css_selector(path)
        self.set_text_of_element(desc, search_term)

    def click_filter_by_description(self):
        self.wait_for_and_click_by_css("#filter_d_description_icon")

    def send_search_term_to_location(self, search_term):
        loc = self.driver.find_element_by_css_selector("#filter_d_location")
        self.set_text_of_element(loc, search_term)

    def click_filter_by_location(self):
        self.wait_for_and_click_by_css("#filter_d_location_icon")

    def click_remove_filters(self):
        self.wait_for_and_click_by_link_text("Remove Filters")

    def get_device_description(self, element):
        return self.get_element_component_text_by_css(element,
                                                      "td:nth-child(3)")

    def get_device_location(self, element):
        return self.get_element_component_text_by_css(element,
                                                      "td:nth-child(4)")

    """
    Servers Page BasePage
    """
    def open_servers_tab(self):
        if self.get_element_located_by_link_text("SERVERS"):
            self.driver.find_element_by_link_text("SERVERS").click()

    def get_list_of_servers(self):
        return self.get_list("servers")

    def get_server_name(self, element):
        return self.get_element_comp_text_by_css(element, "td:nth-child(1)")

    def get_server_role(self, element):
        return self.get_element_comp_text_by_css(element, "td:nth-child(2)")

    def get_server_status(self, element):
        return self.get_element_comp_text_by_css(element, "td:nth-child(3)")

    def get_server_ip_address(self, element):
        return self.get_element_comp_text_by_css(element, "td:nth-child(4)")

    def get_server_description(self, element):
        return self.get_element_comp_text_by_css(element, "td:nth-child(5)")

    def get_server_location(self, element):
        return self.get_element_comp_text_by_css(element, "td:nth-child(6)")

    def click_server_config(self, element):
        element.find_element_by_css_selector("td:nth-child(7) > a").click()

    def click_non_primary_server_local_config(self, element):
        path = "td:nth-child(7) > a:nth-child(2)"
        element.find_element_by_css_selector(path).click()

    def click_server_delete(self, element):
        path = "td:nth-child(7) > a:nth-child(3)"
        element.find_element_by_css_selector(path).click()

    def set_server_name(self, name):
        locator = By.CSS_SELECTOR, "#name"
        self.wait.until(EC.presence_of_element_located(locator))
        self.driver.find_element_by_css_selector("#name").clear()
        self.driver.find_element_by_css_selector("#name").send_keys(name)

    def set_server_description(self, name):
        path = "#description"
        locator = By.CSS_SELECTOR, path
        self.wait.until(EC.presence_of_element_located(locator))
        self.driver.find_element_by_css_selector(path).clear()
        self.driver.find_element_by_css_selector(path).send_keys(name)

    def set_server_location(self, name):
        locator = By.CSS_SELECTOR, "#location"
        self.wait.until(EC.presence_of_element_located(locator))
        self.driver.find_element_by_css_selector("#location").clear()
        self.driver.find_element_by_css_selector("#location").send_keys(name)

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def switch_to_other_window_from(self, first):
        for name in self.driver.window_handles:
            if name != first:
                self.driver.switch_to_window(name)
            else:
                pass

    def get_current_url(self):
        time.sleep(2)
        return self.driver.current_url

    def get_server_name_from_backup_local_config(self):
        path = ("#configure_server " +
                "> div.form_row:nth-child(7) " +
                "> div.form_input_elements")
        return self.get_element_text_by_css(path)
