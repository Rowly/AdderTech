'''
Created on 29 Apr 2013

@author: Mark.rowlands
'''
from selenium.webdriver.support.wait import WebDriverWait
from root.nested.services.selenium_start_service import SeleniumStartService
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from xml.dom.minidom import parseString
import requests
import time
from selenium.webdriver.common.action_chains import ActionChains
from root.nested.services.parameters import parameter_singleton

class BasePage():

    def __init__(self):
        self.driver = SeleniumStartService().start_driver()
        self.wait = WebDriverWait(self.driver, 15)
    #def __init__(self, driver, wait):
        #self.driver = driver
        #self.wait = wait
        self.baseurl = parameter_singleton["url"]
        
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
        return self.wait.until(EC.presence_of_element_located((By.ID, "admin_logo_right"))).text
    
    def get_page_name(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, "admin_logo_left"))).text
    
    def get_footer_text(self):
        if self.get_element_located_by_id("footer_version"):
            return self.driver.find_element_by_id("footer_version").text
    
    def get_text_for_remote_tab(self):
        return self.get_text_of_element_via_xpath("//div[@id='admin_top_nav_bar']/ul/li[3]")
    
    def get_text_for_local_tab(self):
        return self.get_text_of_element_via_xpath("//div[@id='admin_top_nav_bar']/ul/li[4]")
    
    def get_receiver_widget_header(self):
        return self.get_text_of_element_via_xpath("//div[@id='widget_receivers']/div")

    def get_transmitter_widget_header(self):
        return self.get_text_of_element_via_xpath("//div[@id='widget_transmitters']/div")
    
    def get_text_of_remote_subtab_link(self, position):
        return self.get_text_of_element_via_xpath("//div[@id='receivers_links']/ul/li[" + position + "]")

    def get_text_of_local_subtab_link(self, position):
        return self.get_text_of_element_via_xpath("//div[@id='transmitters_links']/ul/li[" + position + "]")
        
    def get_element_located_by_id(self, id_):
        try:
            return self.wait.until(EC.presence_of_element_located((By.ID, id_))).is_displayed()
        except Exception:
            return False

    def get_element_located_by_name(self, name):
        try:
            return self.wait.until(EC.presence_of_element_located((By.NAME, name))).is_displayed()
        except Exception:
            return False
        
    def get_element_located_by_link_text(self, link_text):
        try:
            return self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, link_text))).is_displayed()
        except Exception:
            return False
        
    def get_element_located_by_xpath(self, xpath):
        try:
            return self.wait.until(EC.presence_of_element_located((By.XPATH, xpath))).is_displayed()
        except Exception:
            return False

    def get_element_located_by_css_selector(self, selector):
        try:
            return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector))).is_displayed()
        except Exception:
            return False
    
    def get_information_to_user_text(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'error_message')]"))).text
        
    def get_css_property_of_element_via_id(self, css_property, element_id):
        self.wait.until(EC.presence_of_element_located((By.ID, element_id)))
        return self.driver.find_element_by_id(element_id).value_of_css_property(css_property)
        
    def get_css_property_of_element_via_xpath(self, css_property, xpath):
        self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        return self.driver.find_element_by_xpath(xpath).value_of_css_property(css_property)
    
    def get_text_of_element_via_id(self, id_):
        self.wait.until(EC.presence_of_element_located((By.ID, id_)))
        return self.driver.find_element_by_id(id_).text

    def get_text_of_element_via_xpath(self, xpath):
        self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        return self.driver.find_element_by_xpath(xpath).text

    def get_text_of_element_via_css(self, selector):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
        return self.driver.find_element_by_css_selector(selector).text
    
    def get_text_of_element_component_via_css(self, element, css):
        return element.find_element_by_css_selector(css).text
    
    def get_attribute_via_xpath(self, xpath, attribute):
        self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        return self.driver.find_element_by_xpath(xpath).get_attribute(attribute)

    def get_attribute_via_id(self, id_, attribute):
        self.wait.until(EC.presence_of_element_located((By.ID, id_)))
        return self.driver.find_element_by_id(id_).get_attribute(attribute)
            
    def get_favicon_href(self):
        return self.driver.find_element_by_xpath("//link[contains(@rel, 'icon')]").get_attribute("href")
    
    def get_list_of_links_on_current_page(self):
        return self.driver.find_elements_by_tag_name("a")

    def get_text_of_page_header(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/h1"):
            header_text = self.get_text_of_element_via_xpath("//div[@id='admin_body']/h1")
            if header_text != None:
                return header_text
            else:
                self.driver.refresh()
                self.get_text_of_page_header()
    
    def get_colour_property_of_element(self, element):
        return element.value_of_css_property("color")
    
    def get_options_from_select_element(self, id_):
        self.wait.until(EC.presence_of_element_located((By.ID, id_)))
        select = Select(self.driver.find_element(By.ID, id_))
        return select.options
    
    def select_dropdown_item_by_value(self, id_, value):
        try:
            self.wait.until(EC.presence_of_element_located((By.ID, id_)))
            select = Select(self.driver.find_element(By.ID, id_))
            select.select_by_value(value) 
        except TimeoutException:
            self.driver.refresh()
            self.select_dropdown_item_by_value(id_, value)

    def select_dropdown_item_by_visible_text(self, id_, text):
        self.wait.until(EC.presence_of_element_located((By.ID, id_)))
        select = Select(self.driver.find_element(By.ID, id_))
        select.select_by_visible_text(text)
    
    def click_save(self):
        if self.get_element_located_by_link_text("Save"):
            self.driver.find_element_by_link_text("Save").click()
            while True:
                try:
                    message = self.driver.find_element_by_css_selector("span[id*='ajax_message']").text
                    if (message == "Saving changes..." 
                        or message == "" 
                        or message == "Because this Preset contains multicasting, it will only be available if the global setting includes view/shared mode. Do you still want to save this preset? Yes"
                        or message == "A Receiver can only be used in one connection pair"):
                        break
                    else:
                        raise RuntimeError("Error: %s"%message)
                except NoSuchElementException:
                    break
    
    def click_save_ignore_warnings(self):
        if self.get_element_located_by_link_text("Save"):
            self.driver.find_element_by_link_text("Save").click()
    
    def click_save_settings(self):
        if self.get_element_located_by_link_text("Save Settings"):
            self.driver.find_element_by_link_text("Save Settings").click()
            time.sleep(2)

    def click_save_usb_settings(self):
        if self.get_element_located_by_link_text("Save USB Settings"):
            self.driver.find_element_by_link_text("Save USB Settings").click()
    
    def click_save_features(self):
        if self.get_element_located_by_link_text("Save Features"):
            self.driver.find_element_by_link_text("Save Features").click()
            time.sleep(2)
    
    def click_cancel(self):
        if self.get_element_located_by_link_text("Cancel"):
            self.driver.find_element_by_link_text("Cancel").click()
    
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
    
    def get_dropdown_options_text_by_id(self, id_):
        labels = []
        if self.get_element_located_by_id(id_):
            select = Select(self.driver.find_element_by_id(id_))
            options = select.options
            for option in options:
                labels.append(option.text)
            return labels
    
    def get_current_selected_text_by_id(self, id_):
        if self.get_element_located_by_id(id_):
            select = Select(self.driver.find_element_by_id(id_))
            options = select.options
            for option in options:
                if option.is_selected():
                    return option.text

    def get_dropdown_options_text_by_element(self, element):
        labels = []
        select = Select(element)
        options = select.options
        for option in options:
            labels.append(option.text)
        return labels
    
    def get_current_selected_text_by_element(self, element):
        select = Select(element)
        options = select.options
        for option in options:
            if option.is_selected():
                return option.text
    
    def get_radio_button_label_by_name(self, name):
        if self.get_element_located_by_name(name):
            buttons = self.driver.find_elements_by_name(name)
            for button in buttons:
                if button.is_selected():
                    return button.find_element_by_xpath("./following-sibling::label").text
    
    def toggle_radio_button_by_name(self, name):
        if self.get_element_located_by_name(name):
            buttons = self.driver.find_elements_by_name(name)
            for button in buttons:
                if not button.is_selected():
                    button.click()
                    break
    
    def wait_for_saving_settings_message_to_be_removed(self):
        self.wait.until(EC.invisibility_of_element_located((By.XPATH, "//span[@id='settings_ajax_message']")))

    def get_visibility_of_settings_warning(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@id='settings_ajax_message']")))
            return self.driver.find_element_by_xpath("//span[@id='settings_ajax_message']").is_displayed()
        except Exception:
            return False

    def get_visibility_of_configure_device_warning(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@id='configure_device_ajax_message']")))
            return self.driver.find_element_by_xpath("//span[@id='configure_device_ajax_message']").is_displayed()
        except Exception:
            return False

    def check_for_error_message(self, id_):
        try:
            wait = WebDriverWait(self.driver, 5)
            saving = True
            while(saving):
                wait.until(EC.presence_of_element_located((By.ID, id_)))
                visible_error = self.driver.find_element_by_id(id_).is_displayed()
                if visible_error:
                    message = self.self.driver.find_element_by_id(id_).text
                    if "Saving" not in message:
                        saving = False
                        raise RuntimeError("Encountered Error: " + message)
                    else: saving = True
                else: saving = False
        except Exception:
            pass

    def enter_text_into_input_field(self, id_, text):
        if self.get_element_located_by_id(id_):
            self.driver.find_element_by_id(id_).clear()
            self.driver.find_element_by_id(id_).send_keys(text)
    
    def get_list(self, _type):
        time.sleep(3)
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//tbody/tr")))
            return self.driver.find_elements_by_xpath("//tbody/tr")
        except:
            self.driver.refresh()
            if "session" in self.driver.current_url or "/login.php?r=%2Fadmin%2Findex.php" in self.driver.current_url:
                self.login_as("admin", "password", False)
            if _type is "transmitters":
                self.open_transmitters_tab()
                return self.get_list_of_transmitters()
            elif _type is "receivers":
                self.open_receivers_tab()
                return self.get_list_of_receivers()
            elif _type is "receiver_groups":
                self.open_receivers_tab()
                self.open_view_receiver_groups_page()
                return self.get_list_of_receiver_groups()()
            elif _type is "channels":
                self.open_channels_tab()
                return self.get_list_of_channels()
            elif _type is "channel_groups":
                self.open_channels_tab()
                self.click_view_channel_group_button()
                return self.get_list_of_channels()
            elif _type is "servers":
                self.open_servers_tab()
                return self.get_list_of_servers()
            elif _type is "users":
                self.open_users_tab()
                return self.get_list_of_users()
            elif _type is "user_groups":
                self.open_users_tab()
                return self.open_view_user_groups_page()
                self.get_list_of_user_groups()
            elif _type is "presets":
                self.open_presets_tab()
                return self.get_list_of_presets()
            elif _type is "devices":
                self.open_device_list_directly()
                return self.get_list_of_devices()
                 
                   
    """
    Login Page BasePage
    """
    def login_as(self, username, password, remember):
        self.driver.refresh()
        self.wait.until(EC.presence_of_element_located((By.ID, "username")))
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        if remember == True:
            self.driver.find_element_by_id("remember_me").click()
        else:
            pass
        if self.driver.find_element_by_id("username").get_attribute("value") != "":
            self.driver.find_element_by_id("login").click()
        else:
            self.login_as(username, password, remember)
        
    def get_username_validation_tool_tip_text(self, state):
        xpath = "//div[contains(@class, 'form_row required " + state + "')]/div[contains(@class, 'validation_label')]"
        self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        return self.driver.find_element_by_xpath(xpath).get_attribute("title")
        
    def get_located_login_error_message(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'error_message')]")))
        return self.driver.find_element_by_xpath("//span[contains(@class, 'error_message')]").is_displayed()
    
    def get_login_error_message_text(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.message_box.mb_red.error_message")))
        return self.driver.find_element_by_css_selector("span.message_box.mb_red.error_message").text
    
    def get_located_username_input(self):
        return self.get_element_located_by_id("username")

    def get_located_password_input(self):
        return self.get_element_located_by_id("password")
    
    def get_back_ground_colour(self):
        return self.get_css_property_of_element_via_id("background-color", "login_width_1000")
    
    def get_back_ground_image(self):
        return self.get_css_property_of_element_via_xpath("background-image", "//body")
    
    def get_back_ground_repeat_property(self):
        return self.get_css_property_of_element_via_xpath("background-repeat", "//body")
    
    def get_specific_attribute_of_cell_component_via_xpath(self, element, xpath, attribute):
        return element.find_element_by_xpath(xpath).get_attribute(attribute)
    
    def get_attribute_of_element_component(self, element, attribute):
        return element.get_attribute(attribute)
    
    def get_text_of_element(self, element):
        return element.text

    def set_text_of_element(self, element, text):
        element.clear()
        element.send_keys(text)
    
    def get_text_of_element_component_via_xpath(self, element, xpath):
        return element.find_element_by_xpath(xpath).text
    
    def get_text_of_element_component_via_css_selector(self, element, selector):
        return element.find_element_by_css_selector(selector).text
    
    """
    Dashboard Page BasePage
    """
    def open_dashboard_tab(self):
        if self.get_element_located_by_link_text("DASHBOARD"):
            self.driver.find_element_by_link_text("DASHBOARD").click()
    
    def get_located_dashboard_link(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "DASHBOARD")))
            return self.driver.find_element_by_link_text("DASHBOARD").is_displayed()
        except TimeoutException:
            return False
    
    def click_dashboard_home_link(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element_by_link_text("DASHBOARD")).move_to_element(self.driver.find_element_by_link_text("Home")).click().perform()

    def click_dashboard_settings_link(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element_by_link_text("DASHBOARD")).move_to_element(self.driver.find_element_by_link_text("Home")).move_to_element(self.driver.find_element_by_link_text("Settings")).click().perform()

    def click_dashboard_backups_link(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element_by_link_text("DASHBOARD")).move_to_element(self.driver.find_element_by_link_text("Home")).move_to_element(self.driver.find_element_by_link_text("Backups")).click().perform()
    
    def click_dashboard_updates_link(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element_by_link_text("DASHBOARD")).move_to_element(self.driver.find_element_by_link_text("Home")).move_to_element(self.driver.find_element_by_link_text("Updates")).click().perform()
    
    def click_dashboard_active_connections_link(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element_by_link_text("DASHBOARD")).move_to_element(self.driver.find_element_by_link_text("Home")).move_to_element(self.driver.find_element_by_link_text("Active Connections")).click().perform()
    
    def click_dashboard_connection_log_link(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element_by_link_text("DASHBOARD")).move_to_element(self.driver.find_element_by_link_text("Home")).move_to_element(self.driver.find_element_by_link_text("Connection Log")).click().perform()
            
    def click_dashboard_event_log_link(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element_by_link_text("DASHBOARD")).move_to_element(self.driver.find_element_by_link_text("Home")).move_to_element(self.driver.find_element_by_link_text("Event Log")).click().perform()
    
    def click_dashboard_view_all_active_connects_link(self):
        if self.get_element_located_by_link_text("View all Active Connections"):
            self.driver.find_element_by_link_text("View all Active Connections").click()
            
    def click_dashboard_view_events_link(self):
        if self.get_element_located_by_link_text("View all Events"):
            self.driver.find_element_by_link_text("View all Events").click()

    def click_dashboard_view_all_channels_link(self):
        if self.get_element_located_by_link_text("View all Channels"):
            self.driver.find_element_by_link_text("View all Channels").click()

    def click_dashboard_view_all_channel_changes_link(self):
        if self.get_element_located_by_link_text("View all Channel Changes"):
            self.driver.find_element_by_link_text("View all Channel Changes").click()

    def click_dashboard_view_all_OSD_logins_link(self):
        if self.get_element_located_by_link_text("View all OSD Logins"):
            self.driver.find_element_by_link_text("View all OSD Logins").click()

    def click_dashboard_view_all_users_link(self):
        if self.get_element_located_by_link_text("View all Users"):
            self.driver.find_element_by_link_text("View all Users").click()
    
    def click_dashboard_view_all_receivers_link(self):
        if self.get_element_located_by_link_text("View all Receivers"):
            self.driver.find_element_by_link_text("View all Receivers").click()

    def click_dashboard_view_all_transmitters_link(self):
        if self.get_element_located_by_link_text("View all Transmitters"):
            self.driver.find_element_by_link_text("View all Transmitters").click()
            
    def get_located_upload_input_element(self):
        return self.get_element_located_by_id("uploaded_aim_upgrade_file")
    
    def get_receivers_from_dashboard_widget(self):
        return self.driver.find_elements_by_xpath("//div[@id='widget_receivers']//tbody/tr")

    def click_receiver_connect_via_dashboard_widget(self, element):
        element.find_element_by_xpath("./td[2]/a[2]").click()

    def click_receiver_disconnect_via_dashboard_widget(self, element):
        element.find_element_by_xpath("./td[2]/a[3]").click()
        
    def get_visibility_of_receiver_disconnect_button(self, element):
        try:
            return element.find_element_by_xpath("./td[2]/a[3]").is_displayed()
        except Exception:
            return False
    
    def get_text_from_dashboard_widget_element(self, id_, cell_xpath, not_present_text):
        try:
            if self.get_element_located_by_id(id_):
                if not self.driver.find_element_by_xpath("//div[@id='" + id_ + "']/div[2]").text == not_present_text:
                    names = []
                    rows = self.driver.find_elements_by_xpath("//div[@id='" + id_ + "']//tbody/tr")
                    for row in rows:
                        names.append(row.find_element_by_xpath(cell_xpath).text)
                    return names
        except Exception:
            names = []
            return names
    
    def get_link_text_from_dashboard_widget_element(self, id_, cell_xpath, not_present_text):
        try:
            if self.get_element_located_by_id(id_):
                if not self.driver.find_element_by_xpath("//div[@id='" + id_ + "']/div[2]").text == not_present_text:
                    links = []
                    rows = self.driver.find_elements_by_xpath("//div[@id='" + id_ + "']//tbody/tr")
                    for row in rows:
                        links.append(row.find_element_by_xpath(cell_xpath).get_attribute("href"))
                    return links
        except Exception:
            links = []
            return links
            
    def get_active_connection_user_names_from_dashboard_page(self):
        return self.get_text_from_dashboard_widget_element("widget_active_connections", "./td[3]/a", "No Active Connections")

    def get_active_connection_user_name_links_from_dashboard_page(self):
        return self.get_link_text_from_dashboard_widget_element("widget_active_connections", "./td[3]/a", "No Active Connections")

    def get_active_connection_receiver_names_from_dashboard_page(self):
        return self.get_text_from_dashboard_widget_element("widget_active_connections", "./td[4]/span/a", "No Active Connections")

    def get_active_connection_receiver_name_links_from_dashboard_page(self):
        return self.get_link_text_from_dashboard_widget_element("widget_active_connections", "./td[4]/span/a", "No Active Connections")

    def get_active_connection_channel_names_from_dashboard_page(self):
        return self.get_text_from_dashboard_widget_element("widget_active_connections", "./td[5]/a", "No Active Connections")

    def get_active_connection_channel_name_links_from_dashboard_page(self):
        return self.get_link_text_from_dashboard_widget_element("widget_active_connections", "./td[5]/a", "No Active Connections")

    def get_active_connection_preset_names_from_dashboard_page(self):
        return self.get_text_from_dashboard_widget_element("widget_active_connections", "./td[6]/a", "No Active Connections")

    def get_active_connection_preset_name_links_from_dashboard_page(self):
        return self.get_link_text_from_dashboard_widget_element("widget_active_connections", "./td[6]/a", "No Active Connections")

    def get_event_log_user_names_from_dashboard_page(self):
        return self.get_text_from_dashboard_widget_element("widget_events", "./td[6]/a", "No Active Connections")

    def get_event_log_user_name_links_from_dashboard_page(self):
        return self.get_link_text_from_dashboard_widget_element("widget_events", "./td[6]/a", "No Active Connections")

    def get_event_log_transmitter_names_from_dashboard_page(self):
        return self.get_text_from_dashboard_widget_element("widget_events", "./td[4]/a", "No Active Connections")

    def get_event_log_transmitter_name_links_from_dashboard_page(self):
        return self.get_link_text_from_dashboard_widget_element("widget_events", "./td[4]/a", "No Active Connections")

    def get_event_log_receiver_names_from_dashboard_page(self):
        return self.get_text_from_dashboard_widget_element("widget_events", "./td[5]/a", "No Active Connections")

    def get_event_log_receiver_name_links_from_dashboard_page(self):
        return self.get_link_text_from_dashboard_widget_element("widget_events", "./td[5]/a", "No Active Connections")

    def get_event_log_channel_names_from_dashboard_page(self):
        return self.get_text_from_dashboard_widget_element("widget_events", "./td[7]/a", "No Active Connections")

    def get_event_log_channel_name_links_from_dashboard_page(self):
        return self.get_link_text_from_dashboard_widget_element("widget_events", "./td[7]/a", "No Active Connections")

    def get_channel_names_from_dashboard_page(self):
        return self.get_text_from_dashboard_widget_element("widget_channels", "./td[1]/a", "No Channels found")

    def get_channel_name_links_from_dashboard_page(self):
        return self.get_link_text_from_dashboard_widget_element("widget_channels", "./td[1]/a", "No Channels found")

    def get_channel_configure_links_from_icon_on_dashboard_page(self):
        return self.get_link_text_from_dashboard_widget_element("widget_channels", "./td[2]/a[1]", "No Channels found")

    def get_channel_clone_links_from_icon_on_dashboard_page(self):
        return self.get_link_text_from_dashboard_widget_element("widget_channels", "./td[2]/a[2]", "No Channels found")
    
    def get_user_login_names_from_dashboard_page(self):
        return self.get_text_from_dashboard_widget_element("widget_user_logins", "./td[2]/a", "No Channels found")

    def get_user_login_name_links_from_dashboard_page(self):
        return self.get_link_text_from_dashboard_widget_element("widget_user_logins", "./td[1]/a", "No Channels found")
    
    def get_user_login_configure_links_from_icon_on_dashboard_page(self):
        return self.get_link_text_from_dashboard_widget_element("widget_user_logins", "./td[2]/a[1]", "No Channels found")

    def get_user_login_clone_links_from_icon_on_dashboard_page(self):
        return self.get_link_text_from_dashboard_widget_element("widget_user_logins", "./td[2]/a[2]", "No Channels found")

    def get_user_registration_names_from_dashboard_page(self):
        return self.get_text_from_dashboard_widget_element("widget_users", "./td[2]/a", "No Channels found")

    def get_user_registration_name_links_from_dashboard_page(self):
        return self.get_link_text_from_dashboard_widget_element("widget_users", "./td[2]/a", "No Channels found")
    
    def get_user_registration_configure_links_from_icon_on_dashboard_page(self):
        return self.get_link_text_from_dashboard_widget_element("widget_users", "./td[3]/a[1]", "No Channels found")

    def get_user_registration_clone_links_from_icon_on_dashboard_page(self):
        return self.get_link_text_from_dashboard_widget_element("widget_users", "./td[3]/a[2]", "No Channels found")

    def get_receiver_names_from_dashboard_page(self):
        return self.get_text_from_dashboard_widget_element("widget_receivers", "./td[1]/a", "No Channels found")

    def get_receiver_name_links_from_dashboard_page(self):
        return self.get_link_text_from_dashboard_widget_element("widget_receivers", "./td[1]/a", "No Channels found")
    
    def get_receiver_configure_links_from_icon_on_dashboard_page(self):
        return self.get_link_text_from_dashboard_widget_element("widget_receivers", "./td[2]/a[1]", "No Channels found")

    def get_receiver_connect_links_from_icon_on_dashboard_page(self):
        return self.get_link_text_from_dashboard_widget_element("widget_receivers", "./td[2]/a[2]", "No Channels found")

    def get_transmitter_names_from_dashboard_page(self):
        return self.get_text_from_dashboard_widget_element("widget_transmitters", "./td[1]/a", "No Channels found")

    def get_transmitter_name_links_from_dashboard_page(self):
        return self.get_link_text_from_dashboard_widget_element("widget_transmitters", "./td[1]/a", "No Channels found")
    
    def get_transmitter_confifgure_links_from_icon_on_dashboard_page(self):
        return self.get_link_text_from_dashboard_widget_element("widget_transmitters", "./td[2]/a[1]", "No Channels found")

    def get_channel_change_user_name_from_dashboard_page(self):
        return self.get_text_from_dashboard_widget_element("widget_channel_changes", "./td[2]/a", "No Channels found")
            
    def get_channel_change_user_name_links_from_dashboard_page(self):
        return self.get_link_text_from_dashboard_widget_element("widget_channel_changes", "./td[2]/a", "No Channels found")

    def get_channel_change_receiver_name_from_dashboard_page(self):
        return self.get_text_from_dashboard_widget_element("widget_channel_changes", "./td[3]/a", "No Channels found")
            
    def get_channel_change_receiver_links_from_dashboard_page(self):
        return self.get_link_text_from_dashboard_widget_element("widget_channel_changes", "./td[3]/a", "No Channels found")

    def get_channel_change_channel_name_from_dashboard_page(self):
        return self.get_text_from_dashboard_widget_element("widget_channel_changes", "./td[4]/a", "No Channels found")
            
    def get_channel_change_channel_links_from_dashboard_page(self):
        return self.get_link_text_from_dashboard_widget_element("widget_channel_changes", "./td[4]/a", "No Channels found")
    
    def get_displayed_time_and_date(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "logout")))
        date_as_string = self.driver.find_element_by_id("logout").text
        date_as_string = date_as_string.rstrip("(admin) Logout")
        date_as_string = date_as_string.split()
        if len(date_as_string[2]) == 1:
            date_as_string[2] = "0" + date_as_string[2]
        seperator = " "
        sequence = (date_as_string[0], date_as_string[1], date_as_string[2], date_as_string[3], date_as_string[4])
        return seperator.join(sequence)
    
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
        elif int(aim_time[0]) == int(system_time[0])-1 and aim_time[1] == "59" and system_time[1] == "00":
            hour_match = True
        if hour_match:
            return hour_match
        else: raise RuntimeError("Hour Mismatch %s %s" %(aim_time[0], system_time[0]))
    
    def get_minute_comparison(self, aim_time, system_time):
        aim_time = aim_time.split(" ")
        system_time = system_time.split(" ")
        aim_time = aim_time[0].split(":")
        system_time = system_time[0].split(":")
        aim_time[1] = aim_time[1].strip(",")
        system_time[1] = system_time[1].strip(",") 
        if aim_time[1] == system_time[1] or aim_time[1] == str(int(system_time[1])+1) or aim_time[1] == str(int(system_time[1])-1):
            return True
        else: 
            raise RuntimeError("Minute Mismatch %s %s" %(aim_time[1], system_time[1]))
    
    def get_located_logout_button(self):
        return self.get_element_located_by_link_text("Logout")
    
    def get_logout_button_colour_property(self):
        return self.get_css_property_of_element_via_xpath("color", "//div[@id='logout']/a")
    
    def click_restart(self):
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Restart")))
        self.driver.find_element_by_link_text("Restart").click()

    def click_shutdown(self):
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Shutdown")))
        self.driver.find_element_by_link_text("Shutdown").click()
    
    def get_restart_aim_unit_text_from_lightbox(self):
        return self.get_lightbox_title_text()
    
    def get_shutdown_aim_unit_text_from_lightbox(self):
        return self.get_lightbox_title_text()
    
    def get_restarting_header(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/div/h1"):
            return self.get_text_of_element_via_xpath("//div[@id='admin_body']/div/h1")
    
    def wait_for_reset_to_complete(self):
        wait = WebDriverWait(self.driver, 360)
        try:
            wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div[@id='admin_body']/h1"), "Dashboard"))
        except Exception:
            self.driver.refresh()
            wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div[@id='admin_body']/h1"), "Dashboard"))
    
    def get_visibility_of_dashboard_disconnect_all(self):
        return self.get_element_located_by_css_selector("widget_active_connections > div.widget_content.nopadding > div:nth-child(1) > a")
    
    def click_dashboard_disconnect_all(self):
        if self.get_visibility_of_dashboard_disconnect_all():
            self.driver.find_element_bycss_selector("widget_active_connections > div.widget_content.nopadding > div:nth-child(1) > a").click()
    
    def get_text_of_active_connections_widget(self):
        return self.get_text_of_element_via_css("#widget_active_connections > div.widget_content.nopadding")
    
    
    """
    Dashboard Settings General
    """
                
    def click_general_settings_button(self):
        if self.get_element_located_by_link_text("General"):
            self.driver.find_element_by_link_text("General").click()
    
    def get_check_for_updates_setting(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_radio_button_label_by_name("check_for_aim_updates")
    
    def toggle_check_for_updates(self):
        self.toggle_radio_button_by_name("check_for_aim_updates")

    def get_hide_dormant_devices_setting(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_radio_button_label_by_name("ignore_dormant_devices")
    
    def toggle_hide_dormant_devices(self):
        self.toggle_radio_button_by_name("ignore_dormant_devices")

    def get_grant_all_users_exclusive_access_setting(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_radio_button_label_by_name("allow_users_exclusive_mode")
    
    def toggle_all_users_exclusive_access(self):
        self.toggle_radio_button_by_name("allow_users_exclusive_mode")

    def get_network_medium_setting(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_radio_button_label_by_name("network_medium")
    
    def toggle_network_medium(self):
        self.toggle_radio_button_by_name("network_medium")

    def get_fibre_protocol_setting(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_radio_button_label_by_name("fibre_protocol")
    
    def toggle_fibre_protocol(self):
        self.toggle_radio_button_by_name("fibre_protocol")

    def get_initial_streaming_mode_setting(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_radio_button_label_by_name("initial_streaming_mode")
    
    def toggle_initial_streaming_mode(self):
        self.toggle_radio_button_by_name("initial_streaming_mode")

    def get_api_login_required_setting(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_radio_button_label_by_name("api_login_required")
    
    def toggle_api_login_required(self):
        self.toggle_radio_button_by_name("api_login_required")
    
    def get_allow_connection_mode_options(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.driver.find_elements_by_name("allowed_channel_modes") 
    
    def get_selected_allow_connection_mode(self, index):
        self.wait_for_saving_settings_message_to_be_removed()
        options = self.driver.find_elements_by_name("allowed_channel_modes")
        return options[index].is_selected()
        
    def toggle_allow_connection_mode(self):
        self.toggle_radio_button_by_name("allowed_channel_modes")
    
    def get_osd_timeout_options(self):
        return self.get_dropdown_options_text_by_id("osd_cookie_length")
    
    def get_current_osd_timeout_selection_text(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("osd_cookie_length")
            
    def select_osd_timeout_by_label(self, label):
        self.select_dropdown_item_by_visible_text("osd_cookie_length", label)

    def get_admin_timeout_options(self):
        return self.get_dropdown_options_text_by_id("admin_cookie_length")
    
    def get_current_admin_timeout_selection_text(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("admin_cookie_length")
            
    def select_admin_timeout_by_label(self, label):
        self.select_dropdown_item_by_visible_text("admin_cookie_length", label)

    def get_anonymous_user_options(self):
        return self.get_dropdown_options_text_by_id("anon_user")
    
    def get_current_anonymous_user_selection_text(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("anon_user")
            
    def select_anonymous_user_by_label(self, label):
        self.select_dropdown_item_by_visible_text("anon_user", label)

    def get_rows_per_page_options(self):
        return self.get_dropdown_options_text_by_id("rows_per_page")
    
    def get_current_rows_per_page_selection_text(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("rows_per_page")
            
    def select_rows_per_page_by_label(self, label):
        self.select_dropdown_item_by_visible_text("rows_per_page", label)

    def get_api_anonymous_user_options(self):
        return self.get_dropdown_options_text_by_id("api_anon_user")
    
    def get_current_api_anonymous_user_selection_text(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("api_anon_user")
            
    def select_api_anonymous_user_by_label(self, label):
        self.select_dropdown_item_by_visible_text("api_anon_user", label)
       
    
    """
    Dashboard Setting Transmitters 
    """
    def click_transmitters_settings_button(self):
        if self.get_element_located_by_link_text("Transmitters"):
            self.driver.find_element_by_link_text("Transmitters").click()
    
    def get_magic_eye_options(self):
        return self.get_dropdown_options_text_by_id("magic_eye")
    
    def get_current_magic_eye_selection_text(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("magic_eye")
            
    def select_magic_eye_by_label(self, label):
        self.select_dropdown_item_by_visible_text("magic_eye", label)

    def get_ddc_options(self):
        return self.get_dropdown_options_text_by_id("ddc")
    
    def get_current_ddc_selection_text(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("ddc")
            
    def select_ddc_by_label(self, label):
        self.select_dropdown_item_by_visible_text("ddc", label)

    def get_hot_plug_detect_control_options(self):
        return self.get_dropdown_options_text_by_id("hpd")
    
    def get_current_hot_plug_detect_control_selection_text(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("hpd")
            
    def select_hot_plug_detect_control_by_label(self, label):
        self.select_dropdown_item_by_visible_text("hpd", label)

    def get_hot_plug_detect_signal_period_options(self):
        return self.get_dropdown_options_text_by_id("video_ddc_delay")
    
    def get_current_hot_plug_detect_signal_period_selection_text(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("video_ddc_delay")
            
    def select_hot_plug_detect_signal_period_by_label(self, label):
        self.select_dropdown_item_by_visible_text("video_ddc_delay", label)

    def get_background_refresh_options(self):
        return self.get_dropdown_options_text_by_id("video_br")
    
    def get_current_background_refresh_selection_text(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("video_br")
            
    def select_background_refresh_by_label(self, label):
        self.select_dropdown_item_by_visible_text("video_br", label)

    def get_colour_depth_options(self):
        return self.get_dropdown_options_text_by_id("video_bpp")
    
    def get_current_colour_depth_selection_text(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("video_bpp")
            
    def select_colour_depth_by_label(self, label):
        self.select_dropdown_item_by_visible_text("video_bpp", label)
    
    
    def get_compression_level_options(self):
        return self.get_dropdown_options_text_by_id("video_compression_combo")
    
    def get_current_compression_level_selection_text(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("video_compression_combo")
            
    def select_compression_level_by_label(self, label):
        self.select_dropdown_item_by_visible_text("video_compression_combo", label)
    
    def select_compression_minimum_by_label(self, label):
        self.select_dropdown_item_by_visible_text("video_compression_min", label)

    def select_compression_maximum_by_label(self, label):
        self.select_dropdown_item_by_visible_text("video_compression_max", label)
    
    
    def get_serial_parity_options(self):
        return self.get_dropdown_options_text_by_id("serial_parity")
    
    def get_current_serial_parity_selection_text(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("serial_parity")
            
    def select_serial_parity_by_label(self, label):
        self.select_dropdown_item_by_visible_text("serial_parity", label)

    def get_serial_data_bits_options(self):
        return self.get_dropdown_options_text_by_id("serial_data_bits")
    
    def get_current_serial_data_bits_selection_text(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("serial_data_bits")
            
    def select_serial_data_bits_by_label(self, label):
        self.select_dropdown_item_by_visible_text("serial_data_bits", label)

    def get_serial_stop_bits_options(self):
        return self.get_dropdown_options_text_by_id("serial_stop_bits")
    
    def get_current_serial_stop_bits_selection_text(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("serial_stop_bits")
            
    def select_serial_stop_bits_by_label(self, label):
        self.select_dropdown_item_by_visible_text("serial_stop_bits", label)

    def get_serial_speed_options(self):
        return self.get_dropdown_options_text_by_id("serial_speed")
    
    def get_current_serial_speed_selection_text(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("serial_speed")
            
    def select_serial_speed_by_label(self, label):
        self.select_dropdown_item_by_visible_text("serial_speed", label)
    
    def get_usb_speed_setting(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_radio_button_label_by_name("usb_speed")
    
    def toggle_usb_speed(self):
        self.toggle_radio_button_by_name("usb_speed")

    def get_usb_hub_size_setting(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_radio_button_label_by_name("usb_hub_size")
    
    def toggle_usb_hub_size(self):
        self.toggle_radio_button_by_name("usb_hub_size")

    def get_enable_dummy_boot_keyboard_setting(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_radio_button_label_by_name("fk_enable")
    
    def toggle_enable_dummy_boot_keyboard(self):
        self.toggle_radio_button_by_name("fk_enable")
    
    def get_reserved_usb_port_setting(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("usb_fixed_ports")

    def get_reserved_usb_port_options(self):
        return self.get_dropdown_options_text_by_id("usb_fixed_ports")

    def get_current_reserved_usb_port_selection_text(self):
        #self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("usb_fixed_ports")

    def select_reserved_usb_port_by_label(self, label):
        self.select_dropdown_item_by_visible_text("usb_fixed_ports", label)
    
    """
    Dashboard Setting Receiverss 
    """
    def click_receivers_settings_button(self):
        if self.get_element_located_by_link_text("Receivers"):
            self.driver.find_element_by_link_text("Receivers").click()
    
    def get_login_required_setting(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_radio_button_label_by_name("login_required")
    
    def toggle_login_required(self):
        self.toggle_radio_button_by_name("login_required")

    def get_enable_receiver_osd_alerts_setting(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_radio_button_label_by_name("osd_alerts")
    
    def toggle_enable_receiver_osd_alerts(self):
        self.toggle_radio_button_by_name("osd_alerts")
    
    def get_hid_only_setting(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_radio_button_label_by_name("hid_only")
    
    def toggle_hid_only(self):
        self.toggle_radio_button_by_name("hid_only")

    def get_disable_isochronous_endpoint_osd_alerts_setting(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_radio_button_label_by_name("isochronous_user_warning")
    
    def toggle_disable_isochronous_endpoint_osd_alerts(self):
        self.toggle_radio_button_by_name("isochronous_user_warning")

    def get_enable_isochronous_endpoint_attach_setting(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_radio_button_label_by_name("isochronous_enabled")
    
    def toggle_enable_isochronous_endpoint_attach(self):
        self.toggle_radio_button_by_name("isochronous_enabled")
    
    
    def get_audio_input_type_mode_options(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.driver.find_elements_by_name("audio_is") 
    
    def get_selected_audio_input_type(self, index):
        self.wait_for_saving_settings_message_to_be_removed()
        options = self.driver.find_elements_by_name("audio_is")
        return options[index].is_selected()
    
    def get_video_compatibility_check_options(self):
        return self.get_dropdown_options_text_by_id("video_compatibility_check")
    
    def get_current_video_compatibility_check_selection_text(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("video_compatibility_check")
            
    def select_video_compatibility_check_by_label(self, label):
        self.select_dropdown_item_by_visible_text("video_compatibility_check", label)

    def get_receiver_keyboard_country_code_options(self):
        return self.get_dropdown_options_text_by_id("keyboard_country")
    
    def get_current_receiver_keyboard_country_code_selection_text(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("keyboard_country")
            
    def select_receiver_keyboard_country_code_by_label(self, label):
        self.select_dropdown_item_by_visible_text("keyboard_country", label)
    
    def get_selected_first_osd_hotkey(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("osd_hotkey_1")

    def get_selected_second_osd_hotkey(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("osd_hotkey_2")
    
    def get_osd_hotkey_validation_icon_appearance(self):
        return self.get_css_property_of_element_via_xpath("background-image", "//div[contains(text(), 'OSD Hotkeys')]/following-sibling::div[2]")
    
    def select_second_osd_hotkey(self, label):
        self.select_dropdown_item_by_visible_text("osd_hotkey_2", label)

    def get_selected_first_shortcut_hotkey(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("shortcut_hotkey_1")

    def get_selected_second_shortcut_hotkey(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("shortcut_hotkey_2")
    
    def get_shortcut_hotkey_validation_icon_appearance(self):
        return self.get_css_property_of_element_via_xpath("background-image", "//div[contains(text(), 'Shortcut Hotkeys')]/following-sibling::div[2]")
    
    def select_second_shortcut_hotkey(self, label):
        self.select_dropdown_item_by_visible_text("shortcut_hotkey_2", label)

    def get_selected_first_last_channel_hotkey(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("last_channel_hotkey_1")

    def get_selected_second_last_channel_hotkey(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("last_channel_hotkey_2")
    
    def get_last_channel_hotkey_validation_icon_appearance(self):
        return self.get_css_property_of_element_via_xpath("background-image", "//div[contains(text(), 'Last-Channel Hotkey')]/following-sibling::div[2]")
    
    def select_second_last_channel_hotkey(self, label):
        self.select_dropdown_item_by_visible_text("last_channel_hotkey_2", label)

    def get_selected_first_view_only_mode_hotkey(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("view_only_hotkey_1")

    def get_selected_second_view_only_mode_hotkey(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("view_only_hotkey_2")
    
    def get_view_only_mode_hotkey_validation_icon_appearance(self):
        return self.get_css_property_of_element_via_xpath("background-image", "//div[contains(text(), 'View-Only Mode Hotkeys')]/following-sibling::div[2]")
    
    def select_second_view_only_mode_hotkey(self, label):
        self.select_dropdown_item_by_visible_text("view_only_hotkey_2", label)

    def get_selected_first_shared_mode_hotkey(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("shared_hotkey_1")

    def get_selected_second_shared_mode_hotkey(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("shared_hotkey_2")
    
    def get_shared_mode_hotkey_validation_icon_appearance(self):
        return self.get_css_property_of_element_via_xpath("background-image", "//div[contains(text(), 'Shared Mode Hotkeys')]/following-sibling::div[2]")
    
    def select_second_shared_mode_hotkey(self, label):
        self.select_dropdown_item_by_visible_text("shared_hotkey_2", label)

    def get_selected_first_exclusive_mode_hotkey(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("exclusive_hotkey_1")

    def get_selected_second_exclusive_mode_hotkey(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("exclusive_hotkey_2")
    
    def get_exclusive_mode_hotkey_validation_icon_appearance(self):
        return self.get_css_property_of_element_via_xpath("background-image", "//div[contains(text(), 'Exclusive Mode Hotkeys')]/following-sibling::div[2]")
    
    def select_second_exclusive_mode_hotkey(self, label):
        self.select_dropdown_item_by_visible_text("exclusive_hotkey_2", label)

    def get_selected_first_disconnect_hotkey(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("disconnect_hotkey_1")

    def get_selected_second_disconnect_hotkey(self):
        self.wait_for_saving_settings_message_to_be_removed()
        return self.get_current_selected_text_by_id("disconnect_hotkey_2")
    
    def get_disconnect_hotkey_validation_icon_appearance(self):
        return self.get_css_property_of_element_via_xpath("background-image", "//div[contains(text(), 'Disconnect Hotkeys')]/following-sibling::div[2]")
    
    def select_second_disconnect_hotkey(self, label):
        self.select_dropdown_item_by_visible_text("disconnect_hotkey_2", label)
    
    
    """
    Dashboard Setting Network
    """
    
    def click_network_settings_button(self):
        if self.get_element_located_by_link_text("Network"):
            self.driver.find_element_by_link_text("Network").click()
    
    def select_syslog_enabled(self, state):
        if state:
            self.driver.find_element_by_css_selector("#syslog_enabled_1").click()
        else:
            self.driver.find_element_by_css_selector("#syslog_enabled_0").click()
            
    
    def get_visibility_of_aim_mac_address_2_label(self, connection_type):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='eth1_" + connection_type + "_div']/div/div[contains(text(), 'AIM MAC Address 2')]")))
            return self.driver.find_element_by_xpath("//div[@id='eth1_" + connection_type + "_div']/div/div[contains(text(), 'AIM MAC Address 2')]").is_displayed()
        except Exception:
            return False                                                                                                                                              

    def get_visibility_of_aim_ip_address_2_label(self, connection_type):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='eth1_" + connection_type + "_div']/div/div[contains(text(), 'AIM IP Address 2')]")))
            return self.driver.find_element_by_xpath("//div[@id='eth1_" + connection_type + "_div']/div/div[contains(text(), 'AIM IP Address 2')]").is_displayed()
        except Exception:
            return False                                                                                                                                              

    def get_visibility_of_gateway_ip_address_label(self, connection_type):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='eth1_" + connection_type + "_div']/div/div[contains(text(), 'Gateway IP Address')]")))
            return self.driver.find_element_by_xpath("//div[@id='eth1_" + connection_type + "_div']/div/div[contains(text(), 'Gateway IP Address')]").is_displayed()
        except Exception:
            return False                                                                                                                                              

    def get_visibility_of_netmask_label(self, connection_type):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='eth1_" + connection_type + "_div']/div/div[contains(text(), 'Netmask')]")))
            return self.driver.find_element_by_xpath("//div[@id='eth1_" + connection_type + "_div']/div/div[contains(text(), 'Netmask')]").is_displayed()
        except Exception:
            return False                                                                                                                                              

    def get_visibility_of_dns_server_ip_address_label(self, connection_type):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='eth1_" + connection_type + "_div']/div/div[contains(text(), 'DNS Server IP Address')]")))
            return self.driver.find_element_by_xpath("//div[@id='eth1_" + connection_type + "_div']/div/div[contains(text(), 'DNS Server IP Address')]").is_displayed()
        except Exception:
            return False                                                                                                                                              
    
    def get_visibility_of_aim_mac_address_2_value(self, connection_type):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='eth1_" + connection_type + "_div']/div/div[contains(text(), 'AIM MAC Address 2')]")))
        return self.driver.find_element_by_xpath("//div[@id='eth1_" + connection_type + "_div']/div/div[contains(text(), 'AIM MAC Address 2')]/following-sibling::div").is_displayed()

    def get_visibility_of_aim_ip_address_2_value(self, connection_type):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='eth1_" + connection_type + "_div']/div/div[contains(text(), 'AIM IP Address 2')]")))
        return self.driver.find_element_by_xpath("//div[@id='eth1_" + connection_type + "_div']/div/div[contains(text(), 'AIM IP Address 2')]/following-sibling::div").is_displayed()

    def get_visibility_of_gateway_ip_address_value(self, connection_type):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='eth1_" + connection_type + "_div']/div/div[contains(text(), 'Gateway IP Address')]")))
        return self.driver.find_element_by_xpath("//div[@id='eth1_" + connection_type + "_div']/div/div[contains(text(), 'Gateway IP Address')]/following-sibling::div").is_displayed()

    def get_visibility_of_netmask_value(self, connection_type):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='eth1_" + connection_type + "_div']/div/div[contains(text(), 'Netmask')]")))
        return self.driver.find_element_by_xpath("//div[@id='eth1_" + connection_type + "_div']/div/div[contains(text(), 'Netmask')]/following-sibling::div").is_displayed()

    def get_visibility_of_dns_server_ip_address_value(self, connection_type):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='eth1_" + connection_type + "_div']/div/div[contains(text(), 'DNS Server IP Address')]")))
        return self.driver.find_element_by_xpath("//div[@id='eth1_" + connection_type + "_div']/div/div[contains(text(), 'DNS Server IP Address')]/following-sibling::div").is_displayed()
    
    def get_aim_mac_address_2_value(self, connection_type):
        if self.get_visibility_of_aim_mac_address_2_value(connection_type):
            return self.driver.find_element_by_xpath("//div[@id='eth1_" + connection_type + "_div']/div/div[contains(text(), 'AIM MAC Address 2')]/following-sibling::div").text
    
    def get_aim_ip_address_2_value(self, connection_type):
        if self.get_visibility_of_aim_ip_address_2_value(connection_type):
            return self.driver.find_element_by_xpath("//div[@id='eth1_" + connection_type + "_div']/div/div[contains(text(), 'AIM IP Address 2')]/following-sibling::div").text
            return self.driver.find_element_by_xpath("//div[@id='eth1_dhcp_div']/div/div[contains(text(), 'AIM IP Address 2')]/following-sibling::div").text
    
    def set_network_setting_ip(self, id_, address):
        self.wait.until(EC.presence_of_element_located((By.ID, id_)))
        self.set_text_of_element(self.driver.find_element_by_id(id_), address)
    
    def get_network_setting_ip_validation_icon_appearance(self, form_label):
        return self.get_css_property_of_element_via_xpath("background-image", "//div[contains(text(), '" + form_label +"')]/following-sibling::div[2]")

    def get_network_setting_ip_2_validation_icon_appearance(self, form_label):
        return self.get_css_property_of_element_via_xpath("background-image", "//div[@id='eth1_static_div']//div[contains(text(), '" + form_label +"')]/following-sibling::div[2]")
    
    def set_syslog_ip(self, address):
        self.set_network_setting_ip("ip_syslog", address)
    
    def get_syslog_ip(self):
        return self.driver.find_element_by_id("ip_syslog").get_attribute("value")
    
    def get_syslog_ip_validation_icon_appearance(self):
        return self.get_network_setting_ip_validation_icon_appearance("Syslog IP Address")

    def set_multicast_ip_base(self, address):
        self.set_network_setting_ip("multicast_ip_address_base", address)
    
    def get_multicast_ip_base(self):
        return self.driver.find_element_by_id("multicast_ip_address_base").get_attribute("value")

    def get_multicast_ip_base_validation_icon_appearance(self):
        return self.get_network_setting_ip_validation_icon_appearance("Multicast IP Base")

    def set_aim_ip(self, address):
        self.set_network_setting_ip("ip_aim_server", address)

    def get_aim_ip(self):
        return self.driver.find_element_by_id("ip_aim_server").get_attribute("value")
    
    def get_aim_ip_validation_icon_appearance(self):
        return self.get_network_setting_ip_validation_icon_appearance("AIM IP Address")

    def set_gateway_ip(self, address):
        self.set_network_setting_ip("ip_gateway", address)
    
    def get_gateway_ip_validation_icon_appearance(self):
        return self.get_network_setting_ip_validation_icon_appearance("Gateway IP Address")

    def set_netmask(self, address):
        self.set_network_setting_ip("ip_netmask", address)
    
    def get_netmask_validation_icon_appearance(self):
        return self.get_network_setting_ip_validation_icon_appearance("Netmask")

    def set_dns_server_ip(self, address):
        self.set_network_setting_ip("ip_name_server", address)
    
    def get_dns_server_ip_validation_icon_appearance(self):
        return self.get_network_setting_ip_validation_icon_appearance("DNS Server IP Address")
    
    def set_aim_ip_2(self, address):
        self.set_network_setting_ip("ip_aim_server1", address)

    def get_aim_ip_2_validation_icon_appearance(self):
        return self.get_network_setting_ip_2_validation_icon_appearance("AIM IP Address 2")

    def set_gateway_ip_2(self, address):
        self.set_network_setting_ip("ip_gateway1", address)

    def get_gateway_ip_2_validation_icon_appearance(self):
        return self.get_network_setting_ip_2_validation_icon_appearance("Gateway IP Address")

    def set_netmask_2(self, address):
        self.set_network_setting_ip("ip_netmask1", address)

    def get_netmask_2_validation_icon_appearance(self):
        return self.get_network_setting_ip_2_validation_icon_appearance("Netmask")

    def set_dns_server_ip_2(self, address):
        self.set_network_setting_ip("ip_name_server1", address)
    
    def get_dns_server_ip_2_validation_icon_appearance(self):
        return self.get_network_setting_ip_2_validation_icon_appearance("DNS Server IP Address")

    def select_radio_button_by_id(self, id_):
        clicked = False
        while(clicked == False):
            self.wait.until(EC.presence_of_element_located((By.ID, id_)))
            self.driver.find_element_by_id(id_).click()
            if self.driver.find_element_by_id(id_).is_selected():
                clicked = True
    
    def select_no_ethernet_2(self):
        self.select_radio_button_by_id("eth1_enabled_0")
    
    def select_dhcp_ethernet_2(self):
        self.select_radio_button_by_id("eth1_enabled_1")

    def select_static_ethernet_2(self):
        self.select_radio_button_by_id("eth1_enabled_2")

    def set_snmp_enabled(self, state):
        if state == "yes":
            self.select_radio_button_by_id("snmp_enabled_1")
        else:
            self.select_radio_button_by_id("snmp_enabled_0")
    
    def get_display_state_snmp_username(self):
        return self.get_element_located_by_id("snmp_username")
        
    """
    Dashboard Settings Time
    """
    def click_time_settings_button(self):
        if self.get_element_located_by_link_text("Time"):
            self.driver.find_element_by_link_text("Time").click()
    
    def select_time_zone(self, zone):
        if self.get_element_located_by_id("timezone_area"):
            select = Select(self.driver.find_element_by_id("timezone_area"))
            select.select_by_visible_text(zone)
    
    def select_time_zone_location(self, zone, location):
        self.wait.until(EC.presence_of_element_located((By.ID, "timezone_location_" + zone)))
        select = Select(self.driver.find_element_by_id("timezone_location_" + zone))
        select.select_by_visible_text(location)
        
    def get_all_time_zone_locations_texts(self, zone):
        self.wait.until(EC.presence_of_element_located((By.ID, "timezone_location_" + zone)))
        locations = []
        container = self.driver.find_element_by_id("timezone_location_" + zone)
        options = Select(container)
        options = options.options
        for option in options:
            locations.append(option.text)
        return locations
    
    def get_time_date(self):
        if self.get_element_located_by_id("date_day"):
            select = Select(self.driver.find_element_by_id("date_day"))
            date = select.first_selected_option
            return date.text
    
    def select_time_day(self, day):
        if self.get_element_located_by_id("date_day"):
            select = Select(self.driver.find_element_by_id("date_day"))
            select.select_by_visible_text(day)            
                
    def get_all_time_month_day_texts(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "date_day")))
        days = []
        container = self.driver.find_element_by_id("date_day")
        options = Select(container)
        options = options.options
        for option in options:
            days.append(option.text)
        return days
    
    def get_time_month(self):
        if self.get_element_located_by_id("date_month"):
            select = Select(self.driver.find_element_by_id("date_month"))
            month = select.first_selected_option
            return month.text
    
    def select_time_month(self, month):
        if self.get_element_located_by_id("date_month"):
            select = Select(self.driver.find_element_by_id("date_month"))
            select.select_by_visible_text(month)            

    def get_time_year(self):
        return self.get_attribute_via_id("date_year", "value")
    
    def select_time_year(self, year):
        self.set_text_of_element(self.driver.find_element_by_id("date_year"), year)          
    
    def get_time_as_string(self):
        return self.driver.find_element_by_id("logout").text
    
    def set_ntp_enabled(self, state):
        if state == "yes":
            self.select_radio_button_by_id("ntp_enabled_1")
        else:
            self.select_radio_button_by_id("ntp_enabled_0")
    
    def get_display_state_ntp_servername(self):
        return self.get_element_located_by_id("ntp_on_div")
    
    """
    Dashboard Settings Mail
    """
    def click_mail_settings_button(self):
        if self.get_element_located_by_link_text("Mail"):
            self.driver.find_element_by_link_text("Mail").click()
    
    def click_mail_enable_yes(self):
        self.click_radio_option_by_div_text_and_id("Mail Enabled?", "mail_enabled_1")
 
    def click_mail_enable_no(self):
        self.click_radio_option_by_div_text_and_id("Mail Enabled?", "mail_enabled_0")
    
    def is_server_setting_active(self, id_):
        self.wait.until(EC.presence_of_element_located((By.ID, id_)))
        return self.driver.find_element_by_id(id_).is_enabled()
    
    def is_mail_smpt_domain_name_ip_active(self):
        return self.is_server_setting_active("smtp_host")
 
    def is_mail_smpt_port_active(self):
        return self.is_server_setting_active("smtp_port")
 
    def is_mail_username_active(self):
        return self.is_server_setting_active("smtp_user")
 
    def is_mail_password_active(self):
        return self.is_server_setting_active("smtp_pass")
 
    def is_mail_alert_email_address_active(self):
        return self.is_server_setting_active("alert_email_address")
    
    
    """
    Dashboard Settings Active Directory
    """
    def click_active_directory_settings_button(self):
        if self.get_element_located_by_link_text("Active Directory"):
            self.driver.find_element_by_link_text("Active Directory").click()
    
    def click_active_directory_enable_yes(self):
        self.click_radio_option_by_div_text_and_id("AD Enabled?", "ad_enabled_1")

    def click_active_directory_enable_no(self):
        self.click_radio_option_by_div_text_and_id("AD Enabled?", "ad_enabled_0")
    
    def is_active_directory_account_suffix_active(self):
        return self.is_server_setting_active("ad_account_suffix")
    
    def is_active_directory_base_dn_active(self):
        return self.is_server_setting_active("ad_base_dn")
    
    def is_active_directory_domain_controller_active(self):
        return self.is_server_setting_active("ad_domain_controllers")
    
    def is_active_directory_username_active(self):
        return self.is_server_setting_active("ad_username")
    
    def is_active_directory_password_active(self):
        return self.is_server_setting_active("ad_password")

    def is_active_directory_sync_schedule_never_active(self):
        return self.is_server_setting_active("ad_schedule_0")
    
    def is_active_directory_sync_schedule_hourly_active(self):
        return self.is_server_setting_active("ad_schedule_1")
    
    def is_active_directory_sync_schedule_daily_active(self):
        return self.is_server_setting_active("ad_schedule_2")
    
    def is_active_directory_sync_schedule_weekly_active(self):
        return self.is_server_setting_active("ad_schedule_3")
    
    def get_text_of_mail_settings(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='tab_content_mail']/div/div")))
        return self.driver.find_element_by_xpath("//div[@id='tab_content_mail']/div/div").text
    
    """
    Dashboard Backups BasePage
    """
    def get_download_to_computer_current_setting(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "download_backup")))
        return self.driver.find_element_by_id("download_backup").is_selected()

    def click_download_to_computer(self, set_to):
        self.wait.until(EC.presence_of_element_located((By.ID, "download_backup")))
        current = self.get_download_to_computer_current_setting()
        if set_to == True:
            if current != True:
                self.driver.find_element_by_id("download_backup").click()
        elif set_to == False:
            if current == True:
                self.driver.find_element_by_id("download_backup").click()
    
    def click_settings_link(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//form[@id='backup']//a[contains(text(), 'Settings')]")))
        self.driver.find_element_by_xpath("//form[@id='backup']//a[contains(text(), 'Settings')]").click()
    
    def select_schedule_radio_option(self, id_suffix):
        self.click_radio_option_by_div_text_and_id("Schedule", "backup_schedule_" + id_suffix)
    
    def select_backup_never(self):
        self.select_schedule_radio_option("0")

    def select_backup_hourly(self):
        self.select_schedule_radio_option("1")

    def select_backup_daily(self):
        self.select_schedule_radio_option("2")

    def select_backup_weekly(self):
        self.select_schedule_radio_option("3")
    
    def is_schedule_setting_selected(self, id_suffix):
        self.wait.until(EC.presence_of_element_located((By.ID, "backup_schedule_" + id_suffix)))
        return self.driver.find_element_by_id("backup_schedule_" + id_suffix).is_selected()
    
    def is_schedule_never_selected(self):
        return self.is_schedule_setting_selected("0")

    def is_schedule_hourly_selected(self):
        return self.is_schedule_setting_selected("1")

    def is_schedule_daily_selected(self):
        return self.is_schedule_setting_selected("2")

    def is_schedule_weekly_selected(self):
        return self.is_schedule_setting_selected("3")
    
    def click_backup_now_button(self):
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Backup now")))
        self.driver.find_element_by_link_text("Backup now").click()
    
    def get_list_of_backups(self):
        backups = []
        self.wait.until(EC.presence_of_element_located((By.ID, "selected_backup")))
        select = Select(self.driver.find_element_by_id("selected_backup"))
        options = select.options
        for option in options:
            backups.append(option.text)
        return backups
    
    def wait_for_backing_up_database_message_to_be_removed(self):
        self.wait.until(EC.invisibility_of_element_located((By.ID, "backup_ajax_message")))
    
    def select_backup_via_visible_text(self, text):
        self.select_dropdown_item_by_visible_text("selected_backup", text)
    
    def click_restore_backup(self):
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Restore")))
        self.driver.find_element_by_link_text("Restore").click()
    
    def wait_for_restoring_backup_message_to_be_removed(self):
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.invisibility_of_element_located((By.ID, "restore_server_ajax_message")))
    
    def delete_backup(self, file_name):
        self.driver.execute_script("confirm_delete_backup('" + file_name + "')")
    
    def wait_for_backup_deleted_message_to_be_removed(self):
        self.wait.until(EC.invisibility_of_element_located((By.ID, "restore_server_ajax_message")))
    
    def get_filename_from_element(self, selected):
        select = Select(self.driver.find_element_by_id("selected_backup"))
        element = select.first_selected_option
        return element.get_attribute("value")
    
    def get_list_of_archives(self):
        archives = []
        self.wait.until(EC.presence_of_element_located((By.ID, "selected_archive")))
        select = Select(self.driver.find_element_by_id("selected_archive"))
        options = select.options
        for option in options:
            archives.append(option.text)
        return archives
        
    def select_archive_type_via_visible_text(self, text):
        self.select_dropdown_item_by_visible_text("log_type", text)
    
    def create_archive(self):
        self.driver.execute_script("archive_log()")
    
    def wait_for_archiving_message_to_be_removed(self):
        self.wait.until(EC.invisibility_of_element_located((By.ID, "archive_event_log_ajax_message")))
    
    def wait_for_archiving_message_to_confirm_data_saved(self):
        try:
            self.wait.until(EC.text_to_be_present_in_element_value((By.ID, "archive_event_log_ajax_message"), "Archiving log data..."))
            self.wait.until(EC.text_to_be_present_in_element_value((By.ID, "archive_event_log_ajax_message"), "Log data archived"))
            return True
        except Exception:
            return False 
    
    """
    Transmitter Page BasePage
    """
    def get_transmitters_link_element(self):
        if self.get_element_located_by_link_text("TRANSMITTERS"):
            return self.driver.find_element_by_link_text("TRANSMITTERS")
    
    def open_transmitters_tab(self):
        if self.get_element_located_by_link_text("TRANSMITTERS"):
            self.driver.find_element_by_link_text("TRANSMITTERS").click()

    def get_locals_link_element(self):
        if self.get_element_located_by_link_text("LOCALS"):
            return self.driver.find_element_by_link_text("LOCALS")
        
    def open_locals_tab(self):
        if self.get_element_located_by_link_text("LOCALS"):
            self.driver.find_element_by_link_text("LOCALS").click()
            
    def get_text_of_view_transmitters_link(self):
        return self.get_text_of_element_via_xpath("//div[@id='transmitters_links']/ul/li[1]/a")
    
    def get_text_of_update_firmware_link(self):
        return self.get_text_of_element_via_xpath("//div[@id='transmitters_links']/ul/li[2]/a")
    
    def get_list_of_transmitters(self):
        return self.get_list("transmitters")
    
    def get_total_transmitters_as_text(self):
        total = self.get_text_of_element_via_xpath("//div[@class='pagination_row']/div")
        total = total.split()
        return total[4]
    
    def get_cell_elements(self, element):
        return element.find_elements_by_tag_name("td")
    
    def get_row_id_of_transmitter(self, element):
        return self.get_attribute_of_element_component(element, "id")
    
    def get_transmitter_name(self, element):
        return self.get_text_of_element_component_via_xpath(element, "./td[2]")
    
    def get_transmitter_ip(self, element):
        ip = self.get_text_of_element_component_via_xpath(element, "./td[3]")
        if len(ip) > 11:
            ip = ip[0:11]
        return ip
    
    def get_transmitter_description(self, element):
        return self.get_text_of_element_component_via_xpath(element, "./td[8]")
    
    def get_transmitter_location(self, element):
        return self.get_text_of_element_component_via_xpath(element, "./td[9]")
    
    def get_transmitter_linktext(self, element):
        return self.get_attribute_of_element_component(element.find_element_by_xpath("./td[10]/span[1]/a"), "href")
    
    def get_transmitter_status_image_src(self, element):
        return self.check_online_status_image_src(element.find_element_by_xpath("./td[1]"))
    
    def click_transmitter_configure(self, element):
        element.find_element_by_xpath("./td[10]/span[1]/a").click()
        
    def click_transmitter_statistics(self, element):
        element.find_element_by_xpath("./td[10]/a[2]").click()
    
    def click_transmitter_reboot(self, element):
        element.find_element_by_xpath("./td[10]/span[2]/a").click()
        
    def click_transmitter_identify(self, element):
        element.find_element_by_xpath("./td[10]/a[1]").click()
    
    def check_device_version(self, element):
        return self.get_text_of_element(element)
    
    def check_for_span_type_tooltip(self, element):
        return self.get_specific_attribute_of_cell_component_via_xpath(element, "./span", "class")

    def check_for_ahref_type_tooltip(self, element):
        return self.get_specific_attribute_of_cell_component_via_xpath(element, "./a", "class")
    
    def check_device_type_image_src(self, element):
        return self.get_specific_attribute_of_cell_component_via_xpath(element, "./span[1]/img", "src")

    def check_online_status_image_src(self, element):
        time.sleep(5)
        return self.get_specific_attribute_of_cell_component_via_xpath(element, "./span[2]/img", "src")
    
    def check_form_edit_image_src(self, element):
        return self.get_specific_attribute_of_cell_component_via_xpath(element, "./img", "src")
    
    def check_configure_transmitter_image_src(self, element):
#         return self.get_specific_attribute_of_cell_component_via_xpath(element, "./a[1]/img", "src")
        return self.get_specific_attribute_of_cell_component_via_xpath(element, "./span[1]/a/img", "src")
    
    def check_refresh_arrow_image_src(self, element):
#         return self.get_specific_attribute_of_cell_component_via_xpath(element, "./a[3]/img", "src")
        return self.get_specific_attribute_of_cell_component_via_xpath(element, "./span[2]/a/img", "src")
    
    def check_identify_image_src(self, element):
#         return self.get_specific_attribute_of_cell_component_via_xpath(element, "./a[4]/img", "src")
        return self.get_specific_attribute_of_cell_component_via_xpath(element, "./span[3]/a/img", "src")
    
    def check_delete_image_src(self, element):
#         return self.get_specific_attribute_of_cell_component_via_xpath(element, "./a[5]/img", "src")
        return self.get_specific_attribute_of_cell_component_via_xpath(element, "./a/img", "src")
    
    def get_device_version_via_api(self):
        device_info = {}
        request = requests.get("%s/api/?v=2.3&method=login&username=admin&password=password"%(self.baseurl))
        parsed_response = parseString(request.text)
        token = parsed_response.getElementsByTagName("token")[0].firstChild.nodeValue
        request = requests.get("%s/api/?v=2.3&method=get_devices&token=%s&show_all=1"%(self.baseurl, token))
        parsed_response = parseString(request.text)    
        devices = parsed_response.getElementsByTagName("device")
        for device in devices:
            ids = device.getElementsByTagName("d_id")
            versions = device.getElementsByTagName("d_version")
            device_info[ids[0].firstChild.nodeValue] = versions[0].firstChild.nodeValue
        return device_info
    
    def get_device_id_from_row_id(self, row_id):
        row_id = row_id.replace("row_id_", "")
        return row_id
    
    def open_update_transmitter_firmware_page(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_transmitters_link_element()).move_to_element(self.driver.find_element_by_xpath("//div[@id='transmitters_links']/ul//li/a[contains(text(), 'Update Firmware')]")).click().perform()

    def open_update_local_firmware_page(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_locals_link_element()).move_by_offset(0, 19).move_to_element(self.driver.find_element_by_xpath("//div[@id='transmitters_links']/ul//li/a[contains(text(), 'Update Firmware')]")).click().perform()
        
    def open_view_transmitters_page(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_transmitters_link_element()).move_to_element(self.driver.find_element_by_xpath("//div[@id='transmitters_links']/ul//li/a[contains(text(), 'Update Firmware')]")).move_to_element(self.driver.find_element_by_xpath("//div[@id='transmitters_links']/ul//li/a[contains(text(), 'View Transmitters')]")).click().perform()

    def open_view_locals_page(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_locals_link_element()).move_by_offset(0, 19).move_to_element(self.driver.find_element_by_xpath("//div[@id='transmitters_links']/ul//li/a[contains(text(), 'Update Firmware')]")).move_to_element(self.driver.find_element_by_xpath("//div[@id='transmitters_links']/ul//li/a[contains(text(), 'View Locals')]")).click().perform()
    
    def get_located_name_search_field(self):
        return self.get_element_located_by_id("filter_d_name")
        
    def send_filter_term_to_element(self, id_, term):
        self.enter_text_into_input_field(id_, term)
    
    def send_search_term_to_transmitter_name_field(self, term):
        self.send_filter_term_to_element("filter_d_name", term)

    def send_search_term_to_transmitter_description_field(self, term):
        self.send_filter_term_to_element("filter_d_description", term)
    
    def send_search_term_to_transmitter_location_field(self, term):
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
        if self.get_element_located_by_link_text("Remove Filters"):
            self.driver.find_element_by_link_text("Remove Filters").click()
            
    def click_on_ascend_transmitter_names(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[2]/a[1]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[2]/a[1]").click()

    def click_on_decend_transmitter_names(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[2]/a[2]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[2]/a[2]").click()

    def click_on_ascend_transmitter_descriptions(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[8]/a[1]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[8]/a[1]").click()

    def click_on_decend_transmitter_descriptions(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[8]/a[2]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[8]/a[2]").click()

    def click_on_ascend_transmitter_locations(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[9]/a[1]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[9]/a[1]").click()

    def click_on_decend_transmitter_locations(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[9]/a[2]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[9]/a[2]").click()
            
    def wait_for_and_click_reboot_confirm(self):
        wait = WebDriverWait(self.driver, 120)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Reboot")))
        self.driver.find_element_by_link_text("Reboot").click()
        
    def wait_for_and_click_reset_confirm(self):
        wait = WebDriverWait(self.driver, 120)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Factory Reset")))
        self.driver.find_element_by_link_text("Factory Reset").click()

    def wait_for_and_click_reboot_cancel(self):
        wait = WebDriverWait(self.driver, 120)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Cancel")))
        self.driver.find_element_by_link_text("Cancel").click()
        
    def wait_for_transmitter_added_message(self):
        wait = WebDriverWait(self.driver, 120)
        wait.until(EC.text_to_be_present_in_element((By.XPATH, "//span[@id='warnings']/span"), "1 new Transmitter added. Configure"))
        
    def wait_for_transmitter_rebooting_message(self):
        wait = WebDriverWait(self.driver, 180)
        wait.until(EC.text_to_be_present_in_element((By.XPATH, "//span[@id='warnings']/span"), "1 Transmitter currently offline"))
        
    def wait_for_rebooting_message_to_be_removed(self):
        wait = WebDriverWait(self.driver, 120)
        wait.until(EC.invisibility_of_element_located((By.XPATH, "//span[@id='warnings']/span/a")))
    
    def get_located_search_by_name(self):
        return self.get_element_located_by_id("filter_d_name")    
        
    def get_located_search_by_description(self):
        return self.get_element_located_by_id("filter_d_description")    
        
    def get_located_search_by_location(self):
        return self.get_element_located_by_id("filter_d_location")    
        
        
    """
    Transmitter Configure BasePage
    """
    def get_located_configure_devices_link(self):
        if self.get_element_located_by_link_text("Configure"):
            return self.driver.find_element_by_link_text("Configure").is_displayed()
    
    def click_configure_devices_link(self):
        if self.get_located_configure_devices_link():
            self.driver.find_element_by_link_text("Configure").click()
    
    def assign_new_ip_address(self, id_, message_id):
        self.wait.until(EC.presence_of_element_located((By.ID, id_)))
        counter = 1
        error = True
        while(error == True):
            old_ip = self.driver.find_element_by_id(id_).get_attribute("value")
            new_ip = old_ip.replace("169.254.1", "10.10.10")
            new_ip = new_ip.split(".")
            new_ip[3] = str(int(new_ip[3]) + counter)
            if new_ip[3] == "254":
                new_ip[3] = "33"
            seperator = "."
            new_ip = seperator.join((new_ip[0], new_ip[1], new_ip[2], new_ip[3],))
            self.driver.find_element_by_id(id_).clear()
            self.driver.find_element_by_id(id_).send_keys(new_ip)
            self.driver.find_element_by_link_text("Save").click()
            error = self.get_element_located_by_id(message_id)
        return new_ip
        
    def get_device_id_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            return self.get_text_of_element_via_xpath("//div[contains(text(), 'Device ID')]/following-sibling::div")
        
    def get_online_img_src_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            return self.get_attribute_via_xpath("//div[contains(text(), 'Online?')]/following-sibling::div/span/img", "src")

    def get_date_added_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            return self.get_text_of_element_via_xpath("//div[contains(text(), 'Date Added')]/following-sibling::div")

    def get_mac_address_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            return self.get_text_of_element_via_xpath("//div[contains(text(), 'MAC Address')]/following-sibling::div")

    def get_main_firmware_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            return self.get_text_of_element_via_xpath("//div[contains(text(), 'Main Firmware')]/following-sibling::div")

    def get_backup_firmware_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            return self.get_text_of_element_via_xpath("//div[contains(text(), 'Backup Firmware')]/following-sibling::div")

    def get_ip_address_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            return self.get_attribute_via_xpath("//div[contains(text(), 'IP Address')]/following-sibling::div/input", "value")

    def get_ip_help_text_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            return self.get_text_of_element_via_xpath("//div[contains(text(), 'IP Address')]/following-sibling::div[3]")
    
    def is_radio_selected_by_id(self, id_):
        return self.wait.until(EC.presence_of_element_located((By.ID, id_))).is_selected()

    def is_option_selected_by_div_text_and_id(self, div_text, id_):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), '" + div_text + "')]/following-sibling::div/ul/li/input[@id='" + id_ + "']")))
        return self.driver.find_element_by_xpath("//div[contains(text(), '" + div_text + "')]/following-sibling::div/ul/li/input[@id='" + id_ + "']").is_selected()
    
    def is_option_selected_by_div_text_and_expected_text(self, div_text, expected_text):
        return self.driver.find_element_by_xpath("//div[contains(text(), '" + div_text + "')]/following-sibling::div/select/option[contains(text(), '" + expected_text + "')]").is_selected()

    def is_option_selected_by_div_text_and_value(self, div_text, value):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), '" + div_text + "')]")))
        return self.driver.find_element_by_xpath("//div[contains(text(), '" + div_text + "')]/following-sibling::div/select/option[@value='" + value + "']").is_selected()
    
    def is_option_selected_by_div_text_and_text(self, div_text, text):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), '" + div_text + "')]")))
        return self.driver.find_element_by_xpath("//div[contains(text(), '" + div_text + "')]/following-sibling::div/select/option[(text()='" + text + "')]").is_selected()
    
    def find_selected_option_by_div_text(self, div_text):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), '" + div_text + "')]")))
        return Select(self.driver.find_element_by_xpath("//div[contains(text(), '" + div_text + "')]/following-sibling::div/select")).first_selected_option

    def find_selected_option_by_id(self, id_):
        self.wait.until(EC.presence_of_element_located((By.ID, id_)))
        return Select(self.driver.find_element_by_id(id_)).first_selected_option
        
    def click_radio_button_by_id(self, id_):
        clicked = False
        while(clicked == False):
            self.wait.until(EC.presence_of_element_located((By.ID, id_))).click()
            if self.driver.find_element_by_id(id_).is_selected():
                clicked = True
    
    def click_radio_option_by_div_text_and_id(self, div_text, id_):
        clicked = False
        while(clicked == False):
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), '" + div_text + "')]/following-sibling::div/ul/li/input[@id='" + id_ + "']")))
            self.driver.find_element_by_xpath("//div[contains(text(), '" + div_text + "')]/following-sibling::div/ul/li/input[@id='" + id_ + "']").click()
            if self.is_option_selected_by_div_text_and_id(div_text, id_):
                clicked = True
                
    def get_option_label(self, div_text, postion):
        return self.get_text_of_element_via_xpath("//div[contains(text(), '" + div_text + "')]/following-sibling::div/ul/li[" + postion + "]/label")
    
    def get_option_label_by_value(self, div_text, value):
        return self.get_text_of_element_via_xpath("//div[contains(text(), '" + div_text + "')]/following-sibling::div/select/option[@value='" + value + "']")
    
    def ensure_dummy_keyboard_default_correct(self):
        if self.get_element_located_by_id("configure_device"):
            return self.is_option_selected_by_div_text_and_id("Enable Dummy Boot Keyboard", "tp_fk_enable_-1")

    def get_label_of_dummy_keyboard_radio_one(self):
        if self.get_element_located_by_id("configure_device"):
            return self.get_option_label("Enable Dummy Boot Keyboard", "1")

    def get_label_of_dummy_keyboard_radio_two(self):
        if self.get_element_located_by_id("configure_device"):
            return self.get_option_label("Enable Dummy Boot Keyboard", "2")
    
    def get_label_of_dummy_keyboard_radio_three(self):
        if self.get_element_located_by_id("configure_device"):
            return self.get_option_label("Enable Dummy Boot Keyboard", "3")
        
    def select_dummy_boot_keyboard_global(self):
        self.click_radio_option_by_div_text_and_id("Enable Dummy Boot Keyboard", "tp_fk_enable_-1")
        
    def select_dummy_boot_keyboard_no(self):
        self.click_radio_option_by_div_text_and_id("Enable Dummy Boot Keyboard", "tp_fk_enable_0")
        
    def select_dummy_boot_keyboard_yes(self):
        self.click_radio_option_by_div_text_and_id("Enable Dummy Boot Keyboard", "tp_fk_enable_1")

    def get_dummy_keyboard_help_text_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            return self.get_text_of_element_via_xpath("//div[contains(text(), 'Enable Dummy Boot Keyboard')]/following-sibling::div[3]")

    def ensure_usb_speed_default_correct(self):
        if self.get_element_located_by_id("configure_device"):
            return self.is_option_selected_by_div_text_and_id("USB Speed", "tp_usb_speed_-1")

    def get_label_of_usb_speed_radio_one(self):
        if self.get_element_located_by_id("configure_device"):
            return self.get_option_label("USB Speed", "1")

    def get_label_of_usb_speed_radio_two(self):
        if self.get_element_located_by_id("configure_device"):
            return self.get_option_label("USB Speed", "2")
    
    def get_label_of_usb_speed_radio_three(self):
        if self.get_element_located_by_id("configure_device"):
            return self.get_option_label("USB Speed", "3")

    def select_usb_speed_global(self):
        self.click_radio_option_by_div_text_and_id("USB Speed", "tp_usb_speed_-1")
        
    def select_usb_speed_high_speed(self):
        self.click_radio_option_by_div_text_and_id("USB Speed", "tp_usb_speed_0")
        
    def select_usb_speed_full_speed(self):
        self.click_radio_option_by_div_text_and_id("USB Speed", "tp_usb_speed_1")

    def get_usb_speed_help_text_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            return self.get_text_of_element_via_xpath("//div[contains(text(), 'USB Speed')]/following-sibling::div[3]")

    def ensure_usb_hub_default_correct(self):
        if self.get_element_located_by_id("configure_device"):
            return self.is_option_selected_by_div_text_and_id("USB Hub Size", "tp_usb_hub_size_-1")
        
    def get_label_of_usb_hub_radio_one(self):
        if self.get_element_located_by_id("configure_device"):
            return self.get_option_label("USB Hub Size", "1")

    def get_label_of_usb_hub_radio_two(self):
        if self.get_element_located_by_id("configure_device"):
            return self.get_option_label("USB Hub Size", "2")
    
    def get_label_of_usb_hub_radio_three(self):
        if self.get_element_located_by_id("configure_device"):
            return self.get_option_label("USB Hub Size", "3")

    def get_usb_hub_help_text_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            return self.get_text_of_element_via_xpath("//div[contains(text(), 'USB Hub Size')]/following-sibling::div[3]")

    def get_bandwidth_limit_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            return self.get_text_of_element_via_xpath("//div[contains(text(), 'Peak Bandwidth Limiter')]/following-sibling::div/div[2]")

    def ensure_selected_DDC_setting_from_config_page_correct(self):
        if self.get_element_located_by_id("configure_device"):
            return self.is_option_selected_by_div_text_and_expected_text("DDC", "USE GLOBAL SETTING")
    
    def get_ddc_option_label(self, value):
        if self.get_element_located_by_id("configure_device"):
            return self.get_option_label_by_value("DDC", value)

    def get_ddc_help_text_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            return self.get_text_of_element_via_xpath("//div[contains(text(), 'DDC')]/following-sibling::div[3]")
        
    def ensure_selected_hot_plug_setting_from_config_page_correct(self):
        if self.get_element_located_by_id("configure_device"):
            return self.is_option_selected_by_div_text_and_expected_text("Hot Plug Detect Control", "USE GLOBAL SETTING")

    def get_hot_plug_option_label(self, value):
        if self.get_element_located_by_id("configure_device"):
            return self.get_option_label_by_value("Hot Plug Detect Control", value)

    def get_hot_plug_signal_text_from_config_page_text_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            return self.get_text_of_element_via_xpath("//div[contains(text(), 'Hot Plug Detect Control')]/following-sibling::div[3]")
        
    def ensure_selected_hot_plug_signal_setting_from_config_page_correct(self):
        if self.get_element_located_by_id("configure_device"):
            return self.is_option_selected_by_div_text_and_expected_text("Hot Plug Detect Signal Period", "USE GLOBAL SETTING")

    def get_hot_plug_signal_option_label(self, value):
        if self.get_element_located_by_id("configure_device"):
            return self.get_option_label_by_value("Hot Plug Detect Signal Period", value)

    def get_hot_plug_signal_help_text_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            return self.get_text_of_element_via_xpath("//div[contains(text(), 'Hot Plug Detect Signal Period')]/following-sibling::div[3]")

    def ensure_selected_back_ground_refresh_setting_from_config_page_correct(self):
        if self.get_element_located_by_id("configure_device"):
            return self.is_option_selected_by_div_text_and_expected_text("Background Refresh", "USE GLOBAL SETTING")

    def get_background_refresh_option_label(self, value):
        if self.get_element_located_by_id("configure_device"):
            return self.get_option_label_by_value("Background Refresh", value)

    def ensure_selected_colour_depth_setting_from_config_page_correct(self):
        if self.get_element_located_by_id("configure_device"):
            return self.is_option_selected_by_div_text_and_expected_text("Colour Depth", "USE GLOBAL SETTING")

    def get_colour_depth_option_label(self, value):
        if self.get_element_located_by_id("configure_device"):
            return self.get_option_label_by_value("Colour Depth", value)

    def get_frame_skipping_label_from_config_page(self):
        if self.get_element_located_by_id("configure_device"):
            return self.get_text_of_element_via_xpath("//div[contains(text(), 'Frame Skipping')]/following-sibling::div/div[2]")

    def ensure_selected_serial_parity_setting_from_config_page_correct(self):
        if self.get_element_located_by_id("configure_device"):
            return self.is_option_selected_by_div_text_and_expected_text("Serial Parity", "USE GLOBAL SETTING")

    def get_serial_parity_option_label(self, value):
        if self.get_element_located_by_id("configure_device"):
            return self.get_option_label_by_value("Serial Parity", value)

    def ensure_selected_serial_data_setting_from_config_page_correct(self):
        if self.get_element_located_by_id("configure_device"):
            return self.is_option_selected_by_div_text_and_expected_text("Serial Data Bits", "USE GLOBAL SETTING")

    def get_serial_data_option_label(self, value):
        if self.get_element_located_by_id("configure_device"):
            return self.get_option_label_by_value("Serial Data Bits", value)

    def ensure_selected_serial_stop_setting_from_config_page_correct(self):
        if self.get_element_located_by_id("configure_device"):
            return self.is_option_selected_by_div_text_and_expected_text("Serial Stop Bits", "USE GLOBAL SETTING")

    def get_serial_stop_option_label(self, value):
        if self.get_element_located_by_id("configure_device"):
            return self.get_option_label_by_value("Serial Stop Bits", value)

    def ensure_selected_serial_speed_setting_from_config_page_correct(self):
        if self.get_element_located_by_id("configure_device"):
            return self.is_option_selected_by_div_text_and_expected_text("Serial Speed", "USE GLOBAL SETTING")

    def get_serial_speed_option_label(self, value):
        if self.get_element_located_by_id("configure_device"):
            return self.get_option_label_by_value("Serial Speed", value)
    
    def set_transmitter_ip_via_config_page(self, new_ip):
        if self.get_element_located_by_id("configure_device"):
            self.enter_text_into_input_field("d_ip_address", new_ip)

    def get_transmitter_name_from_config_page(self):
        if self.get_element_located_by_id("d_name"):
            return self.get_attribute_of_element_component(self.driver.find_element_by_id("d_name"), "value")

    def set_transmitter_name_via_config_page(self, text):
        if self.get_element_located_by_id("d_name"):
            self.enter_text_into_input_field("d_name", text)

    def get_transmitter_description_from_config_page(self):
        if self.get_element_located_by_id("d_description"):
            return self.get_attribute_of_element_component(self.driver.find_element_by_id("d_description"), "value")

    def set_transmitter_description_via_config_page(self, text):
        if self.get_element_located_by_id("d_description"):
            self.enter_text_into_input_field("d_description", text)

    def get_transmitter_location_from_config_page(self):
        if self.get_element_located_by_id("d_location"):
            return self.get_attribute_of_element_component(self.driver.find_element_by_id("d_location"), "value")

    def set_transmitter_location_via_config_page(self, text):
        if self.get_element_located_by_id("d_location"):
            self.enter_text_into_input_field("d_location", text)
            
    def get_lightbox_title_text(self):
        return self.get_text_of_element_via_xpath("//div[@id='ibox']//div[@id='ibox_wrapper']//div[@class='lightbox_title']")
        
    def click_lightbox_ok_button(self):
        if self.get_element_located_by_id("ibox"):
            self.driver.find_element_by_link_text("OK").click()
    
    def confirm_no_longer_on_transmitter_config_page(self):
        found = False
        while(found == False):
            if not self.get_text_of_page_header() == "Transmitters > Configure Transmitter":
                found = True


    """
    Channels Page BasePage
    """
    def get_channels_link_element(self):
        if self.get_element_located_by_link_text("CHANNELS"):
            return self.driver.find_element_by_link_text("CHANNELS")
    
    def open_channels_tab(self):
        if self.get_element_located_by_link_text("CHANNELS"):
            self.driver.find_element_by_link_text("CHANNELS").click()
    
    def click_view_channels_subtab_link(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_channels_link_element()).move_to_element(self.driver.find_element_by_xpath("//div[@id='channels_links']/ul//li/a[contains(text(), 'Add Channel')]")).move_to_element(self.driver.find_element_by_xpath("//div[@id='channels_links']/ul//li/a[contains(text(), 'View Channel')]")).click().perform()

    def click_add_channel_subtab_link(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_channels_link_element()).move_to_element(self.driver.find_element_by_xpath("//div[@id='channels_links']/ul//li/a[contains(text(), 'Add Channel')]")).click().perform()
    
    def click_view_channel_groups_subtab_link(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_channels_link_element()).move_to_element(self.driver.find_element_by_xpath("//div[@id='channels_links']/ul//li/a[contains(text(), 'Add Channel')]")).move_to_element(self.driver.find_element_by_xpath("//div[@id='channels_links']/ul//li/a[contains(text(), 'View Channel Groups')]")).click().perform()

    def click_add_channel_group_subtab_link(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_channels_link_element()).move_to_element(self.driver.find_element_by_xpath("//div[@id='channels_links']/ul//li/a[contains(text(), 'Add Channel')]")).move_to_element(self.driver.find_element_by_xpath("//div[@id='channels_links']/ul//li/a[contains(text(), 'Add Channel Group')]")).click().perform()

    def click_batch_delete_mode(self):
        if self.get_element_located_by_id("toggle_batch_delete_button"):
            self.driver.find_element_by_id("toggle_batch_delete_button").click()
    
    def check_for_batch_delete_checkbox(self):
        return self.get_element_located_by_id("toggle_delete_checkbox")

    def check_for_batch_delete_checkbox_for_channel_element(self, element):
        return element.find_element_by_xpath("./td[8]/input").is_displayed()
    
    def click_batch_delete_selector_for_channel_element(self, element):
        element.find_element_by_xpath("./td[8]/input").click()

    def check_for_batch_delete_checkbox_for_channel_group_element(self, element):
        return element.find_element_by_xpath("./td[5]/input").is_displayed()
    
    def click_batch_delete_selector_for_channel_group_element(self, element):
        element.find_element_by_xpath("./td[5]/input").click()
        
    def click_batch_delete_channels(self):
        if self.get_element_located_by_link_text("Delete selected channels"):
            self.driver.find_element_by_link_text("Delete selected channels").click()

    def click_batch_delete_channel_groups(self):
        if self.get_element_located_by_link_text("Delete selected channel groups"):
            self.driver.find_element_by_link_text("Delete selected channel groups").click()

    def click_add_channel_button(self):
        if self.get_element_located_by_xpath("//div[@class='button_wrapper']/a/span[contains(text(), 'Add Channel')]"):
            self.driver.find_element_by_xpath("//div[@class='button_wrapper']/a/span[contains(text(), 'Add Channel')]").click()
    
    def click_view_channel_group_button(self):
        if self.get_element_located_by_xpath("//div[@class='button_wrapper']/a/span[contains(text(), 'View Channel Groups')]"):
            self.driver.find_element_by_xpath("//div[@class='button_wrapper']/a/span[contains(text(), 'View Channel Groups')]").click()
    
    def click_add_channel_group_button(self):
        if self.get_element_located_by_xpath("//span/img[@alt='Add channel group']"):
            self.driver.find_element_by_xpath("//span/img[@alt='Add channel group']").click()
    
    def get_list_of_channels(self):
        return self.get_list("channels")

    def get_list_of_channel_groups(self):
        return self.get_list("channel_groups")
    
    def get_channel_name(self, element):
        return self.get_text_of_element_component_via_xpath(element, "./td[1]")

    def get_channel_group_name(self, element):
        return self.get_text_of_element_component_via_xpath(element, "./td[1]")

    def get_channel_description(self, element):
        return self.get_text_of_element_component_via_xpath(element, "./td[6]")

    def get_channel_group_description(self, element):
        return self.get_text_of_element_component_via_xpath(element, "./td[2]")
    
    def get_channel_location(self, element):
        return self.get_text_of_element_component_via_xpath(element, "./td[7]")
    
    def get_channel_connection_img_src(self, element):
        images = element.find_elements_by_xpath("./td[2]/img")
        sources = []
        for image in images:
            source = self.get_attribute_of_element_component(image, "src")
            sources.append(source)
        return sources
    
    def send_search_term_to_channel_name_field(self, term):
        self.send_filter_term_to_element("filter_c_name", term)

    def send_search_term_to_channel_group_name_field(self, term):
        self.send_filter_term_to_element("filter_cg_name", term)

    def send_search_term_to_channel_description_field(self, term):
        self.send_filter_term_to_element("filter_c_description", term)

    def send_search_term_to_channel_group_description_field(self, term):
        self.send_filter_term_to_element("filter_cg_description", term)
    
    def send_search_term_to_channel_location_field(self, term):
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
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[1]/a[1]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[1]/a[1]").click()

    def click_on_decend_channel_names(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[1]/a[2]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[1]/a[2]").click()

    def click_on_ascend_channel_group_names(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[1]/a[1]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[1]/a[1]").click()

    def click_on_decend_channel_group_names(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[1]/a[2]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[1]/a[2]").click()

    def click_on_ascend_channel_descriptions(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[6]/a[1]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[6]/a[1]").click()

    def click_on_decend_channel_descriptions(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[6]/a[2]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[6]/a[2]").click()

    def click_on_ascend_channel_group_descriptions(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[2]/a[1]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[2]/a[1]").click()

    def click_on_decend_channel_group_descriptions(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[2]/a[2]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[2]/a[2]").click()

    def click_on_ascend_channel_locations(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[7]/a[1]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[7]/a[1]").click()

    def click_on_decend_channel_locations(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[7]/a[2]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[7]/a[2]").click()
    
    def click_configure_channel(self, element):
        element.find_element_by_xpath("./td[8]/a[1]").click()

    def click_configure_channel_group(self, element):
        element.find_element_by_xpath("./td[5]/a[1]").click()
    
    def get_channel_config_linktext(self, element):
        return self.get_attribute_of_element_component(element.find_element_by_xpath("./td[8]/a[1]"), "href")

    def get_channel_group_config_linktext(self, element):
        return self.get_attribute_of_element_component(element.find_element_by_xpath("./td[5]/a[1]"), "href")

    def get_channel_clone_linktext(self, element):
        return self.get_attribute_of_element_component(element.find_element_by_xpath("./td[8]/a[2]"), "href")

    def get_channel_group_clone_linktext(self, element):
        return self.get_attribute_of_element_component(element.find_element_by_xpath("./td[5]/a[2]"), "href")
    
    def click_channel_delete(self, element):
        element.find_element_by_xpath("./td[8]/a[3]").click()

    def click_channel_group_delete(self, element):
        element.find_element_by_xpath("./td[5]/a[3]").click()

    def click_channel_clone(self, element):
        element.find_element_by_xpath("./td[8]/a[2]").click()

    def click_channel_group_clone(self, element):
        element.find_element_by_xpath("./td[5]/a[2]").click()
        
    def click_on_connect_receiver_to_channel_view_only(self, element):
        element.find_element_by_xpath("./td[4]/a[1]").click() 
    
    def click_on_connect_receiver_to_channel_shared_access(self, element):
        element.find_element_by_xpath("./td[4]/a[2]").click() 
    
    def click_on_connect_receiver_to_channel_exclusive_only(self, element):
        element.find_element_by_xpath("./td[4]/a[3]").click() 
    
    def get_delete_channel_text_from_lightbox(self):
        return self.get_lightbox_title_text()
    
    def click_lightbox_cancel_button(self):
        if self.get_element_located_by_id("ibox"):
            self.driver.find_element_by_link_text("Cancel").click()
    
    def click_lightbox_delete_button(self):
        if self.get_element_located_by_id("ibox"):
            self.driver.find_element_by_link_text("Delete").click()
            found = True
            while(found == True):
                if self.check_lightbox_visibility() == False:
                    found = False

    def click_lightbox_disconnect_button(self):
#         Had to use direct URL as clicking button via webdriver would not disconnect
        if self.get_element_located_by_id("ibox"):
            self.driver.get(self.baseurl + "/admin/process_disconnect_all.php?r=%2Fadmin%2Fdevices.php%3Ft%3Drx")

    def open_restart_url(self):
#         Had to use direct URL as clicking button via webdriver would not start restart procedure
        if self.get_element_located_by_id("ibox"):
            self.driver.get(self.baseurl + "/admin/process_power.php?mode=restart")
            
    def check_lightbox_visibility(self):
        time.sleep(1)
        return self.get_element_located_by_id("ibox_overlay")
    
    def confirm_no_longer_on_clone_channel_page(self):
        found = False
        while(found == False):
            if not self.get_text_of_page_header() == "Channels > Configure Cloned Channel":
                found = True

    def confirm_no_longer_on_clone_channel_group_page(self):
        found = False
        while(found == False):
            if not self.get_text_of_page_header() == "Channel Groups > Configure Cloned Channel Group":
                found = True

    def confirm_no_longer_on_configure_channel_group_page(self):
        found = False
        while(found == False):
            if not self.get_text_of_page_header() == "Channel Groups > Configure Channel Group":
                found = True

    def confirm_no_longer_on_configure_channel_page(self):
        found = False
        while(found == False):
            if not self.get_text_of_page_header() == "Channels > Configure Channel":
                found = True

    def confirm_no_longer_on_add_channel_page(self):
        found = False
        while(found == False):
            if not self.get_text_of_page_header() == "Channels > Add Channel":
                found = True
    
   
    """
    Configure Channel BasePage
    """
    def get_channel_name_from_config_page(self):
        if self.get_element_located_by_id("c_name"):
            return self.get_attribute_of_element_component(self.driver.find_element_by_id("c_name"), "value")

    def set_channel_name_via_config_page(self, text):
        if self.get_element_located_by_id("c_name"):
            self.enter_text_into_input_field("c_name", text)
        
    def get_channel_group_name_from_config_page(self):
        if self.get_element_located_by_id("cg_name"):
            return self.get_attribute_of_element_component(self.driver.find_element_by_id("cg_name"), "value")

    def set_channel_group_name_via_config_page(self, text):
        if self.get_element_located_by_id("cg_name"):
            self.enter_text_into_input_field("cg_name", text)

    def get_channel_description_from_config_page(self):
        if self.get_element_located_by_id("c_description"):
            return self.get_attribute_of_element_component(self.driver.find_element_by_id("c_description"), "value")

    def set_channel_description_via_config_page(self, text):
        if self.get_element_located_by_id("c_description"):
            self.enter_text_into_input_field("c_description", text)

    def get_channel_group_description_from_config_page(self):
        if self.get_element_located_by_id("cg_description"):
            return self.get_attribute_of_element_component(self.driver.find_element_by_id("cg_description"), "value")

    def set_channel_group_description_via_config_page(self, text):
        if self.get_element_located_by_id("cg_description"):
            self.enter_text_into_input_field("cg_description", text)

    def get_channel_location_from_config_page(self):
        if self.get_element_located_by_id("c_location"):
            return self.get_attribute_of_element_component(self.driver.find_element_by_id("c_location"), "value")

    def set_channel_location_via_config_page(self, text):
        if self.get_element_located_by_id("c_location"):
            self.enter_text_into_input_field("c_location", text)
    
    def get_selected_video_source(self):
        selected = self.find_selected_option_by_id("video_e_id")
        text = selected.text
        return text
    
    def is_channel_video_source(self, text):
        return self.is_option_selected_by_div_text_and_text("Video 1", text)
        
    def set_channel_video_source(self, index):
        self.wait.until(EC.presence_of_element_located((By.ID, "video_e_id")))
        select = Select(self.driver.find_element(By.ID, "video_e_id"))
        select.select_by_index(index)

    def set_channel_video_source_by_visible_text(self, text):
        self.wait.until(EC.presence_of_element_located((By.ID, "video_e_id")))
        select = Select(self.driver.find_element(By.ID, "video_e_id"))
        select.select_by_visible_text(text)

    def reset_channel_video_source(self, text):
        self.wait.until(EC.presence_of_element_located((By.ID, "video_e_id")))
        select = Select(self.driver.find_element(By.ID, "video_e_id"))
        select.select_by_visible_text(text)
    
    def get_selected_video2_source(self):
        selected = self.find_selected_option_by_id("video1_e_id")
        text = selected.text
        return text
    
    def is_channel_video2_source(self, text):
        return self.is_option_selected_by_div_text_and_text("Video 2", text)
        
    def set_channel_video2_source(self, index):
        self.wait.until(EC.presence_of_element_located((By.ID, "video1_e_id")))
        select = Select(self.driver.find_element(By.ID, "video1_e_id"))
        select.select_by_index(index)

    def set_channel_video2_source_by_visible_text(self, text):
        self.wait.until(EC.presence_of_element_located((By.ID, "video1_e_id")))
        select = Select(self.driver.find_element(By.ID, "video1_e_id"))
        select.select_by_visible_text(text)

    def reset_channel_video2_source(self, text):
        self.wait.until(EC.presence_of_element_located((By.ID, "video1_e_id")))
        select = Select(self.driver.find_element(By.ID, "video1_e_id"))
        select.select_by_visible_text(text)
    
    def get_selected_audio_source(self):
        selected = self.find_selected_option_by_id("audio_e_id")
        text = selected.text
        return text
    
    def is_channel_audio_source(self, text):
        return self.is_option_selected_by_div_text_and_text("Audio", text)
    
    def set_channel_audio_source(self, index):
        self.wait.until(EC.presence_of_element_located((By.ID, "audio_e_id")))
        select = Select(self.driver.find_element(By.ID, "audio_e_id"))
        select.select_by_index(index)

    def set_channel_audio_source_by_visible_text(self, text):
        self.wait.until(EC.presence_of_element_located((By.ID, "audio_e_id")))
        select = Select(self.driver.find_element(By.ID, "audio_e_id"))
        select.select_by_visible_text(text)

    def reset_channel_audio_source(self, text):
        self.wait.until(EC.presence_of_element_located((By.ID, "audio_e_id")))
        select = Select(self.driver.find_element(By.ID, "audio_e_id"))
        select.select_by_visible_text(text)
        
    def get_selected_usb_source(self):
        selected = self.find_selected_option_by_id("usb_e_id")
        text = selected.text
        return text

    def is_channel_usb_source(self, text):
        return self.is_option_selected_by_div_text_and_text("USB", text)
    
    def set_channel_usb_source(self, index):
        self.wait.until(EC.presence_of_element_located((By.ID, "usb_e_id")))
        select = Select(self.driver.find_element(By.ID, "usb_e_id"))
        select.select_by_index(index)

    def set_channel_usb_source_by_visible_text(self, text):
        self.wait.until(EC.presence_of_element_located((By.ID, "usb_e_id")))
        select = Select(self.driver.find_element(By.ID, "usb_e_id"))
        select.select_by_visible_text(text)

    def reset_channel_usb_source(self, text):
        self.wait.until(EC.presence_of_element_located((By.ID, "usb_e_id")))
        select = Select(self.driver.find_element(By.ID, "usb_e_id"))
        select.select_by_visible_text(text)
    
    def get_selected_serial_source(self):
        selected = self.find_selected_option_by_id("serial_e_id")
        text = selected.text
        return text
    
    def is_channel_serial_source(self, text):
        return self.is_option_selected_by_div_text_and_text("Serial", text)
    
    def set_channel_serial_source(self, index):
        self.wait.until(EC.presence_of_element_located((By.ID, "serial_e_id")))
        select = Select(self.driver.find_element(By.ID, "serial_e_id"))
        select.select_by_index(index)

    def set_channel_serial_source_by_visible_text(self, text):
        self.wait.until(EC.presence_of_element_located((By.ID, "serial_e_id")))
        select = Select(self.driver.find_element(By.ID, "serial_e_id"))
        select.select_by_visible_text(text)

    def reset_channel_serial_source(self, text):
        self.wait.until(EC.presence_of_element_located((By.ID, "serial_e_id")))
        select = Select(self.driver.find_element(By.ID, "serial_e_id"))
        select.select_by_visible_text(text)
    
    def get_channel_connections_to_global_settings_selected(self):
        return self.is_option_selected_by_div_text_and_id("Allowed Connections", "c_allowed_modes_0")
    
    def set_channel_connections_to_global_settings(self):
        self.click_radio_option_by_div_text_and_id("Allowed Connections", "c_allowed_modes_0")

    def set_channel_connections_to_view_only(self):
        self.click_radio_option_by_div_text_and_id("Allowed Connections", "c_allowed_modes_4")

    def get_channel_connections_to_view_only_selected(self):
        return self.is_option_selected_by_div_text_and_id("Allowed Connections", "c_allowed_modes_4")

    def set_channel_connections_to_view_shared_only(self):
        self.click_radio_option_by_div_text_and_id("Allowed Connections", "c_allowed_modes_1")

    def get_channel_connections_to_view_shared_only_selected(self):
        return self.is_option_selected_by_div_text_and_id("Allowed Connections", "c_allowed_modes_1")

    def set_channel_connections_to_shared_only(self):
        self.click_radio_option_by_div_text_and_id("Allowed Connections", "c_allowed_modes_5")

    def get_channel_connections_to_shared_only_selected(self):
        return self.is_option_selected_by_div_text_and_id("Allowed Connections", "c_allowed_modes_5")
    
    def set_channel_connections_to_exclusive_only(self):
        self.click_radio_option_by_div_text_and_id("Allowed Connections", "c_allowed_modes_2")

    def get_channel_connections_to_exclusive_only_selected(self):
        return self.is_option_selected_by_div_text_and_id("Allowed Connections", "c_allowed_modes_2")
    
    def set_channel_connections_to_view_shared_and_exclusive(self):
        self.click_radio_option_by_div_text_and_id("Allowed Connections", "c_allowed_modes_3")

    def get_channel_connections_to_view_shared_and_exclusive_selected(self):
        return self.is_option_selected_by_div_text_and_id("Allowed Connections", "c_allowed_modes_3")
    
    def is_channel_specific_option_visible_by_text(self, div_text, text):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), '" + div_text + "')]")))
        return self.driver.find_element_by_xpath("//div[contains(text(), '" + div_text + "')]/following-sibling::div//select/option[contains(text(), '" + text + "')]").is_displayed()
    
    def add_user_to_channel_permission(self, user):
        self.wait.until(EC.presence_of_element_located((By.ID, "all_users")))
        select = Select(self.driver.find_element(By.ID, "all_users"))
        select.select_by_visible_text(user)
        self.driver.find_element_by_id("add_one_user").click()

    def add_user_to_channel_group_permission(self, user):
        self.wait.until(EC.presence_of_element_located((By.ID, "all_users")))
        select = Select(self.driver.find_element(By.ID, "all_users"))
        select.select_by_visible_text(user)
        self.driver.find_element_by_id("add_one_user").click()

    def remove_user_from_channel_permission(self, user):
        self.wait.until(EC.presence_of_element_located((By.ID, "selected_users")))
        select = Select(self.driver.find_element(By.ID, "selected_users"))
        select.select_by_visible_text(user)
        self.driver.find_element_by_id("remove_one_user").click()

    def remove_user_from_channel_group_permission(self, user):
        self.wait.until(EC.presence_of_element_located((By.ID, "selected_users")))
        select = Select(self.driver.find_element(By.ID, "selected_users"))
        select.select_by_visible_text(user)
        self.driver.find_element_by_id("remove_one_user").click()
    
    def check_user_has_channel_permission(self, user):
        return self.is_channel_specific_option_visible_by_text("Users", user)

    def check_user_has_channel_group_permission(self, user):
        return self.is_channel_specific_option_visible_by_text("Users", user)
    
    def add_channel_to_group(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "all_channel_groups")))
        select = Select(self.driver.find_element(By.ID, "all_channel_groups"))
        select.select_by_index("0")
        self.driver.find_element_by_id("add_one_channel_group").click()

    def remove_channel_from_group(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "selected_channel_groups")))
        select = Select(self.driver.find_element(By.ID, "selected_channel_groups"))
        select.select_by_index("0")
        self.driver.find_element_by_id("remove_one_channel_group").click()
    
    def check_channel_in_channel_group(self):
        return self.is_channel_specific_option_visible_by_text("Channel Groups", "group 1")

    def add_channel_to_user_group(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "all_user_groups")))
        select = Select(self.driver.find_element(By.ID, "all_user_groups"))
        select.select_by_index("0")
        self.driver.find_element_by_id("add_one_user_group").click()

    def add_channel_group_to_user_group(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "all_user_groups")))
        select = Select(self.driver.find_element(By.ID, "all_user_groups"))
        select.select_by_index("0")
        self.driver.find_element_by_id("add_one_user_group").click()

    def remove_channel_from_user_group(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "selected_user_groups")))
        select = Select(self.driver.find_element(By.ID, "selected_user_groups"))
        select.select_by_index("0")
        self.driver.find_element_by_id("remove_one_user_group").click()

    def remove_channel_group_from_user_group(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "selected_user_groups")))
        select = Select(self.driver.find_element(By.ID, "selected_user_groups"))
        select.select_by_index("0")
        self.driver.find_element_by_id("remove_one_user_group").click()
    
    def check_channel_in_user_group(self):
        return self.is_channel_specific_option_visible_by_text("User Groups", "group 0")

    def check_channel_group_in_user_group(self):
        return self.is_channel_specific_option_visible_by_text("User Groups", "group 0")
    
    def get_channel_linktext(self, element):
        return self.get_attribute_of_element_component(element.find_element_by_xpath("./td[8]/a[1]"), "href")
    
    def get_channel_group_linktext(self, element):
        return self.get_attribute_of_element_component(element.find_element_by_xpath("./td[5]/a[1]"), "href")
    
    def is_ajax_error_message_displayed_for_channel(self):
        return self.get_element_located_by_id("configure_channel_ajax_message")

    def is_ajax_error_message_displayed_for_channel_group(self):
        return self.get_element_located_by_id("configure_channel_group_ajax_message")
    
    def get_first_channel_name_from_add_select(self):
        select = Select(self.driver.find_element_by_id("all_channels"))
        options = select.options
        return options[0].text
    
    def add_channel_to_channel_group(self, text):
        self.wait.until(EC.presence_of_element_located((By.ID, "all_channels")))
        select = Select(self.driver.find_element(By.ID, "all_channels"))
        select.select_by_visible_text(text)
        self.driver.find_element_by_id("add_one_channel").click()

    def add_all_channels_to_channel_group(self):
        self.driver.find_element_by_id("add_all_channels").click()
    
    def get_list_of_non_member_channels_for_group(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "all_channels")))
        select = Select(self.driver.find_element(By.ID, "all_channels"))
        return select.options
    
    def get_list_of_member_channels_in_group(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "selected_channels")))
        select = Select(self.driver.find_element(By.ID, "selected_channels"))
        return select.options
    
    def channel_name_is_member_of_channel_group(self, text):
        self.wait.until(EC.presence_of_element_located((By.ID, "selected_channels")))
        select = Select(self.driver.find_element(By.ID, "selected_channels"))
        options = select.options
        found = False
        for option in options:
            if option.text == text:
                found = True
        return found
    
    def remove_all_channels_from_group(self):
        if self.get_element_located_by_id("remove_all_channels"):
            self.driver.find_element_by_id("remove_all_channels").click()
    
            
    """
    Receiver Page
    """
    def get_receivers_link_element(self):
        if self.get_element_located_by_link_text("RECEIVERS"):
            return self.driver.find_element_by_link_text("RECEIVERS")
    
    def open_receivers_tab(self):
        if self.get_element_located_by_link_text("RECEIVERS"):
            self.driver.find_element_by_link_text("RECEIVERS").click()

    def get_remotes_link_element(self):
        if self.get_element_located_by_link_text("REMOTES"):
            return self.driver.find_element_by_link_text("REMOTES")
        
    def open_remotes_tab(self):
        if self.get_element_located_by_link_text("REMOTES"):
            self.driver.find_element_by_link_text("REMOTES").click()
            
    def open_view_receivers_page(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_receivers_link_element()).move_to_element(self.driver.find_element_by_xpath("//div[@id='receivers_links']/ul//li/a[contains(text(), 'View Receiver Groups')]")).move_to_element(self.driver.find_element_by_xpath("//div[@id='receivers_links']/ul//li/a[contains(text(), 'View Receivers')]")).click().perform()
    
    def open_view_remotes_page(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_remotes_link_element()).move_to_element(self.driver.find_element_by_xpath("//div[@id='receivers_links']/ul//li/a[contains(text(), 'View Remote Groups')]")).move_to_element(self.driver.find_element_by_xpath("//div[@id='receivers_links']/ul//li/a[contains(text(), 'View Remotes')]")).click().perform()
    
    def open_view_receiver_groups_page(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_receivers_link_element()).move_to_element(self.driver.find_element_by_xpath("//div[@id='receivers_links']/ul//li/a[contains(text(), 'View Receiver Groups')]")).click().perform()

    def open_view_remote_groups_page(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_remotes_link_element()).move_to_element(self.driver.find_element_by_xpath("//div[@id='receivers_links']/ul//li/a[contains(text(), 'View Remote Groups')]")).click().perform()
    
    def open_add_receiver_groups_page(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_receivers_link_element()).move_to_element(self.driver.find_element_by_xpath("//div[@id='receivers_links']/ul//li/a[contains(text(), 'View Receiver Groups')]")).move_to_element(self.driver.find_element_by_xpath("//div[@id='receivers_links']/ul//li/a[contains(text(), 'Add Receiver Group')]")).click().perform()

    def open_add_remote_groups_page(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_remotes_link_element()).move_to_element(self.driver.find_element_by_xpath("//div[@id='receivers_links']/ul//li/a[contains(text(), 'View Remote Groups')]")).move_to_element(self.driver.find_element_by_xpath("//div[@id='receivers_links']/ul//li/a[contains(text(), 'Add Remote Group')]")).click().perform()
    
    def open_update_receiver_firmware_page(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_receivers_link_element()).move_to_element(self.driver.find_element_by_xpath("//div[@id='receivers_links']/ul//li/a[contains(text(), 'View Receiver Groups')]")).move_to_element(self.driver.find_element_by_xpath("//div[@id='receivers_links']/ul//li/a[contains(text(), 'Update Firmware')]")).click().perform()

    def open_update_remote_firmware_page(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_remotes_link_element()).move_to_element(self.driver.find_element_by_xpath("//div[@id='receivers_links']/ul//li/a[contains(text(), 'View Remote Groups')]")).move_to_element(self.driver.find_element_by_xpath("//div[@id='receivers_links']/ul//li/a[contains(text(), 'Update Firmware')]")).click().perform()
    
    def get_list_of_receivers(self):
        return self.get_list("receivers")
    
    def get_row_id_of_receiver(self, element):
        return self.get_attribute_of_element_component(element, "id")
    
    def get_receiver_name(self, element):
        return self.get_text_of_element_component_via_xpath(element, "./td[2]")
    
    def get_receiver_ip(self, element):
        ip = self.get_text_of_element_component_via_xpath(element, "./td[3]")
        if "\n" in ip:
            ip = ip.split("\n")
            ip = ip[0]
        return ip
    
    def get_receiver_description(self, element):
        return self.get_text_of_element_component_via_xpath(element, "./td[9]")
    
    def get_receiver_location(self, element):
        return self.get_text_of_element_component_via_xpath(element, "./td[10]")
    
    def get_receiver_linktext(self, element):
        return self.get_attribute_of_element_component(element.find_element_by_xpath("./td[11]/span[1]/a"), "href")
    
    def get_receiver_status_image_src(self, element):
        return self.check_online_status_image_src(element.find_element_by_xpath("./td[1]"))
        
    def send_search_term_to_receiver_name_field(self, term):
        self.send_filter_term_to_element("filter_d_name", term)

    def send_search_term_to_receiver_description_field(self, term):
        self.send_filter_term_to_element("filter_d_description", term)
    
    def send_search_term_to_receiver_location_field(self, term):
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
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[2]/a[1]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[2]/a[1]").click()

    def click_on_decend_receiver_names(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[2]/a[2]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[2]/a[2]").click()
            
    def click_on_ascend_receiver_descriptions(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[9]/a[1]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[9]/a[1]").click()

    def click_on_decend_receiver_descriptions(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[9]/a[2]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[9]/a[2]").click()

    def click_on_ascend_receiver_locations(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[10]/a[1]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[10]/a[1]").click()

    def click_on_decend_receiver_locations(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[10]/a[2]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[10]/a[2]").click()
    
    def click_receiver_configure(self, element):
        #element.find_element_by_xpath("./td[11]/a[1]").click()
        element.find_element_by_xpath("./td[11]/span[1]/a").click()
    
    def click_receiver_statistics(self, element):
        element.find_element_by_xpath("./td[11]/a[2]").click()
    
    def click_receiver_reboot(self, element):
        element.find_element_by_xpath("./td[11]/span[2]/a").click()
        
    def click_receiver_identify(self, element):
        element.find_element_by_xpath("./td[11]/a[1]").click()
    
    def click_receiver_connect_to_channel(self, element):
        element.find_element_by_xpath("./td[11]/span[4]/a").click()
    
    def get_receiver_channel_connect_linktext(self, element):
        return self.get_attribute_of_element_component(element.find_element_by_xpath("./td[11]/span[4]/a"), "href")
        
    def get_visibility_of_receiver_disconnect(self, element):
        try:
            time.sleep(0.5)
            return element.find_element_by_xpath("./td[11]/span[5]/a/img").is_displayed()
        except Exception:
            return False
    
    def click_receiver_disconnect_from_channel(self, element):
        element.find_element_by_xpath("./td[11]/span[4]/a").click()
    
    def click_disconnect_all_receivers(self):
        if self.get_element_located_by_xpath("//table/thead/tr/th[11]/a"):
            self.driver.find_element_by_xpath("//table/thead/tr/th[11]/a").click()

    def wait_for_receiver_added_message(self):
        wait = WebDriverWait(self.driver, 120)
        wait.until(EC.text_to_be_present_in_element((By.XPATH, "//span[@id='warnings']/span"), "1 new Receiver added. Configure"))
        
    def wait_for_receiver_rebooting_message(self):
        wait = WebDriverWait(self.driver, 120)
        wait.until(EC.text_to_be_present_in_element((By.XPATH, "//span[@id='warnings']/span"), "1 Receiver currently rebooting"))
        
    """
    Receiver Config BasePage
    """
    def set_receiver_ip_via_config_page(self, new_ip):
        if self.get_element_located_by_id("configure_device"):
            self.enter_text_into_input_field("d_ip_address", new_ip)
    
    def get_receiver_name_from_config_page(self):
        if self.get_element_located_by_id("d_name"):
            return self.get_attribute_of_element_component(self.driver.find_element_by_id("d_name"), "value")

    def set_receiver_name_via_config_page(self, text):
        if self.get_element_located_by_id("d_name"):
            self.enter_text_into_input_field("d_name", text)

    def get_receiver_description_from_config_page(self):
        if self.get_element_located_by_id("d_description"):
            return self.get_attribute_of_element_component(self.driver.find_element_by_id("d_description"), "value")

    def set_receiver_description_via_config_page(self, text):
        if self.get_element_located_by_id("d_description"):
            self.enter_text_into_input_field("d_description", text)

    def get_receiver_location_from_config_page(self):
        if self.get_element_located_by_id("d_location"):
            return self.get_attribute_of_element_component(self.driver.find_element_by_id("d_location"), "value")

    def set_receiver_location_via_config_page(self, text):
        if self.get_element_located_by_id("d_location"):
            self.enter_text_into_input_field("d_location", text)
            
    def select_login_required_global(self):
        self.click_radio_option_by_div_text_and_id("Login Required", "rp_login_required_-1")
        
    def select_login_required_no(self):
        self.click_radio_option_by_div_text_and_id("Login Required", "rp_login_required_0")
        
    def select_login_required_yes(self):
        self.click_radio_option_by_div_text_and_id("Login Required", "rp_login_required_1")

    def select_osd_alerts_global(self):
        self.click_radio_option_by_div_text_and_id("Receiver OSD Alerts", "rp_osd_alerts_-1")
        
    def select_osd_alerts_no(self):
        self.click_radio_option_by_div_text_and_id("Receiver OSD Alerts", "rp_osd_alerts_0")
        
    def select_osd_alerts_yes(self):
        self.click_radio_option_by_div_text_and_id("Receiver OSD Alerts", "rp_osd_alerts_1")

    

    def select_audio_input_global(self):
        self.click_radio_option_by_div_text_and_id("Audio Input Type", "rp_audio_is_-1")
        
    def select_audio_input_line(self):
        self.click_radio_option_by_div_text_and_id("Audio Input Type", "rp_audio_is_0")
        
    def select_audio_input_mic(self):
        self.click_radio_option_by_div_text_and_id("Audio Input Type", "rp_audio_is_1")
        
    def select_audio_input_mic_boost(self):
        self.click_radio_option_by_div_text_and_id("Audio Input Type", "rp_audio_is_2")
    
    def select_network_medium_global(self):
        self.click_radio_option_by_div_text_and_id("Network Medium", "network_medium_-1")
        
    def select_network_medium_fibre(self):
        self.click_radio_option_by_div_text_and_id("Network Medium", "network_medium_0")
        
    def select_network_medium_copper(self):
        self.click_radio_option_by_div_text_and_id("Network Medium", "network_medium_1")

    def select_fibre_protocol_global(self):
        self.click_radio_option_by_div_text_and_id("Fibre Protocol", "fibre_protocol_-1")
        
    def select_fibre_protocol_standard_ethernet(self):
        self.click_radio_option_by_div_text_and_id("Fibre Protocol", "fibre_protocol_0")
        
    def select_fibre_protocol_proprietry(self):
        self.click_radio_option_by_div_text_and_id("Fibre Protocol", "fibre_protocol_1")

    def select_video_compatibility_global(self):
        self.click_radio_option_by_div_text_and_id("Video Compatibility Check", "rp_video_compatibility_check_-1")
        
    def select_video_compatibility_no(self):
        self.click_radio_option_by_div_text_and_id("Video Compatibility Check", "rp_video_compatibility_check_0")
        
    def select_video_compatibility_yes(self):
        self.click_radio_option_by_div_text_and_id("Video Compatibility Check", "rp_video_compatibility_check_1")

    def select_video_one_compatibility_global(self):
        self.click_radio_option_by_div_text_and_id("Video Compatibility Check (Monitor 1)", "rp_video_compatibility_check_-1")
        
    def select_video_one_compatibility_no(self):
        self.click_radio_button_by_id("rp_video_compatibility_check_0")
        
    def select_video_one_compatibility_yes(self):
        self.click_radio_button_by_id("rp_video_compatibility_check_1")

    def select_video_two_compatibility_global(self):
        self.click_radio_button_by_id("rp_video_compatibility_check1_-1")
        
    def select_video_two_compatibility_no(self):
        self.click_radio_button_by_id("rp_video_compatibility_check1_0")
        
    def select_video_two_compatibility_yes(self):
        self.click_radio_button_by_id("rp_video_compatibility_check1_1")
        
    def add_receiver_to_receiver_group(self, group_name):
        self.wait.until(EC.presence_of_element_located((By.ID, "all_receiver_groups")))
        select = Select(self.driver.find_element(By.ID, "all_receiver_groups"))
        select.select_by_visible_text(group_name)
        self.driver.find_element_by_id("add_one_receiver_group").click()
    
    def check_receiver_is_group_member(self, group_name):
        return self.is_channel_specific_option_visible_by_text("Receiver Groups", group_name)
    
    def remove_all_receivers_from_receiver_group(self):
        if self.get_element_located_by_id("remove_all_receiver_groups"):
            self.driver.find_element_by_id("remove_all_receiver_groups").click()

    def add_user_to_receiver(self, user):
        self.wait.until(EC.presence_of_element_located((By.ID, "all_users")))
        select = Select(self.driver.find_element(By.ID, "all_users"))
        select.select_by_visible_text(user)
        self.driver.find_element_by_id("add_one_user").click()
    
    def add_all_users_to_receiver(self):
        if self.get_element_located_by_id("add_all_users"):
            self.driver.find_element_by_id("add_all_users").click()
    
    def check_user_has_receiver_permission(self, user):
        return self.is_channel_specific_option_visible_by_text("Users", user)
        
    def remove_all_users_from_receiver(self):
        if self.get_element_located_by_id("remove_all_users"):
            self.driver.find_element_by_id("remove_all_users").click()
    
    def add_receiver_to_user_group(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "all_user_groups")))
        select = Select(self.driver.find_element(By.ID, "all_user_groups"))
        select.select_by_index(0)
        self.driver.find_element_by_id("add_one_user_group").click()        
    
    def remove_receiver_from_user_group(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "selected_user_groups")))
        select = Select(self.driver.find_element(By.ID, "selected_user_groups"))
        select.select_by_index(0)
        self.driver.find_element_by_id("remove_one_user_group").click()
    
    def check_receiver_in_user_group(self):
        return self.is_channel_specific_option_visible_by_text("User Groups", "group 0")
            
    def confirm_no_longer_on_configure_receiver_page(self):
        found = False
        while(found == False):
            if not self.get_text_of_page_header() == "Receivers > Configure Receiver":
                found = True
    
    """
    Receiver USB BasePage
    """
    def open_receiver_usb_settings(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Configure"))).click()

    def open_receiver_usb_settings_2(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "USB settings")))  .click()          
            
    def select_HID_connection_global(self):
        self.click_radio_option_by_div_text_and_id("HID Only", "hid_only_-1")
        
    def select_HID_connection_no(self):
        self.click_radio_option_by_div_text_and_id("HID Only", "hid_only_0")
        
    def select_HID_connection_yes(self):
        self.click_radio_option_by_div_text_and_id("HID Only", "hid_only_1")

    def select_disable_isochronous_endpoint_osd_alerts_global(self):
        self.click_radio_option_by_div_text_and_id("Disable Isochronous Endpoint OSD Alerts", "isochronous_user_warning_-1")
        
    def select_disable_isochronous_endpoint_osd_alerts_no(self):
        self.click_radio_option_by_div_text_and_id("Disable Isochronous Endpoint OSD Alerts", "isochronous_user_warning_0")
        
    def select_disable_isochronous_endpoint_osd_alerts_yes(self):
        self.click_radio_option_by_div_text_and_id("Disable Isochronous Endpoint OSD Alerts", "isochronous_user_warning_1")

    def select_enable_isochronous_endpoint_attach_global(self):
        self.click_radio_option_by_div_text_and_id("Enable Isochronous Endpoint Attach", "isochronous_enabled_-1")
        
    def select_enable_isochronous_endpoint_attach_no(self):
        self.click_radio_option_by_div_text_and_id("Enable Isochronous Endpoint Attach", "isochronous_enabled_0")
        
    def select_enable_isochronous_endpoint_attach_yes(self):
        self.click_radio_option_by_div_text_and_id("Enable Isochronous Endpoint Attach", "isochronous_enabled_1")
    
    """
    Receiver Group BasePage
    """
    def get_list_of_receiver_groups(self):
        return self.get_list("receiver_groups")
    
    def get_receiver_group_name(self, element):
        return self.get_text_of_element_component_via_xpath(element, "./td[1]")
    
    def get_receiver_group_description(self, element):
        return self.get_text_of_element_component_via_xpath(element, "./td[2]")
    
    def get_receiver_group_config_linktext(self, element):
        return self.get_attribute_of_element_component(element.find_element_by_xpath("./td[6]/a[1]"), "href")

    def get_receiver_group_clone_linktext(self, element):
        return self.get_attribute_of_element_component(element.find_element_by_xpath("./td[6]/a[2]"), "href")
    
    def click_add_receiver_group_button(self):
        if self.get_element_located_by_xpath("//span/img[@alt='Add Receiver Group']"):
            self.driver.find_element_by_xpath("//span/img[@alt='Add Receiver Group']").click()
            
    def send_search_term_to_receiver_group_name_field(self, term):
        self.send_filter_term_to_element("filter_rg_name", term)
    
    def click_on_filter_receiver_groups_by_name(self):
        self.click_on_filter("filter_rg_name_icon")
    
    def click_on_remove_receiver_groups_name_filter(self):
        self.click_on_filter("remove_filter_rg_name_icon")
    
    def clear_receiver_groups_names_filter(self):
        self.clear_filter_of_element("filter_rg_name")
        
    def send_search_term_to_receiver_group_description_field(self, term):
        self.send_filter_term_to_element("filter_rg_description", term)
    
    def click_on_filter_receiver_groups_by_description(self):
        self.click_on_filter("filter_rg_description_icon")
    
    def click_on_remove_receiver_groups_description_filter(self):
        self.click_on_filter("remove_filter_rg_description_icon")
    
    def clear_remove_receiver_group_descriptions_filter(self):
        self.clear_filter_of_element("filter_rg_description")
    
    def click_on_ascend_receiver_group_names(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[1]/a[1]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[1]/a[1]").click()

    def click_on_decend_receiver_group_names(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[1]/a[2]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[1]/a[2]").click()
    
    def click_on_ascend_receiver_group_descriptions(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[2]/a[1]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[2]/a[1]").click()

    def click_on_decend_receiver_group_descriptions(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[2]/a[2]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[2]/a[2]").click()
    
    def click_receiver_group_delete(self, element):
        element.find_element_by_xpath("./td[6]/a[3]").click()
    
    def click_batch_delete_selector_for_receiver_group_element(self, element):
        element.find_element_by_xpath("./td[6]/input").click()

    def click_receiver_group_config(self, element):
        element.find_element_by_xpath("./td[6]/a[1]").click()
        
    def click_receiver_group_clone(self, element):
        element.find_element_by_xpath("./td[6]/a[2]").click()
        
    def click_batch_delete_receiver_groups(self):
        if self.get_element_located_by_link_text("Delete selected Receiver Groups"):
            self.driver.find_element_by_link_text("Delete selected Receiver Groups").click()
    
    def check_for_batch_delete_checkbox_for_receiver_group_element(self, element):
        return element.find_element_by_xpath("./td[6]/input").is_displayed()
    
    def get_delete_receiver_text_from_lightbox(self):
        return self.get_lightbox_title_text()
    
    """
    Receiver Group Config
    """
    def get_receiver_group_name_from_config_page(self):
        if self.get_element_located_by_id("rg_name"):
            return self.get_attribute_of_element_component(self.driver.find_element_by_id("rg_name"), "value")

    def set_receiver_group_name_via_config_page(self, text):
        if self.get_element_located_by_id("rg_name"):
            self.enter_text_into_input_field("rg_name", text)
            
    def get_receiver_group_description_from_config_page(self):
        if self.get_element_located_by_id("rg_description"):
            return self.get_attribute_of_element_component(self.driver.find_element_by_id("rg_description"), "value")
    
    def set_receiver_group_description_via_config_page(self, text):
        if self.get_element_located_by_id("rg_description"):
            self.enter_text_into_input_field("rg_description", text)

    def select_receiver_group_login_required_global(self):
        self.click_radio_option_by_div_text_and_id("Login Required", "rg_login_required_-1")
    
    def select_receiver_group_login_required_no(self):
        self.click_radio_option_by_div_text_and_id("Login Required", "rg_login_required_0")
        
    def select_receiver_group_login_required_yes(self):
        self.click_radio_option_by_div_text_and_id("Login Required", "rg_login_required_1")

    def select_receiver_group_osd_alerts_global(self):
        self.click_radio_option_by_div_text_and_id("Enable receiver OSD Alerts", "rg_osd_alerts_-1")
        
    def select_receiver_group_osd_alerts_no(self):
        self.click_radio_option_by_div_text_and_id("Enable receiver OSD Alerts", "rg_osd_alerts_0")
        
    def select_receiver_group_osd_alerts_yes(self):
        self.click_radio_option_by_div_text_and_id("Enable receiver OSD Alerts", "rg_osd_alerts_1")

    def select_receiver_group_HID_connection_global(self):
        self.click_radio_option_by_div_text_and_id("HID Only", "hid_only_-1")
        
    def select_receiver_group_HID_connection_no(self):
        self.click_radio_option_by_div_text_and_id("HID Only", "hid_only_0")
        
    def select_receiver_group_HID_connection_yes(self):
        self.click_radio_option_by_div_text_and_id("HID Only", "hid_only_1")

    def select_receiver_group_disable_isochronous_endpoint_osd_alerts_global(self):
        self.click_radio_option_by_div_text_and_id("Disable Isochronous Endpoint OSD Alerts", "isochronous_user_warning_-1")
        
    def select_receiver_group_disable_isochronous_endpoint_osd_alerts_no(self):
        self.click_radio_option_by_div_text_and_id("Disable Isochronous Endpoint OSD Alerts", "isochronous_user_warning_0")
        
    def select_receiver_group_disable_isochronous_endpoint_osd_alerts_yes(self):
        self.click_radio_option_by_div_text_and_id("Disable Isochronous Endpoint OSD Alerts", "isochronous_user_warning_1")

    def select_receiver_group_enable_isochronous_endpoint_attach_global(self):
        self.click_radio_option_by_div_text_and_id("Enable Isochronous Endpoint Attach", "isochronous_enabled_-1")
        
    def select_receiver_group_enable_isochronous_endpoint_attach_no(self):
        self.click_radio_option_by_div_text_and_id("Enable Isochronous Endpoint Attach", "isochronous_enabled_0")
        
    def select_receiver_group_enable_isochronous_endpoint_attach_yes(self):
        self.click_radio_option_by_div_text_and_id("Enable Isochronous Endpoint Attach", "isochronous_enabled_1")

    def select_receiver_group_video_compatibility_global(self):
        self.click_radio_option_by_div_text_and_id("Enable Video Compatibility Check", "rg_video_compatibility_check_-1")
        
    def select_receiver_group_video_compatibility_no(self):
        self.click_radio_option_by_div_text_and_id("Enable Video Compatibility Check", "rg_video_compatibility_check_0")
        
    def select_receiver_group_video_compatibility_yes(self):
        self.click_radio_option_by_div_text_and_id("Enable Video Compatibility Check", "rg_video_compatibility_check_1")
        
    def get_first_receiver_name_from_add_select(self):
        select = Select(self.driver.find_element_by_id("all_rxs"))
        options = select.options
        return options[0].text
    
    def add_member_receiver_to_receiver_group(self, text):
        self.wait.until(EC.presence_of_element_located((By.ID, "all_rxs")))
        select = Select(self.driver.find_element(By.ID, "all_rxs"))
        select.select_by_visible_text(text)
        self.driver.find_element_by_id("add_one_rx").click()
        
    def add_all_receivers_to_receiver_group(self):
        self.driver.find_element_by_id("add_all_rxs").click()
    
    def check_receiver_name_is_member_of_receiver_group(self, text):
        self.wait.until(EC.presence_of_element_located((By.ID, "selected_rxs")))
        select = Select(self.driver.find_element(By.ID, "selected_rxs"))
        options = select.options
        found = False
        for option in options:
            if option.text == text:
                found = True
        return found
    
    def remove_all_member_receivers_from_receiver_group(self):
        if self.get_element_located_by_id("remove_all_rxs"):
            self.driver.find_element_by_id("remove_all_rxs").click()
    
    def get_first_user_name_from_add_select(self):
        select = Select(self.driver.find_element_by_id("all_users"))
        options = select.options
        return options[0].text
    
    def add_user_to_receiver_group(self, user):
        self.wait.until(EC.presence_of_element_located((By.ID, "all_users")))
        select = Select(self.driver.find_element(By.ID, "all_users"))
        select.select_by_visible_text(user)
        self.driver.find_element_by_id("add_one_user").click()
    
    def add_all_users_to_receiver_group(self):
        if self.get_element_located_by_id("add_all_users"):
            self.driver.find_element_by_id("add_all_users").click()
    
    def check_user_has_receiver_group_permission(self, user):
        return self.is_channel_specific_option_visible_by_text("Users", user)
        
    def remove_all_users_from_receiver_group(self):
        if self.get_element_located_by_id("remove_all_users"):
            self.driver.find_element_by_id("remove_all_users").click()
    
    def get_first_user_group_name_from_add_select(self):
        select = Select(self.driver.find_element_by_id("all_user_groups"))
        options = select.options
        return options[0].text
    
    def add_user_group_to_receiver_group(self, user):
        self.wait.until(EC.presence_of_element_located((By.ID, "all_user_groups")))
        select = Select(self.driver.find_element(By.ID, "all_user_groups"))
        select.select_by_visible_text(user)
        self.driver.find_element_by_id("add_one_user_group").click()
    
    def add_all_user_groups_to_receiver_group(self):
        if self.get_element_located_by_id("add_all_user_groups"):
            self.driver.find_element_by_id("add_all_user_groups").click()
    
    def check_user_group_has_receiver_group_permission(self, user):
        return self.is_channel_specific_option_visible_by_text("User Groups", user)
        
    def remove_all_user_groups_from_receiver_group(self):
        if self.get_element_located_by_id("remove_all_user_groups"):
            self.driver.find_element_by_id("remove_all_user_groups").click()
    
    def confirm_no_longer_on_receiver_group_config_page(self):
        found = False
        while(found == False):
            if not self.get_text_of_page_header() == "Receiver Groups > Configure Receiver Group":
                found = True
    
    """
    Receiver Clone
    """
    def confirm_no_longer_on_clone_receiver_group_page(self):
        found = False
        while(found == False):
            if not self.get_text_of_page_header() == "Receiver Groups > Configure Cloned Receiver Group":
                found = True
    
    """
    Receiver Group Add
    """
    def is_ajax_error_message_displayed_for_receiver_group(self):
        return self.get_element_located_by_id("configure_receiver_group_ajax_message")
    
    def get_list_of_non_member_receivers_for_group(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "all_rxs")))
        select = Select(self.driver.find_element(By.ID, "all_rxs"))
        return select.options

    def get_list_of_member_receivers_in_group(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "selected_rxs")))
        select = Select(self.driver.find_element(By.ID, "selected_rxs"))
        return select.options
    
    def confirm_no_longer_on_receiver_group_add_page(self):
        found = False
        while(found == False):
            if not self.get_text_of_page_header() == "Receiver Groups > Add Receiver Group":
                found = True
    
    def select_login_required_for_receiver_group_global(self):
        self.click_radio_option_by_div_text_and_id("Login Required", "rg_login_required_-1")
        
    def select_login_required_for_receiver_group_no(self):
        self.click_radio_option_by_div_text_and_id("Login Required", "rg_login_required_0")
        
    def select_login_required_for_receiver_group_yes(self):
        self.click_radio_option_by_div_text_and_id("Login Required", "rg_login_required_1")

    def select_enable_osd_alerts_for_receiver_group_global(self):
        self.click_radio_option_by_div_text_and_id("Enable receiver OSD Alerts", "rg_osd_alerts_-1")
        
    def select_enable_osd_alerts_for_receiver_group_no(self):
        self.click_radio_option_by_div_text_and_id("Enable receiver OSD Alerts", "rg_osd_alerts_0")
        
    def select_enable_osd_alerts_for_receiver_group_yes(self):
        self.click_radio_option_by_div_text_and_id("Enable receiver OSD Alerts", "rg_osd_alerts_1")

    def select_hid_only_for_receiver_group_global(self):
        self.click_radio_option_by_div_text_and_id("HID Only", "rg_hid_only_-1")
        
    def select_hid_only_for_receiver_group_no(self):
        self.click_radio_option_by_div_text_and_id("HID Only", "rg_hid_only_0")
        
    def select_hid_only_for_receiver_group_yes(self):
        self.click_radio_option_by_div_text_and_id("HID Only", "rg_hid_only_1")

    def select_disable_isochronous_alerts_for_receiver_group_global(self):
        self.click_radio_option_by_div_text_and_id("Disable Isochronous Endpoint OSD Alerts", "rg_isochronous_user_warning_-1")
        
    def select_disable_isochronous_alerts_for_receiver_group_no(self):
        self.click_radio_option_by_div_text_and_id("Disable Isochronous Endpoint OSD Alerts", "rg_isochronous_user_warning_0")
        
    def select_disable_isochronous_alerts_for_receiver_group_yes(self):
        self.click_radio_option_by_div_text_and_id("Disable Isochronous Endpoint OSD Alerts", "rg_isochronous_user_warning_1")

    def select_enable_isochronous_attach_for_receiver_group_global(self):
        self.click_radio_option_by_div_text_and_id("Enable Isochronous Endpoint Attach", "rg_isochronous_enabled_-1")
        
    def select_enable_isochronous_attach_for_receiver_group_no(self):
        self.click_radio_option_by_div_text_and_id("Enable Isochronous Endpoint Attach", "rg_isochronous_enabled_0")
        
    def select_enable_isochronous_attach_for_receiver_group_yes(self):
        self.click_radio_option_by_div_text_and_id("Enable Isochronous Endpoint Attach", "rg_isochronous_enabled_1")

    def select_enable_video_compatibility_for_receiver_group_global(self):
        self.click_radio_option_by_div_text_and_id("Enable Video Compatibility Check", "rg_video_compatibility_check_-1")
        
    def select_enable_video_compatibility_for_receiver_group_no(self):
        self.click_radio_option_by_div_text_and_id("Enable Video Compatibility Check", "rg_video_compatibility_check_0")
        
    def select_enable_video_compatibility_for_receiver_group_yes(self):
        self.click_radio_option_by_div_text_and_id("Enable Video Compatibility Check", "rg_video_compatibility_check_1")
        
    
    """
    Presets Page BasePage
    """
    def get_presets_link_element(self):
        if self.get_element_located_by_link_text("PRESETS"):
            return self.driver.find_element_by_link_text("PRESETS")
        
    def open_presets_tab(self):
        if self.get_element_located_by_link_text("PRESETS"):
            self.driver.find_element_by_link_text("PRESETS").click()
    
    def open_view_presets_page(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_presets_link_element()).move_by_offset(0, 19).move_to_element(self.driver.find_element_by_xpath("//div[@id='presets_links']/ul//li/a[contains(text(), 'View Presets')]")).click().perform()

    def open_add_presets_page(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_presets_link_element()).move_by_offset(0, 19).move_to_element(self.driver.find_element_by_xpath("//div[@id='presets_links']/ul//li/a[contains(text(), 'Add Preset')]")).click().perform()
        
    def click_add_preset_button(self):
        if self.get_element_located_by_xpath("//div[@class='button_wrapper']/a/span[contains(text(), 'Add Preset')]"):
            self.driver.find_element_by_xpath("//div[@class='button_wrapper']/a/span[contains(text(), 'Add Preset')]").click()
    
    def get_list_of_presets(self):
        return self.get_list("presets")
        
    def get_preset_name(self, element):
        return element.find_element_by_xpath("./td[1]").text
    
    def get_preset_description(self, element):
        return element.find_element_by_xpath("./td[2]").text
    
    def get_preset_allowed_connection_image_src(self, element):
        return element.find_element_by_xpath("./td[4]/img").get_attribute("src")
    
    def check_for_batch_delete_checkbox_for_preset_element(self, element):
        return element.find_element_by_xpath("./td[6]/input").is_displayed()
    
    def click_preset_disconnect(self, element):
        time.sleep(1)
        element.find_element_by_xpath("./td[5]/a/img[@src='/admin/images/silk_icons/disconnect.png']").click()
    
    def click_preset_connect_view_only(self, element):
        time.sleep(1)
        element.find_element_by_xpath("./td[5]/a/img[@src='/admin/images/silk_icons/eye.png']").click()

    def click_preset_connect_shared(self, element):
        time.sleep(1)
        element.find_element_by_xpath("./td[5]/a/img[@src='/admin/images/silk_icons/multicast.png']").click()

    def click_preset_connect_exclusive(self, element):
        time.sleep(1)
        element.find_element_by_xpath("./td[5]/a/img[@src='/admin/images/silk_icons/lock.png']").click()

    def check_for_preset_disconnect_button(self, element):
        try:
            return element.find_element_by_xpath("./td[5]/a/img[@src='/admin/images/silk_icons/disconnect.png']").is_displayed()
        except Exception:
            return False
       
    def check_colour_of_connect_view_only_button(self, element):
        return element.find_element_by_xpath("./td[5]/a/img[@src='/admin/images/silk_icons/eye.png']/parent::a").get_attribute("class")

    def check_colour_of_connect_shared_button(self, element):
        return element.find_element_by_xpath("./td[5]/a/img[@src='/admin/images/silk_icons/multicast.png']/parent::a").get_attribute("class")

    def check_colour_of_connect_exclusive_button(self, element):
        return element.find_element_by_xpath("./td[5]/a/img[@src='/admin/images/silk_icons/lock.png']/parent::a").get_attribute("class")
    
    def get_preset_config_linktext(self, element):
        return self.get_attribute_of_element_component(element.find_element_by_xpath("./td[6]/a[1]"), "href")

    def get_preset_clone_linktext(self, element):
        return self.get_attribute_of_element_component(element.find_element_by_xpath("./td[6]/a[2]"), "href")
    
    def click_preset_configure(self, element):
        element.find_element_by_xpath("./td[6]/a[1]").click()

    def click_preset_clone(self, element):
        element.find_element_by_xpath("./td[6]/a[2]").click()

    def click_preset_delete(self, element):
        element.find_element_by_xpath("./td[6]/a[3]").click()
    
    def get_preset_name_from_config_page(self):
        if self.get_element_located_by_id("cp_name"):
            return self.get_attribute_of_element_component(self.driver.find_element_by_id("cp_name"), "value")
    
    def set_preset_name_via_config_page(self, text):
        if self.get_element_located_by_id("cp_name"):
            self.enter_text_into_input_field("cp_name", text)

    def get_preset_description_from_config_page(self):
        if self.get_element_located_by_id("cp_description"):
            return self.get_attribute_of_element_component(self.driver.find_element_by_id("cp_description"), "value")
    
    def set_preset_description_via_config_page(self, text):
        if self.get_element_located_by_id("cp_description"):
            self.enter_text_into_input_field("cp_description", text)
    
    def confirm_no_longer_on_preset_config_page(self):
        found = False
        while(found == False):
            if not self.get_text_of_page_header() == "Presets > Configure Preset":
                found = True

    def confirm_no_longer_on_preset_clone_page(self):
        found = False
        while(found == False):
            if not self.get_text_of_page_header() == "Presets > Configure Cloned Preset":
                found = True

    def get_list_of_preset_pairs(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[starts-with(@id, 'cp_pair_')]")))
        return self.driver.find_elements_by_xpath("//div[starts-with(@id, 'cp_pair_')]")

    def get_list_of_preset_pair_receiver_selects(self):
        return self.driver.find_elements_by_xpath("//select[starts-with(@id, 'receiver_id_')]")

    def get_list_of_preset_pair_channel_selects(self):
        return self.driver.find_elements_by_xpath("//select[starts-with(@id, 'channel_id_')]")

    def reset_preset_pairs(self):
        pair_delete_buttons = self.driver.find_elements_by_xpath("//div[@class='cp_remove_pair']/a")
        for button_ in pair_delete_buttons:
            button_.click()

    def add_new_preset_pair(self):
        if self.get_element_located_by_xpath("//div[@class='form_row']/a"):
            self.driver.find_element_by_xpath("//div[@class='form_row']/a").click()
            current_receiver_name = Select(self.driver.find_element_by_id("receiver_id_1"))
            current_receiver_name = current_receiver_name.first_selected_option
            current_receiver_name = current_receiver_name.text
            current_channel_name = Select(self.driver.find_element_by_id("channel_id_1"))
            current_channel_name = current_channel_name.first_selected_option
            current_channel_name = current_channel_name.text
            receivers = [] 
            channels = []
            select_receiver = Select(self.driver.find_element_by_id("receiver_id_2"))
            options = select_receiver.options
            for option in options:
                receivers.append(option.text)
            select_channel = Select(self.driver.find_element_by_id("channel_id_2"))
            options = select_channel.options
            for option in options:
                channels.append(option.text)
            for receiver in receivers:
                if receiver not in (current_receiver_name, "- Select a Receiver -"):
                    receiver_name = receiver
            for channel in channels:
                if channel not in (current_channel_name, "- Select a Channel -"):
                    channel_name = channel
            select_receiver = Select(self.driver.find_element_by_id("receiver_id_2"))
            select_receiver.select_by_visible_text(receiver_name)
            select_channel = Select(self.driver.find_element_by_id("channel_id_2"))
            select_channel.select_by_visible_text(channel_name)
    
    def add_all_available_pairs(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='form_row']/a")))

        all_receivers = []
        receivers = Select(self.driver.find_element_by_id("receiver_id_1"))
        receivers = receivers.options
        for receiver in receivers:
            all_receivers.append(receiver.text)
        
        receiver_in_pair = self.get_list_of_preset_pair_receiver_selects()
        all_selected = []
        for pair in receiver_in_pair:
            selected = Select(pair)
            selected = selected.first_selected_option
            all_selected.append(selected.text)
         
        receivers_to_be_selected = list(set(all_receivers) - set(all_selected))
        
        while "- Select a Receiver -" in receivers_to_be_selected:
            receivers_to_be_selected.remove("- Select a Receiver -")
        
        all_channels = []
        channels = Select(self.driver.find_element_by_id("channel_id_1"))
        channels = channels.options
        for channel in channels:
            all_channels.append(channel.text)
        
        channel_in_pair = self.get_list_of_preset_pair_channel_selects()
        all_selected = []
        for pair in channel_in_pair:
            selected = Select(pair)
            selected = selected.first_selected_option
            all_selected.append(selected.text)
        
        channels_to_be_selected = list(set(all_channels) - set(all_selected))
        
        while "- Select a Channel -" in channels_to_be_selected:
            channels_to_be_selected.remove("- Select a Channel -")
        
        if len(receivers_to_be_selected) > len(channels_to_be_selected):
            stop = False
            while stop == False:
                receivers_to_be_selected.pop()
                if len(receivers_to_be_selected) == len(channels_to_be_selected):
                    stop = True

        if len(channels_to_be_selected) > len(receivers_to_be_selected):
            stop = False
            while stop == False:
                channels_to_be_selected.pop()
                if len(receivers_to_be_selected) == len(channels_to_be_selected):
                    stop = True
                
        for receiver in receivers_to_be_selected:
            index = receivers_to_be_selected.index(receiver)
            self.driver.find_element_by_xpath("//div[@class='form_row']/a").click()
            pairs = self.get_list_of_preset_pair_receiver_selects()
            select = Select(pairs[-1])
            select.select_by_visible_text(receiver)
            select = Select(pairs[-1].find_element_by_xpath("./parent::div/following-sibling::div/select[starts-with(@id, 'channel_id_')]"))
            select.select_by_visible_text(channels_to_be_selected[index])
            
    def add_multicast_pair(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='form_row']/a")))
        self.driver.find_element_by_xpath("//div[@class='form_row']/a").click()
        current_receiver_name = Select(self.driver.find_element_by_id("receiver_id_1"))
        current_receiver_name = current_receiver_name.first_selected_option
        current_receiver_name = current_receiver_name.text
        current_channel_name = Select(self.driver.find_element_by_id("channel_id_1"))
        current_channel_name = current_channel_name.first_selected_option
        current_channel_name = current_channel_name.text
        receivers = [] 
        select_receiver = Select(self.driver.find_element_by_id("receiver_id_2"))
        options = select_receiver.options
        for option in options:
            receivers.append(option.text)
        for receiver in receivers:
            if receiver not in (current_receiver_name, "- Select a Receiver -"):
                receiver_name = receiver
        select_receiver = Select(self.driver.find_element_by_id("receiver_id_2"))
        select_receiver.select_by_visible_text(receiver_name)
        select_channel = Select(self.driver.find_element_by_id("channel_id_2"))
        select_channel.select_by_visible_text(current_channel_name)
        self.click_save()
        self.wait.until(EC.presence_of_element_located((By.ID, "configure_connection_preset_ajax_message")))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element_by_xpath("//span[@id='configure_connection_preset_ajax_message']/a").click())

    def add_same_receiver_pair(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='form_row']/a")))
        self.driver.find_element_by_xpath("//div[@class='form_row']/a").click()
        current_receiver_name = Select(self.driver.find_element_by_id("receiver_id_1"))
        current_receiver_name = current_receiver_name.first_selected_option
        current_receiver_name = current_receiver_name.text
        current_channel_name = Select(self.driver.find_element_by_id("channel_id_1"))
        current_channel_name = current_channel_name.first_selected_option
        current_channel_name = current_channel_name.text
        select_receiver = Select(self.driver.find_element_by_id("receiver_id_2"))
        select_receiver.select_by_visible_text(current_receiver_name)
        select_channel = Select(self.driver.find_element_by_id("channel_id_2"))
        select_channel.select_by_visible_text(current_channel_name)
        self.click_save()
    
    def check_for_receiver_single_connnection_error_message(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "configure_connection_preset_ajax_message")))
        return self.driver.find_element_by_id("configure_connection_preset_ajax_message").text

    def select_preset_connection_global(self):
        if self.get_element_located_by_id("cp_allowed_modes_0"):
            self.driver.find_element_by_id("cp_allowed_modes_0").click()

    def select_preset_connection_view_only(self):
        if self.get_element_located_by_id("cp_allowed_modes_4"):
            self.driver.find_element_by_id("cp_allowed_modes_4").click()

    def select_preset_connection_shared(self):
        if self.get_element_located_by_id("cp_allowed_modes_1"):
            self.driver.find_element_by_id("cp_allowed_modes_1").click()

    def select_preset_connection_exclusive(self):
        if self.get_element_located_by_id("cp_allowed_modes_2"):
            self.driver.find_element_by_id("cp_allowed_modes_2").click()

    def select_preset_connection_all(self):
        if self.get_element_located_by_id("cp_allowed_modes_3"):
            self.driver.find_element_by_id("cp_allowed_modes_3").click()
    
    def get_preset_connection_image_srcs(self, element):
        srcs = []
        imgs = element.find_elements_by_xpath("./td[3]/img")
        for img in imgs:
            srcs.append(self.get_attribute_of_element_component(img, "src"))
        return srcs
    
    def get_preset_connection_view_only_button_visibility(self, element):
        return element.find_element_by_css_selector("img[src*='eye.png']").is_displayed()

    def get_preset_connection_shared_button_visibility(self, element):
        return element.find_element_by_css_selector("img[src*='multicast.png']").is_displayed()
    
    def get_preset_connection_exclusive_button_visibility(self, element):
        return element.find_element_by_css_selector("img[src*='lock.png']").is_displayed()
    
    """
    Users BasePage
    """
    
    def get_users_link_element(self):
        if self.get_element_located_by_link_text("USERS"):
            return self.driver.find_element_by_link_text("USERS")
        
    def open_users_tab(self):
        if self.get_element_located_by_link_text("USERS"):
            self.driver.find_element_by_link_text("USERS").click()
    
    def open_view_users_page(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_users_link_element()).move_to_element(self.driver.find_element_by_xpath("//div[@id='users_links']/ul//li/a[contains(text(), 'Add User Group')]")).move_to_element(self.driver.find_element_by_xpath("//div[@id='users_links']/ul//li/a[contains(text(), 'View Users')]")).click().perform()

    def open_add_user_page(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_users_link_element()).move_to_element(self.driver.find_element_by_xpath("//div[@id='users_links']/ul//li/a[contains(text(), 'Add User Group')]")).move_to_element(self.driver.find_element_by_xpath("//div[@id='users_links']/ul//li/a[contains(text(), 'Add User')]")).click().perform()

    def open_view_user_groups_page(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_users_link_element()).move_to_element(self.driver.find_element_by_xpath("//div[@id='users_links']/ul//li/a[contains(text(), 'Add User Group')]")).move_to_element(self.driver.find_element_by_xpath("//div[@id='users_links']/ul//li/a[contains(text(), 'View User Groups')]")).click().perform()

    def open_add_user_group_page(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_users_link_element()).move_to_element(self.driver.find_element_by_xpath("//div[@id='users_links']/ul//li/a[contains(text(), 'Add User Group')]")).click().perform()

    def open_active_directory_page(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_users_link_element()).move_to_element(self.driver.find_element_by_xpath("//div[@id='users_links']/ul//li/a[contains(text(), 'Add User Group')]")).move_to_element(self.driver.find_element_by_xpath("//div[@id='users_links']/ul//li/a[contains(text(), 'Active Directory')]")).click().perform()
    
    def get_list_of_users(self):
        return self.get_list("users")

    def get_user_username(self, element):
        return self.get_text_of_element_component_via_xpath(element, "./td[2]")

    def get_user_firstname(self, element):
        return self.get_text_of_element_component_via_xpath(element, "./td[3]")

    def get_user_lastname(self, element):
        return self.get_text_of_element_component_via_xpath(element, "./td[4]")
    
    def get_user_connection_image_src(self, element):
        return self.get_attribute_of_element_component(element.find_element_by_xpath("./td[8]/img"), "src")
    
    def get_user_config_linktext(self, element):
        return self.get_attribute_of_element_component(element.find_element_by_xpath("./td[12]/a[1]"), "href")

    def get_user_clone_linktext(self, element):
        return self.get_attribute_of_element_component(element.find_element_by_xpath("./td[12]/a[2]"), "href")
    
    def click_batch_delete_selector_for_user_element(self, element):
        element.find_element_by_xpath("./td[12]/input").click()
        
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
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[2]/a[1]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[2]/a[1]").click()

    def click_on_decend_user_usernames(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[2]/a[2]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[2]/a[2]").click()

    def click_on_ascend_user_firstnames(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[3]/a[1]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[3]/a[1]").click()

    def click_on_decend_user_firstnames(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[3]/a[2]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[3]/a[2]").click()

    def click_on_ascend_user_lastnames(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[4]/a[1]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[4]/a[1]").click()

    def click_on_decend_user_lastnames(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[4]/a[2]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[4]/a[2]").click()
    
    def click_user_config(self, element):
        element.find_element_by_xpath("./td[12]/a[1]").click()

    def click_user_clone(self, element):
        element.find_element_by_xpath("./td[12]/a[2]").click()
    
    def click_user_delete(self, element):
        element.find_element_by_xpath("./td[12]/a[3]").click()
    
    def click_batch_delete_users(self):
        if self.get_element_located_by_link_text("Delete selected Users"):
            self.driver.find_element_by_link_text("Delete selected Users").click()
    
    def get_user_email_from_config_page(self):
        if self.get_element_located_by_id("configure_user"):
                email = self.get_attribute_of_element_component(self.driver.find_element_by_id("u_email"), "value")
                if email != "":
                    return email
                elif email == "":
                    return "not@here.com"
    
    def get_user_username_from_config_page(self):
        if self.get_element_located_by_id("configure_user"):
            return self.get_attribute_of_element_component(self.driver.find_element_by_id("u_username"), "value")
    
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
        self.click_radio_option_by_div_text_and_id("Require Password?", "password_mode_set")

    def select_user_no_password(self):
        self.click_radio_option_by_div_text_and_id("Require Password?", "password_mode_none")
    
    def select_aim_admin_no(self):
        self.click_radio_option_by_div_text_and_id("AIM Admin?", "u_admin_0")

    def select_aim_admin_yes(self):
        self.click_radio_option_by_div_text_and_id("AIM Admin?", "u_admin_1")
    
    def select_user_suspended_no(self):
        self.click_radio_option_by_div_text_and_id("Account Suspended?", "u_suspended_0")

    def select_user_suspended_yes(self):
        self.click_radio_option_by_div_text_and_id("Account Suspended?", "u_suspended_1")
    
    def select_user_exclusive_no(self):
        self.click_radio_option_by_div_text_and_id("Allow Exclusive Mode?", "u_allow_exclusive_mode_0")
    
    def select_user_exclusive_global(self):
        self.click_radio_option_by_div_text_and_id("Allow Exclusive Mode?", "u_allow_exclusive_mode_-1")
    
    def select_user_exclusive_yes(self):
        self.click_radio_option_by_div_text_and_id("Allow Exclusive Mode?", "u_allow_exclusive_mode_1")
    
    def add_user_to_usergroup_via_user_config_page(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "all_user_groups")))
        select = Select(self.driver.find_element(By.ID, "all_user_groups"))
        select.select_by_index("0")
        self.driver.find_element_by_id("add_one_user_group").click()
    
    def remove_all_user_groups_from_user_via_user_config_page(self):
        if self.get_element_located_by_id("remove_all_user_groups"):
            self.driver.find_element_by_id("remove_all_user_groups").click()
    
    def check_user_in_user_group_via_user_config_page(self):
        return self.is_channel_specific_option_visible_by_text("User Groups", "group 0")
    
    def add_channel_permission_to_user_via_user_config_page(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "all_channels")))
        select = Select(self.driver.find_element(By.ID, "all_channels"))
        select.select_by_index("0")
        self.driver.find_element_by_id("add_one_channel").click()
    
    def add_all_channel_permissions_to_user_via_user_config_page(self):
        if self.get_element_located_by_id("add_all_channels"):
            self.driver.find_element_by_id("add_all_channels").click()        
    
    def check_channel_permission_for_user_via_user_config_page(self):
        return self.is_channel_specific_option_visible_by_text("Channels", "Channel TX")
    
    def remove_all_channels_from_user(self):
        if self.get_element_located_by_id("remove_all_channels"):
            self.driver.find_element_by_id("remove_all_channels").click()
    
    def add_channel_group_permission_to_user_via_user_config_page(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "all_channel_groups")))
        select = Select(self.driver.find_element(By.ID, "all_channel_groups"))
        select.select_by_index("0")
        self.driver.find_element_by_id("add_one_channel_group").click()
    
    def check_channel_group_permission_for_user_via_user_config_page(self):
        return self.is_channel_specific_option_visible_by_text("Channel Groups", "group 0")
    
    def remove_all_channel_group_permissions_via_user_config_page(self):
        if self.get_element_located_by_id("remove_all_channel_groups"):
            self.driver.find_element_by_id("remove_all_channel_groups").click()
    
    def add_receiver_permission_to_user_via_user_config_page(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "all_rxs")))
        select = Select(self.driver.find_element(By.ID, "all_rxs"))
        select.select_by_index("0")
        self.driver.find_element_by_id("add_one_rx").click()
    
    def check_receiver_permission_for_user_via_user_config_page(self):
        return self.is_channel_specific_option_visible_by_text("Receivers", "RX")
    
    def add_all_receiver_permissions_via_user_config_page(self):
        if self.get_element_located_by_id("add_all_rxs"):
            self.driver.find_element_by_id("add_all_rxs").click()
    
    def remove_all_receiver_permissions_from_user(self):
        if self.get_element_located_by_id("remove_all_rxs"):
            self.driver.find_element_by_id("remove_all_rxs").click()
    
    def add_receiver_group_permission_to_user_via_user_config_page(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "all_receiver_groups")))
        select = Select(self.driver.find_element(By.ID, "all_receiver_groups"))
        select.select_by_index("0")
        self.driver.find_element_by_id("add_one_receiver_group").click()
    
    def check_receiver_group_permission_for_user_via_user_config_page(self):
        return self.is_channel_specific_option_visible_by_text("Receiver Groups", "group 0")
    
    def remove_all_receiver_group_permissions_via_user_config_page(self):
        if self.get_element_located_by_id("remove_all_receiver_groups"):
            self.driver.find_element_by_id("remove_all_receiver_groups").click()
            
    def is_ajax_error_message_displayed_for_user(self):
        return self.get_element_located_by_id("configure_user_ajax_message")
    
    def confirm_no_longer_on_user_config_page(self):
        found = False
        while(found == False):
            if not self.get_text_of_page_header() == "Users > Configure User":
                found = True
    
    """
    User Group BasePage
    """
    def get_list_of_user_groups(self):
        return self.get_list("user_groups")
    
    def get_user_group_name(self, element):
        return self.get_text_of_element_component_via_xpath(element, "./td[2]")
    
    def get_user_group_connection_image_src(self, element):
        return self.get_attribute_of_element_component(element.find_element_by_xpath("./td[6]/img"), "src")
    
    def get_user_group_config_linktext(self, element):
        return self.get_attribute_of_element_component(element.find_element_by_xpath("./td[8]/a[1]"), "href")

    def get_user_group_clone_linktext(self, element):
        return self.get_attribute_of_element_component(element.find_element_by_xpath("./td[8]/a[2]"), "href")
    
    def click_add_user_group_button(self):
        if self.get_element_located_by_xpath("//span/img[@alt='Add User Group']"):
            self.driver.find_element_by_xpath("//span/img[@alt='Add User Group']").click()
        
    def send_search_term_to_user_group_name_field(self, term):
        self.send_filter_term_to_element("filter_ug_name", term)
    
    def click_on_filter_user_groups_by_name(self):
        self.click_on_filter("filter_ug_name_icon")    
    
    def click_on_remove_user_groups_name_filter(self):
        self.click_on_filter("remove_filter_ug_name_icon")
    
    def clear_user_groups_names_filter(self):
        self.clear_filter_of_element("filter_ug_name")
    
    def click_on_ascend_user_group_names(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[2]/a[1]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[2]/a[1]").click()

    def click_on_decend_user_group_names(self):
        if self.get_element_located_by_xpath("//div[@id='admin_body']/table/thead/tr/th[2]/a[2]"):
            self.driver.find_element_by_xpath("//div[@id='admin_body']/table/thead/tr/th[2]/a[2]").click()
    
    def click_user_group_config(self, element):
        element.find_element_by_xpath("./td[8]/a[1]").click()

    def click_user_group_clone(self, element):
        element.find_element_by_xpath("./td[8]/a[2]").click()

    def click_user_group_delete(self, element):
        element.find_element_by_xpath("./td[8]/a[3]").click()
    
    def click_batch_delete_selector_for_user_group_element(self, element):
        element.find_element_by_xpath("./td[8]/input").click()
    
    def click_batch_delete_user_groups(self):
        if self.get_element_located_by_link_text("Delete selected User Groups"):
            self.driver.find_element_by_link_text("Delete selected User Groups").click()
    
    def set_user_group_name_via_config_page(self, name):
        if self.get_element_located_by_id("configure_user_group"):
            self.enter_text_into_input_field("ug_name", name)
    
    def select_user_group_exclusive_no(self):
        self.click_radio_option_by_div_text_and_id("Allow Exclusive Mode?", "ug_allow_exclusive_mode_0")

    def select_user_group_exclusive_global(self):
        self.click_radio_option_by_div_text_and_id("Allow Exclusive Mode?", "ug_allow_exclusive_mode_-1")

    def select_user_group_exclusive_yes(self):
        self.click_radio_option_by_div_text_and_id("Allow Exclusive Mode?", "ug_allow_exclusive_mode_1")
    
    def get_all_members_of_user_group(self):
        users = []
        self.wait.until(EC.presence_of_element_located((By.ID, "selected_users")))
        select = Select(self.driver.find_element(By.ID, "selected_users"))
        options = select.options
        for option in options:
            users.append(option.text) 
        return users
    
    def add_default_members_to_user_group(self):
        default = ["admin", "anon", "api_anon"]
        self.wait.until(EC.presence_of_element_located((By.ID, "all_users")))
        select = Select(self.driver.find_element(By.ID, "all_users"))
        for user in default:
            select.select_by_visible_text(user)
            self.driver.find_element_by_id("add_one_user").click()
    
    def add_member_to_user_group_via_user_config_page(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "all_users")))
        select = Select(self.driver.find_element(By.ID, "all_users"))
        select.select_by_index("0")
        self.driver.find_element_by_id("add_one_user").click()
    
    def check_member_in_user_group_via_user_config_page(self):
        return self.is_channel_specific_option_visible_by_text("Users", "user 0")
    
    def remove_member_from_user_group_permission(self, user):
        self.wait.until(EC.presence_of_element_located((By.ID, "selected_users")))
        select = Select(self.driver.find_element(By.ID, "selected_users"))
        select.select_by_visible_text(user)
        self.driver.find_element_by_id("remove_one_user").click()
    
    def add_channel_permission_to_user_group_via_user_group_config_page(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "all_channels")))
        select = Select(self.driver.find_element(By.ID, "all_channels"))
        select.select_by_index("0")
        self.driver.find_element_by_id("add_one_channel").click()
    
    def check_channel_permission_for_user_group_via_user_group_config_page(self):
        return self.is_channel_specific_option_visible_by_text("Channels", "Channel TX")
    
    def add_all_channel_permissions_to_user_group_via_user_group_config_page(self):
        if self.get_element_located_by_id("add_all_channels"):
            self.driver.find_element_by_id("add_all_channels").click()
        
    def remove_all_channels_from_user_group(self):
        if self.get_element_located_by_id("remove_all_channels"):
            self.driver.find_element_by_id("remove_all_channels").click()

    def add_channel_group_permission_to_user_group_via_user_group_config_page(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "all_channel_groups")))
        select = Select(self.driver.find_element(By.ID, "all_channel_groups"))
        select.select_by_index("0")
        self.driver.find_element_by_id("add_one_channel_group").click()
    
    def check_channel_group_permission_for_user_group_via_user_group_config_page(self):
        return self.is_channel_specific_option_visible_by_text("Channel Groups", "group 0")
    
    def add_all_channel_group_permissions_to_user_group_via_user_group_config_page(self):
        if self.get_element_located_by_id("add_all_channel_groups"):
            self.driver.find_element_by_id("add_all_channel_groups").click()
        
    def remove_all_channel_groups_from_user_group(self):
        if self.get_element_located_by_id("remove_all_channel_groups"):
            self.driver.find_element_by_id("remove_all_channel_groups").click()
   
    def add_receiver_permission_to_user_group_via_user_group_config_page(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "all_rxs")))
        select = Select(self.driver.find_element(By.ID, "all_rxs"))
        select.select_by_index("0")
        self.driver.find_element_by_id("add_one_rx").click()
    
    def check_receiver_permission_for_user_group_via_user_group_config_page(self):
        return self.is_channel_specific_option_visible_by_text("Receivers", "RX")
    
    def add_all_receiver_permissions_to_user_group_via_user_group_config_page(self):
        if self.get_element_located_by_id("add_all_rxs"):
            self.driver.find_element_by_id("add_all_rxs").click()
        
    def remove_all_receivers_from_user_group(self):
        if self.get_element_located_by_id("remove_all_rxs"):
            self.driver.find_element_by_id("remove_all_rxs").click() 
    
    def add_receiver_group_permission_to_user_group_via_user_group_config_page(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "all_receiver_groups")))
        select = Select(self.driver.find_element(By.ID, "all_receiver_groups"))
        select.select_by_index("0")
        self.driver.find_element_by_id("add_one_receiver_group").click()
    
    def check_receiver_group_in_user_group_via_user_group_config_page(self):
        return self.is_channel_specific_option_visible_by_text("Receiver Groups", "group 0")

    def remove_all_receiver_group_permissions_via_user_group_config_page(self):
        if self.get_element_located_by_id("remove_all_receiver_groups"):
            self.driver.find_element_by_id("remove_all_receiver_groups").click()
    
    """
    Add User Group BasePage
    """
    def is_ajax_error_message_displayed_for_user_group(self):
        return self.get_element_located_by_id("configure_user_group_ajax_message")

    
    """
    USB Port Reservation BasePage
    """
    def get_port_reservation_labels(self, suffix):
        return self.get_dropdown_options_text_by_id("port_reservation_" + suffix)
     
    def select_port_reservation_label_by_element(self, element, label):
        select = Select(element)
        select.select_by_visible_text(label)
    
    def get_current_global_receiver_reserved_usb_port_selection_text(self, element):
        select = Select(element)
        return select.first_selected_option.text
    
    def get_list_of_port_reservation_dropdowns(self):
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "select[id^='port_reservation_']")))
        return self.driver.find_elements_by_css_selector("select[id^='port_reservation_']")
    
    def get_list_of_port_reservation_merge_checkboxes(self):
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[id^='merge_']")))
        return self.driver.find_elements_by_css_selector("input[id^='merge_']")
    
    def get_list_of_port_reservation_device_dropdowns(self):
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "select[id^='port_quirk_']")))
        return self.driver.find_elements_by_css_selector("select[id^='port_quirk_']")
    
    def get_list_of_reserved_devices(self, element):
        return self.get_dropdown_options_text_by_element(element)
    
    def select_port_reservation_device_label_by_element(self, element, label):
        select = Select(element)
        select.select_by_visible_text(label)
        
    def get_current_global_receiver_reserved_usb_port_device_selection_text(self, element):
        select = Select(element)
        return select.first_selected_option.text

    def show_advanced_usb_features(self):
        if self.get_element_located_by_id("show_quirks_table"):
            self.driver.execute_script("toggle_quirks_table(1)")
            time.sleep(2)
    
    def get_list_usb_devices(self):
        return self.driver.find_elements_by_css_selector("div#quirks_table_container form#usb_quirks table.zebra tbody tr")
    
    def toggle_hide_usb_device(self, element):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id^='show_quirk']")))
        element.find_element_by_css_selector("input[id^='show_quirk']").click()
    
    def set_status_hide_usb_device_global(self, status):
        self.driver.find_element_by_css_selector("#toggle_show_checkbox").click()
        if self.driver.find_element_by_css_selector("#toggle_show_checkbox").is_selected() == status:
            pass
        else: 
            self.driver.find_element_by_css_selector("#toggle_show_checkbox").click()
    
    def check_show_status_of_usb_device(self, element):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id^='show_quirk']")))
        return element.find_element_by_css_selector("input[id^='show_quirk']").is_selected()
    
    def add_test_usb_device(self, name, desc, kernel, user):
        self.driver.find_element_by_css_selector("#new_quirk_name").clear()
        self.driver.find_element_by_css_selector("#new_quirk_descrip").clear()
        self.driver.find_element_by_css_selector("#new_quirk_kernel").clear()
        self.driver.find_element_by_css_selector("#new_quirk_user").clear()
        self.driver.find_element_by_css_selector("#new_quirk_name").send_keys(name)
        self.driver.find_element_by_css_selector("#new_quirk_descrip").send_keys(desc)
        self.driver.find_element_by_css_selector("#new_quirk_kernel").send_keys(kernel)
        self.driver.find_element_by_css_selector("#new_quirk_user").send_keys(user)
        
    def delete_test_usb_device(self):
        table = self.driver.find_element_by_css_selector("div#quirks_table_container form#usb_quirks table.zebra tbody")
        table.find_element_by_css_selector("input[id^='delete_quirk']").click()
    
    def get_port_merge_selector_state(self, element):
        return element.is_selected()
    
    def toggle_port_merge_state(self, element):
        element.click()
    
    def get_quirk_ajax_message_text(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span#usb_quirks_ajax_message.message_box.mb_red")))
        return self.driver.find_element_by_css_selector("span#usb_quirks_ajax_message.message_box.mb_red").text
    
    """
    Statistics Page BasePage
    """
    def open_statistics_tab(self):
        if self.get_element_located_by_link_text("STATISTICS"):
            self.driver.find_element_by_link_text("STATISTICS").click()
            
    def get_no_enabled_devices_text_from_lightbox(self):
        return self.get_lightbox_title_text() 
    
    def click_open_device_list_within_lightbox(self):
        if self.get_element_located_by_id("ibox"):
            self.driver.find_element_by_link_text("the devices page").click()
    
    def open_device_list_directly(self):
        self.driver.get(self.baseurl + "/admin/devices.php")
    
    def get_list_of_devices(self):
        return self.get_list("devices")
    
    def get_device_name(self, element):
        return self.get_text_of_element_component_via_xpath(element, "./td[2]")
    
    def click_device_statistics_icon(self, element):
        element.find_element_by_xpath("./td[8]/a[2]").click()
        time.sleep(0.5)
    
    def select_rx_bandwidth(self, state):
        if self.driver.find_element_by_css_selector("input[name='rxBandwidth']").is_selected() == state:
            pass
        else: 
            self.driver.find_element_by_css_selector("input[name='rxBandwidth']").click()
            
    def select_rx_throughput(self, state):
        if self.driver.find_element_by_css_selector("input[name='rxData']").is_selected() == state:
            pass
        else: 
            self.driver.find_element_by_css_selector("input[name='rxData']").click()
    
    def select_tx_bandwidth(self, state):
        if self.driver.find_element_by_css_selector("input[name='txBandwidth']").is_selected() == state:
            pass
        else: 
            self.driver.find_element_by_css_selector("input[name='txBandwidth']").click()
    
    def select_tx_throughput(self, state):
        if self.driver.find_element_by_css_selector("input[name='txData']").is_selected() == state:
            pass
        else: 
            self.driver.find_element_by_css_selector("input[name='txData']").click()
    
    def select_framecount(self, state):
        if self.driver.find_element_by_css_selector("input[name='frameCount']").is_selected() == state:
            pass
        else: 
            self.driver.find_element_by_css_selector("input[name='frameCount']").click()

    def select_head0_frame_rate(self, state):
        if self.driver.find_element_by_css_selector("input[name='fcnt0']").is_selected() == state:
            pass
        else: 
            self.driver.find_element_by_css_selector("input[name='fcnt0']").click()

    def select_head1_frame_rate(self, state):
        if self.driver.find_element_by_css_selector("input[name='fcnt1']").is_selected() == state:
            pass
        else: 
            self.driver.find_element_by_css_selector("input[name='fcnt1']").click()
        
    def click_lightbox_submit_button(self):
        if self.get_element_located_by_id("ibox"):
            self.driver.find_element_by_link_text("Submit").click()
    
    def get_device_name_from_statistics_graph(self):
        names = []
        titles = self.driver.find_elements_by_css_selector("#container>div>h2")
        for title in titles:
            names.append(title.text)
        return names

    def get_graph_type_from_statistics_graph_left_axis(self):
        names = []
        axis = self.driver.find_elements_by_css_selector("#container>div>div>div[style*='rotate(-90deg)']:first-of-type")
        for each in axis:
            names.append(each.text)
        return names
        
    def get_graph_type_from_statistics_graph_right_axis(self):
        names = []
        axis = self.driver.find_elements_by_css_selector("#container>div>div>div[style*='rotate(-90deg)']:last-of-type") 
        for each in axis:
            names.append(each.text)
        return names
    
    """
    New Statistics Page BasePage
    """
    def click_show_receivers(self):
        if self.get_element_located_by_css_selector("#filterRxs"):
            self.driver.find_element_by_css_selector("#filterRxs").click()
    
    def click_show_transmitters(self):
        if self.get_element_located_by_css_selector("#filterTxs"):
            self.driver.find_element_by_css_selector("#filterTxs").click()
    
    def get_device_type_img(self, device):
        return device.find_element_by_css_selector("td:nth-child(1)>span>img").get_attribute("src")

    def click_activate_statistics(self, device):
        device_id = device.get_attribute("id").replace("row_id_", "")
        device.find_element_by_css_selector("td:nth-child(5)>a>img#statsImg_%s" %device_id).click()
    
    def click_device_name(self, device):
        device.find_element_by_css_selector("td:nth-child(2)>a").click()
    
    def get_number_device_name_links(self, device):
        return len(device.find_elements_by_css_selector("td:nth-child(2)>a"))
    
    def get_graph_title(self):
        return self.driver.find_element_by_css_selector("div#right>h1").text
    
    def click_disable_all_device_statistics(self):
        if self.get_element_located_by_link_text("Disable All"):
            self.driver.find_element_by_link_text("Disable All").click()
    
    def send_search_term_to_name(self, search_term):
        if self.get_element_located_by_css_selector("#filter_d_name"):
            self.driver.find_element_by_css_selector("#filter_d_name").send_keys(search_term)
    
    def click_filter_by_name(self):
        if self.get_element_located_by_css_selector("#filter_d_name_icon"):
            self.driver.find_element_by_css_selector("#filter_d_name_icon").click()
        
    def send_search_term_to_description(self, search_term):
        if self.get_element_located_by_css_selector("#filter_d_description"):
            self.driver.find_element_by_css_selector("#filter_d_description").send_keys(search_term)
    
    def click_filter_by_description(self):
        if self.get_element_located_by_css_selector("#filter_d_description_icon"):
            self.driver.find_element_by_css_selector("#filter_d_description_icon").click()
        
    def send_search_term_to_location(self, search_term):
        if self.get_element_located_by_css_selector("#filter_d_location"):
            self.driver.find_element_by_css_selector("#filter_d_location").send_keys(search_term)
    
    def click_filter_by_location(self):
        if self.get_element_located_by_css_selector("#filter_d_locatio_icon"):
            self.driver.find_element_by_css_selector("#filter_d_locatio_icon").click()
    
    def click_remove_filters(self):
        if self.get_element_located_by_link_text("Remove Filters"):
            self.driver.find_element_by_link_text("Remove Filters").click()
    
    def get_device_description(self, element):
        return self.get_text_of_element_component_via_css_selector(element, "td:nth-child(3)")
            
    def get_device_location(self, element):
        return self.get_text_of_element_component_via_css_selector(element, "td:nth-child(4)")
            
    """
    Servers Page BasePage
    """
    def open_servers_tab(self):
        if self.get_element_located_by_link_text("SERVERS"):
            self.driver.find_element_by_link_text("SERVERS").click()
    
    def get_list_of_servers(self):
        return self.get_list("servers")
    
    def get_server_name(self, element):
        return self.get_text_of_element_component_via_css(element, "td:nth-child(1)")        

    def get_server_role(self, element):
        return self.get_text_of_element_component_via_css(element, "td:nth-child(2)")        

    def get_server_status(self, element):
        return self.get_text_of_element_component_via_css(element, "td:nth-child(3)")        

    def get_server_ip_address(self, element):
        return self.get_text_of_element_component_via_css(element, "td:nth-child(4)")        

    def get_server_description(self, element):
        return self.get_text_of_element_component_via_css(element, "td:nth-child(5)")
            
    def get_server_location(self, element):
        return self.get_text_of_element_component_via_css(element, "td:nth-child(6)")
    
    def click_server_config(self, element):
        element.find_element_by_css_selector("td:nth-child(7)>a").click()
            
    def click_non_primary_server_local_config(self, element):
        element.find_element_by_css_selector("td:nth-child(7)>a:nth-child(2)").click()
            
    def click_server_delete(self, element):
        element.find_element_by_css_selector("td:nth-child(7)>a:nth-child(3)").click()
    
    def set_server_name(self, name):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#name")))
        self.driver.find_element_by_css_selector("#name").clear()
        self.driver.find_element_by_css_selector("#name").send_keys(name)

    def set_server_description(self, name):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#description")))
        self.driver.find_element_by_css_selector("#description").clear()
        self.driver.find_element_by_css_selector("#description").send_keys(name)
    
    def set_server_location(self, name):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#location")))
        self.driver.find_element_by_css_selector("#location").clear()
        self.driver.find_element_by_css_selector("#location").send_keys(name)
    
    def get_current_window_handle(self):
        return self.driver.current_window_handle
    
    def switch_to_other_window_from(self, first):
        names = self.driver.window_handles
        for name in names:
            if name != first:
                self.driver.switch_to_window(name)
            else: pass
            
    def get_current_url(self):
        return self.driver.current_url
            
    def get_server_name_from_backup_local_config(self):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#configure_server>div.form_row:nth-child(7)>div.form_input_elements"))).text
        