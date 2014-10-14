'''
Created on 9 Jul 2014

@author: Mark
'''
from root.nested.pages.base_page import BasePage

class MailSettingsPage(BasePage):
    
    def click_mail_enable_yes(self):
        self.click_radio_option_by_div_text_and_id("Mail Enabled?", "mail_enabled_1")

    def click_mail_enable_no(self):
        self.click_radio_option_by_div_text_and_id("Mail Enabled?", "mail_enabled_0")
    
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
    
    def click_save_mail_settings(self):
        self.click_save()